"""Check built collection bytes with an existing, unmodified Dyadic checkout.

This only parses packages/catalog metadata. It never installs into an account,
starts models, executes skill resources or enables tools. Run offline.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--skills', type=Path, required=True, help='Built skill ZIP directory')
    parser.add_argument('--agents', type=Path, required=True, help='Built standalone agent ZIP directory')
    parser.add_argument('--bundled-agents', type=Path, required=True)
    parser.add_argument('--plugins', type=Path, required=True, help='Plugin repository root')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.source / 'core'))
    from dyadic_core.tools import load_builtin_tools
    from dyadic_core.workspace import packages
    load_builtin_tools()
    cases = []
    for kind, folder in [('skill', args.skills), ('agent', args.agents), ('bundled-agent', args.bundled_agents)]:
        for path in sorted(folder.glob('*.zip')):
            if path.name == 'collection.zip':
                continue
            body = path.read_bytes()
            case = {'name': kind + '/' + path.name, 'sha256': hashlib.sha256(body).hexdigest()}
            try:
                result = packages.inspect(body, [], filename=path.name, kind='skill' if kind == 'skill' else 'agent')
                if kind == 'skill':
                    assert len(result['skills']) == 1 and not result['agents']
                else:
                    assert len(result['agents']) == 1
                    agent = result['agents'][0]
                    assert agent['usage'] == 'delegate' and agent['memory'] is False and agent['strict_tools'] is True
                    assert not agent['mcp_servers']
                    if kind == 'bundled-agent':
                        assert set(agent['skills']) == set(result['skills'])
                        assert set(agent['requirements']['skills']) == set(agent['skills'])
                    else:
                        assert not result['skills'] and not agent['skills']
                case.update(status='passed', skills=len(result['skills']), agents=len(result['agents']))
            except Exception as exc:
                case.update(status='failed', error=type(exc).__name__ + ': ' + str(exc))
            cases.append(case)
    # The published plugin set must map exactly to the source's surfaced switches.
    module = ast.parse((args.source / 'server/dyadic_server/workspace_api.py').read_text(encoding='utf-8'))
    switches = next(ast.literal_eval(n.value) for n in module.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SURFACED_TOOLS' for t in n.targets))
    expected = {name: label for name, label, description in switches}
    seen = set()
    for path in sorted((args.plugins / 'dyadic').glob('*/plugin.json')):
        manifest = json.loads(path.read_text(encoding='utf-8'))
        ok = manifest['tool'] in expected and expected[manifest['tool']] == manifest['name'] and manifest['tool'] not in seen
        seen.add(manifest['tool'])
        cases.append({'name': 'plugin/' + manifest['id'], 'status': 'passed' if ok else 'failed', 'tool': manifest['tool']})
    cases.append({'name': 'plugin/complete-default-switch-set', 'status': 'passed' if seen == set(expected) else 'failed'})
    # Avoid a green report if a caller pointed at missing or empty build folders.
    for kind, folder in [('skill', args.skills), ('agent', args.agents), ('bundled-agent', args.bundled_agents)]:
        if not any(c['name'].startswith(kind + '/') for c in cases):
            cases.append({'name': kind + '/nonempty-exports', 'status': 'failed', 'error': 'No individual packages found'})
    result = {'schema': 1, 'scope': 'Inert package inspection and default plugin switch matching; no account install or provider calls',
              'passed': sum(c['status'] == 'passed' for c in cases), 'failed': sum(c['status'] == 'failed' for c in cases), 'cases': cases}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('passed', 'failed')}))
    for case in cases:
        if case['status'] != 'passed':
            print(json.dumps(case))
    return bool(result['failed'])


if __name__ == '__main__':
    sys.exit(main())
