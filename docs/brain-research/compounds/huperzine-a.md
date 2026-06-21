---
id: huperzine-a
name: Huperzine A
aliases: [Hup A, HupA, selagine, Huperzia serrata alkaloid, qian ceng ta]
type: compound
klass: Acetylcholinesterase inhibitor (reversible, selective) — research/Rx-adjacent
status: draft
evidence_overall: 2
onset: "acute (plasma appears 5-10 min after oral dose, Tmax ~58 min); cognitive trial readouts in dementia are at weeks. AChE inhibition is pharmacodynamically rapid"
half_life: "terminal (beta) half-life ~12 h (716 +/- 130 min) in healthy volunteers (PMID:18348466)"
dose_range: "50-200 micrograms/day oral (dementia RCTs commonly 200-400 mcg/day; the adolescent trial used 100 mcg/day). NOTE: dosed in MICROGRAMS — narrow margin, easy to overdose vs mg supplements"
cognitive_domains: [episodic-memory, learning, general-cognition-MMSE]
channels:
  - channel: ach
    mechanism: "Potent, reversible, selective inhibition of acetylcholinesterase, raising synaptic acetylcholine — the same drug-class mechanism as donepezil/rivastigmine/galantamine ('donepezil-lite'). This is a pharmacological DRUG action, not a nutrient/substrate effect"
    evidence: 3
    population: impaired
    direction: up
  - channel: glu
    mechanism: "Weak, non-competitive NMDA-receptor antagonist (IC50 ~65-82 micromolar) that attenuates glutamate-/NMDA-mediated calcium influx and excitotoxicity in preclinical models; proposed neuroprotection. Affinity is low relative to clinical exposures, so relevance in humans is uncertain"
    evidence: 1
    population: impaired
    direction: down
safety:
  contraindications: ["Cardiac conduction disorders / bradyarrhythmia (cholinergic vagotonic effect)", "Active peptic ulcer / GI bleeding (cholinergic acid/secretory stimulation)", "Seizure / epilepsy caution", "Asthma / COPD (cholinergic bronchoconstriction)", "Pregnancy & lactation — inadequate data, avoid"]
  interactions: ["Other cholinesterase inhibitors (donepezil, rivastigmine, galantamine) — ADDITIVE cholinergic toxicity, do NOT stack", "Cholinergic agonists / pro-cholinergics (e.g. high-dose choline sources) — additive", "Anticholinergics (antihistamines, TCAs, oxybutynin) — pharmacological antagonism / blunting", "Beta-blockers — additive bradycardia/AV effects", "Succinylcholine / depolarising neuromuscular blockers — prolonged effect (theoretical, AChE-inhibitor class)"]
  notable_risks: ["Cholinergic adverse effects: nausea, GI upset, hypersalivation, sweating, dizziness, blurred vision, bradycardia", "Narrow therapeutic margin — dosed in micrograms; cholinergic crisis on overdose (class effect)", "This is an Rx-adjacent DRUG mechanism, NOT a casual daily supplement", "Most efficacy/safety data come from low-quality, largely Chinese-language dementia trials with risk-of-bias and publication-bias concerns"]
sources:
  - "Li J, Wu HM, Zhou RL, Liu GJ, Dong BR — Huperzine A for Alzheimer's disease, Cochrane Database Syst Rev, 2008 — PMID:18425924 — DOI:10.1002/14651858.CD005592.pub2"
  - "Yang G, Wang Y, Tian J, Liu JP — Huperzine A for Alzheimer's Disease: A Systematic Review and Meta-Analysis of RCTs, PLoS One, 2013 — PMID:24086396 — DOI:10.1371/journal.pone.0074916"
  - "Sun QQ, Xu SS, Pan JL, Guo HM, Cao WQ — Huperzine-A capsules enhance memory and learning performance in 34 pairs of matched adolescent students, Zhongguo Yao Li Xue Bao, 1999 — PMID:10678121"
  - "Qian ZM et al. (PK in human volunteers) — Pharmacokinetics of huperzine A following oral administration to human volunteers, Eur J Drug Metab Pharmacokinet, 2007 — PMID:18348466 — DOI:10.1007/BF03191002"
tags: [nootropic, research-grade, cholinesterase-inhibitor, rx-adjacent]
---

## Summary
Huperzine A is a plant alkaloid (from *Huperzia serrata*) that acts as a **potent, reversible, selective acetylcholinesterase (AChE) inhibitor** — the same drug class as the prescription dementia drugs donepezil, rivastigmine and galantamine ("donepezil-lite"). It is best understood as a **research / Rx-adjacent drug**, not a casual supplement: it is dosed in **micrograms**, has a narrow margin, and produces cholinergic side effects. The bulk of clinical evidence is in **Alzheimer's disease and vascular dementia**, and those trials are **largely Chinese-language, small, and flagged for poor methodological quality and risk of bias** by Cochrane- and meta-analysis-style reviews (PMID:18425924, PMID:24086396). Evidence in **healthy** people is very thin — essentially one oft-cited adolescent-student trial (PMID:10678121). Honest overall grade: **2**.

## Mechanism
- **ach (primary) — AChE inhibition:** Huperzine A reversibly and selectively inhibits acetylcholinesterase, increasing synaptic acetylcholine. This is a *pharmacological* mechanism (a drug action), mechanistically well established and the basis of its dementia use; it is the same target as approved cholinesterase-inhibitor drugs. Graded 3 on mechanism in the **impaired** population where the cholinergic deficit is real; the healthy-subject benefit of further raising ACh is far less certain.
- **glu (secondary, preclinical) — weak NMDA antagonism:** Huperzine A is a *weak*, non-competitive NMDA-receptor antagonist (IC50 ~65,000-82,000 nM) and reduces glutamate-/NMDA-mediated calcium influx and excitotoxicity in cell and animal models, proposed as neuroprotection. Because the affinity is low relative to achievable human plasma levels, clinical relevance is uncertain — **preclinical only, graded 1, direction down** (dampening excitotoxic glutamate signalling).

## Evidence
**Dementia (impaired) — primary evidence base, with strong bias caveats:**
- **Cochrane review (Li et al., 2008, PMID:18425924):** 6 RCTs, 454 AD patients. Huperzine A showed beneficial effects on cognition and behaviour vs placebo, **but only one trial was of adequate quality and size**, so the authors concluded there is **inadequate evidence to recommend its use** and called for rigorous large multi-centre trials. Most trials were low methodological quality.
- **PLoS One systematic review & meta-analysis (Yang et al., 2013, PMID:24086396, DOI:10.1371/journal.pone.0074916):** 20 RCTs, 1,823 AD patients. MMSE improved ~2.9-3.8 points vs placebo at 8/12/16 weeks; however **the two trials using ADAS-Cog found NO significant difference**. **Bias is severe:** ~80% did not report randomisation method, ~95% lacked adequate allocation concealment, ~45% gave no blinding info, **18 of 20 trials were Chinese-language**, and funnel-plot asymmetry suggested publication bias. Authors say findings must be "interpreted with caution due to the poor methodological quality."
- The MMSE-vs-ADAS-Cog discrepancy plus the bias profile means the apparent dementia benefit should be treated as **uncertain**, not established.

**Healthy subjects — very thin:**
- **Sun et al., 1999 (PMID:10678121):** double-blind matched-pair trial in 34 pairs (68) of healthy adolescent students, 100 mcg/day for 4 weeks. Memory Quotient 115 +/- 6 (Hup A) vs 104 +/- 9 (placebo), P<0.01, with improved Chinese-language exam scores. This is the single most-cited healthy-subject study — small, short, single-population, Chinese-language, never robustly replicated. **Insufficient to support healthy cognitive enhancement on its own.**

**Net grade rationale:** mechanism is real and drug-like (3 for ach in impaired), but the *clinical* evidence is dominated by low-quality, bias-flagged dementia trials with an internal MMSE/ADAS-Cog inconsistency, and healthy-subject data are essentially a single small trial. Honest **evidence_overall = 2**. The glutamate/NMDA channel is preclinical only (capped at 1-2; graded 1).

## Safety & interactions
Huperzine A carries the **cholinergic adverse-effect profile of a cholinesterase inhibitor**: nausea, GI upset, hypersalivation, sweating, dizziness, blurred vision, and bradycardia; overdose risks a cholinergic crisis. Because it is dosed in **micrograms with a narrow margin**, accidental over-dosing is easy if treated like a typical milligram supplement.
- **Do NOT stack with other AChE inhibitors** (donepezil, rivastigmine, galantamine) or strong pro-cholinergics — effects are **additive and potentially toxic**.
- Caution with **beta-blockers** (additive bradycardia/AV effects), in **cardiac conduction disease / bradyarrhythmia**, **peptic ulcer or GI bleeding**, **asthma/COPD** (bronchoconstriction), and **seizure** history.
- **Anticholinergic** drugs (sedating antihistamines, TCAs, oxybutynin) pharmacologically oppose it.
- As an AChE-inhibitor class agent it can theoretically prolong **succinylcholine**-type neuromuscular blockade — relevant before surgery/anaesthesia.
- **Pregnancy and lactation:** inadequate data — avoid. Overall this should be treated as a **research/Rx-adjacent drug**, ideally under clinical supervision, not a casual nootropic.

## Open questions
- Does any genuine cognitive benefit survive **high-quality, non-Chinese-language, low-risk-of-bias RCTs**, or is the dementia signal an artefact of poor methodology and publication bias (PMID:18425924, PMID:24086396)?
- Why do **MMSE and ADAS-Cog disagree** in the same meta-analysis — is the MMSE effect real or measurement-biased?
- Is there **any reproducible benefit in healthy adults**, given the evidence rests on a single small adolescent trial (PMID:10678121)?
- Does the **weak NMDA/neuroprotective** mechanism operate at human-achievable concentrations, or is it purely preclinical?
- Long-term safety, tolerance/down-regulation of cholinergic receptors, and optimal/cycling dose in non-demented users — largely **(unsourced)**.
