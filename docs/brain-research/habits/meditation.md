---
id: meditation
name: Meditation / mindfulness
aliases:
  - mindfulness meditation
  - MBSR
  - mindfulness-based stress reduction
  - focused-attention meditation
  - open-monitoring meditation
type: habit
klass: "Stress — mind-body"
origin: natural
source: "Behavioral — mind-body"
status: draft
evidence_overall: 3
onset: "State effects within a single session; trait/clinical effects accrue over ~8 weeks of regular practice (e.g. the standard 8-week MBSR course)"
half_life: ""
dose_range: ""
cognitive_domains:
  - stress/anxiety reduction
  - attention/sustained attention
  - emotion regulation
  - rumination
channels:
  - channel: hpa
    mechanism: "Regular practice is associated with reduced perceived stress and modest reductions in physiological stress markers (cortisol, blood pressure); proposed top-down PFC-mediated dampening of HPA-axis reactivity and amygdala threat response. Effect sizes on biomarkers are small and heterogeneous."
    evidence: 3
    population: both
    direction: down
  - channel: inflam
    mechanism: "Mind-body practice has been associated with small reductions in inflammatory markers (CRP, IL-6) in some RCTs, plausibly secondary to lowered stress/sympathetic tone. Signal is small, inconsistent, and confounded by active-control comparisons."
    evidence: 2
    population: both
    direction: down
  - channel: ntrophic
    mechanism: "Longitudinal MRI studies report changes in gray-matter concentration in hippocampus and emotion-regulation regions after an 8-week course, and altered amygdala-PFC connectivity. Interpreted as experience-dependent plasticity, but small samples, weak controls, and replication concerns keep this emerging rather than established."
    evidence: 2
    population: healthy
    direction: modulate
safety:
  contraindications: []
  interactions: []
  notable_risks:
    - "Meditation-related adverse experiences (anxiety, depersonalization/derealization, re-emergence of traumatic memories) are reported in a minority of practitioners, more often with intensive/long-retreat practice and in vulnerable individuals; under-reported in trials."
sources:
  - "Goyal M et al., JAMA Intern Med, 2014 — PMID:24395196 — DOI:10.1001/jamainternmed.2013.13018 (systematic review/meta-analysis, 47 RCTs/3515 participants; moderate evidence for anxiety, depression, pain; low/insufficient for most other outcomes)"
  - "Pascoe MC et al., J Psychiatr Res, 2017 — PMID:28863392 — DOI:10.1016/j.jpsychires.2017.08.004 (meta-analysis of physiological stress markers; meditation reduced cortisol, CRP, blood pressure vs control — small effects)"
  - "Hölzel BK et al., Psychiatry Res, 2011 — PMID:21071182 — DOI:10.1016/j.pscychresns.2010.08.006 (MBSR; pre-post gray-matter density increases incl. left hippocampus; small controlled longitudinal study)"
tags:
  - mindfulness
  - stress
  - hpa
  - cortisol
  - heterogeneous-evidence
---

## Summary
Meditation/mindfulness (most rigorously studied as the structured 8-week MBSR program, plus focused-attention and open-monitoring styles) is the canonical behavioral lever on the **HPA/stress** channel among habits. Its best-supported effect is **moderate reduction of anxiety, depression, and pain** in clinical and stressed populations; effects on positive well-being, attention, sleep, and physiological biomarkers are smaller and less consistent. The single most important honesty caveat is trial quality: the field's anchor meta-analysis (Goyal 2014) graded most meditation outcomes as low or insufficient evidence after restricting to RCTs with active controls, because much of the literature uses weak/no-treatment comparators, small samples, and self-report. `evidence_overall: 3` reflects the moderate, replicated anxiety/depression/stress signal — held at 3, not 4, because of pervasive active-control and risk-of-bias problems.

## Mechanism
- **hpa (primary, down).** The mechanistic story is top-down regulation: trained attention and reappraisal engage prefrontal control over the amygdala and the HPA axis, reducing perceived stress and stress reactivity. Human biomarker support exists but is modest — meta-analysis finds small reductions in cortisol, CRP, and blood pressure versus controls (Pascoe 2017, PMID:28863392). This is the channel with the most direct human evidence, but the effect sizes are small.
- **inflam (down, secondary).** Reduced sympathetic/HPA tone plausibly lowers low-grade inflammation; some RCTs report small CRP/IL-6 reductions. Findings are inconsistent and shrink when compared against active controls (relaxation, exercise, education), so this is graded emerging (2), not established.
- **ntrophic (modulate, structural plasticity).** Longitudinal MRI reports gray-matter changes in hippocampus and emotion-regulation regions and altered amygdala-PFC functional connectivity after ~8 weeks (Hölzel 2011, PMID:21071182). These are framed as experience-dependent plasticity rather than BDNF-specific neurogenesis, and the studies are small with replication concerns — graded 2.

## Evidence
**Anxiety / depression / stress (best supported).** Goyal et al., *JAMA Intern Med*, 2014 (PMID:24395196) systematically reviewed 47 RCTs (3515 participants) and is the field's reference point. Mindfulness meditation programs showed **moderate evidence** of reduced anxiety (effect size ~0.38 at 8 weeks), depression (~0.30), and pain, with effects comparable to what an antidepressant might be expected to produce in similar populations. Crucially, the review found **low or insufficient evidence** for effects on positive mood, attention, substance use, eating, sleep, and weight — and found **no evidence that meditation programs were better than active treatments** (exercise, drugs, behavioral therapies). This is why the channel grades land at 2-3, not 4: the literature is large but methodologically uneven.

**Physiological stress markers.** Pascoe et al., *J Psychiatr Res*, 2017 (PMID:28863392) pooled RCTs and found meditation reduced resting cortisol, CRP, blood pressure, heart rate, and triglycerides relative to controls — but effect sizes were **small**, and the populations and comparators were heterogeneous. Newer preregistered meta-analyses of inflammatory/stress biomarkers report only small within-group and between-group effects, reinforcing a modest read.

**Brain structure/function.** Hölzel et al., *Psychiatry Res*, 2011 (PMID:21071182) reported pre-post gray-matter density increases (including left hippocampus) after MBSR in a small controlled longitudinal study. Subsequent neuroimaging meta-analyses find regionally inconsistent results and flag small samples and publication bias, so structural claims remain emerging.

**Healthy vs clinical.** The moderate-grade benefits are clearest in clinical/stressed populations (anxiety, depression, chronic pain). In already-healthy, low-stress adults the cognitive/attention benefits are smaller and inconsistent and should not be over-claimed.

Net: best-supported, most relevant claim — meditation produces a moderate reduction in anxiety/depression/perceived stress — rates **Good (3)**. Biomarker and structural-plasticity claims are **Emerging (2)**.

## Safety & interactions (research metadata)
Generally low-risk as practiced in standard programs. However, **meditation-related adverse experiences** are real and under-reported in trials: a minority of practitioners report anxiety, depersonalization/derealization, re-emergence of traumatic memories, or destabilization — more common with intensive or long-retreat practice and in people with trauma or psychiatric vulnerability. No drug interactions. This is research metadata, not medical advice.

## Open questions
- How much of the measured benefit survives rigorous **active-control** comparison (vs relaxation, exercise, supportive education)? Goyal's null vs active treatments is the key unresolved point.
- Are structural/connectivity MRI findings **replicable** at adequate sample sizes, or are they small-study artifacts?
- Dose-response: what is the minimum effective practice (minutes/day, weeks) for durable HPA effects, and do trait effects persist after practice stops?
- Incidence and predictors of **meditation-related adverse events**, which are poorly quantified.
- Do attention/working-memory benefits exist independently of stress/mood improvement in healthy adults, or are they downstream?
