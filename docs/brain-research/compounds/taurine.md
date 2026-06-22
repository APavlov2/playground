---
id: taurine
name: Taurine
aliases: [2-aminoethanesulfonic acid, "L-taurine"]
type: compound
klass: Inhibitory neuromodulator / sulfonic amino acid (osmolyte)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Meat, fish, shellfish; endogenous; energy-drink form synthesized"
status: draft
evidence_overall: 2
onset: "not well characterized in humans; acute energy-drink studies measure effects within ~30-60 min but are caffeine-confounded"
half_life: "~1 h plasma elimination at supraphysiologic oral doses (broadly cited); renally cleared once tubular reabsorption saturates"
dose_range: "0.5-6 g/day in human trials (commonly 1-3 g/day); Singh 2023 mouse work used high body-weight-scaled doses not directly translatable"
cognitive_domains: [relaxation, anxiety, neuroprotection-theoretical]
channels:
  - channel: gaba
    mechanism: "Endogenous inhibitory neuromodulator; partial/full agonist at GABA-A receptors (notably extrasynaptic alpha4-beta-delta subtype in thalamus) and at glycine receptors, gating chloride conductance. Also acts as an osmolyte. Strengthens GABAergic/glycinergic inhibitory tone in CNS. Mechanism is well established at the cellular/preclinical level; a corresponding inhibitory cognitive/anxiolytic effect is NOT demonstrated in healthy humans."
    evidence: 2
    population: preclinical
    direction: down
  - channel: inflam
    mechanism: "Antioxidant and anti-inflammatory actions: scavenges hypochlorous acid via taurine chloramine, attenuates microglial pro-inflammatory cytokine release (TNF-alpha, IL-1beta, IL-6), reduces oxidative stress and apoptosis in models of stroke, neuroinflammation, TBI, and retinal degeneration. Evidence is rodent/in-vitro; human CNS anti-inflammatory effects are not established."
    evidence: 1
    population: preclinical
    direction: down
safety:
  contraindications: []
  interactions: ["Ubiquitous co-ingredient with caffeine in energy drinks — any apparent cognitive/arousal effect in those products is attributable to caffeine, not taurine (confound, not a pharmacologic interaction)", "Theoretical additive inhibitory tone with GABAergic/sedative agents — not clinically documented (unsourced)"]
  notable_risks: ["Generally well tolerated; no consistent serious adverse events at studied oral doses", "EFSA/long-term high-dose neuro safety in humans not fully characterized — treat chronic gram-level dosing as not fully studied", "Energy-drink cardiovascular signals are driven by caffeine/sugar co-ingredients, not taurine per se"]
sources:
  - "Cao et al., International Journal of Food Sciences and Nutrition, 2025 — PMID:40320621 (DOI:10.1080/09637486.2025.2499044) — systematic review/meta-analysis, taurine and cognition (null)"
  - "Singh et al., Science, 2023 — PMID:37289866 (DOI:10.1126/science.abn9257) — taurine deficiency as a driver of aging (animal + human association)"
  - "Ochoa-de la Paz et al., Expert Review of Neurotherapeutics, 2019 — PMID:30892104 (DOI:10.1080/14737175.2019.1593827) — taurine and GABA receptors review"
  - "Jia et al., Journal of Neuroscience, 2008 — PMID:18171928 (DOI:10.1523/JNEUROSCI.3996-07.2008) — taurine activates extrasynaptic thalamic GABA-A receptors"
  - "Giles et al., Pharmacology Biochemistry and Behavior, 2012 — PMID:22819803 (DOI:10.1016/j.pbb.2012.07.004) — caffeine, not taurine, drives energy-drink cognitive effects"
tags: [nootropic, neuromodulator, amino-acid, low-evidence]
---

## Summary
Taurine (2-aminoethanesulfonic acid) is a semi-essential sulfonic amino acid, one of the most abundant free amino acids in the brain, where it functions primarily as an osmolyte and an inhibitory neuromodulator at GABA-A and glycine receptors. Despite strong preclinical interest, direct human evidence for any brain/cognition benefit is **thin**. A 2025 systematic review and meta-analysis of randomized controlled trials found no significant effect of taurine supplementation on cognitive function (Cao et al., 2025 — PMID:40320621). Much of the popular interest comes from (a) energy-drink studies that are confounded by caffeine, and (b) the high-profile Singh et al. 2023 *Science* aging paper, which is largely animal experiments plus human association data, not a cognitive or interventional human trial. Overall evidence is graded **2** (mechanistically grounded and broadly safe, but human cognitive benefit is unproven and most supportive data are preclinical).

## Mechanism
- **Inhibitory neuromodulation (gaba, down — preclinical):** Taurine is an endogenous agonist at both glycine receptors and GABA-A receptors, gating chloride conductance and thereby increasing inhibitory tone. It is a notably potent activator of extrasynaptic alpha4-beta-delta GABA-A receptors in the thalamus at physiological concentrations (Jia et al., 2008 — PMID:18171928) and partial/variable agonism at other GABA-A and glycine receptor subtypes is reviewed in Ochoa-de la Paz et al., 2019 (PMID:30892104). Taurine is also an osmoregulator released under hypoosmotic stress, ischemia, and hyperammonemia. This inhibitory/anxiolytic-leaning mechanism is well characterized at the cellular and rodent level but has **not** been translated into a demonstrated inhibitory cognitive or anxiolytic effect in healthy humans; hence direction is marked **down** but population is **preclinical** and evidence is **2**.
- **Antioxidant / anti-inflammatory neuroprotection (inflam, down — preclinical):** Taurine scavenges reactive oxygen species and, via taurine chloramine, neutralizes hypochlorous acid; it dampens microglial pro-inflammatory cytokine output (TNF-alpha, IL-1beta, IL-6) and reduces apoptosis in rodent/in-vitro models of stroke, LPS neuroinflammation, traumatic brain injury, and retinal degeneration. All of this is preclinical; there is no established human CNS anti-inflammatory benefit. Graded **1**.

## Evidence
**Human cognition — thin and largely null.**
- Cao et al., 2025 (PMID:40320621): systematic review and meta-analysis, 7 RCTs / 9 intervention arms, ~402 participants, taurine 0.2-4 g/day for 4-48 weeks. Taurine alone or with exercise produced **no significant effect** on cognitive scores. A subgroup signal (taurine + therapeutic drugs improving MMSE, WMD 3.09) exists but rests on heterogeneous clinical populations (mild cognitive impairment, dementia, Alzheimer's, psychosis, at-risk older women) and is not evidence of a standalone nootropic effect. Authors conclude there is insufficient evidence to support taurine for enhancing cognition. This null meta-analysis is the main reason the grade is capped at 2.

**Energy-drink confound — caffeine does the work.**
- Giles et al., 2012 (PMID:22819803): dissected energy-drink ingredients (caffeine, taurine, glucose). Taurine alone did **not** enhance cognition (it increased choice reaction time and gave only mixed working-memory reaction-time effects), whereas caffeine enhanced executive control and working memory. Conclusion: caffeine, not taurine or glucose, accounts for energy-drink cognitive effects. Any "taurine improves focus" claim sourced to energy-drink trials is confounded and should be discounted.

**Preclinical neuroprotection / neuromodulation.**
- Mechanistic GABA-A/glycine agonism: Jia et al., 2008 (PMID:18171928) and the receptor review Ochoa-de la Paz et al., 2019 (PMID:30892104). These establish the inhibitory mechanism but are not human cognitive evidence.
- Antioxidant/anti-inflammatory neuroprotection is documented across rodent stroke, neuroinflammation, TBI, and retinal models (preclinical; not individually load-bearing for a human grade, summarized as preclinical literature).

**Aging paper — do NOT overstate.**
- Singh et al., 2023, *Science* (PMID:37289866): showed circulating taurine declines with age in mice, monkeys, and humans; taurine supplementation extended health/life span in mice and improved health span in monkeys; in humans the data are **associational** (lower taurine correlated with age-related disease markers; taurine rose after exercise). There is **no** human interventional cognitive outcome here. The authors themselves state human clinical trials are warranted. A 2024 commentary frames taurine only as a possible aging biomarker (PMID:38435677, secondary), and subsequent human analyses have questioned the deficiency-drives-aging interpretation. Treat Singh 2023 as hypothesis-generating, not as evidence of human brain benefit.

## Safety & interactions (research metadata)
Taurine is generally well tolerated; the RCTs in the cognition meta-analysis (up to 4 g/day) and broader metabolic-syndrome trials report no consistent serious adverse events, and no established contraindications. The most important "interaction" to flag is methodological rather than pharmacologic: taurine is a near-universal co-ingredient with caffeine and sugar in energy drinks, so cardiovascular or arousal effects attributed to those products are driven by caffeine/sugar, not taurine. A theoretical additive inhibitory effect with sedative/GABAergic agents is plausible from the mechanism but is **(unsourced)** clinically. Long-term high-dose (multi-gram, chronic) neuro safety in humans is not fully characterized; pregnancy/pediatric long-term data are limited.

## Open questions
- Does taurine produce any measurable inhibitory/anxiolytic CNS effect in **healthy humans**, or does its established GABA-A/glycine agonism stay subclinical at oral doses (poor CNS penetration / saturated transport)?
- Is the Singh 2023 taurine-deficiency-aging hypothesis supported by interventional human trials, including any cognitive endpoints — currently absent, and partly contested by later human analyses.
- Can the preclinical antioxidant/anti-inflammatory neuroprotection (stroke, TBI, neuroinflammation) be demonstrated in human CNS outcomes, or is it confined to rodent/in-vitro models?
- What is taurine's actual oral PK and brain bioavailability at supplement doses, given saturable renal reabsorption and uncertain blood-brain-barrier transport?
- How much of taurine's nootropic reputation is purely a caffeine halo from energy-drink marketing?
