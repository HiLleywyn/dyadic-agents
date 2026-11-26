# Iris

[Primary Agents](../README.md) · [All Agents](../../README.md) · [Skills](https://github.com/HiLleywyn/dyadic-skills) · [Agents](https://github.com/HiLleywyn/dyadic-agents) · [Plugins](https://github.com/HiLleywyn/dyadic-plugins)

Dyadic’s built-in primary assistant: persona, native-tool discovery, bounded delegation, patch discipline and recording-reference handling.

The [agent.json](agent.json), [instructions.md](instructions.md) and [original source README](SOURCE-README.md) are unmodified snapshots of `agents/iris/` at Dyadic `26ea591af225ed48129a1968db78b3e8f335dc90`. The built-in configuration inherits platform behavior; its single explicit tool switch does not describe the entire runtime.

Iris is retained here as the canonical source definition for inspection and future maintenance. It is deliberately excluded from portable agent builds: the current Store importer creates strict delegated copies and cannot replace the platform’s primary Iris. Updating this repository does not change live Iris. See [compatibility](../../COMPATIBILITY.md).
