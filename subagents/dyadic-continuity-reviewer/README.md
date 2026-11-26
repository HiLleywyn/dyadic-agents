# Continuity Reviewer

[Subagents](../README.md) · [All Agents](../../README.md) · [Skills](https://github.com/HiLleywyn/dyadic-skills) · [Agents](https://github.com/HiLleywyn/dyadic-agents) · [Plugins](https://github.com/HiLleywyn/dyadic-plugins)

Compare a requested revision with Dyadic’s accepted brief and exact file versions; identify lost constraints, intervening edits and stale verification before a new handoff.

Repository-authored addition; not yet part of Dyadic’s official catalog.

| Definition | Purpose |
| --- | --- |
| [agent.json](agent.json) | Native catalog identity, source tool policy, skills and metadata |
| [instructions.md](instructions.md) | Maintained instruction body |
| [import.json](import.json) | Explicit tools suggested by the portable export |

**Role:** delegated specialist. **Source version:** 1.0.0. **Source memory setting:** false.

**Skill dependencies:** [dyadic-current-work](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/workflows/dyadic-current-work), [dyadic-source-conflicts](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/workflows/dyadic-source-conflicts).

**Portable tools:** `workspace.inspect`, `skills.read`.

Build with `python tools/catalog.py build` from the repository root, then upload `dist/dyadic-continuity-reviewer.zip` through Dyadic’s Store import review. The ZIP uses native `dyadic.package` format; a raw folder download with documentation is not the same package. To bundle the matching skills, add `--skills ../skills`.

Imported copies have strict tools, memory off and delegated usage. Tool suggestions start unchecked; select dependencies or use the dependency-bundled export. Importing does not inherit the default agent’s ambient permissions or replace its installed configuration. See [compatibility](../../COMPATIBILITY.md).
