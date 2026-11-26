# Dyadic Compatibility

[Agents](README.md) · [Skills](https://github.com/HiLleywyn/dyadic-skills) · [Plugins](https://github.com/HiLleywyn/dyadic-plugins)

What Dyadic's import and runtime code accepts from this repository. The code references are to the Dyadic platform repository; recheck them against the revision you target.

| Content | Usable route | Limit |
| --- | --- | --- |
| Official specialists | Upload the `dist/<agent-id>.zip` built here through Store import review | Imported copies use the explicit `import.json` tool list, strict tools and memory off; they do not inherit every ambient capability of the built-in default |
| Artifact Auditor, Continuity Reviewer | Same reviewed delegated-agent import | Repository-authored; not official Dyadic defaults. The parent must supply accepted-work and receipt context |
| Skill dependencies | Bind matching installed skills during review, or build with `--skills ../dyadic-skills` | The standalone export does not install or enable missing skills |
| Iris | Inspect and maintain the source snapshot | Not exported: imports are always delegated and cannot replace the built-in primary agent |

## Why packages are built rather than imported from folders

- **Source links.** `core/dyadic_core/workspace/package_sources.py` resolves public GitHub repository/tree/blob URLs, skills.sh pages and direct HTTPS files, and rejects any URL with a query string, so lley.cat folder or raw links (`/r/<uuid>?path=...`) cannot be imported directly. A GitHub folder of this repository still contains a raw agent folder, not a native package (next point).
- **Raw folders.** `package_imports.py` converts native package ZIPs or inline agent instructions. It does not join a catalog `agent.json` with its adjacent `instructions.md`; `tools/catalog.py build` produces the native `dyadic-package.json` archive that the importer expects.
- **Delegated only.** `packages.py` forces imported agents to `usage: delegate`, `memory: false`, `strict_tools: true` and no MCP servers. Primary-agent replacement would need a separately designed product contract.
- **Owner-only context.** `tools/builtin/runs.py` limits recording access to interactive Workspace chats, excluding delegated, unattended and API-key runs. The two repository-authored specialists therefore request no `runs.*` tools and rely on evidence from their parent.
- **No catalog sync.** Dyadic's Store loads its own `catalog/` at startup. A push here does not change the product catalog or upgrade installed account copies.

Parser acceptance (`tools/verify_dyadic.py`) is separate from installation into a live account and from a successful model or tool run.
