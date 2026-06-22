---
id: curcumin
name: Curcumin
aliases:
  - turmeric
  - diferuloylmethane
  - Theracurmin
  - Longvida
  - BCM-95
  - Meriva
type: compound
klass: polyphenol (curcuminoid)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Turmeric (Curcuma longa) rhizome"
status: draft
evidence_overall: 2
onset: weeks (chronic dosing; mood/cognitive endpoints in trials assessed over 4 weeks to 18 months)
half_life: short — unformulated curcumin is rapidly metabolized (plasma activity half-life reported ~min-to-hours; native plasma levels often very low or undetectable). Bioavailable formulations extend exposure modestly. (PMID 24520218)
dose_range: 80–2000 mg/day curcuminoids depending on formulation; Theracurmin 90 mg curcumin twice daily used in the Small 2018 cognition trial (PMID 29246725). Higher unformulated doses (1–4 g/day) used in null AD trials.
cognitive_domains:
  - verbal memory
  - visual memory
  - attention
  - mood (depressive symptoms)
channels:
  - channel: inflam
    mechanism: Inhibition of NF-kB signaling, reduction of pro-inflammatory cytokines (TNF-a, IL-6), and direct antioxidant/free-radical scavenging; preclinically reduces amyloid aggregation and microglial activation. Primary mechanism, strongest preclinically.
    evidence: 2
    population: both
    direction: down
  - channel: ser
    mechanism: Antidepressant-like / serotonergic-monoaminergic modulation; meta-analytic signal for reduced depressive symptoms in clinical trials (adjunctive and standalone). Mechanism partly attributed to anti-inflammatory and monoamine effects.
    evidence: 2
    population: impaired
    direction: modulate
  - channel: ntrophic
    mechanism: Upregulation of BDNF and neurotrophic signaling; reverses stress-induced BDNF reductions in rodent models. Largely preclinical; not directly demonstrated in human brain.
    evidence: 1
    population: preclinical
    direction: up
safety:
  contraindications:
    - active gallbladder disease / biliary obstruction (curcumin is cholekinetic)
    - known hypersensitivity to turmeric/curcuminoids
  interactions:
    - anticoagulants / antiplatelets (warfarin, aspirin, clopidogrel) — additive antiplatelet/bleeding risk (unsourced for magnitude in humans)
    - piperine (black pepper) — markedly increases curcumin bioavailability and may potentiate co-administered drug levels via CYP/UGT inhibition (PMID 24520218)
    - iron — curcumin chelates iron and may lower iron status with chronic high intake (unsourced for clinical significance)
    - drugs metabolized by CYP3A4/CYP2C9/UGT — theoretical pharmacokinetic interaction, especially with piperine co-formulation (unsourced)
  notable_risks:
    - gastrointestinal symptoms (nausea, diarrhea) — dose-limiting; caused withdrawals in AD trials (PMID 23107780)
    - rare hepatotoxicity reports with some high-bioavailability commercial supplements (unsourced)
    - possible reduced iron absorption with chronic use
sources:
  - "Small GW, et al. Memory and Brain Amyloid and Tau Effects of a Bioavailable Form of Curcumin in Non-Demented Adults: A Double-Blind, Placebo-Controlled 18-Month Trial. Am J Geriatr Psychiatry. 2018;26(3):266-277. PMID: 29246725. DOI: 10.1016/j.jagp.2017.10.010"
  - "Ringman JM, et al. Oral curcumin for Alzheimer's disease: tolerability and efficacy in a 24-week randomized, double blind, placebo-controlled study. Alzheimers Res Ther. 2012;4(5):43. PMID: 23107780. DOI: 10.1186/alzrt146"
  - "Baum L, et al. Six-month randomized, placebo-controlled, double-blind, pilot clinical trial of curcumin in patients with Alzheimer disease. J Clin Psychopharmacol. 2008;28(1):110-113. PMID: 18204357. DOI: 10.1097/jcp.0b013e318160862c"
  - "Ng QX, et al. Clinical Use of Curcumin in Depression: A Meta-Analysis. J Am Med Dir Assoc. 2017;18(6):503-508. PMID: 28236605. DOI: 10.1016/j.jamda.2016.12.071"
  - "Prasad S, et al. Recent Developments in Delivery, Bioavailability, Absorption and Metabolism of Curcumin: the Golden Pigment from Golden Spice. Cancer Res Treat. 2014;46(1):2-18. PMID: 24520218. DOI: 10.4143/crt.2014.46.1.2"
tags:
  - polyphenol
  - anti-inflammatory
  - nootropic-candidate
  - mood
  - bioavailability-limited
  - draft
---

## Summary

Curcumin is the principal curcuminoid of turmeric, a polyphenol with potent
preclinical anti-inflammatory and antioxidant activity (NF-kB inhibition,
anti-amyloid effects). Its translational story is dominated by a **notorious
bioavailability problem**: unformulated curcumin is poorly absorbed, rapidly
metabolized, and often undetectable in plasma after oral dosing (PMID 24520218).
This caveat is essential to interpreting every clinical result below — null
trials frequently used poorly absorbed formulations, and the few positive
cognition signals used bioavailable preparations (e.g., Theracurmin).

The overall human evidence for cognitive enhancement is **graded 2** (weak,
hypothesis-generating). The strongest cognition signal is a single small RCT
(Small 2018, n=40) showing memory/attention gains plus reduced amyloid/tau PET
binding — promising but underpowered and unreplicated. Alzheimer's disease
treatment RCTs are largely **null**. A modest **antidepressant meta-analytic
signal** exists in clinically depressed populations. There is little evidence of
benefit in already-healthy adults beyond the Small non-demented (mixed) cohort.

## Mechanism

- **inflam (primary):** Curcumin inhibits NF-kB and downstream pro-inflammatory
  cytokines and acts as a direct antioxidant. Preclinically it reduces amyloid
  aggregation and microglial activation. This is the mechanistically strongest
  and most reproducible action, but most of it is demonstrated *in vitro* and in
  rodents at exposures that human oral dosing struggles to achieve.
- **ser (mood):** Antidepressant-like effects attributed to monoaminergic
  modulation and downstream anti-inflammatory action; supported by clinical
  meta-analysis in depressed patients (graded 2, population-specific).
- **ntrophic (BDNF):** Curcumin upregulates BDNF and reverses stress-induced
  BDNF loss in rodent models. This remains **preclinical** (graded 1); no direct
  human neurotrophic confirmation.

Because the active concentrations reaching the brain in humans are uncertain,
mechanism-to-clinic translation is the central open problem for this compound.

## Evidence

**Cognition — Small et al. 2018 (the headline positive RCT).** Double-blind,
placebo-controlled, 18-month trial in 40 non-demented adults (ages 51–84),
Theracurmin 90 mg curcumin twice daily. Curcumin improved verbal memory
(ES ~0.63, p=0.002) and attention (ES ~0.96, p<0.0001) vs. minimal placebo
change, with FDDNP-PET reductions in amygdala amyloid/tau binding (PMID
29246725). **Honest caveats:** very small n (~20/arm), single site, a single
proprietary bioavailable formulation, and FDDNP-PET (a non-standard tracer) — so
this is a promising but fragile, unreplicated result, not establishment of
efficacy.

**Alzheimer's disease treatment — largely NULL.** Ringman et al. 2012
(24-week RCT, Curcumin C3 Complex) found no clinical or biomarker efficacy, with
notably **low plasma curcumin (~7.3 ng/mL)** underscoring the bioavailability
limitation; GI side effects caused withdrawals (PMID 23107780). Baum et al. 2008
(6-month pilot RCT, 1–4 g/day) likewise showed no significant MMSE or plasma
Aβ-40 differences (PMID 18204357). These nulls are confounded by poor absorption
of the formulations used.

**Depression — modest meta-analytic signal.** Ng et al. 2017 meta-analysis
(6 RCTs, 377 patients) found a statistically significant reduction in depressive
symptoms vs. placebo (SMD ~ -0.34, 95% CI -0.56 to -0.13, p=0.002), with good
tolerability; trials were short (4–8 weeks) and small (PMID 28236605). The
signal is real but in **impaired/depressed** populations, not healthy adults,
and effect sizes are modest.

**Bioavailability — the overriding interpretive lens.** Prasad et al. 2014
review documents curcumin's low aqueous solubility, instability, rapid
metabolism, and very low/undetectable plasma levels after oral dosing; piperine
co-administration and nanoparticle/lipid formulations (Theracurmin, Longvida,
Meriva, BCM-95) substantially raise exposure (PMID 24520218). Any cross-trial
comparison must account for which formulation was used.

## Safety & interactions

- **GI tolerability:** Nausea and diarrhea are the most common, dose-limiting
  effects; caused dropouts in AD trials (PMID 23107780). Generally well tolerated
  at studied doses otherwise.
- **Anticoagulants/antiplatelets:** Curcumin has antiplatelet properties;
  theoretical additive bleeding risk with warfarin, aspirin, clopidogrel, and
  NSAIDs (clinical magnitude in humans **(unsourced)**). Caution perioperatively.
- **Iron chelation:** Curcumin binds iron; chronic high intake may lower iron
  status (clinical significance **(unsourced)**).
- **Piperine / CYP-UGT interactions:** Piperine boosts curcumin bioavailability
  by inhibiting glucuronidation and efflux transporters (PMID 24520218) and may
  similarly raise levels of co-administered CYP3A4/CYP2C9/UGT substrates —
  relevant when supplements are formulated with black pepper extract.
- **Gallbladder disease:** Curcumin stimulates gallbladder contraction; avoid in
  biliary obstruction/active gallstone disease.

## Open questions

- Does the Small 2018 cognition signal replicate in a larger, multi-site RCT
  with a standard amyloid/tau tracer? Currently a single small study.
- How much curcumin (or which metabolites, e.g., tetrahydrocurcumin) actually
  reaches the human brain, and at what concentration relative to mechanistic
  thresholds? Central unresolved issue.
- Are positive results driven by specific bioavailable formulations
  (Theracurmin/Longvida/BCM-95) rather than curcumin per se? Head-to-head
  formulation trials are lacking.
- Is there any cognitive benefit in genuinely healthy, non-symptomatic adults,
  or is the effect confined to inflamed/depressed/at-risk populations?
- Long-term safety of chronic high-bioavailability dosing (hepatic, iron status)
  is under-characterized.
