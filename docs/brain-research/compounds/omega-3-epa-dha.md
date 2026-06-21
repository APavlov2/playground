---
id: omega-3-epa-dha
name: Omega-3 (EPA/DHA, fish oil)
aliases: [fish oil, EPA, DHA, long-chain omega-3]
type: compound
klass: Structural lipid / anti-inflammatory
status: draft
evidence_overall: 2
onset: "Cumulative over weeks-months; mood/depression RCTs typically run 6-12 weeks, cognition trials 6-40 months"
half_life: "Plasma phospholipid turnover days-weeks; membrane (erythrocyte/brain) incorporation reaches steady state over ~3-6 months at gram-level doses; brain DHA washout is very slow (months)"
dose_range: "~1-2 g/day combined EPA+DHA typical; depression signal strongest with EPA-predominant (>=60% EPA) at <=1-2 g/day; AD trials used ~2 g/day DHA"
cognitive_domains: [mood, episodic-memory]
channels:
  - channel: inflam
    mechanism: "EPA and DHA are precursors of specialised pro-resolving mediators (resolvins, protectins/neuroprotectin D1, maresins) that actively drive resolution of inflammation and can dampen neuroinflammation; partly displace arachidonic-acid-derived pro-inflammatory eicosanoids. Strong mechanistic/preclinical basis; human neuroinflammatory cognitive endpoints not robustly demonstrated."
    evidence: 2
    population: both
    direction: down
  - channel: ntrophic
    mechanism: "DHA is the dominant n-3 fatty acid in neuronal membranes (~35% of synaptic-membrane fatty acids, esterified to PE/PS/PC); supports membrane fluidity, receptor/signal-transduction efficiency, synaptogenesis, neurite outgrowth and neurotransmitter release; preclinically raises BDNF. Structural role is well established; downstream cognitive benefit in replete humans is not."
    evidence: 2
    population: both
    direction: up
  - channel: ser
    mechanism: "EPA-predominant formulations reduce depressive symptoms in meta-analysis (mechanism likely anti-inflammatory and membrane/monoaminergic modulation rather than a direct, demonstrated serotonergic effect — channel assignment reflects mood outcome, not a proven 5-HT mechanism). DHA-only formulations are not effective for mood."
    evidence: 3
    population: impaired
    direction: up
safety:
  contraindications: []
  interactions: [anticoagulants/antiplatelets — theoretical additive bleeding risk; pooled RCT evidence shows no overall increase in bleeding, though high-dose purified EPA carries a modest relative increase]
  notable_risks: [mild GI upset / fishy reflux, lipid oxidation of poorly stored product, possible LDL-C rise with high-dose purified EPA formulations]
sources:
  - "Liao et al., Translational Psychiatry, 2019 — PMID:31383846 (meta-analysis, 26 RCTs / 2160 pts; overall SMD -0.28; EPA>=60% effective, DHA-predominant not)"
  - "Sydenham, Dangour & Lim, Cochrane Database Syst Rev, 2012 — PMID:22696350 (prevention in cognitively healthy older adults; 3 RCTs / ~4080; no benefit on cognition)"
  - "Quinn et al., JAMA, 2010 — PMID:21045096 (DHA 2 g/day, 18 mo, mild-moderate Alzheimer disease; no cognitive/functional benefit)"
  - "Zhang et al., Aging Clin Exp Res, 2016 — PMID:26025463 (meta-analysis, 6 RCTs; small WMD 0.15 on MMSE, p=0.003)"
  - "Yurko-Mauro et al., PLoS ONE, 2015 — PMID:25786262 (DHA & adult memory meta-analysis; episodic-memory benefit in adults with mild memory complaints)"
  - "Javaid et al., J Am Heart Assoc, 2024 — PMID:38742535 (bleeding meta-analysis, 11 RCTs / 120,643 pts; rate ratio 1.09, 95% CI 0.91-1.31, NS overall)"
tags: [omega-3, structural-lipid]
---

## Summary
EPA and DHA are long-chain marine omega-3 fatty acids. DHA is a major structural lipid of neuronal/synaptic membranes; EPA is the more potent substrate for anti-inflammatory, pro-resolving lipid mediators. For brain optimisation the honest picture is population-dependent and mostly modest. The best-supported brain effect is on **mood/depression**, and there it is **EPA-predominant formulations** that work — DHA-only does not. For **cognition**, large, well-conducted trials in cognitively-normal older adults and in established Alzheimer disease are largely **null**, so omega-3 should not be presented as a cognition enhancer or dementia preventive in replete people. Signals that look more favourable are concentrated in those with low baseline omega-3 status, mild memory complaints, or active depression — i.e. deficiency-correction rather than supraphysiological enhancement.

## Mechanism
**ntrophic (DHA, structural, up).** DHA constitutes the bulk of brain n-3 long-chain PUFA and ~35% of synaptic-membrane fatty acids, esterified mainly to phosphatidylethanolamine and phosphatidylserine. Its six double bonds confer membrane fluidity that supports lateral mobility of receptors, G-proteins, ion channels and neurotransmitter machinery, and it participates in synaptogenesis, neurite outgrowth and neurotransmitter release. Preclinical work links DHA to BDNF and synaptic-plasticity pathways. The structural biology is solid; what is *not* established is that adding DHA to an already-replete adult brain yields a measurable cognitive gain — hence grade 2 despite strong mechanism.

**inflam (EPA>DHA, down).** EPA and DHA are converted to specialised pro-resolving mediators (resolvins RvE/RvD, protectins/neuroprotectin D1, maresins; Serhan and colleagues) that actively terminate inflammation, and they displace arachidonic-acid-derived pro-inflammatory eicosanoids. This gives a plausible route to lower neuroinflammation. The evidence is strong mechanistically and preclinically but human brain-inflammation cognitive endpoints are not robustly demonstrated; grade 2.

**ser (mood, EPA-predominant, up).** The antidepressant signal is most consistent with EPA-predominant formulations. The mechanism is more likely anti-inflammatory/membrane-mediated than a directly demonstrated serotonergic action; the `ser` channel here tags the mood *outcome*, not a proven 5-HT mechanism.

## Evidence
Be scrupulous: the cognition-enhancement / prevention story is mostly null, while the EPA-for-depression story is genuinely positive.

- **Depression (positive, EPA-predominant):** Liao 2019 (PMID:31383846), meta-analysis of 26 RCTs / 2160 participants, found an overall benefit on depressive symptoms (SMD -0.28, p=0.004). Critically, the effect was driven by EPA: formulations with **>=60% EPA** were effective (EPA-pure SMD -0.50; EPA-major SMD -1.03) whereas DHA-predominant/DHA-only formulations were **not** effective. This is the strongest brain-relevant indication and underpins the grade-3 `ser` channel (population: depressed/impaired).
- **Prevention in cognitively-normal older adults (null):** Sydenham/Cochrane 2012 (PMID:22696350), 3 RCTs / ~4080 randomised (~3536 with follow-up cognitive data), found **no benefit** of omega-3 supplementation on cognitive function in cognitively healthy older people; both arms showed little decline over the trial windows. This null result is central and should not be glossed over.
- **Established Alzheimer disease (null):** Quinn 2010 (PMID:21045096), JAMA, randomised algal DHA 2 g/day vs placebo for 18 months in mild-to-moderate AD; **no effect** on ADAS-Cog, CDR sum-of-boxes, ADCS-ADL, NPI, or brain atrophy rate. Argues against DHA slowing AD progression overall.
- **Mixed/modest cognition meta-analysis:** Zhang 2016 (PMID:26025463), 6 RCTs, reported a statistically significant but **clinically trivial** improvement in MMSE (WMD 0.15, p=0.003). The point estimate is well below any meaningful threshold and sits against the larger null trials above — represent as weak, not as evidence of cognitive enhancement.
- **Low-baseline / mild memory complaints (suggestive):** Yurko-Mauro 2015 (PMID:25786262), DHA-and-adult-memory meta-analysis, found significant episodic-memory improvement specifically in adults with **mild memory complaints** (DHA alone or with EPA, p<.004), with benefit also at >1 g/day in broader adults. Consistent with the recurring pattern that signals concentrate where baseline status/cognition is lower. (Note: this and Zhang are smaller/lower-quality than the Cochrane and JAMA nulls, so they do not overturn the overall grade.)

Net: `evidence_overall: 2`. Genuine, replicated benefit exists for **EPA-predominant supplementation in depression** (would be 3 for that indication alone), but the headline "omega-3 improves cognition / prevents dementia" claim is contradicted by the strongest trials in healthy and AD populations, so the compound's overall brain-optimisation grade is held down.

## Safety & interactions (research metadata)
- **Bleeding / anticoagulants:** the commonly-cited additive bleeding risk is largely **not borne out** at population level — Javaid 2024 (PMID:38742535), 11 RCTs / 120,643 patients, found no overall increase in bleeding (rate ratio 1.09, 95% CI 0.91-1.31, p=0.34). A modest relative increase was seen specifically with **high-dose purified EPA**, of small absolute magnitude (~0.6%). Caution with concurrent anticoagulants/antiplatelets remains prudent but is precautionary rather than strongly evidence-based.
- **GI / palatability:** mild GI upset and fishy reflux are the most common adverse effects (per Cochrane tolerability data).
- **Oxidation:** PUFAs oxidise; poorly manufactured/stored product can carry oxidised lipids (peroxide value), a quality rather than dose issue.
- **Lipids:** high-dose purified EPA can modestly raise LDL-C in some cardiovascular trial populations (cardiology-domain caveat, noted for completeness).

## Open questions
- Does correcting low omega-3 status (low Omega-3 Index) produce cognitive benefit that is absent in replete people? The deficiency-correction vs enhancement distinction is under-tested with stratification by baseline status.
- Is the EPA-over-DHA superiority for mood driven by resolvin/SPM-mediated anti-inflammatory action, and does it predict response only in inflamed/high-CRP depression subgroups?
- Are there earlier-life or longer-horizon prevention windows (mid-life, multi-year) where omega-3 alters dementia trajectory that short trials miss?
- Genotype effects (e.g. APOE4) on brain DHA uptake/metabolism and whether they modify any cognitive response.
