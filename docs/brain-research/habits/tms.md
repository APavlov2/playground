---
id: tms
name: Transcranial magnetic stimulation (TMS / rTMS)
aliases: [TMS, rTMS, repetitive transcranial magnetic stimulation, deep TMS, dTMS, theta-burst stimulation, TBS, iTBS]
type: habit
klass: "Device — neuromodulation"
origin: natural
source: "Device / neuromodulation — transcranial electromagnetic coil inducing focal intracranial currents"
status: draft
evidence_overall: 4
onset: "Single-pulse effects are immediate; therapeutic rTMS courses run daily over ~4–6 weeks; accelerated/iTBS protocols compress this"
half_life: "n/a (external modality; physiological after-effects of a session estimated tens of minutes to ~1 hour)"
dose_range: ""
cognitive_domains: [working-memory, executive-function, mood, attention]
channels:
  - channel: glu
    mechanism: "Pulsed magnetic field induces suprathreshold intracranial current that directly depolarises cortical neurons; repetitive trains produce LTP/LTD-like changes in synaptic efficacy (high-frequency/iTBS facilitatory, low-frequency/cTBS suppressive), NMDA-dependent"
    evidence: 3
    population: both
    direction: modulate
  - channel: da
    mechanism: "High-frequency rTMS of left DLPFC reported to evoke striatal dopamine release (raclopride PET) and to modulate frontostriatal circuits implicated in mood and motivation"
    evidence: 2
    population: both
    direction: up
  - channel: ntrophic
    mechanism: "Preclinical and some human data link rTMS to increased BDNF expression/serum BDNF and plasticity-related signalling; mechanistic, not established as the driver of clinical benefit"
    evidence: 2
    population: both
    direction: up
safety:
  contraindications: [ferromagnetic or active implants near the coil (e.g. cochlear implants, certain aneurysm clips, deep brain stimulators), personal history raising seizure risk requires careful screening]
  interactions: [proconvulsant drugs and seizure-threshold-lowering medications or withdrawal states raise seizure risk]
  notable_risks: [seizure (rare, ~0.1% of patients / ~1 in 30,000 sessions per device labelling, mostly with risk factors), scalp pain/headache, facial twitching, transient hearing effects (ear protection used), syncope]
sources:
  - "Lefaucheur et al., Clinical Neurophysiology, 2020 — PMID:31901449 (evidence-based rTMS guidelines update 2014–2018; Level A for HF-rTMS of left DLPFC in depression)"
  - "FDA de novo 510(k) clearance of NeuroStar TMS for treatment-resistant major depressive disorder, 2008 (first FDA-cleared rTMS depression device)"
  - "Brunoni & Vanderhasselt, Brain and Cognition, 2014 — PMID:24514153 (NIBS/DLPFC working-memory meta-analysis; rTMS improved WM measures, small effects in healthy adults)"
tags: [device, neuromodulation, FDA-cleared, depression]
---

## Summary
TMS uses a pulsed magnetic field to induce focal currents that directly depolarise cortical neurons; delivered in repetitive trains (rTMS, including theta-burst), it drives LTP/LTD-like plasticity. It is the **strongest-evidence device** in this track — but only for a specific clinical indication: high-frequency rTMS of the left dorsolateral prefrontal cortex for major depression carries Level A (definite efficacy) guideline status and FDA clearance. For **healthy-cognition enhancement**, the evidence is far thinner: effects on working memory and executive function in healthy adults are small and inconsistent. These two populations must be kept distinct.

## Mechanism
**glu (primary, modulate).** Unlike tDCS, TMS induces a suprathreshold current sufficient to fire cortical neurons directly. Repetitive trains then induce synaptic plasticity: high-frequency rTMS and intermittent theta-burst (iTBS) tend to be facilitatory (LTP-like), while low-frequency rTMS and continuous theta-burst (cTBS) tend to be suppressive (LTD-like). These after-effects are NMDA-receptor dependent, hence glutamatergic plasticity is the core substrate; `direction: modulate`, graded **3** (mechanism well established; the cognitive translation is what varies).

**da (secondary, up).** High-frequency rTMS of left DLPFC has been reported to evoke striatal dopamine release on raclopride PET and to modulate frontostriatal circuits, a candidate pathway for antidepressant and motivational effects. Human evidence exists but is limited, so **2**.

**ntrophic (secondary, up).** rTMS is linked to increased BDNF and plasticity signalling in preclinical models and some human serum studies. This is mechanistically suggestive but not established as the cause of clinical benefit, so **2**.

## Evidence
The honest core is the gap between a strong clinical indication and weak healthy-enhancement data.

- **Clinical depression (strong):** Lefaucheur 2020 (PMID:31901449), the IFCN evidence-based guidelines update, assigned **Level A (definite efficacy)** to high-frequency rTMS of the left DLPFC for major depression — the only Level A among device options in this track. rTMS for depression is also FDA-cleared (NeuroStar de novo 510(k), 2008, for treatment-resistant MDD), with later clearances for additional devices/protocols (e.g. iTBS, deep TMS). This clinical claim rates **4 (Strong)** and sets `evidence_overall`.
- **Healthy-cognition enhancement (much weaker):** Brunoni & Vanderhasselt 2014 (PMID:24514153) found rTMS of DLPFC improved working-memory measures, but the effects in healthy adults are small; broader healthy-enhancement meta-analyses report modest, heterogeneous gains in executive function at best. This is **2 (emerging)** — the antidepressant evidence does NOT transfer to "makes healthy people smarter."
- **Why the populations differ:** the Level A depression evidence rests on large multi-site RCTs and meta-analyses in a clinical population with a circuit-level target; healthy-cognition studies are smaller, use varied targets/protocols, and produce inconsistent transfer to real-world cognition.
- Other indications (neuropathic pain, post-stroke motor) reach lower guideline levels and are outside this entry's cognitive focus.

Net: best-supported, most relevant claim — HF-rTMS of left DLPFC for depression — rates **Strong (4)**; healthy-cognition enhancement is **Emerging (2)** and explicitly distinguished.

## Safety & interactions (research metadata)
The principal serious risk is **seizure**, which is rare (~0.1% of patients, on the order of ~1 in 30,000 sessions per device labelling) and concentrated in people with predisposing factors; rigorous screening and adherence to published safety limits (e.g. consensus rTMS safety guidelines) keep risk low. Common, benign effects: scalp/coil-site pain, headache, facial muscle twitching, and transient effects on hearing (ear protection is standard). Contraindicated with ferromagnetic/active implants near the coil (cochlear implants, certain aneurysm clips, DBS). Proconvulsant drugs, lowered seizure threshold, and withdrawal states increase seizure risk. This is research metadata, not medical advice.

## Open questions
- Does rTMS produce durable, transferable cognitive enhancement in healthy people, or only state-dependent task effects? Current data favour the latter.
- Optimal targeting (functional-connectivity-guided vs scalp landmark), dose, and protocol (standard HF vs iTBS vs accelerated) for both mood and cognition.
- How much of the antidepressant effect is mediated by glutamatergic plasticity vs dopaminergic/network effects vs nonspecific factors?
- Long-term durability and relapse prevention after a treatment course.
