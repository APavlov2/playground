---
id: methylene-blue
name: Methylene blue (low-dose)
aliases:
  - methylthioninium chloride
  - "MB"
  - "USP methylene blue"
  - methylthioninium
type: compound
klass: mitochondrial electron cycler / redox antioxidant
status: draft
evidence_overall: 2
onset: "~1-2 h (oral; single-dose acute cognitive/fMRI effects)"
half_life: "~5-6.5 h (oral; variable)"
dose_range: "low-dose research range ~0.5-4 mg/kg oral; human fMRI study used a single 280 mg oral dose (~4 mg/kg). NOT the high IV doses (>5-7 mg/kg) used for methemoglobinemia, which are toxic/pro-oxidant."
cognitive_domains:
  - short-term memory
  - sustained attention / vigilance
  - memory retrieval
channels:
  - channel: mito
    mechanism: "Alternative electron carrier in the ETC: at low dose accepts electrons from NADH and donates to cytochrome c, bypassing complex I/III blockade; enhances cytochrome c oxidase activity and oxygen consumption (preclinical)."
    evidence: 2
    population: preclinical
    direction: up
  - channel: inflam
    mechanism: "Redox cycler / free-radical scavenger; reduces ROS and oxidative stress, with reported anti-neuroinflammatory effects (preclinical)."
    evidence: 1
    population: preclinical
    direction: down
  - channel: cbf
    mechanism: "Single human multimodal fMRI study reported increased task-evoked fMRI response (memory, vigilance) and altered functional connectivity; BOLD/CBF-coupled signal change, not a validated perfusion endpoint. Small n."
    evidence: 2
    population: healthy
    direction: modulate
safety:
  contraindications:
    - "G6PD deficiency (risk of hemolysis and worsening methemoglobinemia)"
    - "Concurrent serotonergic drugs (SSRIs, SNRIs, MAOIs, triptans, TCAs) due to MAO-A inhibition / serotonin syndrome risk"
    - "Pregnancy"
  interactions:
    - "SSRIs / SNRIs: serotonin syndrome (potent MAO-A inhibition)"
    - "MAOIs (phenelzine, tranylcypromine, selegiline): hard contraindication"
    - "Triptans, TCAs, bupropion, other serotonergic agents: serotonin toxicity risk"
  notable_risks:
    - "Serotonin syndrome (FDA black-box-level warning for serotonergic co-administration)"
    - "Hemolysis / methemoglobinemia in G6PD deficiency"
    - "Pro-oxidant and toxic at high doses (hormetic / narrow dosing window)"
    - "Blue-green discoloration of urine, stool, and possibly skin/mucosa"
    - "Research-grade item; product purity and dose precision concerns"
sources:
  - "Rodriguez P, et al. Multimodal Randomized Functional MR Imaging of the Effects of Methylene Blue in the Human Brain. Radiology. 2016;281(2):516-526. PMID: 27351678; DOI: 10.1148/radiol.2016152893"
  - "Rodriguez P, et al. Methylene blue modulates functional connectivity in the human brain. Brain Imaging Behav. 2017;11(3):640-648. PMID: 26961091; DOI: 10.1007/s11682-016-9541-6"
  - "Wen Y, et al. Alternative mitochondrial electron transfer as a novel strategy for neuroprotection. J Biol Chem. 2011;286(18):16504-16515. PMID: 21454572; DOI: 10.1074/jbc.M110.208447"
  - "Tucker D, et al. From Mitochondrial Function to Neuroprotection-an Emerging Role for Methylene Blue. Mol Neurobiol. 2018;55(6):5137-5153. PMID: 28840449; DOI: 10.1007/s12035-017-0712-2"
  - "Tatarinova O, et al. Beware of methylene blue in possible G6PD deficiency. Am J Hematol. 2024. PMID: 38606972; DOI: 10.1002/ajh.27324"
  - "Top WM, et al. Perioperative Diagnosis and Treatment of Serotonin Syndrome Following Administration of Methylene Blue. Am J Case Rep. 2016;17:347-351. PMID: 27210537"
tags:
  - research-grade
  - mitochondrial
  - antioxidant
  - MAO-A-inhibitor
  - serotonin-syndrome-risk
  - nootropic-candidate
---

## Summary

Methylene blue (methylthioninium) is a redox-active dye that, at **low doses**, acts as an alternative electron carrier in the mitochondrial electron transport chain and as an antioxidant/free-radical scavenger. Interest as a brain-optimization agent rests largely on a single small human study (Rodriguez 2016, n=26) reporting increased task-evoked fMRI response and a ~7% improvement in memory-retrieval accuracy after a single oral dose. The remainder of the neuro-cognitive evidence is **preclinical**. Graded modestly (evidence_overall 2): a plausible mechanism and one positive small human trial, but no replication and no durable healthy-cognition outcomes. Critically, methylene blue is a **potent MAO-A inhibitor** and carries a serotonin-syndrome warning; it is contraindicated in G6PD deficiency. It is best treated as a research-grade item, not a casual supplement, with strict attention to the low-dose window.

## Mechanism

- **Mitochondrial electron cycling (mito).** At low concentrations methylene blue is reduced to leucomethylene blue, accepting electrons from NADH and donating them to cytochrome c, effectively bypassing complex I/III blockade and supporting cytochrome c oxidase activity and cellular oxygen consumption (Wen 2011, PMID 21454572; Tucker 2018, PMID 28840449). This auto-oxidizing redox couple is the core proposed pro-bioenergetic mechanism.
- **Antioxidant / anti-inflammatory (inflam).** By cycling electrons and scavenging reactive oxygen species, low-dose methylene blue can reduce oxidative stress; preclinical models report attenuated neuroinflammation (Tucker 2018, PMID 28840449). Graded low — preclinical only.
- **MAO-A inhibition (safety mechanism, not a benefit channel).** Methylene blue potently inhibits monoamine oxidase A (in vitro Ki ~27 nM), which raises synaptic monoamines/serotonin. This is the basis of its serotonin-syndrome risk and is flagged here as a **safety mechanism**, not a graded cognitive channel.
- **Hormesis / dosing window.** Effects are biphasic: low doses are pro-oxidant-sparing and bioenergetic; high doses become pro-oxidant and toxic. The therapeutic window is narrow.

## Evidence

- **Human (small n).** Rodriguez 2016 (Radiology; PMID 27351678; DOI 10.1148/radiol.2016152893) was a randomized, double-blind, placebo-controlled multimodal fMRI study (n=26, ages 22-62, single oral dose ~280 mg). It reported increased fMRI response in the bilateral insular cortex during a psychomotor vigilance task, increased response in prefrontal/parietal/occipital cortex during a short-term memory task, and a ~7% increase in correct responses during memory retrieval. A companion analysis (Rodriguez 2017, Brain Imaging Behav; PMID 26961091; DOI 10.1007/s11682-016-9541-6) reported modulation of resting-state functional connectivity. These are acute, single-dose, small-sample findings without replication or durable-outcome data — hence the cbf/imaging channel is graded 2 and the overall grade is held at 2.
- **Preclinical.** Low-dose methylene blue improves mitochondrial respiration and is neuroprotective in cellular and rodent models (Wen 2011, PMID 21454572; Tucker 2018 review, PMID 28840449), including chronic cerebral hypoperfusion and neurodegeneration models. Translation of these effects to healthy human cognition is unproven.
- **Gaps.** No large RCTs of low-dose methylene blue for healthy cognitive enhancement; durable memory/attention benefits, dose-response in healthy people, and long-term safety are not established.

## Safety & interactions

- **Serotonin syndrome / MAOI interaction (primary risk).** Methylene blue is a potent MAO-A inhibitor; combined with SSRIs, SNRIs, MAOIs, triptans, TCAs, or other serotonergic agents it can precipitate serotonin syndrome. The FDA issued a drug-safety communication / black-box-level warning on this interaction, and case reports of perioperative serotonin syndrome are documented (Top 2016, PMID 27210537). Even low doses (<1 mg/kg) can produce clinically significant MAO inhibition. **Hard contraindication with irreversible MAOIs.**
- **G6PD deficiency (contraindicated).** Methylene blue depends on NADPH from the G6PD pathway; in G6PD-deficient individuals it can cause hemolysis and paradoxically worsen methemoglobinemia (Tatarinova 2024, PMID 38606972). Screen before use.
- **Dosing window.** Low-dose (~0.5-4 mg/kg) is the bioenergetic/antioxidant range; high doses (the IV doses used for methemoglobinemia, >5-7 mg/kg) are pro-oxidant and toxic. Dose precision matters; mis-dosing is a real hazard with research-grade material.
- **Urine/tissue discoloration.** Expect blue-green discoloration of urine and stool; possible skin/mucosal staining. Benign but can interfere with pulse oximetry and some lab assays.
- **Other.** Avoid in pregnancy. Product purity is a concern for non-pharmaceutical-grade material.

## Open questions

- Do the acute Rodriguez 2016 imaging/memory effects replicate in a larger, independent sample, and do they translate to durable cognitive benefit in healthy adults?
- What is the dose-response curve for cognitive endpoints in healthy people, and where exactly does benefit transition to pro-oxidant harm?
- Can the MAO-A-driven serotonin-syndrome risk be fully separated from the bioenergetic benefit at low doses, or is it intrinsic? (unsourced as to a definitive low-dose human threshold)
- Long-term safety and any chronic-dosing cognitive effect remain uncharacterized.
