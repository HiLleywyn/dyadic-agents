# Security Reviewer

[Subagents](../README.md) · [All Agents](../../README.md) · [Skills](https://github.com/HiLleywyn/dyadic-skills) · [Agents](https://github.com/HiLleywyn/dyadic-agents) · [Plugins](https://github.com/HiLleywyn/dyadic-plugins)

Review the requested source snapshot or patch with read-only inspection.

Unmodified official definition from Dyadic `96ef2940376710ca0fd02a97f6782aa8e3cd7358`, `catalog/agents/dyadic-security-reviewer`.

| Definition | Purpose |
| --- | --- |
| [agent.json](agent.json) | Native catalog identity, source tool policy, skills and metadata |
| [instructions.md](instructions.md) | Maintained instruction body |
| [import.json](import.json) | Explicit tools suggested by the portable export |

**Role:** delegated specialist. **Source version:** 1.0.0. **Source memory setting:** false.

**Skill dependencies:** [dyadic-security-diff-scan](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/security/dyadic-security-diff-scan), [dyadic-threat-model](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/security/dyadic-threat-model), [evidence-review](https://github.com/HiLleywyn/dyadic-skills/tree/main/dyadic/iris/evidence-review).

**Portable tools:** `workspace.inspect`, `tools.compose`, `skills.read`.
