# Cost log

What each thread actually cost, so Management can estimate new work from
real numbers. Management owns this file; every thread adds its own row.
How to add a row is in the [`log-cost` skill](../../.claude/skills/log-cost/SKILL.md),
and how estimates use it is in
[Management's cost plans](personas/management.md#cost-plans).

## Size units

Size a piece of work by what an agent can count:

- **Threads:** owner and reviewer threads it took.
- **PRs:** pull requests it opened.
- **Rounds:** review or feedback rounds, counting each batch of comments
  the owner answered with a push.
- **Files:** files changed across its PRs.

## Log

Tokens are in thousands (K) or millions (M). *Cache read* is context the
thread re-read on each turn, and is usually most of the cost.

| Date | PR | Thread | Persona | Threads / PRs / rounds / files | Output | Cache read | Cache write | Cost (USD) | Notes |
|------|----|--------|---------|--------------------------------|--------|------------|-------------|------------|-------|
| 2026-10-25 | #10, #11 | Owner | (none; set up the team) | 1 / 2 / ~16 / 27 | 95K | 25.9M | 0.27M | 11.08 | Taken just before merge. Long thread with many small rounds; docs and small scripts only, no app code. |
| 2026-10-25 | #4 (and #5, handed off) | Owner | Management | 1 / 2 / 4 / 3 | 57K | 10.6M | 0.39M | 7.31 | Taken before review, so review rounds aren't included yet. Read all five docs up front; also opened the requirements PR (#5) before the switch to one thread per doc, then handed it off. Docs only. |
| 2026-10-25 | #12 | Owner | Management | 1 / 1 / 0 / 7 | n/a | n/a | n/a | n/a | Usage numbers weren't in the session data (`external_metadata.usage` missing), so none are logged. Docs only. |
| 2026-10-25 | (this PR) | Owner | Management | 1 / 1 / 0 / 14 | n/a | n/a | n/a | n/a | Usage numbers weren't in the session data (`external_metadata.usage` missing). Docs only, plus 8 follow-up issues (#16 to #23) from reading the open doc PRs. |
| 2026-10-25 | #6 | Owner | Product and QA | 1 / 1 / 4 / 3 | 35K | 6.5M | 0.17M | 3.66 | Taken before merge. Took over #5 from the roadmap thread; four rounds (second pass, business analyst pass, test plan findings, persona policies). Docs only. |
| 2026-10-26 | #4 | Owner | Management | 5 / 1 / 4 / 3 | 111K | 32.1M | 0.46M | 13.77 | Change since the 2026-10-25 #4 row (whole thread: 168K / 42.7M / 0.85M / $21.08). Long thread: a mid-review scope change (deploy every phase), hosting cost research with DevOps (Pages, Pipedream, Neon, free hosts), two decision cards, a Security review added at the end, and two master merges. Threads count the owner plus four reviewers, whose rows follow. With them, #4 cost about $31.61 in all. Docs only. |
| 2026-10-26 | #4 | Reviewer | DevOps | 1 / 0 / 1 / 0 | 65K | 6.75M | 0.15M | 4.05 | One review (5 findings) and a check of the fixes, then four follow-up research rounds for the Team Lead on hosting: deploying every phase, Pages vs one host, Pipedream, Neon, and free hosts. The web research (about 20 doc fetches) is most of the cost beyond the review itself. |
| 2026-10-26 | #4 | Reviewer | Product and QA | 1 / 0 / 2 / 0 | 22K | 3.5M | 0.11M | 2.33 | Two review rounds: Changes needed, then Recommend with notes. Most first-round inline comments went out inside the Architecture review because both reviewers share one GitHub pending review. Docs only. |
| 2026-10-26 | #4 | Reviewer | Architecture | 1 / 0 / 2 / 0 | 18K | 3.3M | 0.11M | 2.00 | Review plus one re-review; docs only. Its first review also carried Product and QA's inline comments, because both threads post from one GitHub account. |
| 2026-10-26 | #4 | Reviewer | Security | 1 / 0 / 2 / 0 | 23K | 3.28M | 0.11M | 2.15 | Review and one re-review, added by the Team Lead at the end. Opened #25 and #26. Docs only. |
| 2026-10-26 | (this PR) | Owner | DevOps | 1 / 1 / 0 / 2 | n/a | n/a | n/a | n/a | Usage numbers weren't in the session data (`external_metadata.usage` missing). Repo settings change, blocked for sessions, so the Team Lead applies it; notes only. |
| 2026-10-26 | #6 | Owner | Product and QA | 1 / 1 / 9 / 3 | 146K | 49.4M | 1.03M | 22.66 | Change since the 2026-10-25 row, after merge. Reviews by Architecture, Management, UI/UX, and Security, each with a re-review; five rounds of Team Lead answers, including the Phase 1 scope cuts; changes relayed to the UI spec, test plan, design, and roadmap threads. Long thread with many cross-thread messages. Docs only. |
| 2026-10-26 | #27 (GraphQL), #32 | Owner | Management | 1 / 2 / 3 / 1 | 38K | 27.0M | 1.10M | 15.55 | Change since the 2026-10-26 #4 row (whole thread now 206K / 69.7M / 1.95M / $36.63). Follow-ups after #4: GraphQL to Phase 5, then several rounds aligning the roadmap with requirements #6 as its phases changed (UI spec review, Chrome only, Phase 1 scope cut), plus the glossary link. Long-lived thread, so cache reads dominate. Docs only. |
| 2026-10-26 | #31 | Owner | Product and QA | 1 / 1 / 2 / 9 | 22K | 4.09M | 0.21M | 3.32 | After merge. New glossary moved out of the canvas portal README; screen words came from the UI spec thread. Two small rounds added "orphaned card" and "archived card" from the PR #8 and #32 reviews. No reviewer threads ran. Docs only. |
| 2026-10-26 | #6 | Reviewer | Management | 1 / 0 / 2 / 0 | 34K | 9.5M | 0.28M | 4.80 | Review (Changes needed) and one re-review (Recommend with notes); opened #36 and #37. After the re-review it also handled the Team Lead's Phase 1 scope cuts (single Backlog list, course buttons, NFR-1, Excused). Row added by the owner thread. Docs only. |
| 2026-10-26 | #6 | Reviewer | Architecture | 1 / 0 / 2 / 0 | 33K | 8.99M | 0.31M | 4.93 | Review and one re-review; opened #33 and #34. An API error cut the first turn, which resumed an hour later. Also checked the Phase 1 scope cuts against the design and passed changes to the design thread for #7. Row added by the owner thread. Docs only. |
