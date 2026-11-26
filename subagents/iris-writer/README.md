# Writer

[Subagents](../README.md) · [All Agents](../../README.md) · [Skills](https://github.com/HiLleywyn/dyadic-skills) · [Agents](https://github.com/HiLleywyn/dyadic-agents) · [Plugins](https://github.com/HiLleywyn/dyadic-plugins)

Iris's writing specialist: drafts and edits text for its reader, keeps your meaning and style, and turns meeting notes into decisions and actions.

Unmodified official definition from Dyadic `26ea591af225ed48129a1968db78b3e8f335dc90`, `catalog/agents/iris-writer`.

| Definition | Purpose |
| --- | --- |
| [agent.json](agent.json) | Native catalog identity, source tool policy, skills and metadata |
| [instructions.md](instructions.md) | Maintained instruction body |
| [import.json](import.json) | Explicit tools suggested by the portable export |

**Role:** delegated specialist. **Source version:** 2.0.1. **Source memory setting:** true.

**Skill dependencies:** [house-style](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/house-style), [meeting-actions](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/meeting-actions).

**Portable tools:** `data.web_fetch`, `skills.read`.

Build with `python tools/catalog.py build` from the repository root, then upload `dist/iris-writer.zip` through Dyadic’s Store import review. The ZIP uses native `dyadic.package` format; a raw folder download with documentation is not the same package. To bundle the matching skills, add `--skills ../skills`.

Imported copies have strict tools, memory off and delegated usage. Tool suggestions start unchecked; select dependencies or use the dependency-bundled export. Importing does not inherit the default agent’s ambient permissions or replace its installed configuration. See [compatibility](../../COMPATIBILITY.md).
