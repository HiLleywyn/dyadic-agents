# Dyadic Compatibility

[Agents](README.md) · [Skills](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?ref=store) · [Plugins](https://git.lley.cat/r/ae86ea71-cb4d-4fc5-9ec1-803f8f303989?ref=store) · [Delivery Report](REPORT.md)

This assessment uses unmodified Dyadic source `26ea591af225ed48129a1968db78b3e8f335dc90`. It describes that revision’s import/runtime contracts, not a claim about the version deployed to every account. This task changes only the three collection repositories.

| Content | Usable route today | Remaining limit |
| --- | --- | --- |
| Individual skills | Upload the built skill ZIP through Store import review | Tools, connected services and account On switches must exist; some host-oriented skills describe capabilities unavailable in the online sandbox |
| Six existing specialists | Upload the native agent ZIP built by this repo | Portable copies use explicit tool suggestions, strict tools and memory off; they do not inherit every ambient capability of the official default |
| Artifact Auditor and Continuity Reviewer | The same reviewed delegated-agent package route | Parent must supply accepted-work/receipt context; they have no owner-only recording access and are not official defaults until separately adopted |
| Agent skill dependencies | Bind matching installed skills during review, or build with `--skills ../skills` | Missing or disabled dependencies are not silently installed/enabled by the default standalone export |
| Iris primary definition | Inspect/maintain the source snapshot | Native package imports force delegated usage; they cannot replace the built-in primary Iris |
| Default plugin descriptors | Browse and maintain manifests for the existing built-in tools | No executable plugin import/install protocol exists here; the server implementation and any provider/connector setup remain required |

## Product gaps, with source evidence

1. **Normal lley.cat folder links cannot be imported directly.** `core/dyadic_core/workspace/package_sources.py::source` rejects URL query strings and only resolves GitHub/skills.sh repositories or supported direct files. These repos use `/r/<uuid>?path=...&ref=...`. The raw API links also need query strings. A product change would need explicit gateway support, immutable revision resolution, bounded selected-folder downloads and existing public-source checks. Download/build a ZIP locally in the meantime. Private repositories are not made readable by a link.
2. **Raw native agent folders are not portable imports.** `package_imports.py::convert` accepts native package ZIPs or inline agent instructions; it does not join the catalog’s `agent.json` with adjacent `instructions.md`. Ordinary READMEs and instruction Markdown without agent frontmatter are skipped. The builder in this repository resolves this packaging problem without changing Dyadic: it produces a strict `dyadic-package.json` archive with referenced instructions only.
3. **Primary-agent and plugin installation are different capabilities.** `packages.py::inspect` forces imported agents to `usage: delegate`, `memory: false`, `strict_tools: true`, and no implicit MCP servers. Plugin switches in `catalog.py` target built-in implementations; executable plugins cannot be converted into instructions. Extending either capability requires a separately designed product contract, not a looser ZIP or renamed prompt.
4. **Owner-only context does not transfer automatically to subagents.** `tools/builtin/runs.py::interactive` excludes delegated, unattended and API-key contexts. The two new specialists intentionally request no `runs.*` tools. They require evidence from their parent; this is a documented operating boundary, not a claim of a new delegation bridge.
5. **Repository publishing is not catalog synchronization.** The official Store loader reads the product’s local catalog. A push to these repos neither synchronizes that catalog nor upgrades an account’s installed copies. Repository-only additions remain explicitly labeled. A future sync process needs version, provenance, permission-review and update handling.

## Packaging adaptations

The original six default definitions and Iris remain unchanged. `import.json` supplies an explicit portable tool list for each delegate; inherited defaults are not expanded into an unrestricted package. All imported tool suggestions still require the existing owner review. Bundled skill dependencies must match this repo’s reviewed entrypoint and complete-package hashes, including all resources.

The skills builder includes the security suite’s shared standards inside each exported skill and rewrites only their local link prefix in the generated archive. Source files retain their shared layout. Lley operator skills can link to complementary skills; install/read those siblings when their workflow calls for them. Scripts are packaged as resources and are never run by installation or these checks.

## Verification and Actions limits

Each repository has an offline validator, meaningful package tests, deterministic builders, JUnit output and a custom `.lley/pipeline.json` template. Exact execution results are in the delivery report. Parser acceptance is separate from installation into a live account and from a successful model/tool run. No paid provider evaluation, production deployment or APK change is part of this delivery.

All three repository Actions activation gates were disabled when inspected. A PAT can save a valid pipeline configuration but cannot activate it. Local checks can run the same committed commands; hosted execution requires the owner’s activation and an enabled trigger. The template uses manual runs and leaves push/tag triggers off.
