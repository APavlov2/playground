---
id: example-slug                 # slug, unique; matches filename
name: Example Compound (Alias)
aliases: [other-name]
type: compound                   # compound | habit
klass: Cholinergic               # short category label
status: draft                    # draft | reviewed | verified
evidence_overall: 2              # 1–4, see rubric.md; the badge value
onset: ""                        # e.g. "1–3 hours (acute); weeks (cumulative)"
half_life: ""                    # e.g. "~varies"
dose_range: ""                   # compounds only; leave "" for habits
cognitive_domains: []            # e.g. [attention, memory, processing-speed]
channels:                        # SOURCE OF TRUTH for the Atlas — ids must match taxonomy.md
  - channel: ach                 # one of the 12 ids in taxonomy.md
    mechanism: ""                # the molecular/physiological pathway, not the claimed benefit
    evidence: 2                  # 1–4, graded for THIS channel
    population: both             # healthy | deficient | impaired | both
    direction: up                # up | down | modulate
safety:
  contraindications: []
  interactions: []
  notable_risks: []
sources:                         # real, resolvable refs only — no invented PMIDs/DOIs
  - "Author et al., Journal, Year — PMID/DOI"
tags: []
---

## Summary
2–4 sentences: what it is, primary effect, who it helps.

## Mechanism
Per-channel detail, expanded from the frontmatter. Name the pathway for each
channel listed above.

## Evidence
What the human literature actually shows. Note study quality, population, effect
size, and where it is preclinical-only. Grade per the rubric; explain any
down-grades.

## Safety & interactions (research metadata)
Contraindications, known interactions, notable signals. If none, write
`none known`. This is research metadata, not medical advice.

## Open questions
What is unresolved / worth a deeper dive.
