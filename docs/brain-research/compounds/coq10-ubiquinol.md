---
id: coq10-ubiquinol
name: Coenzyme Q10 / Ubiquinol
aliases: [CoQ10, ubiquinone, ubiquinol, coenzyme Q, CoQ, ubidecarenone]
type: compound
klass: Mitochondrial cofactor / lipophilic antioxidant
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Endogenous; organ meats, fatty fish; commercial form fermentation-produced"
status: draft
evidence_overall: 1
onset: "Plasma levels rise over days-weeks; any putative chronic/cumulative effect. Brain-relevant trials (neurodegeneration) ran for years with no benefit; migraine prophylaxis benefit emerged only by the 3rd treatment month"
half_life: "Plasma elimination ~33 h; tissue stores turn over slowly. Note: oral CoQ10 has poor, variable bioavailability and limited blood-brain-barrier penetration"
dose_range: "Brain/neuro trials used high doses: 1200-2400 mg/day (QE3 Parkinson, 2CARE Huntington). Migraine RCT: 300 mg/day (3x100 mg). Ubiquinol cognition protocol: 200 mg/day. No validated brain-optimisation dose in healthy people"
cognitive_domains: []
channels:
  - channel: mito
    mechanism: "Obligatory electron carrier in the inner-mitochondrial-membrane electron transport chain, shuttling electrons from complex I and II to complex III; supports oxidative phosphorylation/ATP synthesis. Mechanistically real and central to bioenergetics, but cognitive read-through in humans is unproven and the large high-dose neurodegeneration trials (which directly tested a bioenergetic-rescue hypothesis) were null."
    evidence: 1
    population: both
    direction: up
  - channel: inflam
    mechanism: "Reduced (ubiquinol) form is a lipid-phase chain-breaking antioxidant that scavenges peroxyl radicals and regenerates vitamin E, limiting lipid peroxidation; indirectly anti-inflammatory. Plausible redox role, but no demonstrated neuroinflammatory cognitive endpoint in humans; the antioxidant rationale did not translate into clinical benefit in the neurodegeneration RCTs."
    evidence: 1
    population: both
    direction: down
safety:
  contraindications: []
  interactions: [warfarin — CoQ10 is structurally similar to vitamin K and may reduce anticoagulant (INR) effect; antihypertensives — possible modest additive BP-lowering; statins lower endogenous CoQ10 (basis for the separate, non-brain statin-myopathy use)]
  notable_risks: [generally very well tolerated even at 2400 mg/day in trials; mild GI upset (nausea, dyspepsia) most common; no safety signals in large neurodegeneration RCTs]
sources:
  - "McGarry et al. (Huntington Study Group 2CARE Investigators), Neurology, 2017 — PMID:27913695 (2CARE; CoQ10 2400 mg/day, n=609, terminated for futility, no benefit on Total Functional Capacity in Huntington disease)"
  - "Parkinson Study Group QE3 Investigators (Beal et al.), JAMA Neurology, 2014 — PMID:24664227 (QE3; CoQ10 1200 & 2400 mg/day, n=267, terminated for futility, no benefit and slight adverse trend in early Parkinson disease)"
  - "Sándor et al., Neurology, 2005 — PMID:15728298 (migraine prophylaxis RCT, 300 mg/day, 50%-responder rate 47.6% vs 14.4% placebo, NNT 3)"
  - "Parohan et al., Nutritional Neuroscience, 2020 — PMID:30727862 (meta-analysis, 4 RCTs / 221 pts; migraine frequency -1.87 attacks/month, but NS on severity and duration)"
  - "Stough et al., Frontiers in Aging Neuroscience, 2019 — PMID:31191293 (study PROTOCOL only — planned ubiquinol 200 mg/day cognition trial in healthy elderly; no outcome data)"
  - "Nankivell et al., Nutrients, 2025 — PMID:40944284 (review: CoQ10 & cognition; mixed/no clear benefit in healthy people, inconsistent in disease; calls for high-quality RCTs)"
tags: [coq10, mitochondrial, antioxidant, low-evidence-brain]
---

## Summary
Coenzyme Q10 (ubiquinone; its reduced form is ubiquinol) is a lipophilic mitochondrial electron-transport cofactor and lipid-phase antioxidant. Its mechanisms are real bioenergetics and redox biology, which is exactly why it has been heavily tested as a neuroprotective agent. **For brain optimisation in healthy people the human evidence is essentially absent**: there are no positive cognition-enhancement trials in healthy adults, only a published study protocol and reviews noting "mixed / no clear benefit." More importantly, the two largest, best-resourced human brain trials — both directly testing CoQ10's bioenergetic/antioxidant rationale in neurodegeneration — were **null and stopped early for futility** (2CARE in Huntington disease, QE3 in early Parkinson disease). The one brain-adjacent indication with genuine, replicated support is **migraine prophylaxis**, but that is a vascular/headache-frequency endpoint, not cognition. The frequently-cited **statin-myopathy** use is a peripheral-muscle question, not a brain one. Accordingly the overall brain-optimisation grade is held at **1**: strong mechanism, but the decisive human trials that tested it failed.

## Mechanism
**mito (electron transport chain, up).** CoQ10 is the obligatory mobile electron carrier of the inner-mitochondrial-membrane respiratory chain, accepting electrons from complex I (NADH dehydrogenase) and complex II (succinate dehydrogenase) and delivering them to complex III, thereby supporting the proton gradient and ATP synthesis. This is textbook, uncontested biochemistry. The brain is energy-hungry, so a bioenergetic-rescue hypothesis is plausible — and it was exactly the hypothesis tested in Huntington and Parkinson disease. It failed (see Evidence). Graded **1** because the mechanism, while real, did not produce any demonstrated cognitive or disease-modifying read-through in humans, and oral CoQ10 has poor, variable bioavailability with limited blood-brain-barrier penetration, weakening the path from "ETC cofactor" to "brain effect."

**inflam (antioxidant, down).** Ubiquinol (the reduced 2-electron form) is a chain-breaking lipid-soluble antioxidant: it scavenges peroxyl radicals in membranes and lipoproteins and helps regenerate α-tocopherol, limiting lipid peroxidation. This gives a plausible anti-oxidative/anti-neuroinflammatory rationale. Graded **1**: no human neuroinflammatory cognitive endpoint has been demonstrated, and the antioxidant rationale (the explicit basis for the neurodegeneration trials) did not translate into clinical benefit.

## Evidence
Be strict here. The mechanism is seductive; the human brain outcomes are not.

- **Huntington disease — 2CARE (NULL, stopped for futility):** McGarry et al., Neurology 2017 (PMID:27913695). Randomized, double-blind, placebo-controlled trial of CoQ10 **2400 mg/day** in **609** HD patients across ~48 sites. A prespecified interim futility analysis (conditional power <5%) led to early termination; there were **no significant differences** between CoQ10 and placebo on the primary Total Functional Capacity / survival endpoint or secondary measures. The authors conclude the data "do not justify use of CoQ as a treatment to slow functional decline in HD." This is a direct, large, well-powered test of the bioenergetic hypothesis in a brain disease — and it is negative.
- **Early Parkinson disease — QE3 (NULL, stopped for futility):** Parkinson Study Group QE3 Investigators / Beal et al., JAMA Neurology 2014 (PMID:24664227). Randomized trial of CoQ10 **1200 and 2400 mg/day** vs placebo in **267** early PD patients. Terminated after a prespecified **futility** criterion was met; **no evidence of clinical benefit**, and both active arms showed a slight *adverse* trend relative to placebo. Treatment was safe and well tolerated. Again: a direct brain test of the mechanism, negative.
- **Healthy-population cognition (ABSENT data):** There are no positive cognition-enhancement RCTs in healthy adults. Stough et al., Frontiers in Aging Neuroscience 2019 (PMID:31191293) is a **study protocol only** (planned ubiquinol 200 mg/day, 90 days, healthy elderly) — it carries **no outcome data** and must not be cited as evidence of effect. The Nankivell et al. 2025 review (PMID:40944284) summarises the field as **mixed with no clear benefit in healthy people** and inconsistent in disease, explicitly calling for high-quality RCTs. So the "CoQ10/ubiquinol improves cognition in healthy people" claim is **unsupported** by human data.
- **Migraine prophylaxis (POSITIVE, but a different, non-cognitive endpoint):** Sándor et al., Neurology 2005 (PMID:15728298), 300 mg/day RCT, reported a 50%-responder rate for attack frequency of **47.6% (CoQ10) vs 14.4% (placebo), NNT 3**, with benefit emerging by the 3rd month. Parohan et al. meta-analysis, Nutritional Neuroscience 2020 (PMID:30727862), 4 RCTs / 221 participants, found CoQ10 reduced **migraine frequency by ~1.87 attacks/month** but had **no significant effect on attack severity or duration**. This is genuine and replicated — but it is a headache-frequency outcome, not cognition or brain optimisation, and does not lift the cognition grade.
- **Statin-associated myopathy (separate, NON-brain use):** Statins lower endogenous CoQ10, which is the rationale for supplementing it for muscle symptoms. This is a peripheral-muscle question and is noted only to keep it out of the brain claim.

Net: `evidence_overall: 1`. Real, central mitochondrial/antioxidant mechanisms; but the two large human brain trials that directly tested those mechanisms were null and stopped for futility, healthy-cognition data are absent (a protocol and mixed reviews only), and the one solid indication (migraine) is a non-cognitive endpoint. The brain-optimisation framing is not supported.

## Safety & interactions (research metadata)
- **Tolerability:** Excellent. CoQ10 was safe and well tolerated even at **2400 mg/day** in both 2CARE and QE3; mild GI upset (nausea, dyspepsia) is the most common complaint. No safety signals in the large RCTs.
- **Warfarin:** CoQ10 is structurally related to vitamin K and may **antagonise warfarin** (reduce INR/anticoagulant effect) — monitor in anticoagulated patients.
- **Antihypertensives:** possible modest additive blood-pressure lowering (precautionary).
- **Statins:** statins reduce endogenous CoQ10 levels (basis for the separate statin-myopathy use); a pharmacological interaction, not a brain effect.
- **Bioavailability caveat:** oral CoQ10/ubiquinol absorption is poor and highly variable, and CNS penetration is limited — relevant when interpreting any putative brain effect.

## Open questions
- Did the large neurodegeneration trials fail because the bioenergetic hypothesis is wrong for these diseases, or because oral CoQ10 cannot reach brain mitochondria at meaningful concentrations (bioavailability/BBB ceiling)?
- Would better-absorbed formulations (ubiquinol, solubilised/nanoparticle forms) or mitochondria-targeted analogues (e.g. MitoQ) change the brain read-out? (Out of scope here; CoQ10's own trials remain null.)
- Is there any healthy-population cognitive signal at all once the Stough protocol and similar trials report outcomes, or does the "no clear benefit" pattern hold?
- Does the migraine-frequency benefit reflect a vascular/mitochondrial-energetic mechanism that is genuinely brain-relevant, and is it confined to migraineurs with documented mitochondrial/oxidative abnormalities?
