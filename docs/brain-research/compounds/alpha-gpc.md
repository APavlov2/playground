---
id: alpha-gpc
name: Alpha-GPC
aliases:
  - L-alpha-glycerylphosphorylcholine
  - choline alfoscerate
  - choline alphoscerate
  - alpha-glycerylphosphorylcholine
  - A-GPC
  - L-alpha-GPC
type: compound
klass: cholinergic precursor (choline source)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Trace in milk/organ meats; endogenous choline metabolite; commercial form from soy/sunflower lecithin"
status: draft
evidence_overall: 3
onset: acute (GH/some cognitive effects ~30-60 min); cognitive benefit in impaired populations accrues over weeks-months of dosing
half_life: not well characterized in humans; choline moiety incorporated into phospholipid/acetylcholine pools (unsourced)
dose_range: 400-1200 mg/day oral (dementia trials commonly 1200 mg/day in divided doses; acute studies 300-1000 mg single dose)
cognitive_domains:
  - global cognition (ADAS-cog/MMSE) in cognitive impairment
  - memory (impaired populations)
  - attention/processing speed (acute, healthy — limited)
  - motivation (healthy — single study)
channels:
  - channel: ach
    mechanism: Hydrolyzed to free choline and glycerophosphate; supplies choline for acetylcholine synthesis, increasing central cholinergic tone (precursor loading)
    evidence: 3
    population: both
    direction: up
  - channel: ntrophic
    mechanism: Preclinical reports of increased neurotrophic signaling / nerve growth factor receptor expression and reduced age-related neural changes in rodents; not established in humans
    evidence: 2
    population: impaired
    direction: up
safety:
  contraindications:
    - Caution in individuals with elevated cerebrovascular/stroke risk given the 2021 association signal (see Safety)
  interactions:
    - Cholinesterase inhibitors (donepezil): used together in trials (additive cholinergic effect); monitor for cholinergic excess (unsourced as a clinical caution; combination itself is trial-documented — PMID:36683513)
    - Anticholinergic drugs: pharmacodynamic opposition (unsourced)
  notable_risks:
    - "Large 2021 Korean cohort: alpha-GPC use associated with higher 10-year incident stroke risk in dose-responsive manner (total stroke aHR 1.43) — association only, confounding-by-indication possible (PMID:34817582)"
    - Possible choline -> TMAO pathway as proposed cardiovascular mechanism (mechanistic/hypothesis) (unsourced)
    - Generally well tolerated in RCTs; no excess serious adverse events vs placebo in short-term trials (PMID:39300341)
sources:
  - Sagaro GG et al., J Alzheimers Dis, 2023 — PMID:36683513
  - Jeon J et al., BMC Geriatr, 2024 — PMID:39300341
  - De Jesus Moreno Moreno M, Clin Ther, 2003 — PMID:12637119
  - Lee G et al., JAMA Netw Open, 2021 — PMID:34817582
  - Tamura Y et al., Nutrients, 2021 — PMID:34201961
  - Kerksick CM et al., Nutrients, 2024 — PMID:39683633
tags:
  - cholinergic
  - choline-source
  - nootropic
  - dementia
  - mild-cognitive-impairment
  - acetylcholine-precursor
  - cardiovascular-signal
---

## Summary

Alpha-GPC (choline alfoscerate / L-alpha-glycerylphosphorylcholine) is a choline-containing phospholipid used as an acetylcholine precursor. Its strongest human cognitive evidence is in **deficient/impaired populations** — Alzheimer's dementia, vascular/mixed dementia, and mild cognitive impairment — supported by RCTs and a pooled meta-analysis (PMID:36683513). Much of this literature comes from older Italian trials and a research group with industry links, which tempers confidence. Evidence in **healthy/optimizing** subjects is thin: a few small acute or short-term studies suggest modest attention or motivation effects but do not establish a reliable nootropic benefit. A separate exercise-science literature on acute power output and growth-hormone response is **not cognition** and is kept out of the cognitive grading. A 2021 large cohort study raised a dose-responsive stroke-risk association that belongs in any honest safety discussion.

evidence_overall = 3, reflecting the best-supported relevant claim (cognition in impaired populations via multiple agreeing RCTs + meta-analysis), NOT healthy-subject nootropic use (which would be ~2).

## Mechanism

Alpha-GPC is hydrolyzed after absorption to free choline and glycerophosphate. The choline moiety raises plasma choline and is available for acetylcholine synthesis, increasing central cholinergic tone (precursor loading) — the basis for its use in cholinergic-deficit dementias. Compared with dietary choline salts it is relatively bioavailable and crosses into the CNS pool. The glycerophosphate fragment can be incorporated into membrane phospholipids.

- **ach (primary):** precursor supply for acetylcholine; mechanistically well-grounded and consistent with the cholinergic hypothesis of dementia.
- **ntrophic (possible, preclinical):** rodent work reports neurotrophic/NGF-related effects and attenuation of age-related neural changes, but this is not demonstrated in humans — capped at evidence 2.

## Evidence (human literature)

**Impaired/deficient populations (strongest):**

- **Meta-analysis — Sagaro GG et al., J Alzheimers Dis, 2023 (PMID:36683513).** Systematic review/meta-analysis of adult-onset cognitive dysfunction; 7 RCTs + 1 prospective cohort. Alpha-GPC vs placebo/other showed better cognition (MD 3.50, 95% CI 0.36-6.63); alpha-GPC + donepezil improved MMSE vs donepezil alone (MD 1.72, 95% CI 0.20-3.25). This is the anchor for evidence_overall = 3. Note authorship overlaps with a long-running alpha-GPC research program (interpret with mild caution).
- **De Jesus Moreno Moreno M, Clin Ther, 2003 (PMID:12637119).** Multicenter, double-blind, randomized, placebo-controlled trial in mild-to-moderate Alzheimer's; choline alfoscerate 400 mg TID for 180 days improved cognitive scales vs placebo. Older Italian trial; foundational but dated and industry-adjacent.
- **Jeon J et al., BMC Geriatr, 2024 (PMID:39300341).** Recent double-blind RCT, 100 subjects with amnestic mild cognitive impairment, 600 mg/day for 12 weeks. ADAS-cog decreased by 2.34 points more than placebo (favorable); no serious adverse events. Independent, recent, but single small trial in MCI.
- The ASCOMALVA program (donepezil + choline alphoscerate in AD with cerebrovascular damage) reports slowed cognitive decline and brain-atrophy effects; these RCTs are part of the meta-analytic pool above. Specific ASCOMALVA PMIDs were not individually re-verified here, so individual-trial claims beyond the meta-analysis are "(unsourced)" pending direct PMID confirmation.

**Healthy / optimizing populations (thin):**

- **Kerksick CM et al., Nutrients, 2024 (PMID:39683633).** Randomized, double-blind, placebo-controlled crossover, 20 healthy resistance-trained men; acute 315 mg / 630 mg. Stroop test improved with high dose (total score p=0.013; time p=0.021) and low-dose total score (p=0.046); no effect on Flanker or N-Back. Small, single acute study, mixed across tasks.
- **Tamura Y et al., Nutrients, 2021 (PMID:34201961).** Single-blind, placebo-controlled, ~40 healthy volunteers, 400 mg/day for 14 days; self-reported motivation improved, anxiety unchanged. Single-blind and subjective endpoint limit weight.

Together, healthy-subject cognitive evidence supports at most a limited/mixed (evidence ~2) signal — not a robust nootropic claim.

**Not cognition (kept separate):** An acute sports-nutrition literature reports that a single ~600 mg dose before resistance exercise augments post-exercise growth-hormone response and bench-press peak force (e.g., Ziegenfuss et al., J Int Soc Sports Nutr, 2008, conference paper, DOI:10.1186/1550-2783-5-S1-P15). This is a peripheral/performance effect, NOT a cognitive outcome, and does not contribute to cognitive grading.

**Preclinical:** Rodent studies underpin the ntrophic channel and some cholinergic mechanism claims; these remain animal-level and cap that channel at 2.

## Safety & interactions

Alpha-GPC is generally well tolerated in short-term RCTs, with no excess serious adverse events vs placebo (PMID:39300341). Mild GI upset, headache, and (theoretically) cholinergic effects are the usual minor reports (unsourced for specific incidence).

**Cardiovascular signal (notable):** Lee G et al., JAMA Netw Open, 2021 (PMID:34817582) — population-based retrospective cohort of 12,008,977 Koreans aged >=50 without prior stroke/AD. Alpha-GPC use was associated with higher 10-year incident stroke risk in a dose-responsive manner: total stroke adjusted HR 1.43 (95% CI 1.41-1.46), ischemic 1.34 (1.31-1.37), hemorrhagic 1.37 (1.29-1.46). This is an **observational association**, susceptible to confounding by indication (alpha-GPC is prescribed to populations already at elevated cerebrovascular risk in Korea), so causality is unproven. A proposed mechanism is the choline -> gut-microbiome -> TMAO pathway linked to atherosclerosis (mechanistic/hypothesis only) (unsourced). Worth flagging for anyone with elevated stroke/cardiovascular risk, especially with chronic high-dose use.

**Interactions:**
- Cholinesterase inhibitors (donepezil): deliberately combined in trials for additive cholinergic effect (PMID:36683513); monitor for cholinergic excess (clinical caution — unsourced).
- Anticholinergics: expected pharmacodynamic opposition (unsourced).

## Open questions

- Does any cognitive benefit exist in genuinely healthy adults, or is the effect confined to cholinergic-deficient/impaired populations? Current healthy-subject data are small, mixed, and partly subjective.
- Is the 2021 stroke association causal or confounded by indication? No RCT-level cardiovascular safety data exist; this is the single most important unresolved safety question.
- How much of the favorable dementia literature is inflated by industry linkage and older trial methodology? Independent replication (e.g., PMID:39300341) is encouraging but limited.
- Human pharmacokinetics (half-life, CNS choline/acetylcholine dynamics) are poorly characterized.
- Are the neurotrophic (ntrophic) effects seen in rodents translatable to humans? Currently preclinical only.
