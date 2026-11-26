# Analyst

[Subagents](../README.md) · [All Agents](../../README.md) · [Skills](https://github.com/HiLleywyn/dyadic-skills) · [Agents](https://github.com/HiLleywyn/dyadic-agents) · [Plugins](https://github.com/HiLleywyn/dyadic-plugins)

Iris's analyst: computes answers from your data and databases, and reads your documents properly, citing the page for every fact.

Unmodified official definition from Dyadic `26ea591af225ed48129a1968db78b3e8f335dc90`, `catalog/agents/iris-analyst`.

| Definition | Purpose |
| --- | --- |
| [agent.json](agent.json) | Native catalog identity, source tool policy, skills and metadata |
| [instructions.md](instructions.md) | Maintained instruction body |
| [import.json](import.json) | Explicit tools suggested by the portable export |

**Role:** delegated specialist. **Source version:** 2.0.1. **Source memory setting:** true.

**Skill dependencies:** [data-analysis](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/data-analysis), [csv-cleanup](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/csv-cleanup), [sql-analysis](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/sql-analysis), [summarize-documents](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/summarize-documents), [extract-structured-data](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/extract-structured-data), [compare-documents](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/compare-documents).

**Portable tools:** `workspace.inspect`, `workspace.files`, `workspace.python`, `workspace.bash`, `database.schema`, `database.query`, `knowledge.search`, `documents.read`, `documents.write`, `spreadsheets.read`, `spreadsheets.write`, `vision.read_text`, `data.web_fetch`, `skills.read`.

Build with `python tools/catalog.py build` from the repository root, then upload `dist/iris-analyst.zip` through Dyadic’s Store import review. The ZIP uses native `dyadic.package` format; a raw folder download with documentation is not the same package. To bundle the matching skills, add `--skills ../skills`.

Imported copies have strict tools, memory off and delegated usage. Tool suggestions start unchecked; select dependencies or use the dependency-bundled export. Importing does not inherit the default agent’s ambient permissions or replace its installed configuration. See [compatibility](../../COMPATIBILITY.md).
