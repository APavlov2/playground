---
id: zinc
name: Zinc
aliases:
  - Zn
  - zinc gluconate
  - zinc picolinate
  - zinc sulfate
  - zinc acetate
type: compound
klass: essential trace mineral (neuromodulator / enzymatic cofactor)
status: draft
evidence_overall: 2
onset: "deficiency correction over weeks; depression-adjunct trials assess endpoints over 6–12 weeks"
half_life: "no single plasma half-life — homeostatically regulated body pool; no large storage depot, so status reflects ongoing intake"
dose_range: "RDA ~8–11 mg/day (adults); trials use ~25 mg/day elemental zinc as antidepressant adjunct. Tolerable Upper Intake Level (UL) ~40 mg/day elemental zinc for adults"
cognitive_domains:
  - mood (depressive symptoms)
  - reasoning (in deficient children; inconsistent)
  - general cognition (largely null in replete populations)
channels:
  - channel: glu
    mechanism: "Synaptic zinc is co-released from glutamatergic terminals and allosterically inhibits NMDA receptors (high-affinity binding to GluN2A N-terminal domain reduces open probability) and modulates AMPA and GABA-A receptors; acts as ligand at the metabotropic zinc receptor. Core neuromodulatory action. (PMID 39196675)"
    evidence: 3
    population: both
    direction: modulate
  - channel: inflam
    mechanism: "Cofactor for Cu/Zn superoxide dismutase and antioxidant defense; modulates immune signaling and NF-kB. Deficiency increases oxidative stress and inflammation; repletion normalizes it. Mechanistically established, clinical cognitive relevance indirect."
    evidence: 2
    population: deficient
    direction: down
  - channel: ser
    mechanism: "Antidepressant-adjunct signal: zinc added to antidepressants lowers depressive symptom scores in meta-analysis; proposed monoaminergic/NMDA-antagonist-like and BDNF-related mechanisms. Effect in depressed (impaired) populations, modest. (PMID 32885249; 32829928)"
    evidence: 2
    population: impaired
    direction: modulate
  - channel: ntrophic
    mechanism: "Zinc modulates BDNF/TrkB signaling and hippocampal neurogenesis in rodent models; reverses stress-induced BDNF loss preclinically. Not directly demonstrated in human brain."
    evidence: 1
    population: preclinical
    direction: up
safety:
  contraindications:
    - "known hypersensitivity to a zinc salt"
    - "chronic high-dose use without monitoring copper status (risk of copper deficiency)"
  interactions:
    - "quinolone and tetracycline antibiotics (ciprofloxacin, levofloxacin, doxycycline) — zinc chelates these, reducing antibiotic absorption; separate dosing by 2–4 h (PMID 106309)"
    - "copper — chronic excess zinc induces enterocyte metallothionein and blocks copper absorption, causing copper deficiency (PMID 15834043)"
    - "iron — competition for absorption at high doses (clinical magnitude unsourced)"
    - "penicillamine and other copper chelators — additive copper depletion (unsourced)"
  notable_risks:
    - "copper-deficiency myelopathy / myeloneuropathy and anemia/neutropenia from chronic excess zinc — neurological deficits may be only partially reversible (PMID 15834043)"
    - "acute high oral doses cause nausea, vomiting, gastric irritation"
    - "intranasal zinc (not oral) linked to anosmia — separate route, noted for completeness (unsourced for oral)"
sources:
  - "da Silva LEM, et al. Zinc supplementation combined with antidepressant drugs for treatment of patients with depression: a systematic review and meta-analysis. Nutr Rev. 2021;79(1):1-12. PMID: 32885249. DOI: 10.1093/nutrit/nuaa039"
  - "Yosaee S, et al. Zinc in depression: From development to treatment: A comparative/dose response meta-analysis of observational studies and randomized controlled trials. Gen Hosp Psychiatry. 2022;74:110-117. PMID: 32829928. DOI: 10.1016/j.genhosppsych.2020.08.001"
  - "Warthon-Medina M, et al. Zinc intake, status and indices of cognitive function in adults and children: a systematic review and meta-analysis. Eur J Clin Nutr. 2015;69(6):649-661. PMID: 25920424. DOI: 10.1038/ejcn.2015.60"
  - "Krall RF, et al. On the genesis and unique functions of zinc neuromodulation. J Neurophysiol. 2024;132(3):868-887. PMID: 39196675. DOI: 10.1152/jn.00285.2024"
  - "Rowin J, Lewis SL. Copper deficiency myeloneuropathy and pancytopenia secondary to overuse of zinc supplementation. J Neurol Neurosurg Psychiatry. 2005;76(5):750-751. PMID: 15834043"
  - "Neuvonen PJ. Interaction of cations and chelators with the intestinal absorption of tetracycline. PMID: 106309"
tags:
  - essential-mineral
  - neuromodulator
  - deficiency-correction
  - mood
  - depression-adjunct
  - copper-antagonist
  - draft
---

## Summary

Zinc is an essential trace mineral and the second most abundant transition metal
in the brain. It is both an enzymatic cofactor (hundreds of metalloenzymes,
including Cu/Zn-SOD) and a genuine **synaptic neuromodulator** — co-released with
glutamate and allosterically tuning NMDA, AMPA and GABA-A receptors (PMID
39196675). Its brain-optimization story is overwhelmingly a
**deficiency-correction** story, not an enhancement story: benefits concentrate
in zinc-deficient or clinically depressed populations, while in already-replete
healthy adults supplementation provides little cognitive upside and, in excess,
causes real harm via copper deficiency.

The overall evidence is **graded 2**. The most defensible human signal is a
modest **antidepressant-adjunct** effect (meta-analytic SMD ~ -0.36; PMID
32885249). General cognitive benefit in replete people is **not** supported — a
meta-analysis of RCTs found no significant effect of zinc supplementation on
cognition in children (PMID 25920424). Deficient vs. replete status is the
single most important variable for interpreting any claim about zinc.

## Mechanism

- **glu (core neuromodulation, graded 3):** Vesicular zinc is co-released from
  glutamatergic terminals in neocortex, hippocampus, amygdala and auditory
  brainstem. It binds the GluN2A N-terminal domain with high affinity to reduce
  NMDA-receptor open probability, exerts voltage-dependent channel block, and
  allosterically modulates AMPA and GABA-A receptors plus the metabotropic zinc
  receptor (PMID 39196675). This is established neurophysiology — hence the
  higher channel grade — but it describes a homeostatic signaling role, not a
  dose-responsive "more-is-better" enhancement target.
- **inflam (graded 2, deficient):** Zinc is a cofactor for Cu/Zn-SOD and
  antioxidant defense and modulates immune/NF-kB signaling. Deficiency raises
  oxidative stress; repletion normalizes it. The cognitive payoff is indirect.
- **ser (graded 2, impaired):** Adjunctive zinc lowers depressive symptom scores
  in depressed patients (PMID 32885249; 32829928). Proposed mechanisms include
  NMDA-antagonist-like activity and monoaminergic/BDNF modulation.
- **ntrophic (graded 1, preclinical):** Zinc modulates BDNF/TrkB signaling and
  hippocampal neurogenesis in rodents and reverses stress-induced BDNF loss.
  Human neurotrophic confirmation is absent — explicitly preclinical.

## Evidence

**Depression adjunct — the strongest human signal.** da Silva et al. 2021
systematic review and meta-analysis (5 eligible RCTs) found zinc supplementation
combined with antidepressants produced a standardized mean difference of
**-0.36 (95% CI -0.67 to -0.04)** in depressive symptoms vs. placebo, with a
larger effect in those aged ≥40 (SMD -0.61, 95% CI -1.12 to -0.09); study
quality was moderate and trials were few (PMID 32885249). Yosaee et al. 2022
dose-response meta-analysis corroborated that zinc lowers depressive symptom
scores and that higher dietary zinc associates with ~28% lower depression risk in
cohorts, with a non-linear dependence on baseline mood (PMID 32829928). This is a
**real but modest** signal, concentrated in **impaired (depressed)** populations.

**Cognition in replete populations — null.** Warthon-Medina et al. 2015
systematic review and meta-analysis (18 studies; 12 RCTs) found **no significant
overall effect** of zinc supplementation on cognitive function — intelligence,
executive function, or motor skills — in the six pediatric RCTs pooled (PMID
25920424). Individual deficient-population studies are mixed (a few show
reasoning gains; several show no impact). The honest read: supplementing replete
people for cognitive enhancement is not supported.

**Deficiency cognition.** Benefit, where it appears, tracks correction of a
deficit rather than supraphysiologic dosing. Evidence linking zinc deficiency to
impaired cognition is suggestive mainly in the most vulnerable/deficient
children, but lacks consensus and is confounded by co-occurring micronutrient
deficiencies (PMID 25920424). This is the crux of the deficient-vs-replete
distinction.

**Neuromodulation (mechanistic).** The synaptic-zinc literature is robust at the
physiology level (PMID 39196675) and earns the glu channel its grade-3 mechanism
score, but mechanistic strength does not translate into demonstrated cognitive
enhancement in healthy humans — the overall grade is held at 2 accordingly.

## Safety & interactions (research metadata)

- **Copper deficiency from excess zinc (the principal harm).** Chronic high-dose
  zinc induces intestinal metallothionein, which preferentially binds copper and
  sheds it in feces, producing copper deficiency. This can cause
  **myelopathy/myeloneuropathy, sensory ataxia, anemia and neutropenia**;
  hematologic abnormalities resolve with treatment but **neurological deficits
  may only partially reverse** (PMID 15834043). Documented from supplement overuse
  and zinc-containing denture creams. Keep chronic intake below the ~40 mg/day UL
  unless monitoring copper.
- **Antibiotic chelation.** Zinc forms insoluble complexes with quinolones
  (ciprofloxacin, levofloxacin) and tetracyclines (doxycycline), reducing
  antibiotic absorption and risking therapeutic failure; separate dosing by
  **2–4 hours** (PMID 106309).
- **Iron / copper chelators.** High-dose zinc competes with iron absorption
  (clinical magnitude **(unsourced)**) and adds to copper depletion with
  penicillamine **(unsourced)**.
- **Acute GI effects.** High oral doses cause nausea, vomiting, gastric
  irritation; take with food.
- **Intranasal zinc** has been linked to anosmia — a different route, noted only
  for completeness; **(unsourced)** for oral supplements.

This is research metadata, not medical advice.

## Open questions

- Does the antidepressant-adjunct effect hold in larger, higher-quality RCTs, and
  is it driven specifically by baseline-deficient patients? Current trials are few
  and moderate quality.
- Is there any reproducible cognitive benefit from correcting **marginal**
  (subclinical) zinc deficiency in adults, distinct from frank deficiency?
- What is the safe long-term ceiling for cognitive/mood use given the
  copper-deficiency risk, and how should copper be co-monitored?
- How much does the robust synaptic-zinc neuromodulation physiology actually
  matter for human cognition, versus being a homeostatic set-point that
  supplementation cannot beneficially shift?
