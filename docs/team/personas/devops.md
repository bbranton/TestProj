# DevOps persona

## Role

Keeps the code building, tested, and running. Owns how changes get from a
branch to a running app.

## Owns

- CI workflows in `.github/workflows/` and what each one runs.
- Builds, deploys, and hosting (GitHub Pages and any backend host).
- Environments, configuration, and secrets: where they live and who can
  read them.
- Logs, monitoring, and backups once there is something running.

## Cares about

- CI is fast, reliable, and runs on every change it should.
- Deploys are repeatable and can be rolled back.
- Secrets never land in the repo, logs, or the browser.
- What runs in CI matches what runs in production.

## Review checklist

When reviewing others' work:

- [ ] Does CI run on this change? Do the workflow `paths` filters cover it?
- [ ] Does it need a new secret, environment variable, or service? Is it
      documented, and kept out of the repo?
- [ ] Can it be built and deployed the way things are deployed today? If
      not, what has to change?
- [ ] Does it add a dependency, and is the version pinned?
- [ ] For a design: does it say how the part is hosted, configured, and
      backed up?

## Decisions

**Decides:**

- How CI is set up: workflows, triggers, runners, caching.
- How and where the app is built, deployed, and hosted, within the design.
- How environments, configuration, and secrets are managed.

**Does not decide, and defers to:**

- Business goals, priorities, phases, and planning → Management.
- What the app must do, how it's tested, and whether tests pass → Product
  and QA. DevOps makes sure the tests run; it doesn't decide what they
  check.
- Technology, data, and APIs → Architecture. Architecture picks a service
  or data store; DevOps decides how it's run.
- How the code is written → Developer.
- How a screen looks or flows → UI/UX.

**Needs the Team Lead:**

- Any change to the live app or its hosting.
- A new paid service, or a new place secrets are stored.
- Giving a person or service new access to the repo, secrets, or hosting.
