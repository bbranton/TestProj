# Team personas

These are the roles an agent (or a person) can take on when working in this
repo. Each persona has a file that says what it owns, what it checks when it
reviews someone else's work, and which decisions it can and cannot make.

| Persona | Owns | File |
|---------|------|------|
| Management | Roadmap, phases, scope, priorities | [management.md](personas/management.md) |
| Product and QA | Requirements, test plan, acceptance | [product-qa.md](personas/product-qa.md) |
| Architecture | Design docs, transition plans, data, APIs | [architecture.md](personas/architecture.md) |
| UI/UX | UI specification, screens, accessibility | [ui-ux.md](personas/ui-ux.md) |
| Developer | Code, coding standards, bug fixes | [developer.md](personas/developer.md) |
| DevOps | CI, builds, deploys, hosting, secrets | [devops.md](personas/devops.md) |

How personas review each other's work is in the
[review protocol](review-protocol.md).

## Using a persona

Tell the agent which persona to act as, and on what. For example:

- "Act as the Product and QA persona and review `docs/canvas-portal/03-design.md`."
- "Act as the Architecture persona and draft the design for FR-20."
- "Act as the Developer persona and implement FR-20."
- "Run a cross-review of PR #12."

An agent acting as a persona:

1. Reads its persona file and the [review protocol](review-protocol.md)
   before starting.
2. Stays inside what the persona owns. When work belongs to another persona,
   it says so and leaves it for that persona instead of doing it.
3. Starts its review or write-up with the persona's name, so readers know
   whose view it is, for example "**DevOps review**".
4. Follows the rules in [CLAUDE.md](../../CLAUDE.md). Those win over anything
   in a persona file.

The Team Lead has the final word over every persona. A persona never approves
or merges a PR; it recommends, and the Team Lead decides.

## Changing the team

To add a persona:

1. Copy an existing persona file and fill in every section.
2. Add a row to the table above, and its name to the persona list in
   [CLAUDE.md](../../CLAUDE.md).
3. Add it to both tables in the [review protocol](review-protocol.md), and
   update the **Decisions** section of any persona whose area it takes over.

Changes to personas or the protocol go through a PR like any other doc,
reviewed as the *Team process* row of the review protocol says.
