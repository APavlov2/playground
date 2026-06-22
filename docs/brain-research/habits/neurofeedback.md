---
id: neurofeedback
name: EEG neurofeedback
aliases: [neurofeedback, EEG biofeedback, EEG-nf, neurotherapy, SMR training, slow cortical potential training]
type: habit
klass: "Device — neuromodulation"
origin: natural
source: "Device / neuromodulation — scalp EEG recording with real-time operant feedback of a brain signal"
status: draft
evidence_overall: 2
onset: "Training courses typically run dozens of sessions over weeks to months; any within-session learning is incremental"
half_life: "n/a (operant-learning modality; durability of any acquired self-regulation is itself uncertain)"
dose_range: ""
cognitive_domains: [attention, self-regulation, working-memory]
channels:
  - channel: ne
    mechanism: "Premise is operant conditioning of EEG features (e.g. SMR, theta/beta ratio, slow cortical potentials) tied to arousal/attention networks; any specific effect would act via noradrenergic/attentional regulation, but separation of specific from placebo signal is weak"
    evidence: 2
    population: both
    direction: modulate
safety:
  contraindications: []
  interactions: []
  notable_risks: [opportunity cost and expense of long multi-session courses, overstated marketing claims, weak blinding makes benefit attribution unreliable]
sources:
  - "Thibault & Raz, American Psychologist, 2017 — PMID:29016171 (argues placebo/psychosocial factors account for most neurofeedback outcomes; blinding critique)"
  - "Cortese et al., J Am Acad Child Adolesc Psychiatry, 2016 — PMID:27238063 (ADHD neurofeedback meta-analysis; effects vanish with probably-blinded raters and active/sham controls)"
tags: [device, neuromodulation, placebo-concern, emerging]
---

## Summary
EEG neurofeedback presents a person with real-time feedback of a feature of their own brain activity (a frequency band, a ratio, or slow cortical potentials) and rewards them for shifting it, on the premise that learned self-regulation yields cognitive or clinical benefit. The honest reading of the literature is that it is **weakly supported**: when trials use properly blinded outcome raters and active sham controls, apparent benefits largely disappear, and a substantial expert critique attributes most outcomes to placebo and other nonspecific factors. Far-transfer to real-world cognition is weak. Graded **down**.

## Mechanism
**ne (primary, modulate).** The proposed mechanism is operant conditioning of EEG signatures linked to arousal and attention — e.g. sensorimotor rhythm (SMR), theta/beta ratio, or slow cortical potentials — with the idea that successfully up- or down-regulating these biases noradrenergic/attentional state. The conceptual chain is coherent, but the critical problem is that studies rarely demonstrate that *learning to control the targeted signal* is necessary for any benefit. Because specific effects cannot be cleanly separated from nonspecific ones, this is graded **2 (emerging)** and `direction: modulate`, not higher. No other channel is graded — additional pathways are speculative.

## Evidence
The central issue is blinding and placebo, and the data should be graded down explicitly for it.

- **Blinding/placebo critique:** Thibault & Raz 2017 (PMID:29016171), in *American Psychologist*, argue that placebo and psychosocial factors (expectation, motivation, therapist contact, time-on-task) plausibly account for the majority of neurofeedback findings, because few experiments isolate "receiving feedback from a specific brain signal" as the necessary ingredient. Sham-feedback often works about as well as "real" feedback.
- **ADHD (the most-studied indication):** Cortese et al. 2016 (PMID:27238063), a meta-analysis of RCTs, found significant effects on ADHD symptoms only when rated by the **least-blinded** assessors closest to treatment; effects were **not significant** with probably-blinded ratings or in trials with active/sham controls. This is the canonical demonstration that the benefit tracks observer bias, not a specific neurophysiological effect — the main reason for grading down.
- **Far-transfer:** evidence that any trained self-regulation generalises to durable, real-world cognitive improvement (rather than to the trained task or rater impressions) is weak.
- **Counter-arguments exist:** proponents note that some trials fail because participants never actually learn to self-modulate (a "learning failure" rather than a true null), and that better-designed learning-verified trials are needed. That defence does not currently lift the graded evidence above emerging.

Net: best-supported relevant claim rates **Emerging (2)** at most, with explicit down-grading for blinding/placebo confounds and weak far-transfer.

## Safety & interactions (research metadata)
Physically low-risk (passive EEG recording; no current delivered in standard protocols). The salient harms are non-physical: substantial time and financial cost of long multi-session courses, and the risk of overstated commercial claims displacing better-evidenced interventions. No drug interactions. This is research metadata, not medical advice.

## Open questions
- Do learning-verified, double-blind, active-sham trials show any specific effect beyond placebo? This is the field's decisive open question.
- Is there a subgroup or indication where specific neurofeedback effects are real and clinically meaningful?
- Can any trained self-regulation produce durable far-transfer rather than task- or rater-bound gains?
- Which EEG targets, if any, are mechanistically valid rather than convenient?
