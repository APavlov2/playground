---
id: nmn
name: NMN
aliases:
  - nicotinamide mononucleotide
  - "β-nicotinamide mononucleotide"
  - beta-NMN
  - "β-NMN"
type: compound
klass: NAD+ precursor (vitamin B3-related nucleotide)
status: draft
evidence_overall: 1
onset: "single-dose pharmacokinetics show rapid absorption; blood NAD+ elevation accrues over days-to-weeks of repeated dosing"
half_life: "(unsourced) — NMN itself is rapidly cleared/converted; plasma NAD+ metabolite changes are the practical readout, rising over weeks"
dose_range: "human RCTs: 250 mg/day; dose-finding to 300–900 mg/day; metabolic study used 250 mg/day"
cognitive_domains:
  - "(unsourced) — no validated human cognitive-domain endpoint; preclinical signals only (spatial working memory, gait coordination in aged mice)"
channels:
  - channel: mito
    mechanism: "NMN is an NAD+ precursor; raises tissue/blood NAD+ supporting mitochondrial bioenergetics, sirtuin activity, and redox metabolism. Human RCTs confirm blood NAD+ elevation, but downstream brain-bioenergetic benefit is not demonstrated in humans."
    evidence: 2
    population: both
    direction: up
  - channel: ntrophic
    mechanism: "Preclinical: NMN rescued cerebromicrovascular endothelial function and neurovascular coupling and improved cognition in aged mice; protected against β-amyloid-oligomer-induced cognitive impairment and neuronal death in rodents. Neuroprotection is PRECLINICAL only; no human neurotrophic/neuroprotection endpoint."
    evidence: 1
    population: preclinical
    direction: up
safety:
  contraindications: []
  interactions: []
  notable_risks:
    - "Limited long-term human safety data; RCTs to date are short (≤12 weeks) and small."
    - "Reported human tolerability is generally good at 250–900 mg/day, with no serious adverse events attributed in published RCTs; rare mild GI/transient effects."
    - "Regulatory note: in November 2022 the U.S. FDA took the position that NMN is excluded from the dietary-supplement definition (drug-preclusion / 'race-to-market' clause, citing prior investigation as a drug), complicating its supplement status. (FDA later reversed this position in 2025; status has been contested.)"
    - "Theoretical concern (unsourced): biological plausibility that raising NAD+ pathways could affect proliferative/metabolic processes; not established as a clinical risk."
sources:
  - "Yoshino M, et al. Nicotinamide mononucleotide increases muscle insulin sensitivity in prediabetic women. Science. 2021. PMID: 33888596. DOI: 10.1126/science.abe9985"
  - "Igarashi M, et al. Chronic nicotinamide mononucleotide supplementation elevates blood NAD+ levels and alters muscle function in healthy older men. NPJ Aging. 2022. PMID: 35927255. DOI: 10.1038/s41514-022-00084-z"
  - "Kim M, et al. Effect of 12-Week Intake of Nicotinamide Mononucleotide on Sleep Quality, Fatigue, and Physical Performance in Older Japanese Adults: A Randomized, Double-Blind Placebo-Controlled Study. Nutrients. 2022. PMID: 35215405. DOI: 10.3390/nu14040755"
  - "Yi L, et al. The efficacy and safety of β-nicotinamide mononucleotide (NMN) supplementation in healthy middle-aged adults: a randomized, multicenter, double-blind, placebo-controlled, parallel-group, dose-dependent clinical trial. GeroScience. 2022. PMID: 36482258. DOI: 10.1007/s11357-022-00705-1"
  - "Ingestion of β-nicotinamide mononucleotide increased blood NAD levels, maintained walking speed, and improved sleep quality in older adults in a double-blind randomized, placebo-controlled study. GeroScience. 2024. PMID: 38789831. DOI: 10.1007/s11357-024-01204-1"
  - "Tarantini S, et al. NMN supplementation rescues cerebromicrovascular endothelial function and neurovascular coupling responses and improves cognitive function in aged mice. Redox Biol. 2019. PMID: 31015147. DOI: 10.1016/j.redox.2019.101192"
  - "Wang X, et al. Nicotinamide mononucleotide protects against β-amyloid oligomer-induced cognitive impairment and neuronal death. Brain Res. 2016. PMID: 27130898. DOI: 10.1016/j.brainres.2016.04.060"
tags:
  - nad-precursor
  - mitochondrial
  - longevity
  - low-evidence-for-brain
  - preclinical-neuro
  - regulatory-contested
---

## Summary

NMN (β-nicotinamide mononucleotide) is an NAD+ precursor promoted on an NAD+-decline-with-aging rationale. That rationale, along with its neuroprotective and cognitive claims, is **largely preclinical**. Human RCTs do exist, but they target **metabolic and physical endpoints** (muscle insulin sensitivity, NAD+ blood levels, walking speed, sleep quality), not cognition. **Direct brain/cognition RCT evidence in humans is minimal-to-absent**, so brain-specific claims are graded LOW (1). Overall evidence for the **brain** use case is graded **1**.

## Mechanism

NMN is converted to NAD+ via the salvage pathway (NMN → NAD+ through NMNAT enzymes). NAD+ is central to mitochondrial bioenergetics, redox balance (NAD+/NADH), and as a substrate/cofactor for sirtuins and PARPs. The proposed brain benefit is bioenergetic/neurovascular: restoring NAD+ to support mitochondrial function (channel: **mito**) and, in animal models, endothelial/neurovascular and neuroprotective effects (channel: **ntrophic**). In humans, oral NMN reliably **raises blood NAD+ and its metabolites**; the mechanistic chain to improved human brain bioenergetics or cognition is **not demonstrated**.

## Evidence

**Human RCT evidence is metabolic/physical, not cognitive.**

- **Muscle insulin sensitivity:** In postmenopausal prediabetic women, 250 mg/day NMN for 10 weeks increased insulin-stimulated glucose disposal and skeletal-muscle insulin signaling versus placebo (PMID: 33888596). This is a metabolic endpoint, not a brain endpoint.
- **Blood NAD+ and muscle function:** Chronic NMN in healthy older men elevated blood NAD+ and altered muscle function (PMID: 35927255). Physiologic/metabolic readout.
- **Sleep / physical performance:** 250 mg/day for 12 weeks in older Japanese adults affected sleep-quality and physical-performance measures (PMID: 35215405); a separate 2024 RCT (250 mg/day, 12 weeks) raised blood NAD+, maintained 4-m walking speed, and improved Pittsburgh Sleep Quality Index measures (PMID: 38789831). Sleep questionnaires are **not** validated cognitive endpoints.
- **Dose-finding / safety:** A multicenter dose-dependent RCT (300–900 mg/day) in healthy middle-aged adults supported tolerability and NAD+ elevation (PMID: 36482258); endpoints were physical/biochemical.

**Preclinical neuro (animal only):**

- NMN rescued cerebromicrovascular endothelial function and neurovascular coupling and improved spatial working memory and gait coordination in **aged mice** (PMID: 31015147).
- NMN protected against β-amyloid-oligomer-induced cognitive impairment and neuronal death in **rodent** AD models (PMID: 27130898).

**Brain-cognition gap:** There is **no adequately powered human RCT demonstrating a direct cognitive benefit of NMN** — **(unsourced)**. Human cognitive-domain efficacy is therefore unestablished, and the neuroprotective/anti-aging brain rationale rests on preclinical rodent data.

## Safety & interactions

- Short-term human tolerability at 250–900 mg/day appears good in published RCTs, with no serious adverse events attributed; effects reported were mild/transient.
- **Long-term safety data are limited** — trials are ≤12 weeks and small (tens of participants).
- No well-characterized drug interactions or formal contraindications are established in the human literature (interactions and contraindications left empty rather than fabricated).
- **Regulatory note:** In November 2022 the U.S. FDA took the position that NMN is **excluded from the dietary-supplement definition** under the drug-preclusion ("race-to-market") provision, citing prior authorization for investigation as a drug. This complicated NMN's lawful status as a supplement in the U.S. (The FDA later reversed this position in 2025; the regulatory status has been contested over time — verify current status before relying on it.)

## Open questions

- Does NMN produce any **measurable human cognitive benefit**? No direct RCT evidence exists yet — **(unsourced)**.
- Does human oral NMN raise **brain/CNS NAD+** (versus only blood/peripheral NAD+)? Unestablished in humans.
- Do the rodent neurovascular/neuroprotective effects translate to aged or impaired human brains?
- What are the **long-term** (>12 month) safety and any proliferative/metabolic risks of sustained NAD+ elevation?
- Optimal dose, duration, and whether NMN offers any brain advantage over other NAD+ precursors (e.g., nicotinamide riboside) — unresolved.
