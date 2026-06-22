---
id: circadian-consistency
name: Circadian regularity (consistent sleep-wake timing)
aliases:
  - "sleep regularity"
  - "sleep regularity index"
  - "SRI"
  - "consistent sleep schedule"
  - "social jetlag (inverse)"
type: habit
klass: Sleep
origin: natural
source: "Behavioral / circadian — sleep"
status: draft
evidence_overall: 3
onset: "Phase realignment over days; cognitive/mood effects within days-to-weeks; dementia-risk signal accrues over years"
half_life: ""
dose_range: ""
cognitive_domains: [attention, processing-speed, executive-function, mood, emotional-regulation, neuroprotection]
channels:
  - channel: hpa
    mechanism: "Regular sleep-wake timing entrains the suprachiasmatic-nucleus master clock, which gates the cortisol awakening response and the diurnal cortisol rhythm. Irregular timing / social jetlag flattens or misaligns the cortisol curve and produces circadian misalignment of HPA output. Direction is modulate (restore proper phase/amplitude)."
    evidence: 3
    population: both
    direction: modulate
  - channel: glymph
    mechanism: "Glymphatic flux is itself circadian-gated (peaks in the rest phase, AQP4-dependent in animal models). Stable sleep-wake timing aligns the clearance window with consolidated sleep; chronic misalignment is hypothesized to blunt it. Human clearance evidence is indirect (regularity ↔ dementia/brain-volume associations); the circadian-gating mechanism is animal."
    evidence: 2
    population: both
    direction: up
  - channel: ser
    mechanism: "The serotonergic raphe both receives SCN input and feeds back onto the clock; circadian disruption / social jetlag is associated with depressive symptoms and mood dysregulation, and regular timing supports stable mood. Mechanism is partly inferred; direction modulate."
    evidence: 2
    population: both
    direction: modulate
  - channel: inflam
    mechanism: "Circadian misalignment (shift-work / social-jetlag models, forced desynchrony) raises inflammatory markers and impairs glycemic control; regular timing is associated with lower inflammatory load. CNS-specific link inferred from peripheral and shift-work data."
    evidence: 2
    population: both
    direction: down
safety:
  contraindications: []
  interactions:
    - "Evening bright/blue light, late caffeine, and late large meals delay circadian phase and undermine regularity"
    - "Shift work and frequent time-zone travel impose misalignment that behavioral regularity can only partly offset"
  notable_risks:
    - "Sleep-regularity–dementia association is U-shaped: extreme rigidity scores high regularity but the protective signal plateaus — the actionable target is avoiding high irregularity, not maximizing a regularity score"
    - "Observational evidence dominates; reverse causation (early neurodegeneration disrupting rhythms) is plausible"
sources:
  - "Yiallourou et al. (Pase group), Neurology, 2024 — PMID:38165323, DOI:10.1212/WNL.0000000000208029 (UK Biobank, ~88,000; U-shaped SRI–dementia, HR ~1.53 at 5th percentile of regularity)"
  - "Wittmann et al., Chronobiology International, 2006 — PMID:16687322, DOI:10.1080/07420520500545979 (defines 'social jetlag'; links misalignment to poorer sleep/wellbeing)"
  - "Hablitz et al., Nature Communications, 2020 — PMID:32879313, DOI:10.1038/s41467-020-18115-2 (circadian/AQP4-gated glymphatic flow — mouse)"
  - "Xie et al., Science, 2013 — PMID:24136970, DOI:10.1126/science.1241224 (sleep-dependent metabolite clearance — mouse; supports the clearance-window concept)"
tags: [sleep, circadian, sleep-regularity, social-jetlag, dementia-prevention, chronobiology]
---

## Summary
Circadian regularity — going to sleep and waking at consistent times day to day — is emerging as an independent brain-health lever, separable from how *long* or how *deep* you sleep. The day-to-day consistency of the sleep-wake pattern (captured by the Sleep Regularity Index, SRI) shows a U-shaped association with dementia risk in a very large cohort: the most *irregular* sleepers carry the highest risk. Mechanistically, regular timing entrains the suprachiasmatic master clock, stabilizing the cortisol rhythm, mood, and the circadian gating of processes including glymphatic clearance. The flip side — chronic misalignment between body clock and social schedule — is "social jetlag," tied to worse sleep, mood and metabolic markers. Best-supported claim — irregular sleep timing is prospectively associated with higher dementia risk and smaller brain volume — rates **Good (3)** on a single large, well-controlled cohort; many downstream mechanisms remain graded lower and partly preclinical.

## Mechanism
**hpa (modulate) — primary.** Stable sleep-wake timing entrains the SCN, which sets the phase and amplitude of the cortisol rhythm (the cortisol awakening response and evening nadir). Irregular schedules and social jetlag misalign or flatten this curve, a corrosive influence on the other channels. The win is restoration of proper phase/amplitude, hence `modulate`. Human evidence on circadian disruption and cortisol/metabolic dysregulation is fairly consistent (graded 3).

**glymph (up, graded 2).** Glymphatic clearance is itself circadian-gated — in mice it peaks during the rest phase and depends on AQP4 polarization (Hablitz 2020, PMID:32879313), and the broader clearance-during-sleep concept is established (Xie 2013, PMID:24136970). Regular timing should align the clearance window with consolidated deep sleep; chronic misalignment is hypothesized to blunt it. In humans this is supported only indirectly (regularity ↔ dementia and brain-volume associations), so the channel is graded 2; the *depth* lever (see `deep-slow-wave-sleep`) carries the stronger clearance grade.

**ser (modulate).** The serotonergic raphe is reciprocally connected with the SCN; circadian disruption and social jetlag are associated with depressive symptoms and mood instability, and regular timing supports stable affect. The pathway is partly inferential in humans, so graded 2.

**inflam (down).** Forced-desynchrony, shift-work and social-jetlag paradigms raise inflammatory markers and worsen glycemic control; regularity associates with lower inflammatory load. CNS-specific neuroinflammation is inferred from peripheral/shift-work data (graded 2).

## Evidence
- **Sleep regularity and dementia (human, large cohort).** Yiallourou/Pase, Neurology 2024 (PMID:38165323) analyzed ~88,000 UK Biobank participants with accelerometry-derived SRI and found a **U-shaped** association with incident dementia: relative to the median, hazard ratios were ~1.53 at the 5th percentile (most irregular) and ~1.16 at the 95th percentile, with irregular sleep also linked to smaller gray-/white-matter volume. The signal was robust to covariates and partly independent of sleep duration — the key evidence that *regularity* is its own lever. As a single observational cohort it cannot establish causality, and reverse causation (prodromal neurodegeneration disrupting rhythms) remains plausible; graded **Good (3)** rather than 4.
- **Social jetlag (human, foundational + correlational).** Wittmann 2006 (PMID:16687322) defined social jetlag as the mismatch between biological and social clocks (the shift in mid-sleep between work and free days) and linked larger social jetlag to poorer sleep and wellbeing. A wide literature since associates social jetlag with metabolic, mood and cognitive/academic outcomes, but most is cross-sectional and confounded by chronotype and sleep debt — supportive, not definitive.
- **Circadian gating of clearance (animal).** The circadian/AQP4 dependence of glymphatic flow (Hablitz 2020, PMID:32879313) and sleep-dependent clearance (Xie 2013, PMID:24136970) provide the mechanistic rationale for why *timing*, not just amount, of sleep could matter — but these are mouse studies; the human translation is inferred.

Net: best-supported, most decision-relevant claim — irregular sleep-wake timing is prospectively associated with higher dementia risk and smaller brain volume, partly independent of duration — rates **Good (3)**. Mood, inflammatory and glymphatic mechanisms are plausible but graded lower (2) pending causal human data.

## Safety & interactions (research metadata)
No contraindication to maintaining a regular schedule. Practical antagonists are evening bright/blue light, late caffeine, and late large meals (all delay circadian phase), plus structural impositions like **shift work** and frequent transmeridian travel, which behavioral regularity can only partly offset. Note the U-shape: the actionable target is *avoiding high irregularity*, not maximizing a regularity score to the point of rigidity — the protective signal plateaus and the high-regularity arm carries a modest, likely confounded, elevation. Research metadata, not medical advice.

## Open questions
- Is the regularity–dementia association causal, or does prodromal neurodegeneration disrupt circadian rhythms (reverse causation)? Needs repeated-measures and genetic-instrument designs.
- How independent is regularity from sleep duration and depth in driving outcomes, given they co-vary? Yiallourou 2024 suggests partial independence but cannot fully disentangle them.
- Does an intervention that improves sleep regularity (e.g., fixed wake time, morning light) causally lower dementia risk or only correlate?
- What explains the high-regularity arm of the U-shape — confounding, measurement artifact, or a genuine cost of excessive rigidity?
- How much does correcting social jetlag specifically (vs general regularity) change cognitive or pathological trajectories?
