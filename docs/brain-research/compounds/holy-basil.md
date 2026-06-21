---
id: holy-basil
name: Holy basil
aliases: [tulsi, Ocimum tenuiflorum, Ocimum sanctum, holy basil extract, OciBest, Holixer]
type: compound
klass: Adaptogen
status: draft
evidence_overall: 2  # Several small human RCTs (stress/anxiety, metabolic) plus one systematic review (Jamshidi & Cohen 2017, PMID:28400848). Reviewers flag small samples, heterogeneity, and bias; cognition data are thin. Honest grade is 2, not 3.
onset: "Stress/anxiety and metabolic outcomes assessed over ~4-8 weeks of daily dosing; acute kinetics in humans not well characterized (unsourced)"
half_life: "Not well characterized in humans; varies by extract, standardization (e.g., ursolic acid, eugenol, rosmarinic acid content) and preparation (approximate, not firmly established)"
dose_range: "Studied human doses include ~250 mg/day Holixer (125 mg twice daily; Lopresti 2022), 500 mg twice daily standardized leaf extract (Bhattacharyya 2008), and ~1200 mg/day OciBest actives (Saxena 2012). No consensus optimal dose."
cognitive_domains: [stress, anxiety, well-being, sleep]
channels:
  - channel: hpa
    mechanism: "Adaptogenic modulation of the stress axis. In an 8-week RCT (Holixer 250 mg/day) salivary cortisol, salivary amylase, blood pressure, and subjective stress fell vs placebo, with lower hair cortisol at week 8 (Lopresti 2022, PMID:36185698). Direction is best described as normalization of an elevated stress response in stressed-but-healthy adults."
    evidence: 2  # one well-conducted RCT plus supportive but lower-quality stress trials; small/heterogeneous, capped at 2
    population: healthy
    direction: modulate
  - channel: inflam
    mechanism: "Tulsi constituents (eugenol, ursolic acid, rosmarinic acid) show anti-inflammatory and immunomodulatory activity in vitro and in animal models; human anti-inflammatory endpoints are not robustly established. Weight of evidence is PRECLINICAL."
    evidence: 2  # strong preclinical signal, weak direct human confirmation -> capped at 2
    population: preclinical
    direction: down
  - channel: gaba
    mechanism: "Anxiolytic effect reported in a small controlled GAD trial (Bhattacharyya 2008, PMID:19253862); a GABAergic/anxiolytic mechanism is plausible and invoked for related Ocimum species but is NOT directly demonstrated in humans for O. tenuiflorum. Speculative channel."
    evidence: 1  # mechanism inferred, not demonstrated; single small biased anxiety trial
    population: impaired
    direction: modulate
safety:
  contraindications:
    - "Pregnancy / attempting conception — animal data show reversible antispermatogenic/antifertility effects (precautionary; Seth 1981, PMID:7309144)"
  interactions:
    - "Antiplatelet / anticoagulant agents (e.g., aspirin, warfarin, clopidogrel) — eugenol, a tulsi constituent, inhibits platelet aggregation in vitro/animal models; additive bleeding risk is theoretical but plausible (mechanistic only)"
    - "Antidiabetic agents — tulsi lowered glucose/metabolic markers in some trials (Jamshidi & Cohen 2017, PMID:28400848); additive hypoglycemia is theoretical (unsourced for clinical interaction)"
  notable_risks:
    - "Possible reduction in male fertility — reversible decreases in sperm count/motility in rodents (Seth 1981, PMID:7309144); human relevance unestablished"
    - "Generally well tolerated in short human trials; long-term human safety data are limited (Jamshidi & Cohen 2017, PMID:28400848)"
tags: [adaptogen, ayurvedic, stress, anxiolytic]
sources:
  - "Jamshidi N, Cohen MM — Evid Based Complement Alternat Med, 2017 — PMID:28400848 — DOI:10.1155/2017/9217567 (systematic review, 24 studies; benefits for metabolic and psychological-stress outcomes, but small/heterogeneous trials with bias — primary honesty anchor)"
  - "Lopresti AL, Smith SJ, Metse AP, Drummond PD — Front Nutr, 2022 — PMID:36185698 — DOI:10.3389/fnut.2022.965130 (RCT, n=100, Holixer 125 mg BID 8 wk; lower salivary/hair cortisol, amylase, BP, perceived stress, improved sleep)"
  - "Saxena RC, Singh R, Kumar P, et al. — Evid Based Complement Alternat Med, 2012 — PMID:21977056 (OciBest RCT, n=150, ~1200 mg/day 6 wk; self-rated general-stress symptoms reduced ~39% vs placebo; no cortisol measured)"
  - "Bhattacharyya D, Sur TK, Jana U, Debnath PK — Nepal Med Coll J, 2008 — PMID:19253862 (controlled trial, n=35, 500 mg BID 60 d; reduced generalized anxiety, stress, depression; small, open-label-leaning, high bias)"
  - "Seth SD, Johri N, Sundaram KR — Indian J Exp Biol, 1981 — PMID:7309144 (preclinical: antispermatogenic effect of Ocimum sanctum; basis for antifertility/pregnancy caution)"
---

## Summary
Holy basil (tulsi; *Ocimum tenuiflorum* / *Ocimum sanctum*) is an Ayurvedic adaptogen taken primarily for stress, anxiety, and metabolic health. The most credible human signal is a reduction in perceived stress and stress-axis markers (cortisol, blood pressure) in stressed-but-healthy adults, supported by one reasonably well-conducted RCT (Lopresti 2022 — PMID:36185698) and weaker stress/anxiety trials. The key honesty anchor is the systematic review by Jamshidi & Cohen 2017 (PMID:28400848), which found across 24 studies that tulsi shows promise for metabolic disorders, cardiovascular markers, immunity, neurocognition, and psychological stress — but that the trials are small, heterogeneous, and carry methodological bias. Direct cognition data are thin and mostly secondary endpoints. Honest grade for the compound is moderate-at-best (evidence_overall 2). Anti-inflammatory action is largely preclinical, and an anxiolytic/GABAergic mechanism is speculative in humans.

## Mechanism
Tulsi extracts contain eugenol, ursolic acid, rosmarinic acid, and other phytochemicals; commercial extracts (OciBest, Holixer) are standardized differently, complicating mechanism attribution. Proposed channels:

- **HPA / stress axis (hpa):** As an adaptogen, tulsi is proposed to normalize an elevated stress response. The clearest human datum is Lopresti 2022 (PMID:36185698), where Holixer (250 mg/day, 8 weeks) lowered salivary cortisol, salivary amylase, blood pressure, and subjective stress vs placebo, with reduced hair cortisol at week 8. Direction is best read as *modulate/normalize* rather than simple suppression.
- **Inflammation / immune (inflam):** Eugenol, ursolic acid, and rosmarinic acid show anti-inflammatory and immunomodulatory activity in vitro and in animal models. This is the rationale for tulsi's broad "protective" reputation, but human anti-inflammatory endpoints are not robustly established — weight of evidence is PRECLINICAL (grade 2, direction down).
- **GABA / anxiolysis (gaba):** A small controlled GAD trial (Bhattacharyya 2008 — PMID:19253862) reported reduced anxiety, but a specific GABAergic mechanism is inferred, not demonstrated in humans for *O. tenuiflorum*. This channel is speculative (grade 1).

## Evidence
**Systematic review (honesty anchor).**
- Jamshidi & Cohen, *Evid Based Complement Alternat Med* 2017 (PMID:28400848; DOI:10.1155/2017/9217567): systematic review of 24 human studies. Reported therapeutic signals across metabolic disorders (glucose, lipids), cardiovascular markers, immunity, neurocognition, and psychological stress, with no significant adverse effects reported in the included trials. **Critically, the authors flag that the studies are small, heterogeneous in design/dose/preparation, and carry risk of bias**, so conclusions are preliminary. This is the single most important caveat for grading.

**Stress RCTs (stressed-but-healthy populations).**
- Lopresti 2022 (PMID:36185698; DOI:10.3389/fnut.2022.965130): randomized, double-blind, placebo-controlled trial, n=100, Holixer 125 mg twice daily for 8 weeks in adults experiencing stress. Significantly lower salivary cortisol (p=0.001), salivary amylase (p=0.001), systolic (p=0.010) and diastolic (p=0.025) blood pressure, and subjective stress (p<0.001); hair cortisol lower at week 8 (p=0.025); sleep/insomnia measures improved. The strongest single trial, but still single-site and modest in size.
- Saxena 2012 (PMID:21977056): randomized, double-blind, placebo-controlled trial, n=150, OciBest (~1200 mg/day actives) for 6 weeks for general stress. Self-rated stress symptoms (forgetfulness, exhaustion, sleep problems, sexual problems of recent origin) decreased significantly; overall ~39% greater symptom improvement than placebo. Outcomes were entirely self-rated symptom scales with no biomarker (e.g., cortisol) confirmation.

**Anxiety (clinical-leaning population).**
- Bhattacharyya 2008 (PMID:19253862): controlled trial, n=35, 500 mg standardized leaf extract twice daily for 60 days in generalized anxiety disorder. Reported significant (p<0.001) reductions in anxiety, stress, and depression and improved attention/adjustment. Very small, weak randomization/blinding reporting, high risk of bias — hypothesis-generating only.

**Cognition.** Direct cognitive endpoints are thin; "neurocognition" appears only as a secondary/aggregated signal in the systematic review and as attention sub-measures in the small anxiety trial. No adequately powered cognition RCT in healthy adults was found.

**Bottom line:** Replicated direction-of-effect for stress reduction (and stress-axis biomarkers in one trial) in healthy-stressed groups, plus metabolic signals — but small samples, heterogeneous extracts/doses, and pervasive bias keep the honest grade at 2. Cognition efficacy is not established.

## Safety & interactions (research metadata)
Tulsi was generally well tolerated in the short (6-8 week) human trials, with no major adverse events reported (Lopresti 2022 — PMID:36185698; Jamshidi & Cohen 2017 — PMID:28400848). Two specific cautions stand out:

- **Antiplatelet / anticoagulant interaction:** Eugenol, a major tulsi constituent, inhibits platelet aggregation in vitro and in animal models. Co-use with aspirin, warfarin, clopidogrel, or other antiplatelet/anticoagulant agents carries a theoretical additive bleeding risk. This is mechanistic/preclinical, not demonstrated as a clinical interaction in controlled human trials.
- **Antifertility / pregnancy caution:** Ocimum sanctum produced reversible antispermatogenic effects (reduced sperm count/motility) in rodent studies (Seth 1981 — PMID:7309144), and related animal work reports altered reproductive hormones. Human relevance is unestablished, but this supports precautionary avoidance during pregnancy and for men actively trying to conceive.
- **Glucose lowering:** Metabolic trials in the systematic review report reduced glucose/metabolic markers, so additive hypoglycemia with antidiabetic drugs is theoretically plausible (no controlled human interaction data — unsourced).

This section is research metadata, not medical advice.

## Open questions
- **Extract heterogeneity:** OciBest, Holixer, and crude leaf extracts differ in standardization (eugenol/ursolic acid/rosmarinic acid), making cross-study comparison and dosing guidance unreliable.
- **Risk of bias:** the systematic review flags small, heterogeneous, biased trials; an adequately powered, well-reported RCT is still needed, especially for cognition.
- **Cognition gap:** no direct, adequately powered cognitive-performance RCT in healthy adults; cognitive benefit is currently inferred, not shown.
- **Biomarker confirmation:** only Lopresti 2022 measured cortisol/physiological stress markers; other "stress" trials relied on self-report.
- **Antifertility translation:** whether the rodent antispermatogenic signal occurs at human doses is unknown and unstudied in humans.
- **Anticoagulant interaction:** the eugenol antiplatelet signal has not been quantified as a clinical bleeding interaction in humans.
