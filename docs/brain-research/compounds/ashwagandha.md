---
id: ashwagandha
name: Ashwagandha
aliases:
  - Withania somnifera
  - Indian ginseng
  - Winter cherry
  - KSM-66
  - Sensoril
  - Shoden
type: compound
klass: adaptogen (botanical)
status: draft
evidence_overall: 3
onset: "Acute calming variably reported within hours; measurable cortisol/stress and sleep effects accrue over 4-8 weeks of daily dosing."
half_life: "Not well characterized in humans; withanolides are the presumed actives, pharmacokinetics poorly defined (unsourced)."
dose_range: "300 mg twice daily (KSM-66, full-spectrum root) or 120-240 mg/day high-withanolide extracts (Sensoril/Shoden); most stress RCTs used 300-600 mg/day standardized root extract for 6-8 weeks."
cognitive_domains:
  - stress/anxiety reduction
  - sleep quality
  - memory (impaired/MCI; thin evidence)
  - executive function/attention (thin evidence)
channels:
  - channel: hpa
    mechanism: "Reduces serum cortisol and self-reported stress/anxiety vs placebo; primary and best-supported axis. Multiple RCTs and meta-analyses in stressed but otherwise healthy adults."
    evidence: 3
    population: healthy
    direction: down
  - channel: gaba
    mechanism: "Withania somnifera extract shows direct GABAergic activity at ionotropic GABA-A/GABA-rho receptors in vitro; proposed GABA-mimetic/anxiolytic mechanism. Cell/animal only; the responsible constituent is unidentified (withaferin A and withanolide A did not activate these receptors)."
    evidence: 2
    population: preclinical
    direction: up
  - channel: ntrophic
    mechanism: "Root extract (withanolide A) elevated BDNF and enhanced downstream BDNF signaling, reversing chronic-stress depression-like behavior in rodents. Preclinical only; no human neurotrophic biomarker data."
    evidence: 2
    population: preclinical
    direction: up
safety:
  contraindications:
    - "Pregnancy (traditionally regarded as abortifacient; avoid) and lactation."
    - "Active or history of autoimmune disease (e.g., Hashimoto thyroiditis, lupus, RA, MS) given immunostimulant potential."
    - "Pre-existing liver disease or use of other hepatotoxic agents."
    - "Hyperthyroidism / thyrotoxicosis; caution in any thyroid disorder."
  interactions:
    - "Thyroid hormone (levothyroxine) and thyroid status: ashwagandha can raise T3/T4 and lower TSH, risking iatrogenic thyrotoxicosis or additive effect."
    - "Sedatives/CNS depressants (benzodiazepines, alcohol, other GABAergics): possible additive sedation (mechanistically plausible)."
    - "Immunosuppressants: immunostimulant activity may antagonize."
    - "Antidiabetic and antihypertensive agents: possible additive lowering of glucose/blood pressure (unsourced)."
  notable_risks:
    - "HEPATOTOXICITY: documented ashwagandha-induced acute/cholestatic liver injury in case reports (jaundice within ~1-2 weeks of starting; biopsy-confirmed hepatocellular and canalicular cholestasis with necrosis), generally reversible on discontinuation."
    - "Thyrotoxicosis / thyroid dysfunction, including a case of thyrotoxicosis with supraventricular tachycardia."
    - "Immunostimulation that may aggravate autoimmune conditions."
    - "Common mild GI upset, drowsiness; most trials report mild-to-moderate adverse events only."
sources:
  - "Arumugam V et al., Explore (NY), 2024 — PMID:39348746 — DOI:10.1016/j.explore.2024.103062 (meta-analysis: 9 RCTs/558 pts; significant reductions in perceived stress, HAM-A anxiety, serum cortisol)."
  - "Chandrasekhar K, Kapoor J, Anishetty S, Indian J Psychol Med, 2012 — PMID:23439798 — DOI:10.4103/0253-7176.106022 (KSM-66, 300 mg BID; serum cortisol -27.9% vs -7.9% placebo, P=0.002; extract supplied by manufacturer Ixoreal Biomed)."
  - "Cheah KL et al., PLoS One, 2021 — PMID:34559859 — DOI:10.1371/journal.pone.0257843 (sleep meta-analysis: 5 RCTs/400 pts; SMD -0.59, 95% CI -0.75 to -0.42)."
  - "Choudhary D, Bhattacharyya S, Bose S, J Diet Suppl, 2017 — PMID:28471731 — DOI:10.1080/19390211.2017.1284970 (memory/cognition RCT in 50 MCI adults; small, India-based)."
  - "Tóth M et al., Clin Case Rep, 2023 — PMID:36937644 — DOI:10.1002/ccr3.7078 (ashwagandha-induced acute liver injury, cholestatic; reversible on withdrawal)."
  - "Ireland PJ, Hardy T, Burt AD, Donnelly MC, J R Coll Physicians Edinb, 2021 — PMID:34882134 — DOI:10.4997/JRCPE.2021.409 (hepatocellular DILI, 39-year-old woman)."
  - "Kamal HI et al., Cureus, 2022 — PMID:35475098 — DOI:10.7759/cureus.23494 (ashwagandha-associated thyrotoxicosis with supraventricular tachycardia)."
tags:
  - adaptogen
  - anxiolytic
  - cortisol
  - sleep
  - hepatotoxicity-risk
  - thyroid-caution
  - manufacturer-funded-bias
---

## Summary

Ashwagandha (*Withania somnifera*; standardized extracts KSM-66, Sensoril, Shoden) is an Ayurvedic adaptogen whose strongest evidence is for reducing **stress, anxiety, and serum cortisol** in stressed-but-healthy adults, with a secondary, smaller signal for **sleep**. Cognition data (memory, attention) are thinner and largely in impaired/MCI populations or small healthy-adult trials. Most positive RCTs are **small, single-site, India-based, and frequently manufacturer-funded or using manufacturer-supplied extract**, so the literature carries a meaningful risk of bias and likely publication bias. `evidence_overall: 3` reflects the best-supported claim (HPA/cortisol reduction backed by several RCTs plus concordant meta-analyses), not an average; it is held at 3 rather than 4 because of small-trial/funding bias and heterogeneity. Safety is the most important practical caveat: real-world **hepatotoxicity** case reports, **thyroid** stimulation (raised T3/T4), **immunostimulant/autoimmune** cautions, and **pregnancy** contraindication.

## Mechanism

- **HPA axis (primary):** Ashwagandha lowers serum cortisol and subjective stress, consistent with dampening of HPA-axis hyperactivity. This is the channel with direct human biomarker support.
- **GABAergic (preclinical):** Whole-extract *W. somnifera* shows direct activity at ionotropic GABA-A and GABA-rho receptors in heterologous expression systems, supporting a GABA-mimetic anxiolytic hypothesis. Notably the isolated marker withanolides (withaferin A, withanolide A) did **not** activate these receptors, so the active constituent is unidentified — this remains cell/animal-level mechanism, not human pharmacodynamics.
- **Neurotrophic (preclinical):** In rodent chronic-stress models, root extract / withanolide A raised BDNF and enhanced downstream BDNF-pathway signaling, paralleling antidepressant-like behavioral effects. No human neurotrophic biomarker data.
- Withanolides are the presumed bioactives; human pharmacokinetics (absorption, half-life) are poorly characterized.

## Evidence

**Stress / cortisol (best supported).** A 2024 meta-analysis of 9 RCTs (558 participants) found significant reductions vs placebo in Perceived Stress Scale (MD -4.72), Hamilton Anxiety (MD -2.19), and serum cortisol (MD -2.58) — Arumugam et al., *Explore (NY)*, 2024 (PMID:39348746). The foundational RCT (Chandrasekhar et al., *Indian J Psychol Med*, 2012; PMID:23439798) using KSM-66 300 mg BID for 60 days reported serum cortisol falling 27.9% vs 7.9% in placebo (P=0.002) with large stress-scale reductions — but the extract was supplied by manufacturer Ixoreal Biomed and the trial is single-site/India-based, a pattern repeated across much of this literature. Convergent additional meta-analyses report similar cortisol/anxiety reductions; effect sizes vary and heterogeneity is non-trivial.

**Sleep.** Meta-analysis of 5 RCTs (400 participants) found a small but significant improvement in overall sleep (SMD -0.59, 95% CI -0.75 to -0.42), more pronounced in diagnosed insomnia, at ≥600 mg/day, and ≥8 weeks — Cheah et al., *PLoS One*, 2021 (PMID:34559859). Graded 3 for the relevant stress/sleep claim; sleep alone is a smaller, heterogeneous effect.

**Cognition (thin).** The most-cited cognition RCT enrolled 50 adults with **mild cognitive impairment** (impaired population, not healthy), reporting improved memory, executive function, attention, and processing speed over 8 weeks — Choudhary et al., *J Diet Suppl*, 2017 (PMID:28471731). It is small, single-site, and India-based, with no disclosed funding in the available record. Healthy-adult cognition findings exist but are sparse and underpowered. **Healthy vs impaired:** cognition benefit is best documented in impaired/MCI adults; in healthy adults cognition evidence is weak and should not be over-claimed.

**Bias caveat.** Across stress, sleep, and cognition, trials are predominantly small, short, single-center, conducted in India, and often manufacturer-funded or using manufacturer-supplied standardized extract. Treat individual positive trials cautiously and weight the meta-analyses, while recognizing they inherit the primary-study bias.

## Safety & interactions

- **Hepatotoxicity (notable_risks).** Multiple peer-reviewed case reports describe **ashwagandha-induced liver injury**: cholestatic/hepatocellular pattern with jaundice typically 1-2 weeks after starting, biopsy showing canalicular/hepatocellular cholestasis and necrosis, generally reversible after discontinuation (Tóth et al., *Clin Case Rep*, 2023, PMID:36937644; Ireland et al., *J R Coll Physicians Edinb*, 2021, PMID:34882134). Causality in case reports is individual-level; absolute risk appears low but real. Counsel patients to stop and seek care if jaundice, dark urine, or RUQ pain occurs.
- **Thyroid.** Ashwagandha can **raise T3/T4 and lower TSH**; helpful in some subclinical-hypothyroid trials but risky otherwise, with a case of **thyrotoxicosis presenting as supraventricular tachycardia** (Kamal et al., *Cureus*, 2022, PMID:35475098). Caution with thyroid disease and with levothyroxine; monitor thyroid function.
- **Pregnancy.** Contraindicated — traditionally considered abortifacient; avoid in pregnancy and lactation.
- **Autoimmune / immunostimulant.** May stimulate immune activity (Th1); caution or avoid in autoimmune disease and with immunosuppressant therapy.
- **Sedation.** Additive sedation plausible with benzodiazepines, alcohol, and other CNS depressants (mechanistic).

## Open questions

- Are stress/cortisol effects replicable in **large, independent, non-manufacturer-funded, multi-ethnic** trials outside India?
- What is the **absolute incidence** and dose/extract dependence of hepatotoxicity, and which extracts/contaminants are implicated?
- Which constituent drives the **GABAergic** activity, and does it translate to measurable human pharmacodynamics?
- Is there any reliable **cognitive benefit in healthy adults** independent of stress/sleep improvement, or is cognition mostly a downstream/anxiety-mediated effect?
- Human **pharmacokinetics** (active withanolide identity, absorption, half-life) and long-term safety remain inadequately defined.
