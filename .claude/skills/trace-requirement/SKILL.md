---
name: trace-requirement
description: Trace canvas portal requirement IDs (FR-, NFR-) through the design, UI spec, and test plan, or list requirements with no test. Use when reviewing traceability, writing a test plan, or checking a PR's requirement IDs.
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
  named in the design, UI specification, and test plan. The app's code
  is in the CanSync repo, so search it there.
- A doc split by phase is read as all its files, such as
  `02-requirements_phase0.md` and `02-requirements_phase1.md`. An ID with a
  row in more than one phase file prints each row, with its file name.
- With `--untested [PHASE]`, it lists requirements that no test procedure
  names. Ranges such as "FR-10 to FR-12" count for every ID in them.
- Change logs are skipped, since they mention IDs without tracing them.

A mention is not proof of coverage. Read the lines it prints before saying
a requirement is designed or tested.
