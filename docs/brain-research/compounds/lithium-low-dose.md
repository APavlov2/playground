---
id: lithium-low-dose
name: "Lithium (low-dose / microdose)"
aliases:
  - "low-dose lithium"
  - "microdose lithium"
  - "lithium orotate"
  - "lithium carbonate (subtherapeutic)"
  - "nutritional lithium"
type: compound
klass: "alkali metal / mood-stabilizer (subtherapeutic dosing)"
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Trace element in drinking water & foods; supplemental salts (orotate/carbonate) manufactured"
status: draft
evidence_overall: 2
onset: "weeks to months (cognitive/neuroprotective endpoints measured over 12-24 months in trials)"
half_life: "~18-24 h (lithium ion; longer with renal impairment and in the elderly)"
dose_range: "Microdose: ~300 micrograms (0.3 mg) elemental Li/day (Nunes 2013). Low subtherapeutic clinical dose: titrated to serum 0.25-0.5 mmol/L (Forlenza 2011). DISTINCT from therapeutic mood-stabilizer dosing (serum ~0.6-1.2 mmol/L). Water-source epidemiology: micrograms/L exposure, not a supplement dose."
cognitive_domains:
  - memory
  - attention
  - global cognition
  - "disease progression (MCI/AD)"
channels:
  - channel: ntrophic
    mechanism: "GSK-3-beta inhibition (direct and via Akt-mediated inhibitory phosphorylation), reduced tau hyperphosphorylation, increased BDNF signaling, neuroprotection and gray-matter/N-acetylaspartate effects reported at therapeutic doses; in MCI low-dose RCT associated with reduced CSF p-tau and slowed cognitive decline."
    evidence: 2
    population: impaired
    direction: up
  - channel: inflam
    mechanism: "GSK-3-beta inhibition is anti-inflammatory in preclinical models (reduced microglial activation, pro-inflammatory cytokines); human-specific anti-inflammatory data for low-dose lithium on cognition is (unsourced)."
    evidence: 1
    population: preclinical
    direction: down
safety:
  contraindications:
    - "Significant renal impairment (lithium is renally cleared; toxicity risk)"
    - "Uncontrolled or untreated thyroid disease"
    - "Significant dehydration or sodium depletion"
    - "Pregnancy and breastfeeding (Ebstein anomaly / cardiac teratogenicity concern with gestational exposure; risk characterized at therapeutic doses)"
    - "Severe cardiovascular disease"
  interactions:
    - "NSAIDs: reduce renal lithium clearance and raise serum levels"
    - "Thiazide and loop diuretics: raise serum lithium levels"
    - "ACE inhibitors and ARBs: raise serum lithium levels"
    - "Dehydration, low-sodium diet, or excessive sweating: raise serum lithium levels"
    - "Other serotonergic agents (theoretical additive risk)"
  notable_risks:
    - "Narrow therapeutic index at clinical/therapeutic doses; toxicity risk rises steeply above ~1.2 mmol/L"
    - "Hypothyroidism and goiter (thyroid toxicity), chiefly at therapeutic doses"
    - "Nephrogenic diabetes insipidus and chronic kidney injury with long-term therapeutic use"
    - "Tremor, polyuria, weight gain at higher doses"
    - "Microdose/subtherapeutic exposure has a wide safety margin, but supplement products are unregulated and dosing is not standardized"
sources:
  - "Forlenza OV, Diniz BS, Radanovic M, Santos FS, Talib LL, Gattaz WF. Disease-modifying properties of long-term lithium treatment for amnestic mild cognitive impairment: randomised controlled trial. Br J Psychiatry. 2011;198(5):351-356. PMID:21525519 DOI:10.1192/bjp.bp.110.080044"
  - "Nunes MA, Viel TA, Buck HS. Microdose lithium treatment stabilized cognitive impairment in patients with Alzheimer's disease. Curr Alzheimer Res. 2013;10(1):104-107. PMID:22746245 DOI:10.2174/1567205011310010014"
  - "Kessing LV, Gerds TA, Knudsen NN, et al. Association of Lithium in Drinking Water With the Incidence of Dementia. JAMA Psychiatry. 2017;74(10):1005-1010. PMID:28832877 DOI:10.1001/jamapsychiatry.2017.2362"
  - "Memon A, Rogers I, Fitzsimmons SMDD, et al. Association between naturally occurring lithium in drinking water and suicide rates: systematic review and meta-analysis of ecological studies. Br J Psychiatry. 2020;217(6):667-678. PMID:32716281 DOI:10.1192/bjp.2020.128"
  - "Blüml V, Regier MD, Hlavin G, et al. Lithium in the public water supply and suicide mortality in Texas. J Psychiatr Res. 2013;47(3):407-411. PMID:23312137 DOI:10.1016/j.jpsychires.2012.12.002"
tags:
  - lithium
  - neuroprotection
  - "GSK-3-beta"
  - BDNF
  - dementia-prevention
  - MCI
  - microdose
  - ecological-evidence
  - grade-2
---

## Summary

Low-dose and microdose lithium are subtherapeutic exposures distinct from the doses used as a mood stabilizer in bipolar disorder. Interest in lithium for brain optimization rests on three threads: (1) ecological epidemiology linking higher trace lithium in drinking water to lower dementia incidence and lower suicide rates; (2) small clinical trials of subtherapeutic lithium in mild cognitive impairment (MCI) and Alzheimer's disease (AD) suggesting slowed cognitive decline; and (3) a mechanistic rationale centered on GSK-3-beta inhibition, BDNF/neurotrophic signaling, and reduced tau hyperphosphorylation.

Evidence overall is graded **2**. The clinical signal comes from small RCTs/pilots (Forlenza 2011, n=45 randomized; Nunes 2013, an underpowered pilot), and the population-level associations are ecological and therefore vulnerable to confounding. This is a plausible, hypothesis-generating literature, not a confirmed effect. Importantly, the favorable safety profile applies only to the low/microdose range; therapeutic-dose lithium has a narrow therapeutic index with real thyroid and renal toxicity.

## Mechanism

The leading mechanism is inhibition of glycogen synthase kinase-3 beta (GSK-3-beta), both directly and indirectly (via Akt-mediated inhibitory phosphorylation). GSK-3-beta is a key kinase in tau hyperphosphorylation and amyloid precursor protein processing, so its inhibition is proposed to reduce neurofibrillary pathology. Lithium also enhances BDNF and neurotrophic signaling, promotes neuroprotection, and at therapeutic doses has been associated with gray-matter and N-acetylaspartate changes. GSK-3-beta inhibition additionally has anti-inflammatory effects in preclinical models (reduced microglial activation), though human cognitive anti-inflammatory data specific to low-dose lithium is (unsourced).

These mechanisms are best documented at therapeutic concentrations and in preclinical models; whether microgram-range microdoses meaningfully engage these targets in humans is unresolved.

## Evidence

**Water-lithium epidemiology (ecological; confounding caveat).** A nationwide Danish case-control study (73,731 dementia cases vs 733,653 controls) found that higher long-term lithium exposure from drinking water was associated with lower dementia incidence, though the relationship was nonlinear (Kessing 2017, JAMA Psychiatry; PMID:28832877). For suicide, a 2013 Texas study across 226 counties found higher public-water lithium associated with lower suicide mortality (Blüml 2013; PMID:23312137), and a systematic review/meta-analysis of ecological studies reported a consistent inverse (protective) association between water lithium and suicide rates (pooled effect inverse, high heterogeneity I2 ~83%) (Memon 2020, Br J Psychiatry; PMID:32716281). All of these are ecological designs and cannot establish causation; residual confounding by municipality-level factors is acknowledged by the authors.

**Forlenza 2011 MCI RCT.** A 12-month double-blind RCT randomized 45 participants with amnestic MCI to subtherapeutic lithium (serum 0.25-0.5 mmol/L) or placebo. The lithium group showed better performance on the ADAS-Cog and attention tasks and a significant decrease in CSF p-tau, consistent with disease-modifying properties (Forlenza 2011, Br J Psychiatry; PMID:21525519). The sample is small and the result is a single trial.

**Nunes 2013 microdose AD pilot.** A pilot of microdose lithium (300 micrograms/day) over 15 months in AD patients reported stable MMSE scores in the lithium group while controls declined (Nunes 2013, Curr Alzheimer Res; PMID:22746245). This is a small pilot with limited methodological detail and should be treated as hypothesis-generating only.

## Safety & interactions

The central safety theme is the distinction between dose ranges. **Therapeutic-dose lithium** (serum ~0.6-1.2 mmol/L) has a **narrow therapeutic index**: toxicity rises steeply above ~1.2 mmol/L, and chronic use carries risks of **hypothyroidism/goiter** (thyroid toxicity), **nephrogenic diabetes insipidus and chronic kidney injury** (renal toxicity), tremor, polyuria, and weight gain. **Low-dose/microdose** exposures used in the cognitive literature have a much wider safety margin, but supplement products are unregulated and dosing is not standardized.

Key interactions raise serum lithium and can precipitate toxicity: **NSAIDs**, **thiazide and loop diuretics**, and **ACE inhibitors/ARBs** all reduce renal lithium clearance. **Dehydration, low-sodium diets, and heavy sweating** likewise raise levels. **Pregnancy and breastfeeding** are a caution due to cardiac teratogenicity concern (Ebstein anomaly) characterized at therapeutic doses. Significant **renal impairment** and **uncontrolled thyroid disease** are contraindications. Anyone on these interacting drugs or with renal/thyroid disease should not self-administer lithium without monitoring.

## Open questions

- Does microgram-range microdose lithium engage GSK-3-beta / tau pathways in humans, or are clinical signals driven only by the higher subtherapeutic (0.25-0.5 mmol/L) range?
- Are the water-lithium dementia/suicide associations causal, or artifacts of ecological confounding? The nonlinear dementia relationship is unexplained.
- Replication: the MCI/AD findings rest on small single-center trials; adequately powered RCTs (e.g., ongoing feasibility/dose-ranging trials) are needed before any preventive recommendation.
- Optimal dose, biomarker target, and long-term safety of chronic subtherapeutic lithium in healthy or at-risk (non-demented) populations are unknown.
- Effect in **healthy** individuals is essentially unstudied; the human evidence is in impaired/at-risk populations.
