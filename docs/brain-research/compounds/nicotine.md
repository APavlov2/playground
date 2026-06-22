---
id: nicotine
name: Nicotine
aliases: [nicotine patch, nicotine gum, nicotine lozenge, transdermal nicotine, NRT (nicotine replacement therapy)]
type: compound
klass: Nicotinic acetylcholine receptor (nAChR) agonist / stimulant — high dependence liability
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Tobacco & nightshade plants (Nicotiana); purified for patches/gum"
status: draft
evidence_overall: 3
onset: "acute; gum/lozenge ~peak 30 min, transdermal patch slow (hours, steady)"
half_life: "nicotine ~2 h; metabolite cotinine ~16 h (Benowitz 2009)"
dose_range: "research/NRT context: gum/lozenge 2-4 mg per dose; transdermal patch 7-21 mg/24 h. NOT a recommendation — high abuse liability; lab cognition studies often used low single doses (e.g. 1-4 mg gum / 7 mg patch) in nonsmokers."
cognitive_domains: [fine motor, alerting attention, orienting attention, working memory, short-term episodic memory]
channels:
  - channel: ach
    mechanism: "Nicotine is an agonist at neuronal nicotinic acetylcholine receptors (nAChRs), principally the high-affinity alpha4-beta2 subtype (also alpha7). Activation of nAChRs on cortical/thalamic and presynaptic terminals enhances cholinergic signalling and downstream release of multiple neurotransmitters, the proximate basis for acute attention/working-memory effects. Chronic exposure causes receptor desensitization and upregulation (neuroadaptation)."
    evidence: 4
    population: healthy
    direction: up
  - channel: da
    mechanism: "Via alpha4-beta2 (often with alpha6) nAChRs on ventral tegmental area dopamine neurons, nicotine increases DA neuron firing and phasic burst firing, raising dopamine release in the nucleus accumbens — the core reward/reinforcement circuit driving ADDICTION/dependence, and also implicated in motivation and working-memory effects. This channel is the mechanistic basis of nicotine's high abuse liability, flagged prominently."
    evidence: 4
    population: healthy
    direction: up
  - channel: ne
    mechanism: "Nicotinic stimulation increases noradrenergic/sympathetic tone and central arousal (also peripheral catecholamine release contributing to cardiovascular effects). Supports the acute alerting/arousal component of attention effects; human cognitive attribution is mechanistic/indirect."
    evidence: 2
    population: healthy
    direction: up
safety:
  contraindications:
    - "ADDICTION / dependence: high abuse liability — primary contraindication for non-therapeutic cognitive use; do not initiate in nicotine-naive individuals"
    - "Cardiovascular disease (recent MI, unstable angina, serious arrhythmia) — sympathomimetic load"
    - "Uncontrolled hypertension"
    - "Pregnancy and breastfeeding (fetal neurodevelopmental harm; nicotine crosses placenta)"
    - "Adolescents / developing brain (heightened addiction vulnerability and neurodevelopmental concern)"
  interactions:
    - "Sympathomimetics / other stimulants (e.g. caffeine, amphetamines) — additive cardiovascular and arousal effects"
    - "Adenosine (nicotine may alter hemodynamic response during pharmacologic stress testing)"
    - "Smoking-cessation note: stopping smoking alters CYP1A2 (a smoke, not nicotine, effect) — relevant when transitioning between nicotine sources"
    - "Beta-blockers / antihypertensives (nicotine pressor effect may oppose them)"
  notable_risks:
    - "ADDICTION / physical dependence with withdrawal (craving, irritability, anxiety, concentration difficulty) — front-and-center risk"
    - "Cardiovascular: acute heart-rate and blood-pressure increase, vasoconstriction, catecholamine release; effects more intense with rapid (smoked) delivery than slow transdermal/gum (Benowitz 1997)"
    - "Tolerance (neuroadaptation) develops to some effects with repeated exposure"
    - "Nausea, dizziness, headache, palpitations at higher/unaccustomed doses; overdose toxicity possible (especially pediatric exposure to gum/lozenge/liquid)"
    - "Nicotine itself is distinct from combustion toxins, but is the addictive agent and not benign"
sources:
  - "Heishman SJ, Kleykamp BA, Singleton EG. Meta-analysis of the acute effects of nicotine and smoking on human performance. Psychopharmacology (Berl). 2010;210(4):453-469 — PMID:20414766 — doi:10.1007/s00213-010-1848-1"
  - "Benowitz NL. Pharmacology of nicotine: addiction, smoking-induced disease, and therapeutics. Annu Rev Pharmacol Toxicol. 2009;49:57-71 — PMID:18834313 — doi:10.1146/annurev.pharmtox.48.113006.094742"
  - "Benowitz NL. Clinical pharmacology of nicotine: implications for understanding, preventing, and treating tobacco addiction. Clin Pharmacol Ther. 2008;83(4):531-541 — PMID:18305452 — doi:10.1038/clpt.2008.3"
  - "Benowitz NL, Gourlay SG. Cardiovascular toxicity of nicotine: implications for nicotine replacement therapy. J Am Coll Cardiol. 1997;29(7):1422-1431 — PMID:9180099 — doi:10.1016/s0735-1097(97)00079-x"
  - "Benowitz NL, Burbank AD. Cardiovascular toxicity of nicotine: Implications for electronic cigarette use. Trends Cardiovasc Med. 2016;26(6):515-523 — PMID:27079891 — doi:10.1016/j.tcm.2016.03.001"
tags: [nootropic, stimulant, addictive, controlled-interest]
---

## Summary
Nicotine (here considered in non-smoked form — patch, gum, lozenge) is a nicotinic acetylcholine receptor (nAChR) agonist with **genuine acute cognitive effects** in healthy adults. The defining evidence is a meta-analysis (Heishman 2010, PMID:20414766) of 41 double-blind placebo-controlled trials, which found reliable acute improvements in fine motor, alerting and orienting attention, working memory, and short-term episodic memory, with small-to-moderate effect sizes (≈0.16-0.44). Crucially, those gains appeared in nonsmokers and minimally-deprived smokers, so they are **not merely withdrawal relief** — they likely represent true acute enhancement. The dominant caveat, flagged prominently, is **ADDICTION/dependence**: nicotine has high abuse liability (driven by mesolimbic dopamine), plus sympathomimetic **cardiovascular** effects, and tolerance develops with repeated use. The acute cognitive effect must be sharply distinguished from the chronic/dependent state, where benefit is confounded and the addiction/cardiovascular burden dominates. This entry is research metadata, neutral and non-advisory.

## Mechanism

- **ach (nAChR agonist, up) — primary, evidence 4:** Nicotine directly agonizes neuronal nicotinic acetylcholine receptors, principally the high-affinity alpha4-beta2 subtype (and alpha7). nAChRs are ligand-gated cation channels widely expressed on cortical, thalamic and presynaptic terminals; their activation enhances cholinergic transmission and facilitates release of multiple downstream neurotransmitters, which is the proximate substrate for the acute attention and working-memory effects. With chronic exposure these receptors desensitize and upregulate (neuroadaptation), the basis of tolerance and withdrawal (Benowitz 2009, PMID:18834313).

- **da (reward + working memory, up) — evidence 4:** Nicotine, via alpha4-beta2 nAChRs (often with alpha6) on VTA dopamine neurons, increases dopamine-neuron firing and phasic burst firing, raising dopamine release in the nucleus accumbens. This mesolimbic dopamine activation is the **core mechanism of ADDICTION/reinforcement** (high abuse liability) and also contributes to motivation and the working-memory effects. This is the channel that makes nicotine dangerous to initiate; it is graded solidly and flagged.

- **ne (arousal, up) — evidence 2:** Nicotinic stimulation raises noradrenergic/sympathetic tone and central arousal (and peripheral catecholamine release that drives part of the cardiovascular effect). This supports the alerting/arousal component of the attention findings; the specific human cognitive attribution is mechanistic/indirect.

## Evidence

**Acute cognitive effects — anchor source:**

- **Heishman 2010 meta-analysis (PMID:20414766):** 41 double-blind, placebo-controlled laboratory studies (published 1994-2008) in which nicotine was administered and performance assessed in **healthy adult nonsmokers, or smokers who were non-deprived or only minimally deprived (≤2 h)**. Nicotine/smoking produced significant positive effects across six domains: fine motor; alerting attention (accuracy and reaction time); orienting attention (reaction time); short-term episodic memory (accuracy); and working memory (reaction time). Effect sizes ranged ≈0.16-0.44 (small-to-moderate). The authors' key interpretive point: because the gains appeared in nonsmokers and minimally-deprived participants, they are **not confounded by withdrawal relief** and "likely represent true performance enhancement." This is the strongest reason to grade the acute attention/working-memory/fine-motor effect solidly rather than dismiss it as withdrawal reversal.

**Acute vs chronic/dependent — the central distinction:**

- The Heishman result is about **acute, single-dose** administration. It does NOT establish a durable nootropic benefit in habituated/dependent users, where tolerance (neuroadaptation, receptor desensitization/upregulation; Benowitz 2009, PMID:18834313) blunts effects and any apparent "boost" between doses is partly **withdrawal reversal**. The honest framing: nicotine acutely enhances specific narrow domains in non-dependent people, but chronic use shifts the cost-benefit decisively toward dependence and cardiovascular risk.

**Addiction mechanism / abuse liability:**

- **Benowitz 2009 (PMID:18834313)** and **Benowitz 2008 (PMID:18305452):** nicotine binds nicotinic cholinergic receptors to release dopamine (and other transmitters) in the reward pathway; alpha4-beta2* is the principal subtype mediating dependence. Repeated exposure causes desensitization, receptor upregulation, tolerance, and a physical-dependence/withdrawal cycle. This is why abuse liability is high and is flagged as the dominant caveat.

**Cardiovascular:**

- **Benowitz & Gourlay 1997 (PMID:9180099)** and **Benowitz & Burbank 2016 (PMID:27079891):** nicotine is sympathomimetic — increases heart rate and blood pressure and causes vasoconstriction via sympathetic neural stimulation and catecholamine release. Effects are **more intense with rapid (smoked) delivery** than slow transdermal/gum delivery; transdermal nicotine, unlike smoking, does not appear to increase blood coagulability. NRT-formulation cardiovascular risk in clinical trials is small, but nicotine is not cardiovascularly inert and is contraindicated in unstable cardiac disease.

**Overall grade — evidence_overall: 3.** The acute cognitive effect is well-supported by a meta-analysis of controlled trials (genuine, not withdrawal artifact), but effect sizes are small-to-moderate and confined to narrow domains, there is no durable/chronic enhancement evidence, and the addiction + cardiovascular profile is a heavy offsetting caveat. Solid acute signal, serious caveats — grade 3.

## Safety & interactions (research metadata)

- **ADDICTION / dependence (front and center):** Nicotine has **high abuse liability**. Mesolimbic dopamine reinforcement (da channel) drives rapid development of physical and psychological dependence, with a withdrawal syndrome (craving, irritability, anxiety, impaired concentration) on cessation. This is the single most important reason a non-dependent person should not initiate nicotine for cognition. Adolescents and the developing brain are especially vulnerable.
- **Cardiovascular:** acute heart-rate/blood-pressure rise, vasoconstriction, catecholamine release; sympathomimetic. More intense with rapid delivery; contraindicated in recent MI, unstable angina, serious arrhythmia, or uncontrolled hypertension (Benowitz 1997, PMID:9180099).
- **Pregnancy:** nicotine crosses the placenta and is a fetal neurodevelopmental toxin; contraindicated in pregnancy/breastfeeding.
- **Tolerance:** neuroadaptation (receptor desensitization/upregulation) develops with repeated exposure, blunting acute effects and feeding the dependence cycle (Benowitz 2009, PMID:18834313).
- **Other risks:** nausea, dizziness, headache, palpitations at higher/unaccustomed doses; acute toxicity/overdose possible, with pediatric exposure to gum/lozenge/e-liquid a notable poisoning hazard.
- **Interactions:** additive with other stimulants/sympathomimetics (cardiovascular + arousal); may oppose antihypertensives; relevant to adenosine cardiac stress testing. (Note: cessation of *smoking* alters CYP1A2 via combustion products, not nicotine itself — relevant when switching nicotine sources.)

## Open questions
- Does any of the acute domain-specific benefit translate into durable real-world cognitive value, or is it entirely offset by tolerance and dependence with repeated use? (Chronic controlled data are lacking.)
- Magnitude and time-course differences between delivery forms (slow transdermal vs faster gum/lozenge) for the *cognitive* effect specifically, separate from abuse liability.
- Whether non-dependent, slow-delivery use could ever have a defensible benefit/risk ratio is unresolved and clouded by the high addiction liability — the honest default is caution.
- Inter-individual variability (CHRNA5/A3/B4 and CYP2A6 genotype) in both cognitive response and addiction susceptibility.
- Long-term cerebrovascular and cardiovascular consequences of chronic non-smoked nicotine in otherwise healthy users remain incompletely characterized.
