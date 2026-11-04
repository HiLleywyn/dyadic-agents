# Three-Repository Delivery Report

[Agents](README.md) · [Skills](https://git.lley.cat/r/1a151e58-468a-45f1-a028-92c95690ad68?ref=store) · [Plugins](https://git.lley.cat/r/ae86ea71-cb4d-4fc5-9ec1-803f8f303989?ref=store)

The three collections are consolidated on separate `store` branches, ready for review. Each branch was created after fetching and integrating its latest `main`; no Dyadic product changes are included. The existing main branches remain unchanged.

## Contents

- **Skills: 59 packages.** Existing platform/workflow layout retained, the 23 official Iris packages matched to the current inspected source, four new native-context workflows and one catalog-maintenance operator skill. Security exports include their shared standards.
- **Agents: nine definitions.** Iris under `agents/`, six unmodified official specialists and two focused additions under `subagents/`. Eight delegates have portable exports; Iris remains a primary source definition. Every folder describes its role, tool policy, dependencies, origin and import route.
- **Plugins:** all 40 default Dyadic descriptors, individual descriptions/permissions and a navigable catalog. Backend implementations and credentials are outside this collection.
- **All three:** cross-links, machine-readable inventories, source-path/hash provenance, maintenance instructions, deterministic package builders, executable tests and offline custom Actions templates.

## New material

| Addition | Concrete job |
| --- | --- |
| Current Work Revision | Preserve accepted constraints, exact versions and unresolved items through a requested follow-up and Patch |
| Artifact Handoff | Distinguish generation, persistence, package/attachment delivery and visible presentation; locate a missing step |
| Receipt Reconciliation | Explain interrupted runs without conflating execution, accounting estimates, provider receipts or parent/child charges |
| Source Conflict Review | Resolve conflicting supplied documents and accepted requirements without silently expanding the source boundary |
| Catalog Maintenance | Maintain these three collections, immutable provenance, dependency locks, exports and honest compatibility reports |
| Artifact Auditor | Read-only specialist that checks a claimed handoff against files and parent-supplied receipts |
| Continuity Reviewer | Read-only specialist that identifies lost accepted constraints, owner edits and stale verification |

The four workflow skills are under `skills/dyadic/workflows`; the operator skill is under `skills/dyadic/operators`. New agents are marked repository-authored. None is presented as an already deployed official default.

## Verification

| Collection | Offline Linux checks | Built archives |
| --- | --- | --- |
| Skills | 64 passed; no failures, errors or skips | 59 individual skill ZIPs |
| Agents | 17 passed; no failures, errors or skips | Eight standalone delegate ZIPs, plus eight optional dependency-bundled variants |
| Plugins | 45 passed; no failures, errors or skips | 40 descriptor ZIPs |

The **126 collection checks** cover snapshot integrity, catalog/navigation validity, deterministic archive bytes, unsafe paths, package structure, primary-versus-delegated export handling and dependency locks including supporting resources. They ran offline in the same pinned Linux image declared by the Actions templates. [JUnit cases and receipts](verification/README.md) record the actual runs; the other two repositories contain their own evidence directories.

An additional **116 compatibility checks passed** against the existing, unmodified Dyadic checkout at `26ea591af225ed48129a1968db78b3e8f335dc90`: 59 skills, eight standalone agents, eight bundled-agent variants, 40 default plugin switches and one complete-set comparison. See [the compatibility results](verification/dyadic-compatibility.json) and [bundled package checksums](verification/bundled-package-checksums.json). The existing package inspector accepted the skill/agent bytes and enforced strict delegated imports with memory off. All five new skills also passed the skill-creator validator, and the existing 12-skill security suite validator passed.

All three Actions templates passed the live gateway’s configuration preview. They use manual triggers, no network, no credentials and no deployment stage. **Hosted Actions were not run:** the repositories’ activation gates are disabled and the templates have not been applied to their server configurations. Applying the reviewed template and owner activation are separate follow-up steps. A PAT cannot bypass the owner activation gate.

No live account installation, paid inference, provider integration, physical-device check, Dyadic deployment or APK rebuild was performed. The compatibility checks establish parser/catalog acceptance, not end-to-end agent quality or provider availability.

## Integration limits

The practical route is to upload an individual built skill or native agent ZIP for review. Normal lley.cat folder URLs are rejected by the inspected Dyadic URL resolver. Raw catalog agent pairs need packaging; this repo provides it. Primary Iris replacement, executable plugin installation and automatic repository-to-Store synchronization are not supported by the inspected contracts. Delegates need parent-supplied owner-only context.

See [the compatibility report](COMPATIBILITY.md) for concrete source references, adaptations and remaining boundaries. Those are product follow-ups, not changes hidden in this repository work.

## Practical use

Clone the relevant `store` branches, run the documented validator/build commands, and upload an individual skill or native agent ZIP for review. Extract `dist/collection.zip` before choosing a component. For an agent bundle with its actual resources, build with `--skills ../skills`; entrypoint and complete-package hashes must match the reviewed dependency lock. Plugin archives preserve catalog metadata for the existing runtime and do not install provider code.

The next Dyadic work, if separately requested, should start on its own `store` branch after updating from `main`. Highest priority is the public lley.cat source resolver; raw folder conversion and a deliberate catalog-sync contract follow. Primary-agent replacement and executable plugin installation need explicit product design rather than a permission shortcut.
