---
id: tdcs-tacs
name: Transcranial electrical stimulation (tDCS / tACS)
aliases: [tDCS, tACS, transcranial direct current stimulation, transcranial alternating current stimulation, tES]
type: habit
klass: "Device — neuromodulation"
origin: natural
source: "Device / neuromodulation — transcranial scalp electrodes delivering weak (~1–2 mA) direct or alternating current"
status: draft
evidence_overall: 2
onset: "Online effects during stimulation (minutes); after-effects reported to persist tens of minutes to ~1 hour; cumulative effects studied over multi-session courses"
half_life: "n/a (external modality; physiological after-effects of a session estimated up to ~1 hour)"
dose_range: ""
cognitive_domains: [working-memory, attention, executive-function, learning]
channels:
  - channel: glu
    mechanism: "Weak subthreshold current shifts resting membrane potential, biasing neuronal firing probability; anodal tDCS raises cortical excitability and after-effects depend on NMDA-receptor / glutamatergic plasticity (LTP-like), shown via pharmacology and MRS GABA/glutamate changes"
    evidence: 2
    population: both
    direction: modulate
  - channel: gaba
    mechanism: "MRS studies report anodal tDCS reduces local GABA and cathodal tDCS reduces glutamate under the electrode, consistent with excitation/inhibition rebalancing; tACS aims to entrain endogenous oscillations (e.g. gamma/theta) via rhythmic inhibition–excitation"
    evidence: 2
    population: healthy
    direction: modulate
safety:
  contraindications: [implanted cranial metal/electronic devices near electrodes, scalp skin lesions at electrode sites]
  interactions: []
  notable_risks: [skin irritation/redness and rare chemical burns under electrodes, tingling/itching/headache, large between-subject and between-study variability, replication and effect-size controversy, risks largely uncharacterised for unsupervised consumer/DIY use]
sources:
  - "Horvath, Forte & Carter, Brain Stimulation, 2015 — PMID:25701175 (quantitative review: no significant cognitive effect of single-session tDCS in healthy adults across 59 analyses)"
  - "Lefaucheur et al., Clinical Neurophysiology, 2017 — PMID:28709880 (evidence-based therapeutic tDCS guidelines; Level B at best for depression/fibromyalgia/craving, no Level A)"
  - "Brunoni & Vanderhasselt, Brain and Cognition, 2014 — PMID:24514153 (NIBS/DLPFC working-memory meta-analysis; tDCS improved reaction time but not accuracy)"
tags: [device, neuromodulation, replication-controversy, emerging]
---

## Summary
tDCS (direct current) and tACS (alternating current) deliver weak scalp currents (~1–2 mA) intended to nudge cortical excitability — anodal stimulation generally raising and cathodal lowering firing probability, with tACS aiming to entrain ongoing oscillations. The mechanism (subthreshold polarisation with NMDA-dependent after-effects) is reasonably supported. The **behavioural** payoff for healthy-cognition enhancement, however, is genuinely contested: a high-profile quantitative review found no reliable single-session cognitive effect in healthy adults, and the field is marked by small studies, large inter-individual variability, and weak replication. Graded **down** accordingly.

## Mechanism
**glu (primary, modulate).** Unlike TMS, tDCS does not directly trigger action potentials; it applies a weak constant field that shifts resting membrane potential, biasing the probability of firing (anodal depolarising, cathodal hyperpolarising). The lasting after-effects depend on glutamatergic/NMDA-receptor plasticity: pharmacological blockade of NMDA receptors abolishes them, and the effect is best described as LTP/LTD-like modulation rather than simple "up." Hence `direction: modulate`, graded **2**.

**gaba (secondary, modulate).** Magnetic resonance spectroscopy studies report that anodal tDCS lowers local GABA and cathodal tDCS lowers glutamate beneath the electrode, consistent with rebalancing cortical excitation/inhibition. tACS additionally aims to entrain endogenous rhythms (theta, gamma) by rhythmically biasing the excitation–inhibition cycle. The neurochemical signal is real but its link to robust cognitive gains is weak, so **2**.

## Evidence
The mechanism is on firmer ground than the cognitive-enhancement outcomes; the relevant honest call is to separate clinical from healthy-enhancement claims, and to flag replication problems.

- **Healthy-enhancement (graded down):** Horvath, Forte & Carter 2015 (PMID:25701175) reanalysed replicated single-session tDCS outcomes in healthy populations and found a significant effect on *zero* of 59 analyses across 42 cognitive measures — i.e. no reliable single-session cognitive enhancement. This is the central reason the healthy-enhancement claim is graded **2 at most** and arguably lower. The result is itself debated (critics note the inclusion criteria excluded multi-session and physiological outcomes), but it stands as a serious replication/effect-size warning.
- **Working memory specifically:** Brunoni & Vanderhasselt 2014 (PMID:24514153), a meta-analysis of NIBS over DLPFC, found tDCS improved reaction time but not accuracy/error rate — a narrow and modest signal, weaker than the rTMS arm of the same analysis.
- **Clinical (separate, still modest):** Lefaucheur 2017 (PMID:28709880) evidence-based guidelines assigned at best **Level B (probable efficacy)** for anodal DLPFC tDCS in non-drug-resistant depression, fibromyalgia, and craving — and notably **probable inefficacy** for drug-resistant depression. No indication reached Level A. So even the clinical case is "probable," not "definite."
- **Why grade down:** small samples, heterogeneous montages/dosing, large inter-individual variability (the same montage can be excitatory or inhibitory across people), difficulty truly blinding sensation, and a documented file-drawer/replication problem. tACS oscillatory-entrainment effects are likewise small and parameter-sensitive.

Net: best-supported claim — clinical Level B for a few indications — rates **Emerging (2)**. Healthy-cognition enhancement is weaker still and explicitly contested.

## Safety & interactions (research metadata)
At conventional 1–2 mA research doses, common adverse effects are transient: tingling, itching, mild headache, scalp redness; rare chemical/skin burns occur under poorly prepared electrodes. Caution with implanted cranial metal/electronics near electrodes and with broken scalp skin. No established systemic drug interactions. Notably, safety of unsupervised consumer/DIY rigs (higher currents, poor electrode hygiene, off-label montages) is far less characterised. This is research metadata, not medical advice.

## Open questions
- Can multi-session, individually dosed protocols produce reliable cognitive benefit where single-session ones fail, or is the effect fundamentally small?
- How to handle inter-individual variability (current modelling, individualised dosing, responder prediction)?
- Are tACS entrainment effects genuine oscillatory control or low-level artefacts/expectancy?
- How much of reported benefit survives rigorous active-sham blinding and pre-registration?
