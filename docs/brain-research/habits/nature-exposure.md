---
id: nature-exposure
name: Nature exposure / green space
aliases:
  - green space
  - nature contact
  - forest bathing
  - shinrin-yoku
  - attention restoration
type: habit
klass: "Stress — environmental"
origin: natural
source: "Behavioral — environmental"
status: draft
evidence_overall: 2
onset: "Acute mood/rumination/attention shift after a single ~90-min exposure; cumulative epidemiological associations over months-years of residential green-space access"
half_life: ""
dose_range: ""
cognitive_domains:
  - rumination
  - attention/directed-attention restoration
  - stress/mood
channels:
  - channel: hpa
    mechanism: "Time in natural settings is associated with reduced self-reported stress and, in some studies, lower cortisol and blood pressure vs urban settings; proposed reduction in sympathetic/HPA arousal. Cortisol findings are mixed and effect sizes modest."
    evidence: 2
    population: healthy
    direction: down
  - channel: ser
    mechanism: "Nature exposure reduces rumination and improves affect, with reduced subgenual prefrontal cortex (sgPFC) activation — a region implicated in maladaptive self-focused rumination and depression. Framed as affect/mood-circuit modulation rather than a direct serotonergic pharmacology; mechanism is inferred."
    evidence: 2
    population: healthy
    direction: modulate
safety:
  contraindications: []
  interactions: []
  notable_risks:
    - "Environmental hazards of the setting itself (heat/cold, UV, allergens, ticks/insect-borne disease, terrain/injury); not intrinsic to the exposure."
sources:
  - "Bratman GN et al., Proc Natl Acad Sci USA, 2015 — PMID:26124129 — DOI:10.1073/pnas.1510459112 (RCT-style experiment; 90-min nature walk reduced self-reported rumination and subgenual PFC activation vs urban walk; n=38)"
tags:
  - nature
  - green-space
  - attention-restoration
  - rumination
  - emerging-evidence
---

## Summary
Nature exposure ("green space," forest bathing/shinrin-yoku) refers to time spent in natural rather than built environments. Two intertwined claims are made for it: **attention restoration** (Kaplan's ART — natural settings replenish depleted directed attention) and **stress/rumination reduction**. The most decision-relevant and well-identified single finding is Bratman 2015 (PNAS): a 90-minute nature walk reduced both self-reported rumination and subgenual-PFC activation versus a matched urban walk. Beyond that, the literature is a mix of small experiments and large but confounded epidemiology (residential green space correlated with better mental health and lower mortality). `evidence_overall: 2` reflects that this is genuinely **emerging**: mechanistically appealing, supported by a clean experiment and consistent observational data, but with small RCTs, mixed cortisol results, and heavy confounding in the cohort literature.

## Mechanism
- **hpa (down, primary stress route).** Natural settings are associated with reduced subjective stress and, in some studies, lower cortisol, blood pressure, and sympathetic arousal versus urban settings, consistent with stress-recovery theory. Cortisol findings across "forest bathing" studies are heterogeneous and effect sizes are modest, so this is graded emerging (2).
- **ser (modulate, affect/rumination circuit).** Bratman 2015 (PMID:26124129) showed nature exposure reduced rumination alongside **decreased subgenual prefrontal cortex activation** — a node tied to maladaptive self-referential rumination and to depression. This is reported as modulation of the mood/rumination circuit; a direct serotonergic pharmacological mechanism is inferred, not measured, so `ser` is graded 2 and `direction: modulate`. The attention-restoration component (improved directed-attention/working-memory after nature exposure) is a separate proposed benefit that does not map cleanly onto one neurotransmitter channel and is not graded as its own channel here to avoid forcing it.

## Evidence
**Rumination / sgPFC (best identified).** Bratman et al., *PNAS*, 2015 (PMID:26124129) randomized participants (n=38) to a 90-minute walk in a natural vs urban setting and found the nature walk **reduced self-reported rumination and lowered subgenual-PFC activation**, while the urban walk did not. This is the cleanest causal/neural evidence and the anchor for the entry — but it is a single small study and warrants the emerging grade pending replication.

**Stress / cortisol.** "Forest bathing" and green-space experiments report reductions in cortisol, blood pressure, and sympathetic tone in some samples, but results are inconsistent across studies and often use weak controls and small samples. Treat the HPA effect as plausible but not established.

**Epidemiology.** Large observational studies associate residential green-space access with better mental health, less depression/anxiety, and lower all-cause mortality. These are consistent but **heavily confounded** (socioeconomic status, physical activity, air quality, self-selection) and cannot establish causation — so they raise plausibility without lifting the grade past 2. Note also that the Lancet dementia commission framework emphasizes physical inactivity, air pollution, and social isolation as modifiable risks; green space plausibly intersects these but is not itself an established independent dementia lever.

**Healthy vs clinical.** Evidence is mostly in healthy/general-population adults; the acute rumination/attention effects are the best documented there. Clinical antidepressant-grade claims are not supported.

Net: best-supported, most relevant claim — acute nature exposure reduces rumination and sgPFC activation — rates **Emerging (2)**, limited by small samples and reliance on a single clean experiment plus confounded epidemiology.

## Safety & interactions (research metadata)
No intrinsic risk from the exposure. Practical hazards belong to the **setting**: heat/cold, UV, pollen/allergens, ticks and insect-borne disease, and terrain/injury risk. No drug interactions. This is research metadata, not medical advice.

## Open questions
- **Replication** of Bratman 2015 at larger scale, and whether the sgPFC/rumination effect persists beyond the acute window.
- **Dose-response**: how much nature, how often, and whether "~120 min/week" thresholds from survey work hold up causally.
- Disentangling nature contact from its confounds — **physical activity, social context, air quality, sunlight** — which co-occur with green space.
- Are the **cortisol/HPA** effects real and reproducible, or artifacts of weak controls?
- Whether attention-restoration benefits reflect genuine cognitive recovery vs mood-mediated effort/motivation changes.
