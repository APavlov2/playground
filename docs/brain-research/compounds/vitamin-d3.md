---
id: vitamin-d3
name: Vitamin D3 (cholecalciferol)
aliases:
  - cholecalciferol
  - vitamin D
  - "vitamin D3"
  - colecalciferol
type: compound
klass: fat-soluble vitamin / secosteroid prohormone
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Skin synthesis from sunlight; oily fish; supplements from lanolin or lichen"
status: draft
evidence_overall: 2
onset: "weeks to months (serum 25(OH)D rises over 6-12 weeks; any cognitive/mood effect, if present, is slow and concentrated in deficiency correction)"
half_life: "circulating 25(OH)D half-life ~2-3 weeks; parent cholecalciferol ~1-2 days"
dose_range: "800-2000 IU/day typical maintenance/repletion; deficiency correction often 2000-4000 IU/day or clinician-guided loading; tolerable upper intake level 4000 IU/day (IOM)"
cognitive_domains:
  - global cognition (no benefit in replete adults)
  - executive function (deficiency-associated in observational data; not improved by supplementation in trials)
  - processing speed (deficiency-associated observationally)
  - mood/depressive symptoms (mixed; no prevention benefit in replete adults)
channels:
  - channel: ntrophic
    mechanism: "VDR-mediated neurotrophic/neuroprotective signaling: vitamin D receptors are expressed in hippocampus and cortex; calcitriol upregulates neurotrophins (e.g., NGF) and supports neuronal calcium homeostasis and amyloid clearance in preclinical models. Human cognitive translation is unproven."
    evidence: 2
    population: deficient
    direction: up
  - channel: inflam
    mechanism: "Immunomodulatory / anti-neuroinflammatory: calcitriol downregulates pro-inflammatory cytokines and shifts microglial/T-cell phenotype. Mechanistically plausible link to neuroinflammation but no demonstrated cognitive benefit from supplementation."
    evidence: 2
    population: both
    direction: modulate
safety:
  contraindications:
    - "hypercalcemia"
    - "hypervitaminosis D"
    - "conditions with calcitriol-mediated hypercalcemia (e.g., sarcoidosis and other granulomatous diseases)"
    - "known hypersensitivity to cholecalciferol"
  interactions:
    - "thiazide diuretics (additive hypercalcemia risk)"
    - "calcium supplements (additive hypercalcemia/hypercalciuria; relevant in CNS/cardiovascular context)"
    - "digoxin (hypercalcemia potentiates digoxin toxicity)"
    - "CYP3A4-inducing anticonvulsants (phenytoin, phenobarbital, carbamazepine) and rifampin increase vitamin D catabolism, lowering levels"
    - "glucocorticoids and orlistat reduce vitamin D absorption/levels"
  notable_risks:
    - "hypercalcemia, hypercalciuria, and nephrolithiasis at high cumulative doses"
    - "vitamin D toxicity (nephrocalcinosis, soft-tissue calcification, renal dysfunction) typically at sustained very high intakes (>10,000 IU/day chronically; overt toxicity classically >25,000 IU/day)"
    - "small but measurable rise in hypercalcemia incidence with 4000-10,000 IU/day (e.g., ~3% at 4000 IU/day, ~9% at 10,000 IU/day over 3 years)"
sources:
  - "Kang JH, et al. Effect of vitamin D on cognitive decline: results from two ancillary studies of the VITAL randomized trial. Sci Rep. 2021. PMID: 34853363; DOI: 10.1038/s41598-021-02485-8"
  - "Okereke OI, et al. Effect of Long-term Vitamin D3 Supplementation vs Placebo on Risk of Depression or Clinically Relevant Depressive Symptoms and on Change in Mood Scores (VITAL-DEP). JAMA. 2020. PMID: 32749491; DOI: 10.1001/jama.2020.10224"
  - "Goodwill AM, Szoeke C. A Systematic Review and Meta-Analysis of The Effect of Low Vitamin D on Cognition. J Am Geriatr Soc. 2017. PMID: 28758188; DOI: 10.1111/jgs.15012"
  - "Sommer I, et al. Vitamin D deficiency as a risk factor for dementia: a systematic review and meta-analysis. BMC Geriatr. 2017. PMID: 28086755; DOI: 10.1186/s12877-016-0405-0"
  - "Littlejohns TJ, et al. Vitamin D and the risk of dementia and Alzheimer disease. Neurology. 2014. PMID: 25098535; DOI: 10.1212/WNL.0000000000000755"
  - "Chai B, et al. Vitamin D deficiency as a risk factor for dementia and Alzheimer's disease: an updated meta-analysis. BMC Neurol. 2019. PMID: 31722673; DOI: 10.1186/s12883-019-1500-6"
tags:
  - vitamin
  - deficiency-correction
  - cognition
  - mood
  - neuroprotection
  - "null-in-replete"
  - "conditional-in-deficient"
---

## Summary

Vitamin D3 (cholecalciferol) is a fat-soluble secosteroid prohormone with documented vitamin D receptor (VDR) expression in the brain. Its brain-optimization profile is best understood as a **deficiency-correction story, not a nootropic story**. Observational epidemiology consistently links low serum 25(OH)D to higher risk of dementia, cognitive decline, and depressive symptoms (Goodwill 2017 PMID 28758188; Sommer 2017 PMID 28086755; Littlejohns 2014 PMID 25098535). However, **randomized supplementation trials in largely vitamin-D-replete adults are null for cognition** (VITAL cognitive ancillary studies, Kang 2021 PMID 34853363) and **null for depression prevention** (VITAL-DEP, Okereke 2020 PMID 32749491). The honest grade: any plausible benefit concentrates in people who are actually deficient; in replete adults the expected cognitive/mood effect is approximately zero. Overall evidence is graded 2 because the strong signal is observational/correlational and the causal supplementation trials in replete populations are negative.

## Mechanism

VDR and the activating enzyme 1-alpha-hydroxylase are expressed in hippocampus and cortex, providing biological plausibility for two channels:

- **ntrophic (VDR-mediated neurotrophic/neuroprotective signaling):** In preclinical models, calcitriol upregulates neurotrophins (including NGF), supports neuronal calcium homeostasis, and promotes amyloid-beta clearance. This is the strongest mechanistic rationale, but it has **not** translated into measurable cognitive gains in replete humans. Graded for the **deficient** population.
- **inflam (immune / anti-neuroinflammatory modulation):** Calcitriol downregulates pro-inflammatory cytokines and modulates microglial and T-cell activity, a pathway relevant to neuroinflammation in aging and neurodegeneration. Mechanistically plausible in **both** deficient and replete states, but again without demonstrated cognitive payoff from supplementation.

Both channels are graded 2: real molecular mechanism and real observational correlation, but no convincing causal human cognitive/mood benefit outside of deficiency.

## Evidence

**Cognition — RCTs in replete adults are NULL.** The VITAL trial cognitive ancillary studies (Kang 2021, PMID 34853363) randomized older community-dwelling adults to 2000 IU/day vitamin D3 vs placebo. Vitamin D3 was **not associated with cognitive decline** over 2-3 years on either telephone or in-person cognitive batteries. A possible signal in older Black participants was exploratory and requires confirmation. The Goodwill/Szoeke meta-analysis (2017, PMID 28758188) reached the same overall verdict: observational low vitamin D tracks with worse cognition and decline (OR ~1.24 for poorer performance), but **supplementation showed no significant cognitive benefit vs control**.

**Depression — mixed, and NULL for prevention in replete adults.** VITAL-DEP (Okereke 2020, PMID 32749491) randomized 18,353 adults aged 50+ to 2000 IU/day vitamin D3 vs placebo over a median 5.3 years and found **no difference in incident/recurrent depression or clinically relevant depressive symptoms** (HR 0.97, 95% CI 0.87-1.09) and no improvement in mood scores. Smaller trials in deficient or depressed cohorts are heterogeneous, hence the "mixed" framing — but the largest, best-powered prevention trial is clearly null.

**Deficiency observational signal — real but correlational.** Prospective cohort data (Littlejohns 2014, PMID 25098535) found baseline vitamin D deficiency associated with increased incidence of all-cause dementia and Alzheimer disease, with the largest risk in the most severely deficient (e.g., <25 nmol/L). Meta-analyses concur that vitamin D deficiency is associated with elevated dementia risk (Sommer 2017, PMID 28086755; Chai 2019, PMID 31722673; severe-deficiency RR on the order of ~1.5). **Causality is not established** — residual confounding (reverse causation, sun exposure, frailty, comorbidity) is a serious limitation, and the negative RCTs argue against a simple causal supplementation benefit in already-replete people.

**Bottom line:** deficient population — conditional/plausible benefit from repletion; replete population — null. evidence_overall = 2.

## Safety & interactions

Vitamin D3 is well tolerated at standard repletion doses. Daily doses of 400, 4000, and 10,000 IU for up to 3 years are generally safe in non-deficient adults, but **hypercalcemia incidence rises with dose** (roughly 0%, 3%, and 9% respectively in trial data). The IOM tolerable upper intake level is **4000 IU/day**. Overt **vitamin D toxicity** — hypercalcemia, hypercalciuria, nephrolithiasis, nephrocalcinosis, soft-tissue calcification, and renal dysfunction — is associated with sustained very high intake (chronically >10,000 IU/day; classic toxicity >25,000 IU/day).

Key contraindications: pre-existing **hypercalcemia**, hypervitaminosis D, and granulomatous disease (e.g., **sarcoidosis**) where unregulated extrarenal calcitriol synthesis predisposes to hypercalcemia.

Notable interactions:
- **Thiazide diuretics** and **calcium supplements** — additive hypercalcemia/hypercalciuria risk.
- **Digoxin** — hypercalcemia potentiates digoxin toxicity/arrhythmia.
- **CYP-inducing anticonvulsants** (phenytoin, phenobarbital, carbamazepine) and **rifampin** — accelerate vitamin D catabolism and lower serum levels.
- **Glucocorticoids** and **orlistat** — reduce absorption/levels.

## Open questions

- Does vitamin D repletion produce real cognitive or mood benefit specifically in **measured-deficient** individuals (sub-25 to 50 nmol/L), as opposed to replete cohorts? Targeted RCTs enrolling only deficient participants are needed; existing major RCTs largely enrolled replete adults.
- Is there a population subgroup (e.g., older Black adults, suggested by VITAL) with a genuine effect, or is that a false positive from exploratory analysis? (unsourced for confirmation)
- What is the right repletion **target threshold** for brain endpoints — and is there a U-shaped risk where high 25(OH)D offers no added benefit?
- Do the ntrophic and inflam mechanisms operate only at the deficiency margin (threshold/saturation effect), explaining why supplementation in replete adults is inert?
