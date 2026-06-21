---
id: prebiotic-fiber
name: Prebiotic fiber
aliases:
  - GOS
  - galacto-oligosaccharides
  - B-GOS
  - Bimuno
  - FOS
  - fructo-oligosaccharides
  - inulin
  - prebiotics
type: compound
klass: "dietary fiber / fermentable prebiotic (gut-brain axis)"
status: draft
evidence_overall: 2
onset: "weeks (microbiome-mediated; HPA effects reported after ~3 weeks daily intake)"
half_life: "n/a (non-absorbed; fermented in colon to SCFA; not a single-compound PK)"
dose_range: "GOS (B-GOS/Bimuno) ~5.5 g/day; FOS/inulin commonly 5-10 g/day in trials"
cognitive_domains:
  - stress reactivity (HPA)
  - emotional/attentional bias
  - anxiety (subclinical)
  - "general cognition (thin/mixed)"
channels:
  - channel: hpa
    mechanism: "Reduced waking/cortisol-awakening response after 3 weeks B-GOS; proposed via microbiota-gut-brain and vagal/SCFA signaling"
    evidence: 2
    population: healthy
    direction: down
  - channel: inflam
    mechanism: "SCFA (esp. butyrate) from fiber fermentation modulate microglia and pro-inflammatory cytokines and support gut-barrier integrity; largely preclinical, mechanistic"
    evidence: 1
    population: preclinical
    direction: down
safety:
  contraindications: []
  interactions: []
  notable_risks:
    - "GI intolerance: bloating, flatulence, abdominal cramping, osmotic-type loose stools (dose-dependent)"
    - "FODMAP load: GOS/FOS/inulin are fermentable; may worsen symptoms in IBS/SIBO"
    - "Rare hypersensitivity reactions to specific prebiotic preparations (uncommon)"
sources:
  - "Schmidt K, Cowen PJ, Harmer CJ, Tzortzis G, Errington S, Burnet PWJ. Prebiotic intake reduces the waking cortisol response and alters emotional bias in healthy volunteers. Psychopharmacology (Berl). 2015;232(10):1793-1801. PMID: 25449699. DOI: 10.1007/s00213-014-3810-0"
  - "Johnstone N, et al. Anxiolytic effects of a galacto-oligosaccharides prebiotic in healthy females (18-25 years) with corresponding changes in gut bacterial composition. Sci Rep. 2021;11:8302. PMID: 33859330. DOI: 10.1038/s41598-021-87865-w"
  - "Silva YP, Bernardi A, Frozza RL. The Role of Short-Chain Fatty Acids From Gut Microbiota in Gut-Brain Communication. Front Endocrinol (Lausanne). 2020;11:25. PMID: 32082260. DOI: 10.3389/fendo.2020.00025"
tags:
  - prebiotic
  - gut-brain-axis
  - microbiome
  - SCFA
  - butyrate
  - HPA-axis
  - cortisol
  - low-evidence
---

## Summary

Prebiotic fibers (galacto-oligosaccharides [GOS/B-GOS], fructo-oligosaccharides [FOS], inulin) are non-digestible, colonically fermented carbohydrates that act on the brain indirectly via the microbiota-gut-brain axis rather than as direct neuroactive drugs. The signal worth taking seriously is narrow: one small RCT (Schmidt 2015, n=45) found that 3 weeks of B-GOS lowered the cortisol-awakening response and shifted attentional bias away from negative stimuli, with no such effect from FOS. A later RCT in young women (Johnstone 2021) reported reduced subclinical anxiety and negative attentional bias with GOS. Beyond stress/affect endpoints, evidence for improved cognition (memory, attention, executive function) in humans is THIN and mixed, and the principal mechanism (SCFA/butyrate → microglia, gut barrier, vagal signaling) is largely preclinical. Graded LOW-MODEST (overall 2). Main practical downside is GI tolerance (bloating).

## Mechanism

Prebiotics are not absorbed; colonic bacteria (notably Bifidobacterium, which GOS selectively expands) ferment them into short-chain fatty acids (SCFA) — acetate, propionate, and butyrate. Proposed gut-to-brain routes (Silva 2020, PMID 32082260):

- SCFA, particularly butyrate, modulate microglial maturation/activation and pro-inflammatory cytokine secretion, and support intestinal and blood-brain-barrier integrity — relevant to the `inflam` channel but demonstrated chiefly in rodent/germ-free and in vitro models (preclinical).
- Vagal afferent signaling and enteroendocrine/neuroactive metabolite production are proposed conduits to central HPA-axis regulation (the `hpa` channel), consistent with the reduced cortisol-awakening response after B-GOS, though the exact human mechanism remains unestablished (the original authors note this directly).
- Microbiome composition shifts (increased Bifidobacterium) are the most reproducible measured effect; the causal link from microbiome shift to specific cognitive/affective outcomes in humans is not firmly established.

## Evidence

- HPA / cortisol-awakening response (`hpa`, grade 2, healthy): Schmidt 2015 (PMID 25449699) — double-blind RCT, 45 healthy volunteers, 3 weeks of B-GOS, FOS, or placebo (maltodextrin). The salivary cortisol-awakening response was significantly lower after B-GOS vs placebo, and participants showed decreased attentional vigilance to negative vs positive emotional information (dot-probe). No significant effect of FOS. Small, single study — driver of the modest grade.
- Subclinical anxiety / attentional bias (supports `hpa`): Johnstone 2021 (PMID 33859330) — RCT in healthy females 18-25; 4 weeks GOS reduced self-reported anxiety in high-trait-anxiety participants, reduced attentional bias to negative stimuli, and increased Bifidobacterium. Reinforces the affect/stress signal but is a separate small sample, not independent confirmation of a hard cognitive endpoint.
- General cognition (memory/attention/executive function): THIN and MIXED. Human prebiotic-specific cognitive trials are sparse, heterogeneous, and inconsistent; reviews of prebiotics for cognition in older adults report limited and mixed findings, and several trials find no significant cognitive effect. No reliable, replicated human cognitive-enhancement signal — do not over-claim. (unsourced for any specific positive cognitive endpoint claim.)
- Neuroinflammation / SCFA mechanism (`inflam`, grade 1, preclinical): butyrate decreases microglial activation and pro-inflammatory cytokine secretion and drives microglial maturation in germ-free mice; SCFA support barrier integrity (Silva 2020, PMID 32082260). This is mechanistic/preclinical and should not be read as a demonstrated human anti-neuroinflammatory cognitive benefit.

## Safety & interactions

- Generally recognized as safe as a food ingredient; the dominant adverse effect is dose-dependent GI intolerance — bloating, flatulence, abdominal cramping, and osmotic-type loose stools — because the fibers are fermentable.
- FODMAP caution: GOS, FOS, and inulin are high-FODMAP fermentable fibers and can provoke or worsen symptoms in people with IBS or suspected SIBO; consider lower/titrated dosing.
- No well-established drug contraindications or pharmacokinetic drug interactions documented for these prebiotics at typical doses (contraindications/interactions left empty pending verified data).
- Start low and titrate to manage tolerability; bloating typically attenuates with continued use.

## Open questions

- Are the B-GOS cortisol/attentional-bias findings replicable in larger, mixed-sex samples and over longer durations? Single small RCT is the foundation.
- Is there any reproducible effect on hard cognitive endpoints (working memory, processing speed, executive function) in humans, or is the benefit confined to stress/affect measures?
- How much of the SCFA/butyrate → microglia/gut-barrier mechanism translates from rodent/germ-free models to intact humans at achievable colonic SCFA levels?
- Does the Bifidobacterium increase causally mediate the HPA/affect effects, or is it a correlated marker?
- Are GOS effects specific (vs FOS/inulin), and what doses/forms are optimal for any central effect?
