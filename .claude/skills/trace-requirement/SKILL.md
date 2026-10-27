---
name: trace-requirement
description: Trace canvas portal requirement IDs (FR-, NFR-) through the design, UI spec, test plan, and code, or list requirements with no test. Use when reviewing traceability, writing a test plan, or checking a PR's requirement IDs.
---

# Trace a requirement

Mostly used by the requirements engineer and test engineer personas, and by any reviewer checking
that a PR's requirement IDs are real and covered.

Run from the repo root:

```sh
python3 team/QA/scripts/trace.py FR-12 NFR-10
python3 team/QA/scripts/trace.py --untested 1
```

- With IDs, it prints each requirement's text and phase, then where it is
  named in `03-design.md`, `04-ui-specification.md`, `05-test-plan.md`, and
  the code under `canvas-portal/`.
- With `--untested [PHASE]`, it lists requirements that no test procedure
  names. Ranges such as "FR-10 to FR-12" count for every ID in them.
- Change logs are skipped, since they mention IDs without tracing them.

A mention is not proof of coverage. Read the lines it prints before saying
a requirement is designed or tested.
