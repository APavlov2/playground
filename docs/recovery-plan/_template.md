---
id: example-slug                 # slug, unique; matches filename
name: Example Lever (Alias)
aliases: []
type: compound                   # compound | habit
klass: Metabolic                 # short category label
tier: 1                          # 1 | 2 | optional | rx | avoid  (maps to PLAN.md tiering)
status: draft                    # draft | reviewed | verified
evidence_overall: 2              # 1–4, see rubric.md; the badge value
onset: ""                        # e.g. "weeks (cumulative)"
half_life: ""                    # compounds only
dose_range: ""                   # compounds only; leave "" for habits
target_metrics: []               # e.g. [waist, liver-enzymes, triglycerides, resting-bp]
channels:                        # SOURCE OF TRUTH for the Atlas — ids must match taxonomy.md
  - channel: insulin             # one of the 12 ids in taxonomy.md
    mechanism: ""                # the molecular/physiological pathway, not the claimed benefit
    evidence: 2                  # 1–4, graded for THIS channel
    population: target           # target | healthy | both   (target = MASLD + IR + obesity)
    direction: up                # up | down | modulate
cardiac_safety:                  # FIRST-CLASS overlay — fill every field or mark "none known"
  beta_blocker_interaction: ""   # interaction with nebivolol / beta-blockade
  bp_effect: ""                  # raises | lowers | neutral — and why it matters here
  rhythm_signal: ""              # PVC / palpitation / arrhythmia signal, either direction
  hepatic_load: ""               # liver-enzyme competition / hepatotoxicity risk
  sign_off_required: false       # true if PLAN.md gates it behind cardiologist approval
safety:
  contraindications: []
  interactions: []
  notable_risks: []
sources:                         # real, resolvable refs only — no invented PMIDs/DOIs
  - "Author et al., Journal, Year — PMID/DOI"
tags: []
---

## Summary
2–4 sentences: what it is, primary effect on the metabolic/cardiac cluster, and how
it fits the master lever (visceral fat loss).

## Mechanism
Per-channel detail, expanded from the frontmatter. Name the pathway for each
channel listed above (e.g. AMPK activation, hepatic de novo lipogenesis, GLUT4
translocation, vagal tone).

## Evidence
What the human literature actually shows. Note study quality, population (target vs
healthy), effect size, and where it is preclinical-only. Grade per the rubric;
explain any down-grades.

## Cardiac safety (under nebivolol + PVCs + exaggerated BP response)
Expand the `cardiac_safety` block in prose: beta-blocker interaction, BP effect,
rhythm/PVC signal, hepatic load, and whether this needs cardiologist sign-off before
starting. This section is load-bearing — do not skip it.

## Safety & interactions (research metadata)
Other contraindications, interactions, notable signals. If none, write `none known`.
Research metadata, not medical advice or clearance.

## Open questions
What is unresolved / worth a deeper dive.
