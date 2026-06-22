---
id: probiotics
name: Probiotics (Psychobiotics)
aliases:
  - psychobiotics
  - gut-brain axis modulators
  - Lactobacillus
  - Bifidobacterium
  - Lactobacillus rhamnosus
  - Bifidobacterium longum
type: compound
klass: live microbial supplement (gut-brain axis)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Fermented foods (yogurt, kefir, kimchi); cultured strains"
status: draft
evidence_overall: 2
onset: "Mood/anxiety changes accrue over ~4-8 weeks of daily dosing in trials; acute single-dose CNS effects not established."
half_life: "Not a single-molecule pharmacokinetic; colonization is usually transient and strain-dependent, with most strains cleared within days-to-weeks after stopping (unsourced for specific strains)."
dose_range: "Highly strain- and product-specific; mood/stress RCTs commonly used ~1x10^9 to 1x10^10 CFU/day of single or multi-strain Lactobacillus/Bifidobacterium for 4-8 weeks. No validated dose-response for cognition."
cognitive_domains:
  - depressive symptoms (small benefit; larger in clinical samples)
  - anxiety symptoms (small benefit)
  - subjective stress (small benefit)
  - global cognition (thin; mostly MCI/AD, not healthy)
channels:
  - channel: hpa
    mechanism: "Gut-brain axis modulation of HPA-axis output. Meta-analysis (46 RCTs) shows a modest cortisol reduction (low certainty); a separate healthy-volunteer meta-analysis found reduced subjective stress but NO significant cortisol change. Effect is strain-specific and heterogeneous; much mechanistic detail (vagal afferent signaling, microbial metabolites acting on the HPA axis) is preclinical."
    evidence: 2
    population: both
    direction: down
  - channel: ser
    mechanism: "Proposed modulation of serotonergic signaling via gut-derived serotonin (enterochromaffin cells produce most body 5-HT), tryptophan/kynurenine metabolism, and short-chain fatty acids (SCFAs); links to small antidepressant/anxiolytic effects in meta-analyses. The serotonergic pathway itself is largely inferred/preclinical, not demonstrated by human central 5-HT biomarkers."
    evidence: 2
    population: both
    direction: modulate
  - channel: inflam
    mechanism: "Strengthened gut-barrier integrity and reduced systemic/neuro-inflammation (lowered LPS translocation, altered cytokines) is a leading proposed route to mood and cognition effects. In humans this is mostly biomarker/secondary-endpoint and mechanistic; the anti-inflammatory-to-cognition causal chain is preclinical-leaning."
    evidence: 2
    population: both
    direction: down
safety:
  contraindications:
    - "Severe immunocompromise (e.g., neutropenia, post-transplant, advanced HIV): risk of probiotic bacteremia/fungemia."
    - "Critically ill patients, especially with central venous catheters: documented fungemia/bacteremia signal; the PROPATRIA pancreatitis trial showed increased mortality."
    - "Short-gut / severely compromised intestinal barrier and premature/very-low-birthweight neonates outside monitored protocols."
  interactions:
    - "Antibiotics: concurrent antibiotics can reduce viability of live strains (separate dosing commonly advised)."
    - "Immunosuppressants: theoretical higher translocation/infection risk in immunosuppressed hosts (mechanistic)."
    - "No well-characterized CYP-mediated drug interactions; psychotropic interaction data are sparse (unsourced)."
  notable_risks:
    - "PROBIOTIC SEPSIS: rare Lactobacillus/Bifidobacterium bacteremia and Saccharomyces boulardii fungemia, almost exclusively in immunocompromised, critically ill, or central-catheter patients."
    - "Increased mortality observed with multispecies probiotics in predicted severe acute pancreatitis (PROPATRIA RCT) - do not use in that setting."
    - "Common, mild, usually self-limiting: bloating, flatulence, GI discomfort, especially early in use."
    - "Product-quality variability: CFU counts, strain identity, and contamination are inconsistent across over-the-counter products (supplements are loosely regulated)."
sources:
  - "Liu RT, Walsh RFL, Sheehan AE, Neurosci Biobehav Rev, 2019 — PMID:31004628 — DOI:10.1016/j.neubiorev.2019.03.023 (34 controlled trials; probiotics small but significant for depression d=-0.24 and anxiety d=-0.10; larger in clinical/medical samples d=-0.45; prebiotics not significant)."
  - "Goh KK, Liu YW, Kuo PH, Chung YE, Lu ML, Chen CH, Psychiatry Res, 2019 — PMID:31563280 — DOI:10.1016/j.psychres.2019.112568 (meta-analysis of human studies; probiotics improved depressive symptoms vs placebo; effect significant in major depression but not general population; multi-strain > single-strain)."
  - "Zhang N et al., Brain Behav, 2020 — PMID:32662591 — DOI:10.1002/brb3.1699 (7 RCTs, 1146 healthy volunteers; reduced subjective stress SMD=-0.14, p=.03; NO significant cortisol effect, SMD=-0.02, p=.89)."
  - "Jain M, Anand A, Sharma N, Shamim MA, Enioutina EY, Nutrients, 2024 — PMID:39458560 — DOI:10.3390/nu16203564 (46 RCTs, 3516 participants; modest cortisol reduction SMD=-0.45, low certainty; substantial heterogeneity)."
  - "Goldenberg JZ et al. / safety syntheses; Saccharomyces boulardii fungemia, CDC EID 2021 — DOI:10.3201/eid2708.210018 (fungemia/infection associated with probiotic use, predominantly in critically ill / central-catheter patients)."
  - "Besselink MG et al. (PROPATRIA), Lancet, 2008 — PMID:18280327 — DOI:10.1016/S0140-6736(08)60207-X (multispecies probiotics increased mortality in predicted severe acute pancreatitis)."
tags:
  - psychobiotic
  - gut-brain-axis
  - strain-specific
  - depression
  - anxiety
  - cortisol
  - inflammation
  - thin-cognition-evidence
  - immunocompromised-caution
---

## Summary

Probiotics ("psychobiotics") are live microbial supplements - mostly *Lactobacillus* and *Bifidobacterium* strains - proposed to influence mood, stress, and cognition through the bidirectional **gut-brain axis**. The strongest human evidence is for a **small** reduction in **depression** and **anxiety** symptoms (Liu 2019: depression d=-0.24, anxiety d=-0.10; Goh 2019), with the effect notably **larger in clinically diagnosed/depressed populations** than in healthy community samples. Effects are **strain-specific and heterogeneous** - results from one product or strain do not generalize to others, and multi-strain formulations sometimes outperform single strains. Cognition data are **thin and mixed**: most positive cognitive findings come from MCI/Alzheimer populations, not healthy adults. Mechanisms (vagal signaling, gut serotonin/SCFAs, HPA modulation, reduced inflammation) are biologically plausible but remain **largely preclinical or biomarker-level** in humans. `evidence_overall: 2` reflects the best-supported claim - a small, replicated antidepressant/anxiolytic signal of uncertain clinical magnitude - held down by strain heterogeneity, modest effect sizes, and thin cognition data, not averaged across channels.

## Mechanism

- **HPA axis (stress/cortisol):** Probiotics are proposed to dampen HPA-axis reactivity via the gut-brain axis. A large meta-analysis (Jain 2024, 46 RCTs) found a modest cortisol reduction (SMD=-0.45, low certainty), but a healthy-volunteer meta-analysis (Zhang 2020) found reduced *subjective* stress with **no** significant cortisol change - so the physiological-stress effect is inconsistent. Upstream pathways (vagal afferent signaling, microbial metabolites reaching the HPA axis) are mostly demonstrated in animals.
- **Serotonergic (ser):** Enterochromaffin cells produce the majority of the body's serotonin; probiotics may modulate gut 5-HT, tryptophan/kynurenine metabolism, and SCFA production, plausibly linking to the small antidepressant/anxiolytic effect. Central serotonergic engagement is **inferred**, not shown by human CNS biomarkers.
- **Inflammation / gut barrier (inflam):** Improved epithelial barrier integrity and reduced systemic inflammation (lower LPS translocation, altered cytokines) is a leading hypothesized route to mood and cognitive benefit. In humans this is mostly secondary-endpoint/biomarker; the inflammation-to-cognition causal chain is preclinical-leaning.
- **Strain specificity is itself a mechanism caveat:** different strains have different metabolic and immunologic properties, so pooled "probiotic" effects mask large between-strain variability.

## Evidence

**Depression and anxiety (best supported, small).** Liu et al. (*Neurosci Biobehav Rev*, 2019; PMID:31004628), 34 controlled trials, found probiotics produced small but significant reductions in depression (d=-0.24, p<.01) and anxiety (d=-0.10, p=.03), while prebiotics did not differ from placebo. Crucially, **sample type moderated** the depression effect: clinical/medical samples showed a larger effect (d=-0.45) than community samples. Goh et al. (*Psychiatry Res*, 2019; PMID:31563280) similarly found probiotics improved depressive symptoms versus placebo, with the effect **significant in major depression but not in the general (healthy) population**, and multi-strain formulations outperforming single strains. **Healthy vs clinical:** the mood benefit is best documented in clinically depressed/anxious populations; in healthy adults the antidepressant signal is weak and should not be over-claimed.

**Stress / cortisol (mixed).** Zhang et al. (*Brain Behav*, 2020; PMID:32662591), 7 RCTs in 1146 healthy volunteers, found a small reduction in *subjective* stress (SMD=-0.14, p=.03) but **no significant effect on cortisol** (SMD=-0.02, p=.89). The larger Jain et al. meta-analysis (*Nutrients*, 2024; PMID:39458560), 46 RCTs, found a modest cortisol reduction (SMD=-0.45) but rated it **low certainty** with substantial heterogeneity. Net: a soft, inconsistent HPA signal - graded 2.

**Cognition (thin / mixed).** Positive cognitive meta-analyses are concentrated in **mild cognitive impairment and Alzheimer's disease** populations (improvements in global cognition reported), not healthy adults. Healthy-adult cognition findings are sparse, often single small trials (e.g., a *B. longum* BB68S RCT in older adults), and at least one psychobiotic RCT (*L. rhamnosus* JB-1) **failed** to alter stress or cognition in healthy men. There is no robust meta-analytic basis for a cognitive-enhancement claim in healthy people; this domain is deliberately not graded as a primary channel.

**Bias / heterogeneity caveat.** Trials vary enormously in strain, dose, duration, and population; many are small; "probiotic" is not one intervention. Effects favor Asian study populations and clinical samples in subgroup analyses, and publication/strain-selection bias is plausible. Weight meta-analyses, but recognize they pool heterogeneous strains.

## Safety & interactions

- **Generally safe in healthy people:** the most common adverse effects are mild and self-limiting - bloating, flatulence, transient GI discomfort, usually early in use.
- **Immunocompromised / critically ill (key caution).** Rare but serious **probiotic bacteremia** (*Lactobacillus*, *Bifidobacterium*) and **fungemia** (*Saccharomyces boulardii*) occur almost exclusively in immunocompromised, critically ill, or central-venous-catheter patients (CDC EID 2021, DOI:10.3201/eid2708.210018). *S. boulardii* is specifically advised against in these groups.
- **Severe acute pancreatitis:** the PROPATRIA RCT (Besselink et al., *Lancet*, 2008; PMID:18280327) found **increased mortality** with multispecies probiotics in predicted severe acute pancreatitis - a clear do-not-use setting.
- **Antibiotics** reduce live-strain viability (separate dosing commonly advised); **immunosuppressants** raise theoretical translocation/infection risk.
- **Product quality** is inconsistent: over-the-counter probiotics vary in actual CFU, strain identity, and contamination because supplements are loosely regulated. This is research metadata, not medical advice.

## Open questions

- **Which strains, at what doses,** actually drive the antidepressant/anxiolytic effect, and can strain-specific (not pooled) effects be replicated independently?
- Is there any **reliable mood or cognitive benefit in healthy adults**, or is the signal confined to clinically depressed/anxious and impaired (MCI/AD) populations?
- Why is the **cortisol** signal inconsistent (reduced subjective stress without cortisol change in healthy volunteers)? Is HPA modulation real or an artifact of heterogeneity?
- How much of the proposed **vagal / serotonergic / anti-inflammatory** mechanism translates from animals to measurable human CNS endpoints?
- What is the **durability** of any benefit given largely transient colonization, and what are long-term safety data in vulnerable subgroups?
