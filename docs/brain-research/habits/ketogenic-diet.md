---
id: ketogenic-diet
name: "Ketogenic diet / exogenous-ketone brain fuel"
aliases:
  - keto diet
  - ketosis
  - nutritional ketosis
  - exogenous ketones
  - MCT (medium-chain triglyceride)
  - ketone ester
  - modified Atkins diet
type: habit
klass: "Diet — metabolic (ketogenic)"
origin: natural                  # macronutrient pattern; ketones are endogenous metabolites (MCT/esters are food-derived)
source: "Dietary pattern (very-low-carbohydrate, high-fat) and food-derived ketogenic substrates (MCT oil, ketone esters/salts)"
status: draft
evidence_overall: 2
onset: "Nutritional ketosis within ~2-4 days of carbohydrate restriction; exogenous ketones/MCT raise blood BHB acutely (~30-90 min); cognitive endpoints assessed over weeks-months"
half_life: ""
dose_range: ""
cognitive_domains: [global-cognition, memory, executive-function, metabolic-resilience]
channels:
  - channel: mito
    mechanism: "Ketone bodies (BHB, acetoacetate) enter the brain via monocarboxylate transporters and are oxidised to acetyl-CoA, generating ATP independently of glucose uptake/glycolysis — bypassing the region-specific cerebral glucose hypometabolism that begins presymptomatically in aging and Alzheimer's. Provides an alternative fuel whose brain uptake is preserved in MCI/AD"
    evidence: 3
    population: impaired
    direction: up
  - channel: cbf
    mechanism: "Ketone uptake by the brain rises in proportion to blood ketone level via MCT-mediated transport; ketosis modestly increases cerebral metabolic substrate delivery/utilisation. Distinct from perfusion per se — graded cautiously"
    evidence: 2
    population: impaired
    direction: up
  - channel: inflam
    mechanism: "BHB inhibits the NLRP3 inflammasome and acts as an HDAC inhibitor altering antioxidant gene expression; ketosis reduces ROS production relative to glycolytic metabolism in preclinical models"
    evidence: 2
    population: preclinical
    direction: down
  - channel: glu
    mechanism: "Ketogenic metabolism shifts the glutamate/GABA balance (increased GABA synthesis, reduced glutamatergic excitotoxicity) — the established basis for ketogenic-diet efficacy in epilepsy; relevance to non-epileptic cognition is indirect"
    evidence: 2
    population: impaired
    direction: modulate
safety:
  contraindications:
    - "Inborn errors of fat metabolism (e.g. carnitine deficiencies, pyruvate carboxylase deficiency, porphyria)"
    - "Pancreatitis / severe hepatic disease"
    - "Type 1 diabetes without supervision (ketoacidosis risk)"
  interactions:
    - "SGLT2 inhibitors — combined euglycemic ketoacidosis risk"
    - "Insulin/sulfonylureas — dose adjustment needed; hypoglycaemia"
  notable_risks:
    - "'Keto flu' (fatigue, headache, electrolyte loss) during adaptation"
    - "Dyslipidemia (LDL rise in a subset), GI intolerance to MCT (dose-limiting diarrhea)"
    - "Long-term adherence is poor; restrictive pattern hard to sustain"
sources:
  - "Cunnane SC, et al. Brain energy rescue: an emerging therapeutic concept for neurodegenerative disorders of ageing. Nat Rev Drug Discov. 2020;19(9):609-633. PMID: 32709961. DOI: 10.1038/s41573-020-0072-x"
  - "Phillips MCL, et al. Randomized crossover trial of a modified ketogenic diet in Alzheimer's disease. Alzheimers Res Ther. 2021;13(1):51. PMID: 33622392. DOI: 10.1186/s13195-021-00783-x"
  - "de Cabo R, Mattson MP. Effects of Intermittent Fasting on Health, Aging, and Disease. N Engl J Med. 2019;381(26):2541-2551. PMID: 31881139. DOI: 10.1056/NEJMra1905136"
tags: [diet, ketones, bioenergetic, glucose-hypometabolism, alzheimers, mct]
---

## Summary
The ketogenic diet (very-low-carbohydrate, high-fat) and food-derived ketogenic substrates (MCT oil, ketone esters/salts) shift the brain toward burning ketone bodies — beta-hydroxybutyrate (BHB) and acetoacetate — instead of glucose. The compelling brain rationale is bioenergetic: cerebral glucose uptake declines region-specifically and presymptomatically in aging and Alzheimer's, but **ketone uptake by the brain remains intact in MCI/AD**, so ketones can partially "rescue" the energy deficit (Cunnane 2020). The strongest mechanistic case is therefore in the *impaired/at-risk aging* population, not healthy optimisers. Human cognitive evidence exists but is limited and mixed — small feasibility/crossover trials in AD/MCI and MCT-supplementation studies — so this is graded **Emerging-to-Good (overall 2)**: the mito/brain-fuel mechanism is well supported (3) where the glucose deficit exists, but the clinical cognitive payoff in RCTs is still small, short, and not consistently replicated.

## Mechanism
- **mito (primary, up — strongest in the impaired brain).** Ketones cross the blood-brain barrier via monocarboxylate transporters and feed directly into the TCA cycle as acetyl-CoA, producing ATP without needing glucose transport or glycolysis. This is the load-bearing mechanism: it sidesteps the cerebral glucose hypometabolism that is an early, possibly causal feature of AD. Cunnane 2020 (PMID 32709961) documents that brain ketone uptake is *unimpaired* in MCI/AD while glucose uptake is reduced ~20-30% — making ketones a rational "brain energy rescue." Graded **3**, population **impaired**, because the deficit it corrects is largely absent in healthy young brains (where the benefit drops toward 1-2).
- **cbf (up, cautious).** Brain ketone uptake scales with blood ketone concentration; ketosis raises the delivery and utilisation of an alternative substrate. This is substrate availability more than perfusion, so it is graded **2** and flagged as distinct from true vasoactive/perfusion effects.
- **inflam (down — preclinical-leaning).** BHB inhibits the NLRP3 inflammasome and acts as an endogenous HDAC inhibitor, upregulating antioxidant gene programs; ketone-based metabolism generates less ROS than glycolysis in models. Mostly preclinical; graded **2**.
- **glu (modulate).** Ketogenic metabolism increases GABA synthesis and reduces glutamatergic excitotoxic tone — the mechanistic basis of the diet's *established* efficacy in drug-resistant epilepsy. Its relevance to ordinary cognition is indirect; graded **2**, direction **modulate** (the goal is balance, not blanket up/down).

## Evidence
- **Brain-energy rationale.** Cunnane 2020 (PMID 32709961) is the anchor: a Nature Reviews Drug Discovery review establishing that AD features early, region-specific cerebral glucose hypometabolism while ketone metabolism is preserved, and that ketogenic interventions (diet, MCT, esters) raise brain ketone uptake and improve some bioenergetic and cognitive measures in MCI. This makes the *mechanism* a solid 3 in the impaired population — it is the clinical translation that is thinner.
- **Ketogenic diet in AD — feasibility/crossover.** Phillips 2021 (PMID 33622392), a randomized crossover trial of a modified ketogenic diet in clinically diagnosed AD, showed the diet was feasible, safe and tolerable over 12 weeks and reported improvements in daily function and quality of life versus a usual-diet comparator. Important caveats: small sample, short duration, crossover design, and modest/secondary cognitive signals — supportive but not definitive efficacy.
- **MCT / exogenous ketone studies.** A body of small trials (MCT supplements, ketone drinks; e.g. the BENEFIC-type kMCT studies referenced in Cunnane's work) show acute and sub-chronic improvements on some cognitive measures in MCI, often dose-dependent with achieved ketonemia, and often concentrated in APOE4-negative subgroups. These are small and heterogeneous; collectively **Emerging (2)**.
- **Healthy adults.** Direct evidence that ketogenic eating *enhances* cognition in healthy, metabolically normal adults is weak and confounded by the adaptation phase ("keto flu") and adherence difficulty. The strongest case remains deficit-correction in the aging/at-risk brain, not optimisation of a healthy one.

Net: best-supported, most relevant claim — ketones provide an alternative brain fuel that bypasses cerebral glucose hypometabolism and may benefit cognition in MCI/AD — rates the mechanism a **3 (impaired population)**, but because the clinical cognitive RCT evidence is small/short/mixed, the entry's `evidence_overall` badge is set to **2** to avoid overstating the translated benefit.

## Safety & interactions (research metadata)
Contraindicated in inborn errors of fat metabolism (carnitine/pyruvate-carboxylase deficiencies, porphyria), pancreatitis, severe hepatic disease, and unsupervised type 1 diabetes (ketoacidosis risk). Interacts dangerously with SGLT2 inhibitors (euglycemic ketoacidosis) and requires dose adjustment of insulin/sulfonylureas. Common effects: "keto flu" (fatigue, headache, electrolyte depletion) during adaptation, LDL elevation in a subset, and dose-limiting GI intolerance to MCT oil. Long-term adherence is poor — the restrictiveness of the pattern is itself a major limitation on any sustained brain benefit. This is research metadata, not medical advice.

## Open questions
- Does ketogenic intervention slow cognitive *decline* in MCI/AD in an adequately powered, long-duration RCT, or only improve short-term bioenergetic/function measures? Current trials are small and brief.
- Is the diet (with its restriction and weight loss) superior, equivalent, or inferior to exogenous ketones/MCT that deliver ketosis without carbohydrate restriction?
- Why does benefit appear concentrated in APOE4-negative individuals in several ketone studies, and what does that imply for who responds?
- Is there any cognitive benefit in healthy, metabolically normal adults, or is the effect confined to the glucose-hypometabolic aging brain?
- Long-term cardiovascular safety (LDL response heterogeneity) and adherence remain the practical ceilings on this lever.
