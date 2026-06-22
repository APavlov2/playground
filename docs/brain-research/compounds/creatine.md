---
id: creatine
name: Creatine (creatine monohydrate)
aliases: [creatine monohydrate, Cr]
type: compound
klass: Neuroenergetic
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Red meat & fish; endogenous synthesis; supplement is synthesized monohydrate"
status: draft
evidence_overall: 3
onset: "Acute (single high dose ~0.35 g/kg shows effects within hours under stress); brain stores saturate slowly over ~2-4 weeks at 5 g/day"
half_life: "~3 h plasma; brain total-creatine turnover is far slower (washout over weeks)"
dose_range: "3-5 g/day for chronic brain saturation; ~0.35 g/kg single dose in acute sleep-deprivation work; up to 20 g/day loading in some trials"
cognitive_domains: [working-memory, processing-speed, short-term-memory, mental-fatigue, reasoning]
channels:
  - channel: mito
    mechanism: "Phosphocreatine/creatine-kinase system buffers cytosolic ATP/ADP in neurons; supplementation raises brain total creatine and phosphocreatine, supporting rapid ATP regeneration during high metabolic demand or energetic stress (sleep deprivation, hypoxia, aging)"
    evidence: 3
    population: both
    direction: up
safety:
  contraindications: []
  interactions: []
  notable_risks: [transient water-weight gain, occasional GI discomfort at loading doses; renal-impairment caution is precautionary not evidence-based]
sources:
  - "Avgerinos et al., Experimental Gerontology, 2018 — PMID:29704637 (systematic review of RCTs in healthy adults)"
  - "Prokopidis et al., Nutrition Reviews, 2023 — PMID:35984306 (meta-analysis; memory, older-adult subgroup)"
  - "Xu et al., Frontiers in Nutrition, 2024 — PMID:39070254 (meta-analysis, 16 RCTs/492 participants; memory SMD 0.31, processing speed)"
  - "Rae et al., Proc Biol Sci, 2003 — PMID:14561278 (vegetarian crossover RCT; working memory + Raven's)"
  - "Gordji-Nejad et al., Scientific Reports, 2024 — PMID:38418482 (single high-dose creatine under sleep deprivation; 31P-MRS)"
  - "Dechent et al., Am J Physiol, 1999 — PMID:10484486 (oral creatine raises human brain total creatine ~8.7% by 31H-MRS)"
tags: [nootropic, bioenergetic]
---

## Summary
Creatine is an endogenous nitrogenous compound (synthesised from glycine/arginine/methionine and obtained from meat/fish) that, as phosphocreatine, serves as a rapid spatial-temporal ATP buffer in high-demand tissues including brain. Oral supplementation measurably raises brain total creatine and phosphocreatine, and the clearest cognitive benefit appears not in already-replete, well-rested omnivores but when the brain's energy supply is stressed or stores are low — i.e. sleep deprivation, aging, and vegetarians/low-baseline individuals. In healthy rested young adults the effect on cognition is small and inconsistent.

## Mechanism
**mito (primary, up).** The creatine–phosphocreatine/creatine-kinase (CK) shuttle regenerates ATP from ADP at sites of high energy turnover and buffers the ATP/ADP ratio faster than oxidative phosphorylation alone. Neurons and astrocytes express CK isoforms; phosphocreatine acts as a temporal energy reserve during bursts of demand and a spatial shuttle between mitochondria and cytosolic ATPases. Supplementation increases the substrate pool: oral creatine raises human brain total creatine on the order of ~5-9% measurable by MRS (Dechent 1999, PMID:10484486), and acute high dosing alters cerebral high-energy phosphates (PCr/Pi, ATP) and pH under sleep-deprivation stress (Gordji-Nejad 2024, PMID:38418482). The cognitive payoff is therefore expected to be largest precisely when the bioenergetic system is taxed — consistent with the human data below. (No well-supported direct neurotransmitter channel — glu/ach/da effects are mechanistically plausible but not established in human cognitive trials, so they are omitted rather than graded low.)

## Evidence
Human literature is moderate quality and population-dependent.

- **Aggregate cognition (healthy adults):** Avgerinos 2018 (PMID:29704637), a systematic review of 6 RCTs (n=281), found short-term memory and intelligence/reasoning may improve, but effects on attention, long-term memory and reaction time were inconsistent. It noted vegetarians improved more than meat-eaters and that younger replete subjects showed little change.
- **Memory meta-analysis:** Prokopidis 2023 (PMID:35984306) pooled RCTs and reported a modest overall memory benefit (SMD ≈ 0.29, 95% CI 0.04-0.53), driven heavily by older adults (66-76 y: SMD ≈ 0.88) with negligible effect in younger adults (SMD ≈ 0.03). Important caveat: a published letter (Eckert & Pascher, PMID:36644917) showed double-counting of non-independent outcomes inflated the result; on re-analysis the overall effect lost significance except in older adults. Grade this down accordingly.
- **Broader meta-analysis:** Xu 2024 (PMID:39070254), 16 RCTs / 492 participants, found significant benefits for memory (SMD 0.31, 95% CI 0.18-0.44, moderate GRADE certainty) and processing speed, but no significant effect on overall cognition or executive function, and larger benefit in diseased/impaired groups.
- **Vegetarian / low-baseline subgroup:** Rae 2003 (PMID:14561278), a double-blind placebo-controlled crossover in 45 vegetarians (5 g/day, 6 weeks), found significant gains in working memory (backward digit span) and Raven's matrices. Benton & Donohoe similarly found benefit concentrated in vegetarians. Later replications in mixed populations have been weaker/mixed, so the vegetarian-specific signal is suggestive but not settled.
- **Sleep deprivation / acute energetic stress:** Gordji-Nejad 2024 (PMID:38418482), double-blind, single ~0.35 g/kg dose during 21 h sleep deprivation (n=15), improved working memory and processing speed and tracked corresponding changes in cerebral high-energy phosphates and pH by 31P-MRS. This is the strongest mechanistic-plus-behavioural human signal for the "energy buffer under stress" model, though small and needing replication.

Net: best-supported, most relevant claim — creatine improves memory/processing-speed when brain bioenergetics are stressed or stores are low (aging, sleep deprivation, vegetarians) — rates **Good (3)**. In already-replete rested young omnivores the effect is small/uncertain (≈2).

## Safety & interactions (research metadata)
Creatine monohydrate is among the best-tolerated supplements studied. No established contraindications at cognitive doses; commonly reported effects are transient water-weight gain and occasional GI discomfort at high loading doses. Caution in pre-existing renal impairment is precautionary rather than evidence-based — controlled studies have not shown renal harm in healthy individuals. No clinically significant drug interactions are established for cognitive-dose use. This is research metadata, not medical advice.

## Open questions
- Does chronic saturation (5 g/day for weeks) produce durable cognitive benefit in healthy rested omnivores, or is the benefit confined to deficit/stress states? Current data lean toward the latter.
- Optimal dosing for brain (vs muscle): brain creatine saturates more slowly and less completely than muscle; whether higher chronic doses (>5 g) meaningfully raise brain creatine and cognition is unresolved.
- How robust is the vegetarian-subgroup effect given mixed replications and small samples?
- Replication and generalisation of the acute high-dose sleep-deprivation finding (Gordji-Nejad) beyond n=15.
- Statistical-independence problems flagged in the memory meta-analyses mean pooled effect sizes should be treated cautiously pending cleaner re-analyses and larger pre-registered RCTs.
