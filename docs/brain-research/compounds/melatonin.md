---
id: melatonin
name: Melatonin
aliases:
  - "N-acetyl-5-methoxytryptamine"
  - "MT"
type: compound
klass: indoleamine hormone / chronobiotic
status: draft
evidence_overall: 3
onset: "30-60 min (immediate-release); chronobiotic phase-shift effect accrues over days"
half_life: "~30-60 min (immediate-release, highly variable); prolonged-release formulations extend exposure"
dose_range: "0.3-5 mg oral; ~0.3-0.5 mg approximates physiologic levels and is effective for circadian timing; up to ~4 mg studied for sleep onset"
cognitive_domains:
  - sleep onset / sleep quality
  - circadian phase alignment
  - daytime alertness (secondary to improved sleep timing)
channels:
  - channel: glymph
    mechanism: "Endogenous circadian signal; exogenous dosing shifts circadian phase (advances DLMO) and modestly shortens sleep-onset latency. Sleep/circadian timing is the well-supported human effect. Direct enhancement of glymphatic amyloid-beta clearance is demonstrated only in animal models."
    evidence: 3
    population: both
    direction: modulate
  - channel: inflam
    mechanism: "Direct free-radical scavenging plus induction of antioxidant enzymes (SOD, catalase, glutathione peroxidase); reduces circulating pro-inflammatory cytokines in clinical trials. CNS-specific neuroinflammation/neuroprotection benefit is largely preclinical."
    evidence: 2
    population: both
    direction: down
safety:
  contraindications:
    - "Known hypersensitivity to melatonin or formulation excipients"
    - "Activities requiring full alertness shortly after dosing (driving) due to possible sedation/next-day grogginess"
  interactions:
    - "Fluvoxamine (CYP1A2 inhibition): markedly raises melatonin levels"
    - "CYP1A2 inhibitors/inducers generally (e.g., ciprofloxacin; smoking induces and lowers levels)"
    - "Sedatives/hypnotics/CNS depressants: additive sedation"
    - "Anticoagulants/antiplatelets (e.g., warfarin): possible additive effect, monitor"
    - "Antihypertensives and antidiabetic agents: possible BP and glucose modulation"
  notable_risks:
    - "Next-day grogginess/drowsiness, headache, dizziness"
    - "Vivid dreams; transient mood changes reported"
    - "Wrong-timing dosing can shift circadian phase in the unintended direction"
    - "OTC product label-dose inaccuracy and melatonin overdosing in children (unintentional ingestions rising)"
    - "Limited long-term human safety data, especially in children and during pregnancy/lactation"
sources:
  - "PMID: 12076414 (Herxheimer & Petrie, Cochrane Database Syst Rev 2002, melatonin for jet lag; DOI: 10.1002/14651858.CD001520)"
  - "PMID: 23691095 (Ferracioli-Oda et al., PLoS One 2013, meta-analysis primary sleep disorders; DOI: 10.1371/journal.pone.0063773)"
  - "PMID: 21120122 (van Geijlswijk et al., Sleep 2010, exogenous melatonin in delayed sleep phase disorder meta-analysis; DOI: 10.1093/sleep/33.12.1605)"
  - "PMID: 38888087 (Cruz-Sanabria et al., J Pineal Res 2024, dose-response meta-analysis of timing/dose; DOI: 10.1111/jpi.12985)"
  - "PMID: 29637859 (Pappolla et al., Curr Alzheimer Res 2018, melatonin enhances Abeta lymphatic clearance in transgenic mice; DOI: 10.2174/1567205015666180411092551)"
  - "PMID: 33581247 (Cho et al., Brain Behav Immun 2021, anti-inflammatory effects meta-analysis; DOI: 10.1016/j.bbi.2021.01.034)"
  - "PMID: 27500468 (Reiter et al., J Pineal Res 2016, melatonin as antioxidant review; DOI: 10.1111/jpi.12360)"
tags:
  - chronobiotic
  - circadian
  - sleep
  - jet-lag
  - hypnotic
  - antioxidant
  - preclinical-neuroprotection
---

## Summary

Melatonin is best understood as a **chronobiotic** — a signal that shifts the circadian clock — rather than as a true sleeping pill or a cognitive enhancer. Its strongest, well-replicated human benefits are in **circadian timing**: reducing jet lag, advancing sleep in delayed sleep-phase disorder, and aligning sleep-wake rhythm. As a **hypnotic** its effect is real but **modest**: meta-analyses show only a small reduction in sleep-onset latency (on the order of minutes). The popular "brain cleaning" narrative — melatonin enhancing glymphatic amyloid-beta clearance and providing neuroprotection — is **largely preclinical** (transgenic mouse and in-vitro models) and should not be presented as an established cognitive or anti-Alzheimer benefit in humans. evidence_overall is graded 3 on the strength of the chronobiotic/sleep-timing literature, not on the unproven neuroprotection claims.

## Mechanism

Endogenous melatonin is secreted by the pineal gland under suprachiasmatic-nucleus control, rising in the biological evening and signaling "internal night." Exogenous melatonin acts on MT1/MT2 receptors to (1) shift circadian phase along a phase-response curve — evening/pre-bedtime dosing advances the clock — and (2) modestly promote sleep onset. The phase-shifting (chronobiotic) action is the dominant and most robust mechanism; the direct sleep-inducing (hypnotic) action is weaker.

Separately, melatonin is a direct free-radical scavenger and induces endogenous antioxidant enzymes (SOD, catalase, glutathione peroxidase), giving it antioxidant/anti-inflammatory activity (PMID: 27500468). A proposed mechanism for cognitive/neuroprotective benefit is enhanced glymphatic/lymphatic clearance of amyloid-beta — but this is demonstrated in animal models (PMID: 29637859), not in human cognition trials.

## Evidence

**Chronobiotic — strong.**
- Jet lag: The Cochrane review (PMID: 12076414) found melatonin "remarkably effective" for jet lag across 5+ time zones; 8 of 10 trials showed significant reductions in jet-lag score, with maximal effect near ~0.3-0.5 mg taken at destination bedtime.
- Delayed sleep-phase disorder: Meta-analysis (PMID: 21120122) found melatonin advanced endogenous melatonin onset (DLMO) by ~1.18 h (95% CI 0.89-1.48) and decreased sleep-onset latency by ~23 min, confirming a genuine circadian phase-shifting effect.

**Hypnotic — modest.**
- Primary sleep disorders meta-analysis (PMID: 23691095): melatonin reduced sleep-onset latency by ~7.06 min (95% CI 4.37-9.75), increased total sleep time by ~8.25 min (95% CI 1.74-14.75), and improved sleep quality (SMD 0.22). The authors explicitly characterize the effect as **modest** and smaller than standard hypnotics, but with a benign side-effect profile.
- Dose-response meta-analysis (PMID: 38888087): effect on sleep-onset latency and total sleep time peaked around ~4 mg/day, with timing (administering ~3 h before desired bedtime) a significant predictor — reinforcing that timing matters as much as dose, consistent with a chronobiotic mechanism.

**Glymphatic / amyloid clearance / neuroprotection — preclinical only.**
- Melatonin (2 mg/mL in drinking water) enhanced Abeta lymphatic/glymphatic clearance in Tg2576 transgenic mice (PMID: 29637859). This is an **animal model**; there is no robust human cognition or disease-modification trial establishing a glymphatic "brain-cleaning" benefit. Treat as hypothesis-generating, not as a demonstrated human cognitive enhancement.

**Anti-inflammatory / antioxidant — mixed/preclinical for CNS.**
- A clinical meta-analysis (PMID: 33581247) found melatonin reduces circulating pro-inflammatory markers (e.g., TNF-alpha, IL-6, CRP) in various conditions. Mechanistic antioxidant review: PMID: 27500468. CNS-specific neuroprotection remains primarily preclinical.

## Safety & interactions

- **Next-day effects:** Most common issues are next-morning grogginess/drowsiness, headache, and dizziness — more likely at higher doses, with prolonged-release formulations, or when dosed late. Lower physiologic doses (~0.3-0.5 mg) minimize hangover.
- **Drug interactions:** Melatonin is metabolized largely by CYP1A2. The CYP1A2 inhibitor **fluvoxamine** dramatically increases melatonin levels; other CYP1A2 inhibitors (e.g., ciprofloxacin) similarly raise exposure, while smoking induces CYP1A2 and lowers levels. Additive sedation with hypnotics/benzodiazepines/alcohol. Possible additive effects with anticoagulants/antiplatelets (monitor), antihypertensives, and antidiabetic agents.
- **Pregnancy/lactation:** Insufficient human safety data; generally avoid unless clearly indicated and clinician-directed.
- **Children:** Used clinically (e.g., DSPD, neurodevelopmental conditions) but long-term safety data are limited; OTC product mislabeling and rising pediatric accidental ingestions are a real public-health concern — secure supply and verify dose.
- **Dosing guidance:** For circadian/jet-lag use, low doses (~0.3-0.5 mg) timed to target bedtime are effective and physiologic; for sleep onset, ~0.5-5 mg taken ~30-60 min (or up to ~3 h) before desired bedtime. More is not clearly better and raises grogginess risk. Timing is critical — mistimed dosing can shift the clock the wrong way.

## Open questions

- Does any human evidence support a glymphatic/amyloid-clearance or neuroprotective benefit, or does it remain confined to animal models? (Currently preclinical: PMID: 29637859.)
- Optimal dose and formulation (immediate vs prolonged release) for sleep-onset versus circadian realignment, given large interindividual pharmacokinetic variability.
- Long-term safety of chronic use, particularly in children and adolescents, and effects on endogenous melatonin secretion and pubertal timing.
- Whether the modest hypnotic effect is clinically meaningful for primary insomnia versus its clearer role in circadian/timing disorders.
- Reliability and accuracy of OTC product labeling (actual vs stated melatonin content).
