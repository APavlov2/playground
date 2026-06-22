# Evidence Rubric (1–4)

The honesty layer. Every channel effect is graded on this scale, and each entry's
`evidence_overall` badge is the grade of its **best-supported, most relevant**
claim. When in doubt, **grade down** and say why in the body.

| Score | Label | Bar |
|-------|-------|-----|
| **4** | Strong | Consistent meta-analyses / well-established human effect |
| **3** | Good | Multiple human RCTs pointing the same way |
| **2** | Emerging | Limited / mixed human data **or** strong preclinical only |
| **1** | Preclinical / anecdotal | Mechanistic, animal, or anecdotal; minimal human support |

## How to apply it

- **Grade per channel.** Each `channels[].evidence` is graded on its own merits.
  A compound can be a 4 on one channel and a 1 on another. That is normal and
  expected — say so.
- **Set the badge.** `evidence_overall` = the grade of the agent's strongest,
  most decision-relevant claim. It drives the Atlas badge. It is **not** an
  average of the channels.
- **Population gates the grade.** Distinguish effects in *healthy / optimising*
  subjects from *deficiency-correction* in deficient/impaired subjects. Many
  compounds only clear bar 3–4 when correcting a deficit and drop to 1–2 in
  already-replete healthy people. Record this in `channels[].population` and the
  body.
- **Preclinical stays preclinical.** A strong mechanistic or animal story without
  human RCTs is a **2 at most** (a `1` if it is purely mechanistic/anecdotal).
  "Popular," "widely used," or "ancient remedy" is **not** evidence.
- **No invented support.** Every non-trivial claim needs at least one real,
  resolvable source (PMID/DOI). If you cannot find support, mark the claim
  `unsourced` in the body and grade accordingly — do **not** fabricate a citation
  or an effect size.

## Worked intuition

- Meta-analysis of RCTs showing a consistent effect → **4**
- Two or three decent RCTs agreeing, no meta-analysis yet → **3**
- One small RCT, or mixed RCTs, or only rodent data however clean → **2**
- "Mechanism suggests it should work" / forum reports only → **1**
