# Audit rules

## Evidence priority

Use evidence in this order:

1. Repository configuration or source at a recorded commit.
2. Official governance, security, release, and contribution documents.
3. Official CI, coverage, release, advisory, and artifact-verification pages.
4. OpenSSF page selections only as leads, never as proof of current implementation.
5. Search snippets only to locate primary evidence.

## Status rules

- Use `Met` only when evidence addresses every material clause and time window.
- Use `Unmet` when a canonical file lacks a required element, a threshold is below target, or a mechanism is demonstrably absent.
- Use `N/A` only if the criterion permits it; explain why the trigger does not apply.
- Retain `?` when proof depends on private settings, private incidents, unperformed empirical testing, or an unaudited repository-wide claim.
- A SHOULD/SUGGESTED item may be `Unmet`; it still needs justification.

## Dependency line

End every decided block with:

```text
[dependancy]: <why this status is correct>. <direct evidence URL/path>
```

Prefer stable blob URLs. Record a commit SHA when branch URLs are used. Use multiple links when the requirement spans repositories.

## Improvement line

End every `Unmet` block with an actionable path to `Met`:

```text
[improvement]: <concrete next steps plus the canonical file/path to change>
```

- Name the exact document, workflow, or configuration to add or change; do not repeat the evidence already given in `[dependancy]`.
- State what the change must demonstrate so the criterion can be re-verified as `Met`.
- Add this line only to `Unmet`; `Met`, `N/A`, and unresolved `?` blocks do not get one.
- A MUST gap blocks the badge level, so describe the minimal compliant change first; a SHOULD/SUGGESTED gap still needs a realistic improvement path.
- The plan does not prove compliance: re-verify against direct evidence before changing the status.

## Status detail documents

After filling `structure.md`, produce one markdown document per non-Met status (`unmet.md`, `na.md`, `unknown.md`) that records every criterion in that status. Each entry includes the criterion id, MUST/SHOULD level, a plain-language summary of the requirement, the involved files, and the same evidence as the corresponding `structure.md` block:

- `Unmet`: why it fails, the concrete path to `Met` (mirror its `[improvement]` line), and the files to change.
- `N/A`: why the official trigger does not apply, and the evidence that the trigger is absent.
- `?`: exactly what public or private evidence is missing and the next verification step (e.g., maintainer confirmation, empirical test, sample statistics).

Keep counts and status splits identical to `structure.md` and the audit summary. The documents summarize decisions; never introduce new statuses or contradict the summary.

## Difficult cases

- **DCO/CLA**: require a legal statement, sign-off instructions, meaning, and enforcement.
- **Access continuity**: multiple maintainers do not prove redundant control of domains, registries, release secrets, and private channels.
- **Bus factor**: active maintainers from multiple organizations plus ownership evidence can support `Met`.
- **Roadmap**: cover at least the next year from the audit date and describe intended and excluded scope.
- **Security requirements**: deployment hardening advice is not enough; document guarantees and non-guarantees.
- **Accessibility**: do not infer WCAG compliance from a framework; require audit/test evidence.
- **Vulnerability credit**: query the exact preceding 12 months, then request confirmation of private records.
- **Regression tests**: require a reproducible six-month bug-fix sample and numerator/denominator.
- **Coverage**: use current project statement coverage, not patch coverage.
- **Repeatable build**: inspect timestamps, archives, paths, and build ids.
- **Signed release**: checksums are not signatures; require verification instructions.
- **Signed tag**: signed commits or artifacts do not prove the tag object is signed.
- **Input validation**: examples do not prove all trust boundaries use allowlists.
- **Memory-unsafe analysis**: Go/Rust can normally use `N/A` without delivered C/C++ or equivalent code; explain CGO/FFI scope.

## Preservation

- Never overwrite an existing `structure.md` during generation.
- Hash and back up a file before in-place auditing.
- Preserve user prose and order.
- Modify known statuses only when requested or contradicted by direct evidence.
- Keep unresolved items visible instead of manufacturing certainty.
