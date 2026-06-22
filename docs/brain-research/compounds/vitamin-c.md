---
id: vitamin-c
name: Vitamin C
aliases:
  - Ascorbate
  - Ascorbic acid
  - L-ascorbic acid
type: compound
klass: "Water-soluble vitamin / antioxidant / enzymatic cofactor"
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Fruits & vegetables (citrus, peppers); supplements synthesized"
status: draft
evidence_overall: 2
onset: "Repletion of depleted tissue stores over days to weeks; brain/plasma ascorbate are homeostatically buffered, so acute dosing in replete people changes little."
half_life: "Plasma half-life is dose- and status-dependent (roughly 10-30 days for whole-body turnover at steady state); renal threshold near saturation means excess is excreted."
dose_range: "RDA ~75-90 mg/day (adults); ~100-200 mg/day saturates plasma and tissues in most people. Tolerable Upper Intake Level 2000 mg/day. Higher oral/IV doses are investigational and carry added risk."
cognitive_domains:
  - "Memory (immediate/delayed recall)"
  - "Attention/focus"
  - "Processing speed"
  - "Reaction time"
channels:
  - channel: ne
    mechanism: "Obligate electron donor (cofactor) for dopamine-beta-hydroxylase, converting dopamine to norepinephrine in neurosecretory vesicles; supports catecholamine synthesis."
    evidence: 2
    population: both
    direction: up
  - channel: da
    mechanism: "Ascorbate participates in catecholamine pathway regulation and protects dopaminergic neurons from dopamine-derived oxidative stress; modulatory rather than a direct dopamine-raising effect."
    evidence: 1
    population: preclinical
    direction: modulate
  - channel: inflam
    mechanism: "Major brain antioxidant and free-radical scavenger; regenerates other antioxidants (vitamin E, glutathione) and limits oxidative stress. Brain maintains high, homeostatically regulated ascorbate."
    evidence: 2
    population: both
    direction: modulate
safety:
  contraindications: []
  interactions:
    - "Non-heme iron: ascorbate enhances intestinal absorption of non-heme (dietary/supplemental) iron; relevant in iron-overload conditions (e.g. hemochromatosis, thalassemia)."
    - "High-dose IV ascorbate can interfere with point-of-care glucose meters (falsely elevated readings)."
  notable_risks:
    - "High oral doses commonly cause GI upset (diarrhea, nausea, abdominal cramping)."
    - "Oxalate load: vitamin C is metabolized partly to oxalate; high doses raise calcium-oxalate kidney-stone risk, especially with prior nephrolithiasis or renal impairment."
    - "G6PD deficiency: high-dose (especially IV) ascorbate can precipitate acute hemolysis."
sources:
  - "Travica N, et al. Vitamin C Status and Cognitive Function: A Systematic Review. Nutrients. 2017. PMID:28867798 DOI:10.3390/nu9090960"
  - "Travica N, et al. Plasma Vitamin C Concentrations and Cognitive Function: A Cross-Sectional Study. Front Aging Neurosci. 2019. PMID:31001107 DOI:10.3389/fnagi.2019.00072"
  - "Sharma Y, et al. Relationship between Vitamin C Deficiency and Cognitive Impairment in Older Hospitalised Patients: A Cross-Sectional Study. Antioxidants (Basel). 2022. PMID:35326113 DOI:10.3390/antiox11030463"
  - "Rice ME. Ascorbate regulation and its neuroprotective role in the brain. Trends Neurosci. 2000. PMID:10782126 DOI:10.1016/s0166-2236(99)01543-x"
  - "May JM, et al. Ascorbic acid efficiently enhances neuronal synthesis of norepinephrine from dopamine. Brain Res Bull. 2013. PMID:23022576 DOI:10.1016/j.brainresbull.2012.09.009"
  - "LiverTox: Vitamin C. NIDDK. NBK548448 (updated 2021)."
tags:
  - vitamin
  - antioxidant
  - cofactor
  - deficiency-correction
  - catecholamine
  - safe-otc
---

## Summary

Vitamin C (ascorbate) is a water-soluble vitamin that the brain actively concentrates and maintains at high, homeostatically regulated levels. Its plausible cognitive relevance rests on two well-established roles: as an obligate enzymatic cofactor (notably for dopamine-beta-hydroxylase in norepinephrine synthesis) and as a major CNS antioxidant.

This is primarily a **deficiency-correction** story. The cognitive signal concentrates in people who are depleted or frankly deficient: deficient individuals score worse and moderate-to-severe deficiency tracks with cognitive impairment. In replete, healthy adults, supplementation shows little to no cognitive upside, and most controlled evidence is cross-sectional or associational rather than interventional. Grade is held conservatively at **2/4** overall for this reason. It is generally safe at dietary-to-moderate doses; risks emerge mainly at high doses (GI upset, oxalate stones, hemolysis in G6PD deficiency).

## Mechanism

- **Catecholamine cofactor (ne, da):** Ascorbate donates electrons to dopamine-beta-hydroxylase (DBH), the copper-dependent enzyme in neurosecretory vesicles that hydroxylates dopamine to norepinephrine. In neuronal cells, intracellular ascorbate in the ~0.2-0.5 mM range supports half-maximal norepinephrine synthesis, consistent with DBH kinetics; the effect is rapid and occurs at physiologically achievable concentrations (May et al. 2013, PMID:23022576). Ascorbate also protects dopaminergic neurons against dopamine-autoxidation oxidative stress (modulatory; largely preclinical).
- **Antioxidant / redox (inflam):** Ascorbate is a primary low-molecular-weight reductant and free-radical scavenger in brain, CSF and plasma, acting within an antioxidant network alongside glutathione and vitamin E. Brain ascorbate is held at high, tightly regulated concentrations, and Rice (2000, PMID:10782126) frames it as "normally neuroprotective" with additional neuromodulatory roles (e.g. glutamate-ascorbate heteroexchange at uptake sites).
- **Homeostatic buffering:** Because the brain concentrates ascorbate (neuronal levels enriched many-fold over extracellular fluid; CSF ~100-300 uM) and saturates at modest intakes, extra supplementation in replete people produces little additional CNS ascorbate, which mechanistically explains the lack of upside above adequacy.

## Evidence

**Deficiency and cognition (the strongest, most consistent signal):**
- Sharma et al. (2022, PMID:35326113): cross-sectional study of 160 hospitalized patients aged >=75. Vitamin C deficiency (<11 umol/L) was associated with cognitive impairment, adjusted OR 2.93 (95% CI 1.05-8.19, p=0.031); deficient patients had lower MMSE scores. Associational, hospitalized/older cohort, reverse-causation not excluded.
- Travica et al. (2019, PMID:31001107): cross-sectional comparison of adequate (>=28 umol/L) vs deficient (<28 umol/L) plasma vitamin C. Adequate group performed better on immediate recall (10.64 vs 9.17, p=0.001), delayed recall (9.74 vs 7.64, p<0.001), processing speed (SDMT 49.73 vs 41.38, p=0.039), and several reaction-time/recognition tasks. Cross-sectional only; cannot establish causation or supplementation benefit.
- Travica et al. (2017, PMID:28867798): systematic review of 50 studies (5 RCTs, 24 prospective, 17 cross-sectional, 4 case-control). Cognitively intact groups had higher mean vitamin C than impaired groups, but no correlation between vitamin C and MMSE within already-impaired individuals. Authors call the association "potential" and flag major methodological limitations; supplementation in replete adults was not shown to improve cognition.

**Antioxidant / neuroprotective role:** Rice (2000, PMID:10782126) reviews ascorbate as part of the intracellular antioxidant network and as normally neuroprotective. This is mechanistic/preclinical support, not evidence of cognitive enhancement in replete humans.

**Concentration data:** CSF ascorbate ~100-300 uM; neuronal uptake enriches intracellular ascorbate up to ~20-fold over extracellular fluid (Rice 2000, PMID:10782126). High brain set-point with saturable transport is the basis for the deficiency-vs-replete distinction.

**Replete healthy adults:** No robust controlled evidence that supplementation above adequacy meaningfully improves cognition. Claims of benefit in this population are **(unsourced)** at the grade of a confirmed cognitive endpoint.

## Safety & interactions

- **General tolerability:** Dietary and moderate supplemental doses are well tolerated. High oral doses commonly cause GI symptoms (diarrhea, nausea, abdominal discomfort) (LiverTox, NBK548448). Tolerable Upper Intake Level is 2000 mg/day.
- **Oxalate kidney stones:** Vitamin C is partly metabolized to oxalate; high doses increase calcium-oxalate stone risk, with elevated concern in those with prior nephrolithiasis, renal impairment, or on hemodialysis.
- **G6PD deficiency / hemolysis:** High-dose, especially IV, ascorbate can precipitate acute hemolysis in glucose-6-phosphate-dehydrogenase (G6PD)-deficient individuals; screening is advised before high-dose IV use.
- **Iron absorption:** Ascorbate enhances non-heme iron absorption; caution in iron-overload states (hemochromatosis, thalassemia, repeated transfusion).
- **Lab interference:** High-dose IV ascorbate can falsely elevate point-of-care glucose meter readings.
- **Liver:** Not associated with clinically apparent liver injury (LiverTox likelihood score E).

## Open questions

- Does correcting marginal/depleted (not frankly scorbutic) vitamin C status causally improve cognition, or is low vitamin C a marker of poorer overall health? The deficiency associations cannot separate these.
- Are there interventional RCTs of repletion in deficient adults with sensitive cognitive endpoints? Existing trials largely failed to measure plasma concentrations, limiting interpretation.
- What, if any, cognitive endpoint moves in replete healthy adults? Current data suggest little; this needs a properly powered, status-stratified RCT to confirm the null.
- Population-specific effects (older adults, low dietary intake, smokers with higher turnover) on the catecholamine/norepinephrine axis remain underexplored in humans.
