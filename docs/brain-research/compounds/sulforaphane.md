---
id: sulforaphane
name: Sulforaphane
aliases:
  - "broccoli sprout isothiocyanate"
  - "SFN"
  - "1-isothiocyanato-4-(methylsulfinyl)butane"
  - "broccoli sprout extract"
type: compound
klass: "phytochemical / Nrf2 pathway activator (isothiocyanate)"
status: draft
evidence_overall: 2
onset: "Single-dose plasma Cmax ~1-3 h after sprout/extract ingestion; clinical behavioral/cognitive effects (where seen) accrue over weeks of daily dosing (~4-18 weeks in trials)."
half_life: "Plasma half-life of sulforaphane and its mercapturic-acid metabolites ~2-3 h; rapidly conjugated and renally excreted. Pharmacodynamic Nrf2 target-gene induction outlasts plasma exposure."
dose_range: "Trial doses 50-150 µmol/day sulforaphane equivalents from broccoli sprout extract (Singh 2014). Note: sulforaphane vs glucoraphanin precursor + myrosinase strongly affects delivered dose; glucoraphanin without active myrosinase is 3-4x less bioavailable, and sulforaphane itself is only moderately stable in aqueous solution (Fahey 2015)."
cognitive_domains:
  - "(none robustly established in healthy adults)"
  - "social interaction / aberrant behavior (autism, signal mixed/modest)"
  - "verbal learning, spatial working memory, reasoning (schizophrenia secondary outcomes only)"
channels:
  - channel: inflam
    mechanism: "Nrf2/Keap1 pathway activation upregulates antioxidant-response-element (ARE) genes (NQO1, HO-1, glutathione synthesis), reducing oxidative stress and neuroinflammatory signaling. This is the primary, well-established mechanism."
    evidence: 3
    population: preclinical
    direction: down
  - channel: glu
    mechanism: "Theoretical/preclinical: attenuation of oxidative-glutamatergic toxicity and modulation of redox-sensitive glutamate handling; proposed relevance to schizophrenia adjunct rationale. Human glutamatergic effects not demonstrated."
    evidence: 2
    population: preclinical
    direction: modulate
safety:
  contraindications:
    - "Known hypersensitivity to cruciferous (Brassica) vegetables or broccoli sprout products."
  interactions:
    - "Theoretical additive antioxidant/Nrf2 effects with other Nrf2 activators; clinical significance unknown (unsourced)."
    - "Goitrogenic glucosinolate co-constituents in raw cruciferous preparations may theoretically interact with thyroid function/iodine, especially in iodine-deficient individuals (theoretical)."
  notable_risks:
    - "Mild gastrointestinal complaints (nausea, flatulence, reflux, diarrhea) most common in trials."
    - "Theoretical goitrogenic effect from glucosinolate-rich preparations; not established as clinically significant at trial doses."
    - "Reports of olfactory/taste effects and, rarely, behavioral activation or insomnia in autism trials."
    - "Long-term safety data in healthy adults limited; product/dose standardization is poor (sulforaphane vs glucoraphanin, stability)."
sources:
  - "Singh K, et al. Sulforaphane treatment of autism spectrum disorder (ASD). PNAS. 2014;111(43):15550-15555. PMID: 25313065. DOI: 10.1073/pnas.1416940111"
  - "Zimmerman AW, et al. Randomized controlled trial of sulforaphane and metabolite discovery in children with Autism Spectrum Disorder. Mol Autism. 2021;12(1):38. PMID: 34034808. DOI: 10.1186/s13229-021-00447-5"
  - "Hei G, Smith RC, et al. Sulforaphane Effects on Cognition and Symptoms in First and Early Episode Schizophrenia: A Randomized Double-Blind Trial. Schizophr Bull Open. 2022;3(1):sgac024. PMID: 39144775. DOI: 10.1093/schizbullopen/sgac024"
  - "Wang R, Ren Z, Li Y. The effect of sulforaphane on autism spectrum disorder: systematic review and meta-analysis. EXCLI J. 2025;24. PMID: 40458076. DOI: 10.17179/excli2025-8239"
  - "Fahey JW, et al. Sulforaphane Bioavailability from Glucoraphanin-Rich Broccoli: Control by Active Endogenous Myrosinase. PLoS One. 2015;10(11):e0140963. DOI: 10.1371/journal.pone.0140963"
tags:
  - nrf2
  - antioxidant
  - anti-inflammatory
  - isothiocyanate
  - autism
  - schizophrenia
  - phytochemical
  - modest-evidence
---

## Summary

Sulforaphane is a broccoli-sprout-derived isothiocyanate and one of the most potent dietary activators of the Nrf2/Keap1 antioxidant-response pathway. Its antioxidant and anti-inflammatory mechanism is well-established at the molecular and preclinical level. However, **human brain evidence is limited and confined to clinical populations**: autism RCTs show mixed-to-modest behavioral signals, and small schizophrenia adjunct studies show cognitive effects only on secondary outcomes. There is essentially **no RCT evidence for cognitive enhancement in healthy adults**. Graded modestly (evidence_overall 2). Note the important practical distinction between sulforaphane itself and its precursor glucoraphanin (which requires myrosinase for conversion), plus sulforaphane's moderate aqueous instability — both materially affect delivered dose.

## Mechanism

The primary mechanism is activation of the Nrf2 (NFE2L2) transcription factor. Sulforaphane modifies cysteine residues on Keap1, releasing Nrf2 to translocate to the nucleus and induce antioxidant-response-element (ARE)-driven genes — NQO1, heme oxygenase-1 (HO-1), glutathione synthesis enzymes, and other phase-II detoxification/antioxidant effectors. The downstream effect is reduced oxidative stress and dampened neuroinflammatory signaling (**inflam** channel, primary). A secondary, more speculative rationale concerns oxidative-glutamatergic toxicity: by restoring redox balance, sulforaphane may modulate glutamate-related excitotoxic processes (**glu** channel, preclinical/theoretical only). These mechanisms motivate the autism and schizophrenia trial programs, where oxidative stress and neuroinflammation are implicated.

## Evidence

**Autism RCTs (mixed/modest).** The landmark trial, Singh et al. 2014 (PNAS; PMID 25313065), randomized 44 young males (13-27 y) with moderate-to-severe ASD to sulforaphane (50-150 µmol/day) vs placebo for 18 weeks. It reported substantial, reversible improvements in social interaction, aberrant behavior, and verbal communication (e.g., ~34% reduction in ABC scores), with effects fading 4 weeks after stopping. A subsequent, more rigorous RCT — Zimmerman et al. 2021 (Mol Autism; PMID 34034808) — in 45 children with ASD found **no statistically significant effect on its primary outcome** (Ohio Autism Clinical Impressions Scale; effect sizes small but positive) and a significant improvement only on the secondary ABC measure, not on SRS-2. A 2025 systematic review/meta-analysis of six RCTs (Wang et al., EXCLI J; PMID 40458076) found small-to-moderate pooled benefits (total symptoms SMD -0.27; aberrant behavior -0.43; hyperactivity -0.58; social interaction -0.43) but non-significant effects on irritability, anxiety, and several social subdomains, with adverse events comparable to placebo. Overall: a consistent but modest signal in ASD, with the most rigorous single trial negative on its primary endpoint.

**Schizophrenia adjunct (small, secondary-outcome only).** Hei, Smith et al. 2022 (Schizophr Bull Open; PMID 39144775) randomized 172 first/early-episode schizophrenia patients (151 with follow-up) to sulforaphane vs placebo over 22 weeks. The **primary outcome (MATRICS overall composite) was not significant**, and there were no effects on PANSS symptoms. Improvements appeared only on secondary MATRICS domains (spatial working memory, verbal learning, reasoning/problem-solving). Well tolerated. Interpreted as hypothesis-generating, warranting further trials.

**Healthy-adult cognition (thin/absent).** No methodologically robust RCT evidence for cognitive enhancement in healthy adults was identified (unsourced). The clinical signal is specific to ASD and schizophrenia populations and should not be extrapolated to healthy cognition.

## Safety & interactions

Sulforaphane / broccoli sprout extract was generally well tolerated across trials, including in children. The most common adverse effects are gastrointestinal (nausea, flatulence, reflux, loose stools). A **theoretical goitrogenic concern** exists for glucosinolate-rich cruciferous preparations affecting thyroid/iodine handling, but this has not emerged as a clinically meaningful problem at studied doses. Rarely, autism trials noted behavioral activation, insomnia, or olfactory effects. Drug interaction data are sparse; additive effects with other Nrf2 activators are theoretical (unsourced). **Practical caveat:** product potency is highly variable — sulforaphane vs glucoraphanin precursor, presence/absence of active myrosinase, and sulforaphane's moderate aqueous instability (Fahey 2015) all change the delivered dose substantially. Long-term safety in healthy adults is not well characterized.

## Open questions

- Does sulforaphane benefit cognition in healthy adults at all? No RCT evidence currently supports this.
- Why do primary outcomes tend to fail while secondary outcomes (ABC in autism; MATRICS subdomains in schizophrenia) show signals — true effect on specific domains, or multiple-comparison artifact?
- Optimal formulation and dosing: standardized sulforaphane vs glucoraphanin + myrosinase, and how to control for stability/bioavailability across products.
- Are behavioral effects in ASD driven by the Nrf2/anti-inflammatory mechanism, or by other isothiocyanate actions?
- Durability: Singh 2014 effects reversed after washout — does chronic dosing sustain benefit, and what is long-term safety?
