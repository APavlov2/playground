---
id: l-theanine
name: L-Theanine
aliases: [theanine, N-ethyl-L-glutamine]
type: compound
klass: Relaxant / glutamate analogue
status: draft
evidence_overall: 3
onset: "acute, ~30-60 min (subjective relaxation / EEG changes)"
half_life: "~1 h (plasma; ~58-74 min reported across human PK studies)"
dose_range: "100-400 mg/day (most RCTs 200-400 mg); single acute doses 50-250 mg in EEG work"
cognitive_domains: [relaxation, stress, attention, sleep-quality]
channels:
  - channel: hpa
    mechanism: "Attenuation of acute stress reactivity; reduced subjective stress and salivary cortisol response to a cognitive stressor (acute). Chronic basal-cortisol effects not established (one 28-day RCT null)."
    evidence: 3
    population: healthy
    direction: down
  - channel: gaba
    mechanism: "Promotion of occipital/frontal alpha-band EEG activity ('wakeful relaxation'); inhibition of cortical neuron over-excitation. GABAergic involvement is mechanistically plausible but not directly demonstrated in humans."
    evidence: 2
    population: healthy
    direction: modulate
  - channel: glu
    mechanism: "Structural glutamate/glutamine analogue; binds ionotropic glutamate receptors at low affinity, modest NMDA/AMPA and glutamate-transporter interactions, partial glutaminase competition. Direction is modulatory (not simple agonism/antagonism); human glutamatergic data are largely preclinical or schizophrenia-adjunct."
    evidence: 2
    population: preclinical
    direction: modulate
safety:
  contraindications: []
  interactions: ["May potentiate antihypertensives (mild BP-lowering signal under stress) — theoretical", "Commonly co-dosed with caffeine to offset jitteriness — combination, not standalone"]
  notable_risks: ["Generally well tolerated; no serious adverse events in RCTs at <=400 mg/day"]
sources:
  - "Hidese et al., Nutrients, 2019 — PMID:31623400 (DOI:10.3390/nu11102362)"
  - "Kimura et al., Biological Psychology, 2007 — PMID:16930802 (DOI:10.1016/j.biopsycho.2006.06.006)"
  - "White et al., Nutrients, 2016 — PMID:26797633 (DOI:10.3390/nu8010053)"
  - "Moulin et al., Neurology and Therapy, 2024 — PMID:38758503 (DOI:10.1007/s40120-024-00624-7)"
  - "Gomez-Ramirez et al., Brain Topography, 2009 — PMID:18841456 (DOI:10.1007/s10548-008-0068-z)"
  - "Dassanayake/Kahathuduwa et al., Nutritional Neuroscience, 2022 — PMID:32777998 (DOI:10.1080/1028415X.2020.1804098)"
  - "Lyon et al., Alternative Medicine Review, 2011 — PMID:22214254"
  - "Matyus et al., Journal of Clinical Medicine, 2025 — PMID:41227106 (DOI:10.3390/jcm14217710)"
tags: [nootropic, relaxant]
---

## Summary
L-Theanine (N-ethyl-L-glutamine) is an amino acid found in tea (Camellia sinensis) and a structural analogue of glutamate/glutamine. Its best-supported effect in humans is attenuation of acute stress reactivity and promotion of "relaxation without sedation," reflected in EEG alpha-wave changes. Effects on stress and some attention measures are supported by multiple RCTs; effects on sleep are population-specific (e.g., ADHD boys, anxious/stressed adults) and on cognition are mixed (a 2025 meta-analysis found benefit limited to specific visual-processing tasks at higher doses). Overall evidence is graded **3** (multiple RCTs, but small samples, mixed cognitive outcomes, and confounded multi-ingredient trials prevent a 4).

## Mechanism
- **Glutamate analogue (glu, modulate):** L-Theanine is structurally similar to glutamate and glutamine and interacts weakly with ionotropic glutamate receptors and glutamate transporters, and competes at glutaminase. The net effect is modulatory, not straightforward agonism or antagonism. Most direct glutamatergic evidence is preclinical; human glutamatergic data come mainly from schizophrenia adjunct work and are limited. Avoid implying theanine simply "raises" or "blocks" glutamate.
- **Cortical excitation / alpha waves (gaba, modulate):** Theanine is proposed to dampen excitatory cortical neuron firing during stress (Kimura et al., 2007 — PMID:16930802). Human EEG/MEG studies show modulation of alpha-band oscillatory activity — increased resting alpha at low doses and reduced tonic alpha during demanding attention tasks (Gomez-Ramirez et al., 2009 — PMID:18841456; White et al., 2016 — PMID:26797633). GABAergic mechanisms are plausible (preclinical reports of raised brain GABA) but are **(unsourced)** at the human level; hence graded 2 and labeled modulate rather than a confident "GABA up."
- **HPA / stress axis (hpa, down):** Acute dosing reduces subjective stress and physiological stress markers (heart rate, salivary IgA) and salivary cortisol response to challenge (Kimura 2007; White 2016). Chronic basal cortisol lowering is not established.

## Evidence
**Acute stress reactivity (HPA) — strongest signal.**
- Kimura et al., 2007 (PMID:16930802): crossover RCT, n=12, acute mental-arithmetic stressor. L-Theanine reduced heart-rate and salivary-IgA stress responses vs placebo, attributed to reduced sympathetic activation / inhibited cortical over-excitation. Note: this trial measured HR and s-IgA, **not** cortisol; small sample.
- White et al., 2016 (PMID:26797633): double-blind crossover, n≈26-34 healthy adults, 200 mg L-theanine in a nutrient drink + acute cognitive stressor. Subjective stress reduced at 1 h; salivary cortisol response reduced at 3 h (p=0.047); MEG posterior alpha increased at 2 h but only in high-trait-anxiety participants. **Caveat: the drink also contained alpha-GPC, phosphatidylserine, and chamomile — a confounded multi-ingredient formulation, not pure theanine.**

**Sub-chronic stress/anxiety (healthy adults).**
- Hidese et al., 2019 (PMID:31623400): 4-week crossover RCT, n=30 healthy adults, 200 mg/day. Reduced trait anxiety (STAI-T, p=0.006), depressive symptoms (SDS, p=0.019), and improved Pittsburgh Sleep Quality Index (p=0.013, incl. sleep latency/disturbance subscales); some verbal-fluency/executive improvement, strongest in low-baseline performers. Cortisol not measured.
- Moulin et al., 2024 (PMID:38758503): 28-day RCT, n=30 healthy adults with moderate stress, 400 mg/day (AlphaWave). Perceived Stress Scale fell in both arms (no clear placebo separation by day 28); **no between-group difference in salivary cortisol**; Stroop reaction time improved ~21% in the theanine arm; sleep-architecture shifts suggested consolidation. Tempers chronic-cortisol claims.

**Attention / alpha-wave EEG.**
- Gomez-Ramirez et al., 2009 (PMID:18841456): 168-channel EEG, n=13, 250 mg acute, visuo-spatial attention task. Significant reduction in tonic (background) alpha vs placebo with topographic shift; interpreted as supporting sustained attention.
- Dassanayake/Kahathuduwa et al., 2022 (PMID:32777998): double-blind placebo-controlled crossover, dose-response (100/200/400 mg). L-Theanine improved neurophysiological measures of selective attention in a dose-dependent manner.

**Cognition (mixed / weak).**
- Matyus et al., 2025 (PMID:41227106): systematic review + meta-analysis, 5 RCTs / 148 healthy adults. No significant overall effect on simple reaction time or Stroop; significant dose-dependent improvement only in recognition/visual reaction time at 400 mg. GRADE = low to very low. This is why overall cognitive benefit is not graded above 3.

**Sleep (population-specific).**
- Lyon et al., 2011 (PMID:22214254): RCT, n=98 boys (8-12) with ADHD, 400 mg/day, 6 weeks, actigraphy. Higher objective sleep percentage and sleep efficiency vs placebo; sleep latency and several parameters unchanged; well tolerated. Sleep benefit in healthy adults rests largely on the PSQI subscale findings in Hidese 2019, so sleep claims are best framed as population-specific rather than general.

## Safety & interactions (research metadata)
Generally well tolerated across RCTs at doses up to 400 mg/day, with no serious adverse events reported (Lyon 2011; Moulin 2024). No established contraindications. Theoretical mild blood-pressure lowering under stress could be additive with antihypertensives (theoretical, **(unsourced)** clinically). Frequently combined with caffeine to offset stimulant jitter, but that is a combination outcome distinct from standalone theanine. Pregnancy/lactation and pediatric long-term safety beyond the ADHD trial are not well characterized — treat as unknown.

## Open questions
- Does theanine lower **basal** (non-challenge) cortisol with chronic dosing? Current chronic RCT (Moulin 2024) is null.
- Direct human evidence for GABA elevation and for the direction of glutamatergic modulation is lacking — most is preclinical.
- Is the alpha/MEG benefit specific to high-trait-anxiety individuals (as White 2016 suggests), i.e., does responder status depend on baseline anxiety?
- Sleep benefits beyond specific populations (ADHD, stressed/anxious adults) in healthy normal sleepers are unconfirmed.
- Many positive trials are small (n=12-34) and several use multi-ingredient formulations; larger pure-theanine RCTs are needed to move evidence toward 4.
