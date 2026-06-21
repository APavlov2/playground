---
id: resveratrol
name: Resveratrol
aliases:
  - trans-resveratrol
  - "3,5,4'-trihydroxy-trans-stilbene"
type: compound
klass: polyphenol stilbenoid
status: draft
evidence_overall: 2
onset: "acute CBF effects ~45 min post-dose; cognitive/cerebrovascular benefits (if any) accrue over weeks to months"
half_life: "parent compound short (~1-3 h); extensively conjugated to sulfate/glucuronide metabolites with longer apparent half-life (reported up to ~9 h)"
dose_range: "75 mg twice daily (chronic, postmenopausal trials) to 250-500 mg single dose (acute CBF); AD trial escalated to 1000 mg twice daily"
cognitive_domains:
  - verbal memory
  - overall cognitive composite
  - cerebrovascular responsiveness
channels:
  - channel: cbf
    mechanism: "Increased cerebral blood flow / cerebrovascular responsiveness, likely via eNOS-mediated nitric oxide signaling; acute dose-dependent CBF rise in healthy adults and chronic improvement in cerebrovascular responsiveness in postmenopausal women"
    evidence: 3
    population: both
    direction: up
  - channel: inflam
    mechanism: "Antioxidant and putative SIRT1/AMPK activation reducing oxidative and inflammatory signaling; largely preclinical, not validated as a cognitive mechanism in humans"
    evidence: 1
    population: preclinical
    direction: down
  - channel: mito
    mechanism: "Proposed SIRT1/PGC-1alpha-driven mitochondrial biogenesis and improved bioenergetics; preclinical/mechanistic only, no human cognitive confirmation"
    evidence: 1
    population: preclinical
    direction: modulate
safety:
  contraindications: []
  interactions:
    - "anticoagulants / antiplatelet agents (theoretical additive bleeding risk)"
    - "CYP450 substrates (resveratrol inhibits CYP1A2, CYP2C9, CYP3A4 in vitro)"
    - "estrogenic / hormone-sensitive therapies (phytoestrogen activity)"
  notable_risks:
    - "gastrointestinal upset (nausea, diarrhea) at higher doses"
    - "phytoestrogenic activity: caution in hormone-sensitive conditions"
    - "in the Turner AD trial, greater brain-volume loss occurred in the resveratrol arm (significance uncertain)"
    - "poor oral bioavailability (<1%) limits parent-compound exposure"
sources:
  - "Kennedy DO, et al. Effects of resveratrol on cerebral blood flow variables and cognitive performance in humans: a double-blind, placebo-controlled, crossover investigation. Am J Clin Nutr. 2010;91(6):1590-7. PMID: 20357044. DOI: 10.3945/ajcn.2009.28641"
  - "Evans HM, Howe PRC, Wong RHX. Effects of Resveratrol on Cognitive Performance, Mood and Cerebrovascular Function in Post-Menopausal Women; A 14-Week Randomised Placebo-Controlled Intervention Trial. Nutrients. 2017;9(1):27. PMID: 28054939. DOI: 10.3390/nu9010027"
  - "Thaung Zaw JJ, Howe PRC, Wong RHX. Long-term effects of resveratrol on cognition, cerebrovascular function and cardio-metabolic markers in postmenopausal women (RESHAW): A 24-month randomised, double-blind, placebo-controlled, crossover study. Clin Nutr. 2021;40(3):820-829. PMID: 32900519. DOI: 10.1016/j.clnu.2020.08.025"
  - "Turner RS, et al. A randomized, double-blind, placebo-controlled trial of resveratrol for Alzheimer disease. Neurology. 2015;85(16):1383-91. PMID: 26362286. DOI: 10.1212/WNL.0000000000002035"
  - "Walle T, et al. High absorption but very low bioavailability of oral resveratrol in humans. Drug Metab Dispos. 2004;32(12):1377-82. PMID: 15333514. DOI: 10.1124/dmd.104.000885"
tags:
  - polyphenol
  - stilbenoid
  - cerebral-blood-flow
  - cerebrovascular
  - postmenopausal
  - low-bioavailability
---

## Summary

Resveratrol is a plant-derived stilbenoid polyphenol marketed for cognitive and vascular "anti-aging" benefit. The single most important caveat is its **very poor oral bioavailability** (<1% of parent compound), because resveratrol is rapidly conjugated to sulfate and glucuronide metabolites on first pass (Walle 2004, PMID 15333514). Human cognitive evidence is **mixed and population-dependent**, justifying only a modest overall grade (2).

The clearest human signal is on **cerebral blood flow / cerebrovascular function**, not on direct cognition. Acute dosing increases CBF in healthy young adults but does **not** acutely improve cognitive performance (Kennedy 2010). Chronic dosing in **postmenopausal women** has shown cerebrovascular and cognitive benefit over months (Evans 2017; RESHAW, Thaung Zaw 2021). A 52-week Alzheimer disease trial (Turner 2015) was primarily a safety/biomarker study and did not demonstrate clear cognitive benefit. The widely cited SIRT1/AMPK/mitochondrial mechanism is **largely preclinical** and should not be presented as established in humans.

## Mechanism

- **Cerebrovascular (cbf):** The best-supported human mechanism. Resveratrol acutely raises cerebral blood flow (dose-dependent, frontal cortex) during cognitive tasks, plausibly through eNOS/nitric-oxide-mediated vasodilation. Chronically it improves cerebrovascular responsiveness to hypercapnic and cognitive stimuli in postmenopausal women.
- **Anti-inflammatory / antioxidant (inflam):** Proposed activation of SIRT1 (a NAD+-dependent deacetylase) and AMPK, downregulating oxidative and inflammatory pathways. This is **largely preclinical** and not confirmed as a cognitive mechanism in humans (graded 1).
- **Mitochondrial (mito):** Proposed SIRT1/PGC-1alpha-driven mitochondrial biogenesis and improved bioenergetics. **Preclinical/mechanistic only** in this context (graded 1).

The low systemic exposure of parent resveratrol creates a persistent mechanistic gap: many in vitro SIRT1/AMPK effects occur at concentrations far above achievable human plasma levels, so the relevance of conjugated metabolites to brain effects remains uncertain.

## Evidence

- **Kennedy 2010 (PMID 20357044) — healthy, acute; CBF up but no cognition.** Double-blind, placebo-controlled crossover in 24 healthy young adults (250 mg, 500 mg, placebo). Resveratrol produced dose-dependent increases in cerebral blood flow variables (deoxyhemoglobin, total hemoglobin via NIRS) during cognitive tasks, but did **not** improve cognitive performance acutely. This is the key honesty point: CBF effect without acute cognitive benefit.
- **Evans 2017 (PMID 28054939) — postmenopausal, chronic; cognitive + cerebrovascular benefit.** 14-week RCT, 80 postmenopausal women, 75 mg twice daily. Reported ~17% increase in cerebrovascular responsiveness and improvements in verbal memory and overall cognitive performance, correlated with the cerebrovascular change. Suggests benefit in this specific population over months.
- **RESHAW / Thaung Zaw 2021 (PMID 32900519) — postmenopausal, long-term.** 24-month randomised, double-blind, placebo-controlled crossover, 75 mg twice daily. Reported significant improvement in overall cognitive performance (~33% over placebo at 12 months) plus improved cerebral blood flow velocity / cerebrovascular responsiveness and better insulin sensitivity; verbal memory gains notable in women aged 65+. Reinforces the postmenopausal-chronic signal but does not generalize to healthy young or acute use.
- **Turner 2015 (PMID 26362286) — Alzheimer disease; safety/biomarker, not clearly cognitive.** 52-week phase 2 RCT, 119 patients with mild-to-moderate AD, escalated to 1000 mg twice daily. Primarily assessed safety, tolerability, and biomarkers (plasma/CSF Abeta40/42, tau) and MRI volumetrics. Resveratrol was safe and well tolerated and CNS-penetrant, but did **not** establish clear cognitive benefit; notably, brain-volume loss was greater in the resveratrol arm — a finding of uncertain significance that argues for caution rather than enthusiasm.

**Net read:** Consistent human CBF/cerebrovascular signal; cognitive benefit largely confined to chronic dosing in postmenopausal women; no acute cognitive benefit in healthy adults; no clear AD cognitive benefit. Grade 2 (modest).

## Safety & interactions

- **Anticoagulants / antiplatelets:** Theoretical additive bleeding risk via antiplatelet activity; caution with warfarin, DOACs, aspirin, and around surgery.
- **Estrogenic activity:** Resveratrol is a phytoestrogen; use caution in hormone-sensitive conditions (e.g., certain breast/endometrial cancers) and with hormone therapies.
- **Gastrointestinal:** Nausea and diarrhea reported, more frequent at the higher doses used in the AD trial.
- **CYP enzymes:** In vitro inhibition of CYP1A2, CYP2C9, and CYP3A4; potential to alter metabolism of co-administered drugs cleared by these pathways (clinical magnitude uncertain).
- **Bioavailability:** <1% parent-compound bioavailability (Walle 2004) is itself a safety-relevant limitation — effective exposure is dominated by conjugated metabolites, complicating dose-response and interaction prediction.

## Open questions

- Does the human CBF effect translate to durable cognitive benefit outside the postmenopausal population? Healthy young/acute data say no acutely. (unsourced for healthy chronic non-menopausal cognition)
- Is the postmenopausal benefit driven by an estrogen-deficiency-specific cerebrovascular interaction, or generalizable to other estrogen-low states?
- Are the in-human effects mediated by parent resveratrol, its sulfate/glucuronide metabolites, or downstream metabolites? Mechanistic attribution to SIRT1/AMPK/mitochondrial pathways remains preclinical.
- What explains the greater brain-volume loss in the Turner AD arm, and is it adverse, pseudoatrophy, or noise?
- Does bioavailability-enhanced formulation (e.g., piperine co-administration, micronization) change the human cognitive picture? (unsourced for cognitive outcomes)
