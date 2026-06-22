---
id: vagus-nerve-stimulation
name: Vagus nerve stimulation (VNS / taVNS)
aliases: [VNS, taVNS, tVNS, transcutaneous auricular vagus nerve stimulation, cervical VNS, invasive vagus nerve stimulation]
type: habit
klass: "Device — neuromodulation"
origin: natural
source: "Device / neuromodulation — implanted cervical vagus stimulator (invasive) or transcutaneous auricular/cervical electrode (non-invasive)"
status: draft
evidence_overall: 2
onset: "Acute neuromodulatory effects within a session; plasticity/memory effects emerge over paired-training or multi-session courses; clinical effects over months"
half_life: "n/a (external/implanted modality; central neuromodulator after-effects estimated minutes after a burst)"
dose_range: ""
cognitive_domains: [memory, learning, attention, executive-function]
channels:
  - channel: ne
    mechanism: "Vagal afferents project via nucleus tractus solitarius to the locus coeruleus, driving noradrenergic release across cortex; LC/NE engagement is considered a primary route for VNS-enhanced plasticity and memory"
    evidence: 2
    population: both
    direction: up
  - channel: ach
    mechanism: "VNS engages basal-forebrain cholinergic projections; cortical cholinergic (and noradrenergic) fibres are required for VNS-driven cortical map plasticity in animal models"
    evidence: 2
    population: both
    direction: up
  - channel: ntrophic
    mechanism: "Paired VNS gates timing-specific cortical reorganisation (targeted-plasticity therapy); preclinical work links this to plasticity-related signalling, supporting rehabilitation pairing"
    evidence: 2
    population: both
    direction: up
safety:
  contraindications: [bilateral or prior cervical vagotomy for invasive VNS, caution with significant cardiac conduction disease]
  notable_risks: [invasive VNS — surgical risk, voice alteration/hoarseness, cough, dyspnea, bradycardia; taVNS — generally mild ear/skin irritation, local discomfort]
  interactions: []
sources:
  - "Hays, Rennaker & Kilgard, Progress in Brain Research, 2013 — PMID:24309259 (targeting plasticity with VNS; LC-NE and cholinergic mechanisms, paired rehabilitation)"
  - "Engineer et al., Nature, 2011 — PMID:21228773 (VNS paired with tones reverses pathological plasticity in a tinnitus model; targeted-plasticity proof of concept)"
  - "Cortese-style note: taVNS healthy-cognition reviews (e.g. Ridgewell et al., 2021) report small acute executive-function gains — described; primary aggregate effect sizes remain heterogeneous and unsourced at the meta-analytic level here"
tags: [device, neuromodulation, plasticity, emerging]
---

## Summary
Vagus nerve stimulation drives central neuromodulator systems by stimulating vagal afferents — either via an implanted cervical electrode (invasive VNS) or a non-invasive transcutaneous auricular/cervical electrode (taVNS). The key mechanism for cognition is engagement of the locus-coeruleus noradrenergic and basal-forebrain cholinergic systems, which gate cortical plasticity; pairing brief VNS with training can sculpt timing-specific reorganisation ("targeted-plasticity therapy"). For brain-optimisation purposes the field is **emerging**: the plasticity mechanism is well demonstrated preclinically and underpins approved rehabilitation pairing (e.g. stroke), but human healthy-cognition effects from taVNS are small, acute, and heterogeneous.

## Mechanism
**ne (primary, up).** Vagal afferents synapse in the nucleus tractus solitarius, which projects to the locus coeruleus; VNS increases LC noradrenergic firing and cortical NE release. This LC-NE engagement is considered a primary route by which VNS widens plasticity and enhances memory consolidation (Hays 2013, PMID:24309259). Graded **2** — strong preclinical mechanism, limited human cognitive confirmation.

**ach (secondary, up).** VNS also recruits basal-forebrain cholinergic projections. Critically, cortical depletion of cholinergic (or noradrenergic) fibres blocks VNS-driven cortical map plasticity in animals, showing both systems are required — not incidental. Human-specific cholinergic cognitive data are limited, so **2**.

**ntrophic (secondary, up).** The defining feature of "targeted-plasticity therapy" is that a brief VNS burst paired with a sensory/motor event gates timing-specific cortical reorganisation. Engineer 2011 (PMID:21228773) showed VNS paired with tones reverses pathological auditory plasticity in a tinnitus model — proof of concept that VNS opens a plasticity window. This supports rehabilitation pairing; the neurotrophic-signalling detail is preclinical, so **2**.

## Evidence
The honest split is between a robust preclinical plasticity mechanism (and approved rehabilitation pairing) and modest, emerging human cognition data.

- **Mechanism / targeted plasticity (strongest, but largely preclinical):** Hays 2013 (PMID:24309259) reviews how VNS engages LC-NE and cholinergic systems to enhance plasticity, and Engineer 2011 (PMID:21228773, *Nature*) is the canonical demonstration that precisely timed VNS pairing reorganises cortex and corrects a pathological state. This is a clean, influential mechanism — but per the rubric, animal-model plasticity caps at **2** for the human-cognition claim.
- **Clinical rehabilitation (invasive VNS):** paired-VNS plus rehabilitation has progressed to clinical use for upper-limb recovery after ischemic stroke (and invasive VNS is long-established for epilepsy and treatment-resistant depression). These are clinical/impaired populations and distinct from healthy enhancement; the rehabilitation evidence is the most translation-ready strand but is indication-specific.
- **Healthy-cognition (taVNS, emerging and modest):** small studies of transcutaneous auricular VNS in healthy adults report acute, small-to-moderate gains most consistently in executive function, with heterogeneous effects on working memory, inhibition, and shifting. Aggregate effect sizes are inconsistent across reviews; I have not anchored a single resolvable meta-analytic effect size here, so the precise magnitude is left **unsourced** and the claim is graded conservatively at **2 (emerging)**.
- **Why not higher:** human healthy-enhancement trials are small, sham-control quality varies (taVNS sensation complicates blinding), and durable far-transfer is unestablished.

Net: best-supported, most relevant claim — VNS-gated plasticity / acute taVNS executive-function effects — rates **Emerging (2)**. The plasticity *mechanism* is strong; the healthy-cognition *outcome* evidence is not yet.

## Safety & interactions (research metadata)
**Invasive VNS** carries surgical implantation risk and stimulation-related effects: hoarseness/voice alteration, cough, throat discomfort, dyspnea, and occasional bradycardia; contraindicated after bilateral/prior cervical vagotomy and used cautiously with significant cardiac conduction disease. **taVNS** is much lower-risk, with mild ear/skin irritation or local discomfort the main complaints. No established systemic drug interactions for cognitive-dose use. This is research metadata, not medical advice.

## Open questions
- Do acute taVNS executive-function gains in healthy adults replicate in larger, well-blinded trials and translate to durable benefit?
- Optimal taVNS parameters (location, frequency, intensity, on/off timing) and whether they can reliably reproduce the LC-NE "plasticity window" non-invasively.
- How closely does non-invasive taVNS engage the LC-NE/cholinergic circuitry compared with invasive VNS?
- Aggregate human effect sizes for cognition remain heterogeneous and partly unsourced at meta-analytic level — a clean pre-registered synthesis is needed.
