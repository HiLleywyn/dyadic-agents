# Security Reviewer

[Subagents](../README.md) · [All Agents](../../README.md) · [Skills](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?ref=store) · [Agents](https://git.lley.cat/r/dadd28be-7d91-432f-beb0-00d285e8f02b?ref=store) · [Plugins](https://git.lley.cat/r/ae86ea71-cb4d-4fc5-9ec1-803f8f303989?ref=store)

Review the requested source snapshot or patch with read-only inspection.

Unmodified official definition from Dyadic `96ef2940376710ca0fd02a97f6782aa8e3cd7358`, `catalog/agents/dyadic-security-reviewer`.

| Definition | Purpose |
| --- | --- |
| [agent.json](agent.json) | Native catalog identity, source tool policy, skills and metadata |
| [instructions.md](instructions.md) | Maintained instruction body |
| [import.json](import.json) | Explicit tools suggested by the portable export |

**Role:** delegated specialist. **Source version:** 1.0.0. **Source memory setting:** false.

**Skill dependencies:** [dyadic-security-diff-scan](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?path=dyadic/security/dyadic-security-diff-scan&ref=store), [dyadic-threat-model](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?path=dyadic/security/dyadic-threat-model&ref=store), [evidence-review](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?path=dyadic/iris/evidence-review&ref=store).

**Portable tools:** `workspace.inspect`, `tools.compose`, `skills.read`.
