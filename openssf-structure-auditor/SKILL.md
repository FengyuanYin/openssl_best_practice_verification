---
name: openssf-structure-auditor
description: Generate a rule-preserving structure.md from an OpenSSF Best Practices project criteria page, then inspect the project's source repositories and fill each criterion with Met, Unmet, N/A, or ? plus evidence. Use when auditing an OpenSSF Passing/Silver/Gold questionnaire, completing an existing structure.md without rewriting its prose, producing evidence-backed badge answers, or validating that every decided item has a [dependancy] line.
---

# OpenSSF Structure Auditor

Follow the workflow in order. Treat the OpenSSF page as the source of criterion text, the repository as the source of project facts, and `structure.md` as a user-owned artifact whose existing prose must be preserved.

## Step 0: Collect inputs and protect existing work

Obtain the exact OpenSSF criteria URL, source repository URL, any separate community/website/security repositories, and the target `structure.md` path.

If `structure.md` already exists:

1. Read it completely and record its SHA-256.
2. Do not run the generator with `--force`.
3. Preserve every existing sentence, heading order, blank explanatory section, and user-added note unless the user explicitly requests a rewrite.
4. Change only status tokens and append `[dependancy]:` evidence when auditing unknown entries.

Use `assets/structure-template.md` only to learn the expected style and rules. Never copy its Karmada-specific decisions into a different project.

## Step 1: Install script dependencies

Create an isolated environment in the task workspace, not inside the user's source repository:

```powershell
python -m venv .openssf-audit-venv
.\.openssf-audit-venv\Scripts\python.exe -m pip install -r <skill-dir>\requirements.txt
```

On POSIX systems use `.openssf-audit-venv/bin/python`. Reuse an environment only when `requests` and `beautifulsoup4` import successfully.

## Step 2: Read the OpenSSF page and generate the skeleton

When no target file exists, run:

```powershell
python <skill-dir>\scripts\fetch_structure.py `
  --url "<openssf-project-level-url>" `
  --output "<target>\structure.md"
```

The default sets every item to `[?]` so stale self-certification is not treated as current truth. Use `--status-source page` only when the user explicitly wants the page selections copied.

If network access fails, browse or download the exact page through an available browser/web tool, save the HTML locally, and pass a `file:///...` URL. If `structure.md` exists, skip generation and continue with it. The generator must refuse to overwrite it.

## Step 3: Inspect repositories before deciding statuses

Read `references/audit-rules.md` before the first audit. Then:

1. Record the inspected commit SHA and audit date.
2. Read repository instructions such as `AGENTS.md`.
3. Use `rg`/`rg --files` to locate governance, contribution, security, release, CI, test, coverage, dependency, signing, architecture, and roadmap evidence.
4. Inspect linked community and website repositories when documentation is delegated there.
5. Query time-sensitive public evidence when needed: current releases, advisories, coverage badges, signed tags, supported branches, and live project pages.
6. Prefer direct source files and official project pages over summaries.
7. Never infer private access continuity, private vulnerability history, or organization settings from public membership lists alone.

Audit criteria in document order and work section by section.

## Step 4: Fill `structure.md` according to its rules

For each `[?]`:

1. Identify the criterion keyword and whether N/A is allowed.
2. Gather direct evidence.
3. Choose exactly one status:
   - `[Met]`: sufficient evidence proves every material clause.
   - `[Unmet]`: evidence proves the practice is missing or insufficient.
   - `[N/A]`: the official criterion allows N/A and its trigger does not apply.
   - `[?]`: public evidence is insufficient; do not guess.
4. Replace only the status token in the third-level heading.
5. Append the final line of the criterion block:

```text
[dependancy]: <concise reasoning plus direct URLs or repository paths>
```

6. For negative conclusions, cite the canonical location and state what required element is absent.
7. For time-window criteria, include the cutoff date and request maintainer confirmation of private records.

Do not add `[dependancy]` to unresolved `[?]`. Do not mark an item Met merely because the OpenSSF page selected Met. Use `apply_patch` for controlled edits and reread each edited section.

## Step 5: Validate rules and preservation

Run:

```powershell
python <skill-dir>\scripts\validate_structure.py "<target>\structure.md"
```

Fix all errors. Warnings for missing machine-readable criterion ids can remain when the user's original text omitted an id.

When a truth document is available, evaluate it:

```powershell
python <skill-dir>\scripts\evaluate_against_truth.py `
  --candidate "<candidate-structure.md>" `
  --truth "<truth-structure.md>"
```

For a freshly generated all-unknown skeleton, add `--skeleton`. Confirm generation against an existing path fails without changing its hash. For an in-place audit, review the diff and confirm existing prose changed only where authorized.

## Step 6: Decide completion

Complete a run only when:

- Validator errors are `0`.
- Dependency coverage for decided criteria is `100%`.
- Existing-file preservation is `100%`.
- Structural recall against supplied truth is at least `95%`.
- Decision recall against supplied truth is at least `80%` of truth-decided entries.
- Status agreement against supplied truth is at least `90%` for comparable decided entries.

Unknown entries are acceptable only when the fact requires private state, an empirical audit, or a maintainer decision. List each remaining `[?]`, missing evidence, and next verification step.

## Resources

- `scripts/fetch_structure.py`: fetch and parse criteria; refuse overwrite by default.
- `scripts/validate_structure.py`: enforce status and evidence rules.
- `scripts/evaluate_against_truth.py`: calculate completion metrics.
- `scripts/test_skill.py`: deterministic regression tests.
- `references/audit-rules.md`: evidence hierarchy and difficult decisions.
- `assets/structure-template.md`: immutable style/truth fixture.
