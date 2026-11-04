# Builder

[Subagents](../README.md) · [All Agents](../../README.md) · [Skills](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?ref=store) · [Agents](https://git.lley.cat/r/dadd28be-7d91-432f-beb0-00d285e8f02b?ref=store) · [Plugins](https://git.lley.cat/r/ae86ea71-cb4d-4fc5-9ec1-803f8f303989?ref=store)

Prepare and verify focused code changes in the native isolated sandbox.

Unmodified official definition from Dyadic `26ea591af225ed48129a1968db78b3e8f335dc90`, `catalog/agents/dyadic-builder`.

| Definition | Purpose |
| --- | --- |
| [agent.json](agent.json) | Native catalog identity, source tool policy, skills and metadata |
| [instructions.md](instructions.md) | Maintained instruction body |
| [import.json](import.json) | Explicit tools suggested by the portable export |

**Role:** delegated specialist. **Source version:** 1.0.1. **Source memory setting:** false.

**Skill dependencies:** [debug-code](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?path=dyadic/iris/debug-code&ref=store), [collaborative-review](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?path=dyadic/iris/collaborative-review&ref=store), [evidence-review](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?path=dyadic/iris/evidence-review&ref=store).

**Portable tools:** `workspace.inspect`, `workspace.files`, `workspace.patch_preview`, `workspace.python`, `workspace.bash`, `skills.read`.

Build with `python tools/catalog.py build` from the repository root, then upload `dist/dyadic-builder.zip` through Dyadic’s Store import review. The ZIP uses native `dyadic.package` format; a raw folder download with documentation is not the same package. To bundle the matching skills, add `--skills ../skills`.

Imported copies have strict tools, memory off and delegated usage. Tool suggestions start unchecked; select dependencies or use the dependency-bundled export. Importing does not inherit the default agent’s ambient permissions or replace its installed configuration. See [compatibility](../../COMPATIBILITY.md).
