# Evidence Rubric (1–4)

The honesty layer, identical in scale to the brain study. Every channel effect is
graded on this scale, and each entry's `evidence_overall` badge is the grade of its
**best-supported, most relevant** claim. When in doubt, **grade down** and say why.

| Score | Label | Bar |
|-------|-------|-----|
| **4** | Strong | Consistent meta-analyses / well-established human effect |
| **3** | Good | Multiple human RCTs pointing the same way |
| **2** | Emerging | Limited / mixed human data **or** strong preclinical only |
| **1** | Preclinical / anecdotal | Mechanistic, animal, or anecdotal; minimal human support |

## How to apply it

- **Grade per channel.** Each `channels[].evidence` is graded on its own merits. A
  lever can be a 4 on `liver` and a 1 on `rhythm`. Say so.
- **Set the badge.** `evidence_overall` = the grade of the lever's strongest,
  most decision-relevant claim. Not an average.
- **Population gates the grade.** Distinguish effects in the **target picture**
  (MASLD + insulin resistance + obesity) from effects in already-healthy subjects.
  Many supplements only clear bar 3–4 when correcting a deficit or a dysfunction.
- **Preclinical stays preclinical.** A clean mechanistic or rodent story without
  human RCTs is a **2 at most**. "Popular," "traditional," or "natural" is not
  evidence.
- **No invented support.** Every non-trivial claim needs a real, resolvable source
  (PMID/DOI). No support → mark it `unsourced`; never fabricate a citation or an
  effect size.

## Evidence vs. safety — keep them separate

The evidence grade answers *"does it work?"* The `cardiac_safety` block answers
*"is it safe under nebivolol + PVCs + exaggerated BP response?"* These are
**independent axes**:

- Berberine can be **evidence 3–4** on `insulin`/`liver` **and** carry a serious
  cardiac-safety flag (additive BP-lowering, hepatic enzyme competition, rhythm
  signal) at the same time.
- A lever is never described as "recommended" or "safe to start" here — the plan
  reserves that for the cardiologist. Grade the evidence; document the safety;
  leave clearance to the doctor.
