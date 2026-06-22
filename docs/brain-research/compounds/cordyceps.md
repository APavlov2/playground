---
id: cordyceps
name: Cordyceps
aliases:
  - "Cordyceps militaris"
  - "Ophiocordyceps sinensis"
  - "Cordyceps sinensis"
  - "Cs-4"
  - "cordycepin"
  - "3'-deoxyadenosine"
  - "caterpillar fungus"
  - "dong chong xia cao"
type: compound
klass: "medicinal fungus / nucleoside analog (cordycepin)"
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Cordyceps fungi (militaris / sinensis)"
status: draft
evidence_overall: 1
onset: "(unsourced) — anti-fatigue/ergogenic effects in trials assessed after 1–6 weeks of daily supplementation; acute single-dose cognitive onset not characterized"
half_life: "(unsourced for whole extract); cordycepin itself is rapidly deaminated by adenosine deaminase in plasma (short-lived) unless co-administered with a deaminase inhibitor — human PK poorly characterized"
dose_range: "Trial range 1–4 g/day fermented mycelium (Cs-4) or C. militaris extract, divided; no validated brain/cognition dose. Cordycepin content varies widely by product."
cognitive_domains:
  - "(unsourced) — no validated human cognitive-domain effects"
  - "fatigue/perceived exertion (indirect, exercise studies)"
channels:
  - channel: mito
    mechanism: "Promotes cellular energy/ATP production (ATP-generation pathway biomarkers; proposed PPAR-γ / mitochondrial-biogenesis involvement); associated anti-fatigue and aerobic-capacity effects in exercise studies — peripheral/muscle data, not brain-specific"
    evidence: 2
    population: healthy
    direction: up
  - channel: inflam
    mechanism: "Cordycepin reduces neuroinflammation and oxidative stress in rodent CNS injury/disease models — inhibits microglial pro-inflammatory polarization (NF-κB / Notch1), lowers brain oxidative markers, raises antioxidant enzymes; preclinical only"
    evidence: 2
    population: preclinical
    direction: down
safety:
  contraindications:
    - "Autoimmune conditions (theoretical immunostimulation; e.g. MS, SLE, RA)"
    - "Pre-surgical use (antiplatelet/bleeding signal) — discontinue ahead of surgery"
  interactions:
    - "Antiplatelet/anticoagulant agents (warfarin, aspirin) — plausible additive bleeding risk; C. militaris inhibits platelet aggregation (PMID:37970560)"
    - "Immunosuppressants (e.g. cyclosporine) — theoretical opposition via NK/T-cell modulation (limited human data)"
  notable_risks:
    - "Product quality/adulteration: wild vs cultivated differ substantially; surveys found corticosteroid-adulterated and unregistered products; label cordycepin content unreliable without third-party testing"
    - "Heavy-metal (e.g. arsenic) variation in wild material"
sources:
  - "PMID: 20804368 — Chen et al. Effect of Cs-4 (Cordyceps sinensis) on Exercise Performance in Healthy Older Subjects: A Double-Blind, Placebo-Controlled Trial. J Altern Complement Med. 2010. DOI: 10.1089/acm.2009.0226"
  - "PMID: 27408987 — Hirsch et al. Cordyceps militaris Improves Tolerance to High-Intensity Exercise After Acute and Chronic Supplementation. J Diet Suppl. 2017."
  - "PMID: 33312018 — Beneficial Effect of Cordyceps militaris on Exercise Performance via Promoting Cellular Energy Production. Mycobiology. 2020."
  - "PMID: 34130727 — Cordycepin confers long-term neuroprotection via inhibiting neutrophil infiltration and neuroinflammation after traumatic brain injury. J Neuroinflammation. 2021."
  - "PMID: 34334512 — The effect of cordycepin on brain oxidative stress and protein expression in streptozotocin-induced diabetic mice. J Vet Med Sci. 2021."
  - "PMID: 37970560 — Antithrombotic and Antiplatelet Effects of Cordyceps militaris. Mycobiology. 2020."
tags:
  - compound
  - fungus
  - cordycepin
  - anti-fatigue
  - ergogenic
  - preclinical-neuro
  - low-evidence
  - adulteration-risk
---

## Summary

Cordyceps (most studied as *Cordyceps militaris* and the fermented *Ophiocordyceps/Cordyceps sinensis* product Cs-4) is a medicinal fungus whose signature nucleoside, cordycepin (3'-deoxyadenosine), drives most of the proposed bioactivity. **The bulk of human data concern exercise, fatigue, and aerobic performance — not cognition — and even there results are mixed and come from small trials.** Brain/cognition evidence is essentially **preclinical** (rodent antioxidant, anti-neuroinflammatory, and neuroprotection models). For that reason, brain claims are graded **LOW (overall 1)**: there is a direct human-cognition evidence gap. The plausible CNS-relevant signals are (a) cellular-energy/anti-fatigue effects (channel **mito**, graded 2 from peripheral/exercise data) and (b) reduced neuroinflammation/oxidative stress (channel **inflam**, graded 2, preclinical only). Product quality is a serious caveat: wild-vs-cultivated differences, frequent adulteration/substitution, and occasional pharmaceutical adulterants. A possible antiplatelet/bleeding and immunostimulant interaction profile warrants caution.

## Mechanism

- **Cellular energy / ATP (mito):** In a mouse exercise-performance study, *C. militaris* ethyl-acetate extract influenced biomarkers of the **ATP-generation pathway** with little effect on muscle-fatigue biomarkers, suggesting performance benefit via increased ATP production rather than reduced fatigue per se; proposed involvement of PPAR-γ–controlled mitochondrial-biogenesis genes (PMID: 33312018). The Cs-4 human trial reported improved aerobic metabolism (VO2 and ventilatory-threshold measures) in older subjects (PMID: 20804368). These are peripheral/skeletal-muscle and whole-body energetics data; **direct brain bioenergetic effects in humans are (unsourced)**.
- **Anti-neuroinflammation / antioxidant (inflam):** Cordycepin reduces microglial pro-inflammatory polarization (NF-κB, Notch1 pathways), limits neutrophil infiltration, preserves blood-brain-barrier and white-matter integrity after traumatic brain injury in mice (PMID: 34130727), and lowers brain oxidative-stress markers while raising antioxidant enzyme activity, with improved object-recognition performance in streptozotocin-diabetic mice via AMPK/autophagy (ULK1) signaling (PMID: 34334512). **All CNS mechanism data here are rodent/in-vitro.**
- **Adenosine-analog identity:** Cordycepin is a structural analog of adenosine, which underlies both its broad signaling effects and its rapid plasma deamination — relevant to uncertain bioavailability.

## Evidence

**Human — exercise / fatigue / aerobic performance (mixed, small; NOT cognition):**
- Cs-4 (*C. sinensis*), 6 weeks, healthy older adults: significant increases in VO2max and metabolic/ventilatory threshold vs placebo (PMID: 20804368). Small n; effects modest and near threshold significance.
- *C. militaris*: acute and chronic supplementation improved tolerance to high-intensity exercise (PMID: 27408987). Small, short-duration.
- Across the literature, findings are **inconsistent** — some trials show ventilatory-threshold/VO2peak benefit, others (e.g., trained cyclists) show no significant change. Certainty is limited by small samples, heterogeneous protocols, weak randomization reporting, and lack of trial registration.

**Preclinical — brain/cognition (antioxidant / anti-neuroinflammatory / neuroprotective):**
- Cordycepin in mouse TBI: long-term neuroprotection via reduced neutrophil infiltration and neuroinflammation (PMID: 34130727).
- Cordycepin in streptozotocin-diabetic mice: reduced brain oxidative stress, improved recognition memory, AMPK/autophagy signaling (PMID: 34334512).
- Additional rodent/in-vitro reports describe anti-microglial-activation and anti-ischemic effects (consistent direction, same preclinical tier).

**Direct brain-cognition human evidence:** **(unsourced)** — no adequate randomized human trial of Cordyceps/cordycepin on cognition (memory, attention, executive function) was identified. This is the central limitation and the reason for the LOW overall grade.

## Safety & interactions

- **Product quality / adulteration:** Wild *O. sinensis* is rare and hard to cultivate, so substitution and adulteration are common; wild and cultivated material differ substantially (e.g., arsenic/heavy-metal profiles, polysaccharide and cordycepin content, absence of the insect-derived matrix in cultivated mycelium). Real-world surveys have found unregistered products and some adulterated with **corticosteroids**. Authenticity should ideally be confirmed by combined DNA and chemical analysis. Treat label cordycepin content as unreliable absent third-party testing.
- **Antiplatelet / bleeding (interactions):** *C. militaris* extract inhibits ADP- and collagen-induced platelet aggregation (antiplatelet, though without a clear anticoagulation effect in that assay) (PMID: 37970560); a case of excessive post-extraction bleeding in a daily user has been described (case report, "(unsourced)" beyond secondary reference). Plausible additive bleeding risk with warfarin, aspirin, other antiplatelet/anticoagulant agents — caution and provider awareness warranted.
- **Immunostimulant / autoimmune (interactions):** Cordyceps modulates NK- and T-cell activity; theoretical concern in autoimmune conditions (e.g., MS, SLE, RA) and possible opposition to immunosuppressants (e.g., cyclosporine after transplant). Human interaction data are limited/theoretical.

## Open questions

- No validated human cognitive endpoints — does any anti-fatigue or anti-neuroinflammatory signal translate to measurable cognition in humans? (currently **(unsourced)**)
- Human pharmacokinetics/bioavailability of cordycepin (rapid adenosine-deaminase deamination) and what oral dose, if any, reaches brain-relevant exposure.
- Whether *C. militaris* (higher cordycepin) vs fermented *C. sinensis* (Cs-4) differ meaningfully for any CNS endpoint.
- Standardized, third-party-verified products: which cordycepin/adenosine content corresponds to studied effects?
- Real-world bleeding and autoimmune interaction risk magnitude — beyond single case reports and mechanistic plausibility.
