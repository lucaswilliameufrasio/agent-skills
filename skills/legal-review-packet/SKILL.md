---
name: legal-review-packet
description: >-
  Prepare drafts and questions for a lawyer's opinion and send them as one
  readable packet. Use when a feature, policy, contract clause, or product
  decision needs legal validation before release; when asked to write a clause
  draft ("minuta") for counsel; or to gather every open legal question into a
  single PDF to share by chat or e-mail. Never present the drafts as legal advice
  and never mark a review as done without the actual opinion.
---

# Legal review packet

Engineering and product can draft the questions and the clause text; only
counsel can give the opinion. The goal is a packet a lawyer can read without
repository access: what is being decided, the proposed text, and the exact
questions, with the risky points called out.

## 1. Gather every open legal question first

Before writing, search the places the project records pending legal work, so
counsel gets everything at once instead of one item per message:

- clause drafts and policy drafts marked as pending review (front matter such as
  `review: pending-legal`, "draft", "minuta", "não é parecer jurídico");
- tracker issues whose acceptance criteria say "legal validation", "parecer",
  "jurídico", "counsel", "DPIA/RIPD" or name a regulation article;
- features already shipped behind a flag that waits for the opinion, and
  features already **live** whose card asked for validation before release
  (report these first: they carry present risk);
- decision records that postponed legal review.

Read each source; do not list an item from a keyword hit alone. A card that
only mentions privacy is not a legal question unless it asks counsel to decide
something. Write each item as one question counsel can answer, with the tracker
or file reference.

## 2. Write each clause draft with a fixed shape

Keep drafts in the repository (versioned, reviewable) and export them, never the
other way around. Use [the draft template](references/clause-draft-template.md):

1. Front matter: title, `status: draft`, owner, contract, `review: pending-legal`,
   updated date.
2. A disclaimer that it is a technical and product draft, **not a legal opinion**,
   and what stays blocked until the opinion (for example a feature flag that
   stays off until the opinion and the clause are in the contract).
3. Objective: who decides and who answers for the decision (usually the party
   that acts, not the platform), in plain words.
4. Point of attention: the rule or right the clause must stay compatible with,
   and the product limits that keep it compatible (what is never affected).
5. Suggested clauses, numbered (1.1, 1.2 …): what the party may do, what it does
   not do, what the affected people see, what is recorded, who is responsible,
   and how the party commits to use it.
6. Open questions for counsel, one per line.

Describe the behavior the product actually has. Do not promise a duration,
appeal channel, or notice that is not built; list it as a question instead.

## 3. Build the packet

One PDF, in the reader's language:

1. **Cover**: date, one paragraph of context, and the numbered questions grouped
   by urgency: already live, ready but switched off, needs a decision before
   building. Each question names its reference.
2. One section per clause draft, each starting on a new page.
3. Annexes with longer drafts (terms, privacy policy) when they are part of the
   request.

Use [`scripts/build_packet.mjs`](scripts/build_packet.mjs): it turns a cover
Markdown and a list of Markdown files into an A4 PDF (front matter removed,
relative links reduced to text, page break per file). It needs Node with the
`marked` package and a Playwright Chromium; run it from a project that already
has them instead of installing packages globally:

```sh
node build_packet.mjs --out packet.pdf --cover cover.md draft-a.md draft-b.md
```

Open the PDF and check the cover and at least one clause page before sharing.

## 4. Share and record

- A private repository link does not open for an outside lawyer: send the PDF.
  Say where the file is and give a copy command if it must move between machines.
- Sending to counsel is the person's action; do not send messages or e-mails
  on their behalf unless asked.
- Keep the review state honest: the draft stays `pending-legal`, the flag stays
  off, and the tracker item stays open until the opinion arrives. When it does,
  update the clause, attach or reference the opinion, then change the state.

## Avoid

- Calling a draft "approved", "compliant" or "reviewed" without the opinion.
- Inventing legal conclusions, article numbers or obligations; quote the source
  the project already cites and ask counsel about the rest.
- Sending partial packets when the request is "everything pending".
- Hiding live risk: shipped features that skipped a requested validation go at
  the top of the cover.
