---
id: citicoline
name: Citicoline (CDP-choline)
aliases: [cytidine diphosphate-choline, CDP-choline]
type: compound
klass: Cholinergic
status: draft
evidence_overall: 3
onset: "cumulative (weeks; trials typically read out at 4-12 weeks). Acute single-dose cognitive effects are weak/unestablished"
half_life: "biphasic; orally it is hydrolysed to choline + cytidine and incorporated into the choline/uridine pools — terminal elimination of label is slow (days), so 'plasma half-life' is not a clean descriptor"
dose_range: "500-2000 mg/day oral (most cognition RCTs used 250-500 mg/day; vascular trials up to 1000 mg/day)"
cognitive_domains: [attention, episodic-memory, processing-speed, psychomotor-speed]
channels:
  - channel: ach
    mechanism: "Hydrolysed to choline, raising substrate availability for acetylcholine synthesis; supports cholinergic membrane integrity"
    evidence: 2
    population: both
    direction: up
  - channel: ntrophic
    mechanism: "Supplies cytidine (→ uridine/CTP) and choline for the Kennedy pathway, driving phosphatidylcholine and structural membrane phospholipid synthesis & neuronal repair"
    evidence: 2
    population: both
    direction: up
  - channel: da
    mechanism: "Preclinical and review literature report increased striatal dopamine release/levels and possible upregulation of dopamine receptor density; not directly demonstrated in healthy human cognition trials"
    evidence: 1
    population: impaired
    direction: up
safety:
  contraindications: []
  interactions: []
  notable_risks: ["Generally very well tolerated; mild GI upset and headache reported, not consistently above placebo", "Pregnancy/lactation safety data limited (unsourced)", "Theoretical caution with strong cholinergic/anticholinergic regimens (unsourced)"]
sources:
  - "Fioravanti M & Yanagi M, Cochrane Database Syst Rev, 2005 — PMID:15846601"
  - "Bonvicini M et al., Nutrients, 2023 — PMID:36678257"
  - "Nakazaki E et al., J Nutr, 2021 — PMID:33978188"
  - "Cotroneo AM et al. (IDEALE), Clin Interv Aging, 2013 — PMID:23403474"
  - "McGlade E et al., J Atten Disord, 2019 — PMID:26179181"
  - "Bruce SE et al., Int J Food Sci Nutr, 2014 — PMID:25046515"
  - "Secades JJ, Methods Find Exp Clin Pharmacol, 2006 — PMID:17171187"
tags: [nootropic, choline]
---

## Summary
Citicoline (CDP-choline) is an endogenous intermediate in phosphatidylcholine synthesis that, on oral dosing, supplies choline and cytidine/uridine to neuronal membrane and acetylcholine pathways. The best human evidence is in **aging, age-associated memory impairment, and vascular cognitive impairment**, where meta-analyses and RCTs show modest cognitive benefit (PMID:15846601, PMID:36678257). Evidence in **healthy young/middle-aged adults** is thinner and partly industry-linked, but several small RCTs report improved attention and psychomotor speed (PMID:26179181, PMID:25046515). It is consistently well tolerated.

## Mechanism
- **ntrophic (membrane synthesis):** Orally administered citicoline is hydrolysed in the gut/liver to cytidine and choline, which re-form CDP-choline intracellularly and feed the Kennedy pathway to build phosphatidylcholine and other structural phospholipids — the rationale for membrane repair and neuroprotection (PMID:17171187). This is mechanistically well established but human cognitive read-throughs are indirect.
- **ach (cholinergic substrate):** The liberated choline is a substrate for acetylcholine synthesis. Plausible and supported by the cholinergic biology, but a direct, dose-dependent ACh effect on cognition in healthy humans is not cleanly demonstrated, so graded conservatively.
- **da (dopaminergic):** Review and preclinical sources report increased dopamine (and noradrenaline) release and possible receptor-density changes (PMID:17171187, and the IDEALE discussion PMID:23403474). This is mechanistic/preclinical, not shown as a measured dopaminergic cognitive effect in humans — graded 1.
- **cbf / ne not included as separate graded channels:** noradrenergic/CBF effects are mentioned in reviews but lack standalone controlled human cognitive support; omitted rather than over-claimed.

## Evidence
**Strongest population — impaired / aging:**
- Cochrane review (Fioravanti & Yanagi, 2005, PMID:15846601): pooled aged subjects with memory disorders through vascular MCI/dementia; found evidence of benefit on memory and behaviour (effect on memory reported ~SMD 0.19 in earlier analyses) but not clearly on attention. Authors flagged short trials and heterogeneous diagnostic criteria.
- Bonvicini et al. meta-analysis (Nutrients, 2023, PMID:36678257): 7 studies; citicoline improved cognitive status, pooled SMDs ranging ~0.56 (95% CI 0.37-0.75) to 1.57 (95% CI 0.77-2.37). **Crucially, the authors graded overall evidence as low/very-low quality (GRADE) and likely biased** — so the large SMDs should be read cautiously.
- IDEALE (Cotroneo et al., 2013, PMID:23403474): open-label, 349 elderly with mild vascular cognitive impairment, 500 mg twice daily for 9 months; MMSE stable in treated vs decline in controls, no benefit on activities of daily living, no adverse events. Open-label design limits causal weight.

**Healthy / optimising population (thinner, often industry-funded):**
- Nakazaki et al. (J Nutr, 2021, PMID:33978188): RCT, n=100 healthy older adults (50-85 y) with age-associated memory impairment, 500 mg/day for 12 weeks; significant improvement in episodic and composite memory vs placebo (composite mean 3.78 vs 0.72, P=0.0052). This is older adults with subjective impairment, not young healthy.
- McGlade et al. (J Atten Disord, 2019, PMID:26179181): RCT, 75 healthy adolescent males, 250/500 mg for 28 days; improved attention (p=0.02) and psychomotor speed (p=0.03), dose-dependent. Small, single-sex, short.
- Bruce et al. (Int J Food Sci Nutr, 2014, PMID:25046515): RCT, n=60 healthy adults, citicoline-**caffeine** combination beverage; faster reaction/maze times and better processing-speed accuracy. Confounded by caffeine, so cannot isolate citicoline.

**Net:** consistent, replicated benefit in impaired/aging cohorts (multiple RCTs + meta-analyses → 3), but the meta-analytic quality is rated low by the authors themselves, and healthy-young evidence is limited, small, and partly confounded/industry-linked. Best-supported relevant claim (cognition in aging/impaired) supports an honest **evidence_overall = 3**, not 4.

## Safety & interactions (research metadata)
Very favourable tolerability across decades of use as an endogenous compound (PMID:17171187). Adverse events in trials are mostly mild GI disturbance and transient headache and are generally not significantly above placebo; large pooled safety analyses show comparable AE rates between citicoline and placebo arms. No significant systemic cholinergic toxicity reported. Pregnancy/lactation safety data are limited (unsourced). No well-documented major drug interactions established (unsourced).

## Open questions
- Does citicoline produce reliable **acute** (single-dose) cognitive enhancement, or only cumulative effects?
- Magnitude and reality of benefit in **healthy young** adults given small, short, partly industry-funded trials — needs larger independent RCTs.
- How much of meta-analytic effect is inflated by low study quality and publication bias (flagged in PMID:36678257)?
- Whether the dopaminergic/noradrenergic mechanisms (PMID:17171187) translate to measurable human cognitive channels or remain preclinical.
- Optimal dose for cognition (250 vs 500 vs 1000+ mg/day) and durability after discontinuation.
