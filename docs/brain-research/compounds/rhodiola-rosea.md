---
id: rhodiola-rosea
name: Rhodiola rosea
aliases: [golden root, arctic root, roseroot, rosavins, salidroside]
type: compound
klass: Adaptogen
status: draft
evidence_overall: 2  # Multiple RCTs and two systematic reviews exist, but reviews judge nearly all trials to be at HIGH RISK OF BIAS with poor reporting; results are contradictory. Honest grade is 2, not 3.
onset: "Acute-to-days for mental fatigue (single/repeated low-dose stress paradigms show same-day effects); stress/burnout outcomes over 1-12 weeks"
half_life: "Not well characterized in humans; salidroside/rosavin pharmacokinetics vary by extract and standardization (approximate, not firmly established)"
dose_range: "~200-600 mg/day of standardized extract (commonly SHR-5 / WS 1375), typically standardized to ~3% rosavins and ~1% salidroside; studied doses include 400 mg/day (burnout) and 576 mg/day (stress-related fatigue)"
cognitive_domains: [mental-fatigue, stress, attention, well-being]
channels:
  - channel: hpa
    mechanism: "Adaptogenic modulation of the stress axis; standardized extract reduced the salivary cortisol response to awakening vs placebo in stress-related fatigue, alongside anti-fatigue effects"
    evidence: 2
    population: healthy-stressed (fatigue syndrome / stress-related fatigue; burnout)
    direction: modulate  # net direction is normalization; cortisol-awakening response reduced in Olsson 2009, but evidence is limited and from small/biased trials
  - channel: mito
    mechanism: "Cellular-energy / anti-fatigue. Salidroside upregulates mitochondrial biogenesis markers (PGC-1a, TFAM) and activates AMPK in vitro/animal models. Weight of evidence here is PRECLINICAL; human anti-fatigue trials do not directly measure mitochondrial endpoints"
    evidence: 2  # strong preclinical mechanistic signal, no direct human mitochondrial outcome data -> capped at 2
    population: preclinical (in vitro / animal); human fatigue data indirect
    direction: up
  - channel: ser
    mechanism: "Preclinical monoamine modulation (reported effects on serotonergic signaling in rodent models); no robust human confirmation"
    evidence: 1
    population: preclinical
    direction: modulate
  - channel: da
    mechanism: "Preclinical monoamine modulation (reported effects on dopaminergic signaling in rodent models); no robust human confirmation"
    evidence: 1
    population: preclinical
    direction: modulate
  - channel: ne
    mechanism: "Preclinical monoamine modulation (reported effects on noradrenergic signaling in rodent models); no robust human confirmation"
    evidence: 1
    population: preclinical
    direction: modulate
safety:
  contraindications: []
  notable_risks:
    - "Possible activation / overstimulation; anecdotal reports of insomnia, irritability, or jitteriness, especially at higher doses or late-day dosing (not well quantified in trials) — (unsourced beyond general tolerability data)"
  interactions:
    - "Theoretical interactions via CYP/P-gp and with stimulants, antidepressants (monoamine modulation), and antihypertensives/anticoagulants are commonly cited but NOT well established in controlled human studies (unsourced)"
tags: [adaptogen, anti-fatigue]
sources:
  - "Hung SK, Perry R, Ernst E — Phytomedicine, 2011 — PMID:21036578 (systematic review of RCTs; reporting quality generally poor, no trial met all CONSORT criteria)"
  - "Ishaque S, Shamseer L, Bukutu C, Vohra S — BMC Complement Altern Med, 2012 — PMID:22643043 (systematic review, physical/mental fatigue; ALL included studies high risk of bias or reporting flaws)"
  - "Spasov AA, Wikman GK, Mandrikov VB, Mironova IA, Neumoin VV — Phytomedicine, 2000 — PMID:10839209 (SHR-5, students/exam stress RCT)"
  - "Olsson EM, von Schéele B, Panossian AG — Planta Med, 2009 — PMID:19016404 (SHR-5 576 mg/day, stress-related fatigue; reduced cortisol-awakening response)"
  - "Kasper S, Dienel A — Neuropsychiatr Dis Treat, 2017 — PMID:28367055 (open-label burnout trial, WS 1375 400 mg/day, 12 wk; safety)"
  - "Xing S, Yang X, Li W, et al. — Oxid Med Cell Longev, 2014 — PMID:24868319 (preclinical: salidroside stimulates mitochondrial biogenesis, PGC-1a/TFAM)"
---

## Summary
Rhodiola rosea is an adaptogenic root extract used primarily for fatigue, stress, and mental performance under stress. The most consistent signal in human trials is reduction of subjective and cognitive (mental) fatigue and improved well-being in healthy-but-stressed populations (students under exam stress, shift workers, people with stress-related fatigue, burnout). However, the evidence base is undermined by methodological quality: two independent systematic reviews conclude that nearly all RCTs carry a HIGH RISK OF BIAS or significant reporting flaws, and that results across trials are contradictory (Hung 2011 — PMID:21036578; Ishaque 2012 — PMID:22643043). Net honest grade for the compound is moderate-at-best (evidence_overall 2). Mechanistic/anti-fatigue claims at the cellular (mitochondrial) and monoamine level rest largely on preclinical work.

## Mechanism
Rhodiola's two principal marker constituents are the rosavins and salidroside; extracts are typically standardized to roughly 3% rosavins / 1% salidroside. Proposed mechanisms span several channels:

- **HPA / stress axis (hpa):** As an adaptogen, Rhodiola is proposed to normalize stress-axis signaling. The clearest human datum is Olsson 2009 (PMID:19016404), where the standardized SHR-5 extract (576 mg/day) significantly reduced the cortisol response to awakening versus placebo in subjects with stress-related fatigue, paralleling its anti-fatigue effect. Direction is best described as *modulate/normalize* rather than simple cortisol suppression; the data are limited and from small trials.
- **Mitochondrial / cellular energy (mito):** Salidroside upregulates mitochondrial biogenesis (PGC-1a, TFAM) and activates AMPK in vitro and in animal models (Xing 2014 — PMID:24868319). This provides a plausible anti-fatigue / cellular-energy rationale, but the weight of evidence is PRECLINICAL — human fatigue trials do not directly measure mitochondrial endpoints, so this should not be read as confirmed human mechanism.
- **Monoamines (ser / da / ne):** Animal studies report modulation of serotonergic, dopaminergic, and noradrenergic signaling, which is often invoked to explain mood/anti-fatigue effects. These are mechanistic/preclinical only (grade 1) and not confirmed in humans.

## Evidence
**Systematic reviews (the key honesty anchor).**
- Hung, Perry & Ernst, *Phytomedicine* 2011 (PMID:21036578): systematic review of RCTs across Rhodiola species. No included study met all CONSORT criteria; reporting quality was generally poor. Some evidence suggested benefit for physical/mental performance and certain mental-health-related outcomes, but the authors flagged the evidence as inconclusive due to quality.
- Ishaque, Shamseer, Bukutu & Vohra, *BMC Complement Altern Med* 2012 (PMID:22643043): 11 trials (10 RCTs, 1 CCT) on physical and mental fatigue. Only 2/6 physical-fatigue trials and 3/5 mental-fatigue RCTs reported Rhodiola as effective. Crucially, the authors concluded that **all included studies exhibit either a high risk of bias or reporting flaws that hinder assessment of true validity**, and that the literature is contradictory. This is the single most important caveat for grading.

**Representative primary RCTs (healthy-stressed populations).**
- Spasov 2000 (PMID:10839209): double-blind, placebo-controlled pilot RCT in foreign students during an examination period, SHR-5 low-dose for ~20 days. Reported significant improvements in physical fitness, mental fatigue, and neuro-motoric tests (p<0.01) and self-rated well-being (p<0.05); authors noted the dose was probably suboptimal. Small pilot; bias risk per the reviews above.
- Olsson 2009 (PMID:19016404): double-blind, placebo-controlled, parallel-group RCT, n=60, SHR-5 576 mg/day for 28 days, fatigue-syndrome population. Significant anti-fatigue effect (Pines burnout scale), improved attention/concentration indices (CCPT-II), and reduced cortisol-awakening response vs placebo. One of the better-designed trials but still small.

**Burnout (clinical-leaning population).**
- Kasper & Dienel 2017 (PMID:28367055): multicenter, **open-label, single-arm** exploratory trial, WS 1375 400 mg/day for 12 weeks in 118 burnout patients. Symptom scores (emotional exhaustion, fatigue, loss of zest) improved over time, with some change as early as 1 week. Because it is open-label and uncontrolled, this is hypothesis-generating only and does not establish efficacy; its main contribution is tolerability data (see Safety).

**Bottom line:** Replicated direction-of-effect for mental fatigue/stress in healthy-stressed groups, but small samples, heterogeneous extracts/doses, and pervasive high risk of bias keep the honest grade at 2. Clinical (e.g., true depression/anxiety disorders) efficacy is not established here.

## Safety & interactions (research metadata)
Generally well tolerated in the studied populations. In the Kasper 2017 burnout trial (PMID:28367055), adverse events were mostly mild-to-moderate with a low event rate (~0.015 events/observation day) and high compliance (~98.6%); the single serious adverse event (UTI hospitalization) was judged unrelated to treatment. The most commonly described practical issue is potential **activation/overstimulation** (anecdotal insomnia, jitteriness, irritability), favoring morning/early dosing — but this is not well quantified in trials (unsourced). Cited interaction concerns (CYP/P-gp; additive effects with stimulants, antidepressants given monoamine modulation, antihypertensives, anticoagulants) are largely theoretical and not established in controlled human studies (unsourced). This section is research metadata, not medical advice.

## Open questions
- **Standardization heterogeneity:** trials use different extracts (SHR-5, WS 1375) and rosavin/salidroside ratios, making cross-study comparison and dosing guidance unreliable.
- **Risk of bias:** both systematic reviews flag nearly universal high risk of bias / poor reporting; a rigorously designed, adequately powered, well-reported RCT is still needed.
- **Mechanism gap:** mitochondrial and monoamine mechanisms are preclinical; no human study links a defined molecular mechanism to the observed anti-fatigue effect.
- **Acute vs sustained / dose-response:** onset kinetics, optimal dose (Spasov suspected sub-optimal dosing), and durability of effects are poorly characterized.
- **Clinical populations:** efficacy for diagnosed depression/anxiety vs healthy-stressed fatigue remains unresolved.
