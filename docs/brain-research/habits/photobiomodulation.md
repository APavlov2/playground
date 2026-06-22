---
id: photobiomodulation
name: Photobiomodulation (transcranial red/near-infrared light)
aliases: [tPBM, t-PBM, low-level laser therapy, LLLT, transcranial PBM, near-infrared light therapy]
type: habit
klass: "Device — photobiomodulation"
origin: natural
source: "Device / neuromodulation — transcranial red/near-infrared light (typically 620–680 nm and 800–1100 nm LED or laser)"
status: draft
evidence_overall: 2
onset: "Acute effects on cerebral oxygenation/oscillations within a single session (minutes); cognitive/clinical effects studied over single sessions to multi-week courses"
half_life: "n/a (external modality; biological after-effects of a session estimated to persist hours)"
dose_range: ""
cognitive_domains: [attention, working-memory, executive-function, mental-fatigue]
channels:
  - channel: mito
    mechanism: "Photons in the red/NIR window are absorbed by mitochondrial cytochrome-c-oxidase (Complex IV); proposed to photodissociate inhibitory nitric oxide from the enzyme, increasing electron transport, membrane potential and ATP synthesis"
    evidence: 2
    population: both
    direction: up
  - channel: cbf
    mechanism: "NIR exposure and downstream NO release reported to increase cerebral blood flow and tissue oxygenation over irradiated cortex (measured by NIRS/fMRI in small human studies)"
    evidence: 2
    population: healthy
    direction: up
  - channel: inflam
    mechanism: "Preclinical models show reduced oxidative stress, lower pro-inflammatory cytokines and decreased neuronal apoptosis after tPBM; human anti-inflammatory data are sparse"
    evidence: 1
    population: preclinical
    direction: down
safety:
  contraindications: []
  interactions: []
  notable_risks: [thermal skin/scalp heating or burns at high power densities or with laser sources, eye exposure risk requiring protection, large uncertainty in scalp-to-cortex light penetration and effective dose]
sources:
  - "Salehpour et al., Molecular Neurobiology, 2018 — PMID:29327206 (narrative review of brain photobiomodulation; cytochrome-c-oxidase/NO mechanism)"
  - "Salehpour et al., Photobiomodulation Photomedicine and Laser Surgery, 2019 — PMID:31549906 (systematic review/meta-analysis, healthy young adults; cognition SMD ~0.83, high heterogeneity)"
  - "Hamblin, BBA Clinical, 2017 (review of CCO photoacceptor mechanism) — described, see Salehpour 2018 for primary synthesis"
tags: [device, neuromodulation, mitochondrial, emerging]
---

## Summary
Transcranial photobiomodulation (tPBM) applies red and near-infrared light (roughly 620–1100 nm) to the scalp with the goal of driving a mitochondrial photochemical effect in cortex. The dominant proposed mechanism is absorption by cytochrome-c-oxidase, boosting electron transport and ATP. In humans the modality is best characterised as **emerging**: a handful of small single-session studies and one meta-analysis in healthy young adults report cognitive improvement, but study quality is low, heterogeneity is high, blinding is difficult, and the fundamental question of how much light actually reaches cortex is unresolved. Most of the strongest mechanistic claims come from cell and rodent work.

## Mechanism
**mito (primary, up).** The signature claim is that red/NIR photons are absorbed by cytochrome-c-oxidase (Complex IV of the electron transport chain), which acts as the principal chromophore. The leading model (Salehpour 2018, PMID:29327206) is that light photodissociates inhibitory nitric oxide bound to CCO, relieving inhibition of electron transport and transiently increasing membrane potential, ATP output, and a brief signalling burst of reactive oxygen species and NO. This is a plausible, repeatedly described mechanism, but in humans it is inferred rather than directly demonstrated at the cortical level, so it is graded **2 (emerging)** rather than higher.

**cbf (secondary, up).** NIR exposure and downstream NO release are reported to raise cerebral blood flow and cortical oxygenation; small human studies using NIRS and fMRI have shown acute hemodynamic changes over the irradiated region. Effect sizes and reproducibility are uncertain, so this is **2**.

**inflam (preclinical, down).** Animal and cell models show reduced oxidative stress, lower inflammatory cytokines, and less apoptosis after tPBM. Human anti-inflammatory/neuroprotective data are minimal, so this stays **1 (preclinical)**.

## Evidence
Human literature is thin and methodologically weak; preclinical literature is large but does not raise the human grade.

- **Healthy-enhancement (the relevant population here):** Salehpour 2019 (PMID:31549906) pooled six full-text studies of healthy young adults and reported improved cognition with a large standardized mean difference (~0.83, 95% CI ~0.46–1.21, adjusted upward after trim-and-fill). The authors themselves flag modest methodological quality and high heterogeneity. A large SMD from a small, heterogeneous, hard-to-blind literature should be treated cautiously — single-session sham-controlled designs in this field are vulnerable to expectancy and to dosimetry inconsistency. Net: **2 (emerging)**, not 3.
- **Mechanistic human signals:** small NIRS/fMRI studies show acute changes in cortical oxygenation and oscillatory activity during/after tPBM, supporting *some* real biological effect of the light, but not establishing a durable cognitive benefit.
- **Preclinical:** rodent and cell work on CCO photoacceptance, ATP, oxidative stress, and recovery in injury/aging models is the bulk of the evidence base (synthesised in Salehpour 2018, PMID:29327206). Per the rubric, strong preclinical-only evidence caps at 2 and does not lift the human grade.
- **Dosimetry caveat (the central unknown):** scalp, skull and tissue strongly attenuate light, and estimates of how much reaches cortex vary widely. Wavelength, power density, fluence, pulsing, and device contact all differ across studies, making cross-study comparison and "correct dose" essentially unsettled.

Net: best-supported relevant claim — acute cognitive/hemodynamic effects in healthy adults — rates **Emerging (2)**. Clinical applications (e.g. TBI, neurodegeneration, depression) remain investigational and are not graded higher here.

## Safety & interactions (research metadata)
Generally well tolerated in short-term studies. Principal physical risks are thermal: scalp/skin heating or burns at high irradiance, and retinal hazard from direct laser/LED exposure (eye protection is standard). No established systemic drug interactions. Long-term safety of repeated cortical exposure is not well characterised. This is research metadata, not medical advice.

## Open questions
- How much light of a given wavelength actually reaches human cortex, and what is the effective dose-response? This dosimetry gap undercuts almost every other claim.
- Are the reported cognitive gains real and specific, or largely expectancy/placebo in small unblinded designs? Larger pre-registered sham-controlled RCTs are needed.
- Does any acute hemodynamic/oscillatory change translate into durable cognitive or clinical benefit?
- Optimal parameters (continuous vs pulsed, wavelength, fluence, session frequency) are unresolved and may differ by indication.
