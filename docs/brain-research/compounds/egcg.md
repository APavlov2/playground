---
id: egcg
name: EGCG
aliases:
  - "epigallocatechin gallate"
  - "epigallocatechin-3-gallate"
  - "EGCG"
  - "green tea catechin"
type: compound
klass: "polyphenol (flavan-3-ol catechin)"
status: draft
evidence_overall: 2
onset: "~0.5-2 h (acute EEG/CBF effects); cognitive/clinical effects, if any, over weeks-months"
half_life: "~3-5 h (plasma; dose-dependent, low oral bioavailability)"
dose_range: "Human trials: ~135-300 mg acute; TESDAD chronic 9 mg/kg/day. SAFETY CEILING: keep concentrated-extract EGCG below 800 mg/day (EFSA hepatotoxicity threshold)."
cognitive_domains:
  - attention
  - "calmness / mood (self-reported)"
  - "memory (Down syndrome, adjunct only)"
  - "executive / inhibitory control (Down syndrome, adjunct only)"
channels:
  - channel: inflam
    mechanism: "Direct antioxidant / radical scavenging; modulation of NF-kB and pro-inflammatory signalling (largely preclinical/in-vitro)."
    evidence: 2
    population: preclinical
    direction: down
  - channel: cbf
    mechanism: "Acute oral EGCG modulates cerebral blood flow (frontal cortex), measured by NIRS; effect not linked to cognitive change."
    evidence: 2
    population: healthy
    direction: modulate
  - channel: gaba
    mechanism: "Proposed calming / relaxation effect; acute EEG shift (increased alpha/beta/theta) and self-rated calmness. Mechanism inferred, not directly demonstrated; caffeine/L-theanine confound when delivered as green tea."
    evidence: 2
    population: healthy
    direction: modulate
  - channel: da
    mechanism: "Preclinical / mechanistic reports of dopaminergic modulation (e.g., COMT inhibition, MAO effects). Human cognitive relevance unclear."
    evidence: 1
    population: preclinical
    direction: modulate
safety:
  contraindications:
    - "Pre-existing liver disease or elevated transaminases"
    - "Concurrent hepatotoxic medications"
  interactions:
    - "Reduces non-heme iron absorption (chelation) when taken with meals"
    - "May reduce folate bioavailability (dihydrofolate reductase inhibition reported)"
    - "Additive/idiosyncratic hepatotoxicity risk with other liver-stressing agents or alcohol"
    - "Reported to reduce absorption/efficacy of some drugs (e.g., nadolol); caffeine co-exposure in green tea products"
  notable_risks:
    - "HEPATOTOXICITY: high-dose concentrated green tea extract can cause idiosyncratic acute liver injury, including rare liver failure"
    - "EFSA (2018): EGCG at or above 800 mg/day as a supplement raises serum transaminases; no single safe extract dose could be set"
    - "Risk highest on an empty stomach and with concentrated/ethanolic extracts"
sources:
  - "de la Torre R, et al. Safety and efficacy of cognitive training plus epigallocatechin-3-gallate in young adults with Down's syndrome (TESDAD): a double-blind, randomised, placebo-controlled, phase 2 trial. Lancet Neurol. 2016. PMID: 27302362; DOI: 10.1016/S1474-4422(16)30034-5"
  - "Scholey A, et al. Acute neurocognitive effects of epigallocatechin gallate (EGCG). Appetite. 2012. PMID: 22127270; DOI: 10.1016/j.appet.2011.11.016"
  - "Wightman EL, et al. Epigallocatechin gallate, cerebral blood flow parameters, cognitive performance and mood in healthy humans: a double-blind, placebo-controlled, crossover investigation. Hum Psychopharmacol. 2012. PMID: 22389082; DOI: 10.1002/hup.1263"
  - "EFSA ANS Panel. Scientific opinion on the safety of green tea catechins. EFSA Journal. 2018;16(4):5239. PMID: 32625874; DOI: 10.2903/j.efsa.2018.5239"
  - "Grajecki D, et al. Green tea extract-associated acute liver injury: Case report and review. Clin Liver Dis (Hoboken). 2022. PMID: 36523867; DOI: 10.1002/cld.1254"
tags:
  - polyphenol
  - catechin
  - "green tea"
  - antioxidant
  - "down syndrome"
  - hepatotoxicity-risk
  - "caffeine-confound"
  - "low-evidence"
---

## Summary

EGCG is the principal catechin in green tea and a potent antioxidant. As a brain-optimization compound, the **human cognitive evidence is limited and mixed (graded LOW-MODEST, 2)**. Acute studies in healthy adults show EEG shifts and self-reported calmness, plus modulation of cerebral blood flow, but these have generally **not** translated into measurable cognitive performance gains. The most cited positive cognitive result comes from a Down-syndrome population (TESDAD), as an adjunct to cognitive training, not from healthy enhancement. A **major safety concern** dominates: high-dose concentrated green tea extract can cause idiosyncratic hepatotoxicity.

Critically, much of green tea's reputed "calm alertness" is **confounded by caffeine and L-theanine** present in whole green tea; isolated EGCG should not be credited with those combined effects.

## Mechanism

- **Antioxidant / anti-inflammatory (inflam):** Direct free-radical scavenging and downregulation of pro-inflammatory signalling (NF-kB); strongest as a mechanistic/preclinical rationale rather than a demonstrated cognitive driver.
- **Cerebrovascular (cbf):** Acute oral EGCG alters frontal-cortex cerebral blood flow (NIRS), but in the same study this was decoupled from cognition.
- **Calming / GABAergic (gaba, modulate):** Acute EGCG produced EEG changes (increased alpha/beta/theta) and increased self-rated calmness — interpreted as a relaxed-attentive state. The GABAergic mechanism is inferred, not directly shown.
- **Dopaminergic (da):** Preclinical reports of COMT/MAO interaction; human cognitive relevance unestablished (graded 1).
- Low oral bioavailability of EGCG complicates extrapolation from in-vitro potency to brain effects.

## Evidence

**Acute, healthy adults (mixed):**
- Scholey et al. 2012 (PMID 22127270): 300 mg EGCG increased EEG alpha/beta/theta activity (frontal/central midline) and raised self-rated calmness / lowered stress — but this is a physiological/mood signal, not demonstrated task-level cognitive enhancement.
- Wightman et al. 2012 (PMID 22389082): 135-270 mg EGCG modulated cerebral blood flow (reduced frontal oxy-/total-hemoglobin) **with no effect on cognitive performance or mood**. This directly tempers enthusiasm: CBF change did not equal cognitive benefit.

**Caffeine confound:** These isolated-EGCG studies are valuable precisely because whole green tea co-delivers caffeine and L-theanine. Calming/attention claims attached to "green tea" frequently reflect that combination, not EGCG alone.

**Chronic, clinical (Down syndrome):**
- de la Torre et al. 2016, TESDAD (PMID 27302362): 12-month double-blind RCT, EGCG 9 mg/kg/day **plus** cognitive training vs placebo plus training in young adults with Down syndrome. The combination improved visual recognition memory, inhibitory control, and adaptive behaviour. Important caveats: (1) it is an adjunct-to-training effect, not EGCG monotherapy; (2) it is a population with a specific neurobiology (this targets DYRK1A overexpression), so it does **not** generalize to healthy cognitive enhancement.

**Net grading:** Overall cognition evidence in healthy people is weak and inconsistent; the clearest positive signal is disease-specific and adjunctive. Hence evidence_overall = 2.

## Safety & interactions

**HEPATOTOXICITY (primary risk — flag prominently):**
- High-dose, concentrated green tea **extract** (not brewed tea) is associated with idiosyncratic acute liver injury, including rare cases of acute hepatitis and liver failure (Grajecki et al. 2022, PMID 36523867).
- **EFSA 2018** (PMID 32625874; DOI 10.2903/j.efsa.2018.5239): EGCG at or above **800 mg/day** as a food supplement produces statistically significant rises in serum transaminases; EFSA could not establish a safe dose for EGCG from concentrated extracts. Brewed green tea infusions are generally regarded as safe.
- Risk appears higher with concentrated/ethanolic extracts and intake on an empty stomach.

**Other interactions:**
- **Iron:** EGCG chelates non-heme iron, reducing absorption — relevant for those with low iron status; separate from iron-rich meals/supplements.
- **Folate:** Reported inhibition of dihydrofolate reductase may reduce folate bioavailability.
- **Additive liver stress:** Avoid combining with other hepatotoxic agents or significant alcohol.
- **Drug absorption / caffeine:** Some drug-absorption interactions reported; green tea products also carry caffeine, which has its own pharmacology.

## Open questions

- Does isolated EGCG produce any reliable cognitive benefit in healthy adults, or are reported effects entirely physiological (EEG/CBF) and mood-level?
- How much of green tea's "calm focus" is EGCG vs caffeine + L-theanine? Properly factorial designs are needed.
- Does the TESDAD adjunctive benefit generalize beyond Down syndrome, or is it tied to DYRK1A-specific biology?
- What is the true dose-response and idiosyncratic-susceptibility profile for hepatotoxicity (genetic/metabolic predictors)?
- Can low bioavailability be overcome safely without raising hepatotoxicity risk?
