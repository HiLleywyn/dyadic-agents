# Dyadic Agents

[Skills](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?ref=main) · [Agents](https://git.lley.cat/r/dadd28be-7d91-432f-beb0-00d285e8f02b?ref=main) · [Plugins](https://git.lley.cat/r/ae86ea71-cb4d-4fc5-9ec1-803f8f303989?ref=main)

Named agent definitions and delegated specialists for Dyadic. This repository keeps identity and task boundaries; reusable procedures live in Skills, and built-in tool switches live in Plugins.

## Browse

- [Primary agents](agents/README.md): Iris, preserved from the platform source.
- [Subagents](subagents/README.md): the six existing Dyadic specialists plus Artifact Auditor and Continuity Reviewer.
- [Machine-readable catalog](catalog.json): names, descriptions, paths and roles.
- [Compatibility and blockers](COMPATIBILITY.md): what the current importer and runtime can use.
- [Maintenance](MAINTENANCE.md): refreshes, exports, dependency locks and checks.
- [Delivery report](REPORT.md): completed repository work and verification limits.

The two additions have deliberately narrow jobs. Artifact Auditor locates the unsupported step between a claimed output and an actual handoff. Continuity Reviewer catches lost accepted constraints, intervening owner edits and stale checks during follow-up work. Both use only read-only workspace inspection and skill reading, with evidence supplied by their parent.

## Build and use

With Python 3.11+ and PyYAML available:

```text
python tools/catalog.py check
python .lley/run.py
python tools/catalog.py build
python tools/catalog.py build --skills ../skills --output dist-with-skills
```

Import an individual `dist/<agent-id>.zip` using Dyadic’s reviewed package upload. `dist/collection.zip` groups the individual archives for download; extract it first. The optional second build includes each agent’s matching skill resources and checks the dependency lock. The default build keeps skills in their own repository and presents required skills for the owner to bind in review.

The source `agent.json` and `instructions.md` remain intact. Exports use the current native package format, explicit permission suggestions, strict delegated usage and memory off. They do not replace default agents or enable account tools automatically. Iris is not exported as a pretend installable primary agent.

For compatibility verification in an existing Dyadic test environment, `tools/verify_dyadic.py` accepts `--source ../dyadic --skills ../skills/dist --agents dist --bundled-agents dist-with-skills --plugins ../plugins --report reports/dyadic-compatibility.json`. It parses the exported bytes using the unmodified product inspector and compares plugin switches; it makes no account installations or provider calls. Run it offline after both standalone and dependency-bundled builds.

## Provenance

Official snapshots come from Dyadic `26ea591af225ed48129a1968db78b3e8f335dc90`. [provenance.json](provenance.json) records source paths and SHA-256 values. New specialists are separately labeled and are not represented as deployed official defaults. No runtime/provider implementation, credentials, user conversations or private case evidence is included. Existing licenses and attribution remain with their original resources; project-authored material is now offered under MIT with upstream notices preserved.

## Source, mirrors and licensing

The [HiLleywyn/dyadic-agents](https://github.com/HiLleywyn/dyadic-agents) GitHub repository is canonical. [lley.cat](https://git.lley.cat/r/dadd28be-7d91-432f-beb0-00d285e8f02b) is its synchronized mirror. Project-authored definitions, documentation and tooling use [MIT](LICENSE); preserve notices attached to imported resources.

## What an agent package defines

An agent definition combines identity, instructions, declared tools and bounded delegation. It is not a running process or a replacement for server-side policy. `agent.json` and `instructions.md` retain the actual source definition; `import.json` describes reviewed import suggestions. The runtime resolves installed skills and tools under the user's account and current permissions.

Primary Iris remains separate from delegated specialists. A subagent receives the parent's explicit task and permitted evidence, acts within its declared tools and returns a result. The source package cannot confer billing authority, access another account, install a provider key or silently widen a delegation. Skill dependencies are recorded in [the lock](compatibility/skill-dependencies.json), rather than guessed from a display name.

## Reproduce the catalog and exports

```sh
git clone https://github.com/HiLleywyn/dyadic-agents.git
cd dyadic-agents
python -m pip install PyYAML
python tools/catalog.py check
python .lley/run.py
python tools/catalog.py build
```

For dependency-inclusive archives, clone [dyadic-skills](https://github.com/HiLleywyn/dyadic-skills) alongside this checkout and use the documented `--skills ../dyadic-skills` build. The source-only and bundled forms deliberately retain the same agent IDs and role boundaries. A collection ZIP is a download container; import its individual supported packages rather than pretending it is one new primary agent.

The tests validate source metadata, links, dependency identities and actual archive contents. `tools/verify_dyadic.py` can inspect these bytes with an existing private Dyadic checkout without installing an account package or making model calls. [Compatibility](COMPATIBILITY.md) records supported formats and genuine blockers; [maintenance](MAINTENANCE.md) explains how official snapshots are refreshed from immutable source.

## Platform and related sources

[Dyadic Developers](https://dyadic.app/developers/) documents the platform contract. [Skills](https://github.com/HiLleywyn/dyadic-skills) contain reusable procedures, while [plugins](https://github.com/HiLleywyn/dyadic-plugins) describe built-in tool capabilities. [Matrix](https://dyadic.app/developers/matrix/) coordinates durable reviewed work; its [engine source](https://github.com/HiLleywyn/dyadic-matrix) is separately auditable. Both GitHub Actions and `lley.cat` Actions validate catalog pushes; source publication does not activate runtime agents or a delivery pipeline.
