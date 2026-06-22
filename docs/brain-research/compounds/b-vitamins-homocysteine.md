---
id: b-vitamins-homocysteine
name: "B-vitamins for homocysteine lowering (B6 + folate/B9 + B12)"
aliases:
  - "homocysteine-lowering B vitamins"
  - "B6/B9/B12 combination"
  - "folic acid + B12 + B6"
  - "VITACOG regimen"
type: compound
klass: vitamin / methyl-donor cofactor (homocysteine axis)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Foods (B6 poultry/fish; folate leafy greens/legumes; B12 animal products); supplements synthesized"
status: draft
evidence_overall: 2
onset: "weeks (homocysteine falls within ~weeks); cognitive/structural effects require 12-24 months of treatment"
half_life: "varies by vitamer; B12 body stores measured in years, folate weeks, B6 (PLP) ~days. Effect is on chronic homocysteine status, not acute pharmacokinetics."
dose_range: "VITACOG regimen: folic acid 0.8 mg/d, vitamin B12 (cyanocobalamin) 0.5 mg/d, vitamin B6 (pyridoxine) 20 mg/d. B12 deficiency correction: 1 mg/d oral or parenteral."
cognitive_domains:
  - "episodic/verbal memory (delayed recall) — benefit only in elevated-homocysteine MCI"
  - "global cognition / clinical decline (CDR-SB) — benefit only in elevated-homocysteine MCI"
  - "no measurable domain benefit in unselected/replete older adults"
channels:
  - channel: cbf
    mechanism: "Homocysteine is an independent vascular risk factor; B6/B9/B12 lower plasma homocysteine, reducing endothelial dysfunction and small-vessel/vascular contribution to cerebral atrophy. In high-Hcy MCI, the regimen slowed whole-brain and regional grey-matter atrophy."
    evidence: 3
    population: impaired
    direction: modulate
  - channel: inflam
    mechanism: "Elevated homocysteine is associated with oxidative stress, endothelial inflammation, and accelerated brain atrophy; lowering Hcy via remethylation/transsulfuration cofactors is the proposed protective route. Mechanistically plausible and tied to the atrophy signal, but anti-inflammatory effect is inferred rather than directly the trial endpoint."
    evidence: 2
    population: impaired
    direction: down
  - channel: mito
    mechanism: "B-vitamins are one-carbon/methylation and energy-metabolism cofactors (folate/B12 in remethylation, B6 in transsulfuration toward cysteine/glutathione); impaired one-carbon metabolism with hyperhomocysteinemia may compromise mitochondrial/redox function. Speculative for cognition; not a directly demonstrated cognitive mechanism."
    evidence: 1
    population: deficient
    direction: modulate
safety:
  contraindications:
    - "Untreated/undiagnosed vitamin B12 deficiency when giving high-dose folic acid alone: folate can correct the anemia while neurological damage progresses (see notable_risks). Always assess B12 status before high folate."
    - "Known hypersensitivity to any component."
  interactions:
    - "Levodopa (without carbidopa): high-dose pyridoxine (B6) accelerates peripheral levodopa decarboxylation and can reduce its efficacy."
    - "Anticonvulsants / methotrexate / sulfasalazine / metformin / proton-pump inhibitors: can lower folate or B12 status; baseline status may be altered."
    - "Omega-3 (DHA/EPA) status modifies effect: B-vitamin cognitive benefit in MCI was seen mainly when baseline omega-3 was in the upper-normal range (PMID 26757190)."
  notable_risks:
    - "\"Folate masking of B12 deficiency\": high-dose folic acid can normalize megaloblastic anemia while subacute combined degeneration / neuropathy progresses unrecognized (PMID 38987872)."
    - "High-dose / chronic pyridoxine (B6) can cause a dose- and duration-dependent sensory peripheral neuropathy; doses >50 mg/d for extended periods are discouraged (PMID 37447150). The 20 mg/d VITACOG dose is below typical neurotoxic thresholds but B6-containing supplements warrant caution."
    - "Benefit is conditional, not universal: in unselected older adults there is no demonstrated cognitive benefit, so risk-free does not mean useful outside the elevated-Hcy / deficient subgroup."
sources:
  - "Smith AD, Smith SM, de Jager CA, et al. Homocysteine-lowering by B vitamins slows the rate of accelerated brain atrophy in mild cognitive impairment: a randomized controlled trial. PLoS One. 2010;5(9):e12244. PMID 20838622. DOI 10.1371/journal.pone.0012244"
  - "de Jager CA, Oulhaj A, Jacoby R, Refsum H, Smith AD. Cognitive and clinical outcomes of homocysteine-lowering B-vitamin treatment in mild cognitive impairment: a randomized controlled trial. Int J Geriatr Psychiatry. 2012;27(6):592-600. PMID 21780182. DOI 10.1002/gps.2758"
  - "Clarke R, Bennett D, Parish S, et al; B-Vitamin Treatment Trialists' Collaboration. Effects of homocysteine lowering with B vitamins on cognitive aging: meta-analysis of 11 trials with cognitive data on 22,000 individuals. Am J Clin Nutr. 2014;100(2):657-66. PMID 24965307. DOI 10.3945/ajcn.113.076349"
  - "Oulhaj A, Jernerén F, Refsum H, Smith AD, de Jager CA. Omega-3 fatty acid status enhances the prevention of cognitive decline by B vitamins in mild cognitive impairment. J Alzheimers Dis. 2016;50(2):547-57. PMID 26757190. DOI 10.3233/JAD-150777"
  - "Moore E, Mander A, Ames D, Carne R, Sanders K, Watters D. Cognitive impairment and vitamin B12: a review. Int Psychogeriatr. 2012;24(4):541-56. PMID 22221769"
  - "Miller JW, et al. Excess folic acid and vitamin B12 deficiency: clinical implications? (folate masking review). 2024. PMID 38987872"
  - "Vrolijk MF, et al. The role of vitamin B6 in peripheral neuropathy: a systematic review. 2023. PMID 37447150"
tags:
  - vitamin
  - homocysteine
  - methylation
  - one-carbon-metabolism
  - vascular
  - brain-atrophy
  - MCI
  - conditional-benefit
  - deficiency-correction
---

## Summary

B-vitamins on the homocysteine axis — pyridoxine (B6), folate (B9), and cobalamin (B12) — lower plasma homocysteine and are sometimes promoted for cognitive protection. The honest reading of the literature is that benefit is **conditional, not universal**. The headline positive signal comes from the VITACOG trial (Oxford OPTIMA): in older adults with mild cognitive impairment (MCI) and **elevated baseline homocysteine**, two years of high-dose B6/B9/B12 slowed the rate of brain atrophy (PMID 20838622) and slowed cognitive/clinical decline (PMID 21780182), with the largest effects in those with Hcy above ~11-13 µmol/L. By contrast, large pooled analyses in **unselected** populations — most authoritatively the B-Vitamin Treatment Trialists' Collaboration meta-analysis of 11 trials / ~22,000 individuals (PMID 24965307) — found that B-vitamins reliably lower homocysteine but produce **no measurable cognitive benefit**. Separately, correcting genuine **B12 deficiency** is clinically important in its own right (PMID 22221769). Bottom line: the value of this intervention is gated on elevated homocysteine and/or B-status deficiency. In replete, low-Hcy people, the expected cognitive benefit is essentially nil.

## Mechanism

Homocysteine sits at a metabolic crossroads. It is remethylated to methionine using **folate (B9)** and **vitamin B12** as cofactors (via methionine synthase / the methyl-folate cycle), and it is disposed of by transsulfuration to cysteine using **vitamin B6**-dependent enzymes. Deficiency of any of the three raises plasma homocysteine. Elevated homocysteine is an independent vascular risk factor and is epidemiologically associated with accelerated brain atrophy and cognitive decline, plausibly through endothelial dysfunction, oxidative stress, and small-vessel cerebrovascular contribution (channels **cbf** and **inflam**). Supplying the cofactors lowers homocysteine and, in the high-Hcy MCI subgroup, slowed grey-matter atrophy in regions vulnerable to Alzheimer pathology. One-carbon metabolism also feeds methylation and redox/glutathione pathways, giving a speculative tie to **mito** function, but this has not been demonstrated as a cognitive mechanism. Crucially, lowering homocysteine is necessary but apparently **not sufficient** for cognitive benefit — in replete people Hcy falls without cognition changing.

## Evidence

**Positive — but only in elevated-homocysteine MCI.**
- VITACOG (Smith 2010, PMID 20838622): single-center, double-blind RCT, 271 MCI participants ≥70 y, folic acid 0.8 mg + B12 0.5 mg + B6 20 mg/d vs placebo for 24 months; MRI subset n=187. Rate of brain atrophy was reduced by ~30% overall and up to ~53% in those with **baseline homocysteine in the top tertile (>13 µmol/L)**. Effect was homocysteine-dependent — minimal in low-Hcy participants.
- de Jager 2012 (PMID 21780182): cognitive/clinical outcomes from the same trial. B-vitamins slowed decline in global cognition and CDR sum-of-boxes, again concentrated in participants with **elevated baseline homocysteine**.
- Oulhaj/Jernerén 2016 (PMID 26757190): the B-vitamin cognitive benefit was further conditional on **omega-3 (DHA/EPA) status**, appearing mainly when baseline omega-3 was in the upper-normal range — another layer of conditionality (a single-trial post-hoc interaction, hypothesis-generating).

**Null — in general/unselected populations.**
- Clarke 2014, B-Vitamin Treatment Trialists' Collaboration (PMID 24965307): meta-analysis of 11 trials with cognitive data on ~22,000 individuals. B-vitamins lowered homocysteine by ~28% but had **no significant effect** on global cognition or any individual cognitive domain. This is the strongest, largest body of evidence and is why the overall grade is conservative. Multiple later meta-analyses of folate/B12 in unselected or AD populations similarly show homocysteine reduction without consistent cognitive benefit.

**B12 deficiency is a distinct, real entity.**
- Moore 2012 (PMID 22221769): cognitive impairment associated with B12 deficiency; cognition improved with supplementation specifically in those with **pre-existing deficiency** (serum B12 <150 pmol/L or Hcy markedly elevated), with better outcomes when treated early. This supports the deficient/impaired-population framing rather than a healthy-population enhancement claim.

Interpretation: the data are best modeled as a **deficiency/elevated-Hcy correction** effect, not a general nootropic. VITACOG remains a single, relatively small center trial whose subgroup finding has not been clearly replicated at scale, which is why evidence_overall = 2 despite the cbf channel being graded 3 within the elevated-Hcy subgroup.

## Safety & interactions

Generally well tolerated at the doses studied, but two specific risks deserve emphasis:

1. **Folate masking of B12 deficiency.** High-dose folic acid can correct the megaloblastic anemia of B12 deficiency while the **neurological** lesion (subacute combined degeneration, peripheral neuropathy, cognitive change) progresses undetected (PMID 38987872). Because this regimen pairs folate with B12, the combination mitigates this within the supplement — but giving folate without confirming B12 status (e.g., self-administered high-dose folic acid) is the hazard. Assess B12 before high-dose folate.

2. **High-dose / chronic pyridoxine (B6) neuropathy.** B6 can cause a dose- and duration-dependent **sensory peripheral neuropathy**; extended intake >50 mg/d is discouraged (PMID 37447150). The VITACOG dose (20 mg/d) sits below common neurotoxic thresholds, but cumulative intake from multiple supplements should be checked.

Interactions: high-dose **B6 reduces levodopa efficacy** when carbidopa is absent. Several drugs (methotrexate, sulfasalazine, anticonvulsants, metformin, PPIs) alter folate/B12 status and may shift baseline. Omega-3 status modifies the cognitive effect (PMID 26757190).

## Open questions

- Is the VITACOG elevated-homocysteine subgroup effect **reproducible** in an adequately powered, prospectively-enrolled high-Hcy MCI trial? (Largely the open question; the headline rests on one center.)
- Is homocysteine itself **causal**, or a marker for B-status/vascular risk that the vitamins happen to track?
- What is the right **screening threshold** (homocysteine and/or B12/folate) that defines who actually benefits, and does treating to a target Hcy matter?
- Does the **omega-3 interaction** hold up, implying B-vitamins only help when DHA/EPA status is adequate?
- Optimal **vitamer and dose** (e.g., methylcobalamin vs cyanocobalamin, methylfolate vs folic acid), and how to capture benefit while minimizing B6 neuropathy and folate-masking risk.
- Whether any benefit is **prevention of decline** specifically (slowing atrophy) rather than improvement of existing cognition.
