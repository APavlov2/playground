---
id: time-restricted-eating
name: "Time-restricted eating / intermittent fasting"
aliases:
  - intermittent fasting
  - TRE
  - TRF
  - "16:8"
  - alternate-day fasting
  - intermittent metabolic switching
type: habit
klass: "Diet — fasting"
origin: natural                  # behavioral timing of food intake; nothing ingested
source: "Behavioral — dietary timing (compressed eating window / periodic energy restriction)"
status: draft
evidence_overall: 2
onset: "Metabolic switch to ketosis within ~12-36 h of fasting; any cognitive adaptations presumed over weeks-months (largely unquantified in humans)"
half_life: ""
dose_range: ""
cognitive_domains: [working-memory, mood, metabolic-resilience]
channels:
  - channel: mito
    mechanism: "Fasting depletes hepatic glycogen and triggers the glucose-to-ketone 'metabolic switch'; beta-hydroxybutyrate (BHB) is oxidised by neurons for ATP and signals stress-resistance pathways; fasting/CR stimulates mitochondrial biogenesis and autophagy/mitophagy in preclinical models"
    evidence: 2
    population: preclinical
    direction: up
  - channel: ntrophic
    mechanism: "BHB acts as a signalling molecule that induces BDNF expression; intermittent fasting/exercise raise hippocampal BDNF in rodents, linked to enhanced synaptic plasticity and neurogenesis. Robust preclinically; not yet demonstrated as a cognitive effect in human RCTs"
    evidence: 1
    population: preclinical
    direction: up
  - channel: inflam
    mechanism: "Periodic fasting lowers oxidative stress markers, activates autophagy (cellular waste/protein-aggregate clearance) and can shift inflammatory tone; BHB inhibits the NLRP3 inflammasome in preclinical work"
    evidence: 2
    population: both
    direction: down
  - channel: gaba
    mechanism: "Intermittent fasting reported to enhance GABAergic tone and reduce neuronal hyperexcitability in rodent models (proposed anxiolytic/seizure-protective route); no direct human cognitive confirmation"
    evidence: 1
    population: preclinical
    direction: up
safety:
  contraindications:
    - "History of eating disorder"
    - "Type 1 diabetes / insulin or sulfonylurea use (hypoglycaemia risk) without medical supervision"
    - "Pregnancy, lactation, underweight, frailty"
  interactions:
    - "Glucose-lowering medications — fasting amplifies hypoglycaemia risk"
    - "Medications requiring food co-administration"
  notable_risks:
    - "Transient irritability, headache, hunger, poor concentration during adaptation ('fasting fog')"
    - "Risk of disordered-eating reinforcement in susceptible individuals"
sources:
  - "de Cabo R, Mattson MP. Effects of Intermittent Fasting on Health, Aging, and Disease. N Engl J Med. 2019;381(26):2541-2551. PMID: 31881139. DOI: 10.1056/NEJMra1905136"
  - "Mattson MP, et al. Intermittent metabolic switching, neuroplasticity and brain health. Nat Rev Neurosci. 2018;19(2):63-80. PMID: 29321682. DOI: 10.1038/nrn.2017.156"
  - "Cunnane SC, et al. Brain energy rescue: an emerging therapeutic concept for neurodegenerative disorders of ageing. Nat Rev Drug Discov. 2020;19(9):609-633. PMID: 32709961. DOI: 10.1038/s41573-020-0072-x"
tags: [diet, fasting, ketones, autophagy, bdnf, preclinical-heavy]
---

## Summary
Time-restricted eating (TRE) and intermittent fasting (IF) compress food intake into a limited daily window (e.g. 16:8) or impose periodic energy restriction, triggering a metabolic switch from glucose to fat-derived ketones. The brain-health rationale is mechanistically attractive: ketone bodies (especially beta-hydroxybutyrate) fuel neurons and act as signalling molecules that induce BDNF, stimulate autophagy and mitochondrial biogenesis, and dampen inflammasome activity. **The honest grading caveat is central: almost all of the cognitive/neuroplasticity evidence is preclinical (rodent).** Human IF trials are numerous but overwhelmingly target weight and cardiometabolic endpoints, not cognition, and the few cognitive readouts are small, short and inconsistent. This entry is therefore graded **Emerging (2)** at best (for the metabolic/autophagy mechanism with strong preclinical support), with the neurotrophic claim graded **1 / preclinical**.

## Mechanism
- **mito (metabolic switch, up — but preclinical for cognition).** Once hepatic glycogen is depleted (~12-36 h fasting, faster with exercise), the body shifts to lipolysis and hepatic ketogenesis. BHB crosses into the brain via monocarboxylate transporters and is oxidised to acetyl-CoA, generating ATP independently of glycolysis. In animal models fasting/caloric restriction also upregulates mitochondrial biogenesis and mitophagy. The energetic logic is sound (Cunnane 2020, PMID 32709961), but a measurable *cognitive* dividend in healthy humans is not established.
- **ntrophic (BDNF, up — preclinical).** BHB is not merely fuel; it induces BDNF expression, and intermittent fasting raises hippocampal BDNF in rodents alongside improved learning and increased neurogenesis (Mattson 2018, PMID 29321682). This is the headline "fasting grows the brain" claim — and it is the one most aggressively graded down here: it rests on animal data and mechanistic plausibility, with **no human RCT** showing fasting-driven cognitive gain via BDNF. Graded **1**.
- **inflam (down).** Periodic fasting activates autophagy (clearance of damaged proteins/organelles), lowers oxidative-stress markers, and BHB inhibits the NLRP3 inflammasome preclinically. Some human IF trials do show reduced inflammatory and oxidative markers, so this channel earns a **2** (mixed/limited human data plus strong preclinical) rather than a 1.
- **gaba (up — preclinical).** Rodent work links IF to enhanced GABAergic tone and reduced network hyperexcitability (proposed anxiolytic and seizure-protective effects). No human cognitive confirmation; graded **1** and included for mechanistic completeness only.

## Evidence
- **Mechanistic / review backbone.** de Cabo & Mattson 2019 (PMID 31881139) and Mattson 2018 (PMID 29321682) lay out the "intermittent metabolic switching" framework — ketones as fuel and signal, BDNF induction, autophagy, stress resistance. These are authoritative *reviews of mechanism*, heavily weighted toward animal and cellular data, not demonstrations of human cognitive benefit. They must be read as hypothesis, not proof.
- **Human cognition data are thin.** The large human IF literature is dominated by weight-loss and cardiometabolic outcomes. Dedicated, adequately powered RCTs of IF/TRE with cognition as a primary endpoint in healthy adults are essentially absent; where cognitive measures appear they are secondary, small, short, and produce mixed or null results. During the adaptation phase some people report *worse* concentration ("fasting fog"). The brain-health case in humans is therefore promissory.
- **Brain-energy rationale (aging overlap).** Cunnane 2020 (PMID 32709961) supports the idea that supplying ketones can rescue an aging/AD brain's glucose-hypometabolism deficit — but that evidence comes mostly from *exogenous ketones / MCT* and ketogenic-diet studies (see ketogenic-diet entry), not from intermittent fasting per se. Borrowing it to justify IF specifically is a mechanistic extrapolation.

Net: best-supported, most relevant claim — IF/TRE drives a glucose-to-ketone metabolic switch with autophagy and anti-inflammatory effects that *plausibly* support brain resilience — rates **Emerging (2)**. The specific cognitive/BDNF brain-enhancement narrative is **preclinical (1)** in humans and should not be presented as established. Graded down deliberately per the brief.

## Safety & interactions (research metadata)
Contraindicated or requiring supervision in: history of eating disorder; insulin/sulfonylurea-treated or type 1 diabetes (hypoglycaemia); pregnancy/lactation; underweight or frail individuals. Glucose-lowering drugs interact with fasting to raise hypoglycaemia risk; some medications require food co-administration. Common transient effects during adaptation include irritability, headache, hunger and impaired concentration. A non-trivial behavioural risk is reinforcement of disordered eating in susceptible people. This is research metadata, not medical advice.

## Open questions
- Does any IF/TRE protocol produce a *measurable, replicated cognitive benefit* in humans, or is the brain story confined to rodents? This is the central gap.
- Is endogenous ketosis from fasting cognitively equivalent to exogenous ketones/MCT, or does the fasting state add (autophagy) or subtract (energy-availability, sleep disruption) on net?
- Optimal window/cadence (16:8 vs alternate-day vs 5:2) for any neural endpoint is entirely unresolved.
- How much of any benefit is fasting per se versus the weight loss and improved metabolic health it produces?
- Long-term effects on sleep, mood and HPA-axis tone are under-characterised and could cut against cognition.
