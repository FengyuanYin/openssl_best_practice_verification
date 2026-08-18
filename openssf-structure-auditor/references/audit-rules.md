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
