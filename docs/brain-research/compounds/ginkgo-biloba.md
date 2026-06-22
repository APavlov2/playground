---
id: ginkgo-biloba
name: Ginkgo biloba (EGb 761)
aliases: [ginkgo, EGb 761, EGb761, Tanakan, Tebonin, ginkgo leaf extract]
type: compound
klass: Botanical vasoactive/antioxidant
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Ginkgo biloba leaf (EGb 761 standardized extract)"
status: draft
evidence_overall: 2
onset: "weeks to months (cumulative); dementia-treatment trials assess outcomes at ~22-26 weeks. No reliable acute cognitive effect in healthy adults."
half_life: "Terpene lactones: ginkgolide A ~4-5 h, ginkgolide B ~6-7 h, bilobalide ~3 h (single-dose PK of EGb 761 constituents). Whole-extract effect is multi-constituent; no single governing half-life (largely approximate)."
dose_range: "120-240 mg/day standardized extract EGb 761 (typically 120 mg twice daily). Dementia-treatment benefit, where present, concentrates at 240 mg/day."
cognitive_domains: [memory, global-function, activities-of-daily-living, attention, neuropsychiatric-symptoms]
channels:
  - channel: cbf
    mechanism: "Primary putative mechanism. Vasoactive/hemorheologic effects attributed to terpene trilactones (ginkgolides, bilobalide) and flavonol glycosides: ginkgolide B is a platelet-activating-factor (PAF) antagonist, with reported increases in microcirculation and reduced blood viscosity. Cerebral-perfusion changes are documented mechanistically, but the cognition read-through is graded down: the two large dementia-PREVENTION RCTs (GEM, GuidAge) were null, so improved CBF does not translate into prevention of cognitive decline."
    evidence: 2
    population: impaired
    direction: modulate
  - channel: inflam
    mechanism: "Antioxidant / free-radical scavenging and anti-inflammatory activity of flavonoid glycosides (quercetin, kaempferol) and terpenoids; reduction of oxidative stress and mitochondrial-protective effects reported. Predominantly preclinical / mechanistic; not established as the basis of any human cognitive benefit."
    evidence: 1
    population: preclinical
    direction: modulate
  - channel: ach
    mechanism: "Possible cholinergic modulation (increased hippocampal acetylcholine release, muscarinic/nicotinic receptor effects) reported in rodent models. No human confirmation; speculative for the cognitive signal."
    evidence: 1
    population: preclinical
    direction: up
safety:
  contraindications:
    - "Known hypersensitivity to Ginkgo biloba"
    - "Peri-operative period — discontinue ~1-2 weeks before surgery due to bleeding risk (practice guidance)"
    - "Active bleeding disorder or significant bleeding risk (relative)"
  interactions:
    - "Anticoagulants / antiplatelets (warfarin, DOACs, aspirin, clopidogrel) — additive bleeding risk via PAF antagonism / antiplatelet effect; key safety item, case reports of bleeding (spontaneous hyphema, subdural/intracerebral hematoma)"
    - "Antiplatelet herbals/supplements (fish oil, vitamin E, garlic) — additive bleeding-risk theory"
    - "Possible lowering of seizure threshold — caution with anticonvulsant therapy / epilepsy; contamination with ginkgotoxin (4'-O-methylpyridoxine) implicated"
    - "CYP/transporter interactions (e.g., efavirenz, omeprazole, some statins) reported in vitro / limited clinical — generally modest"
  notable_risks:
    - "Bleeding events (case-report level; large RCTs did not show a clear excess of major hemorrhage, but signal exists for hemorrhagic stroke)"
    - "Seizure threshold lowering / reports of seizures, attributed to ginkgotoxin in seed/leaf material"
    - "Mild GI upset, headache, dizziness, allergic skin reactions"
sources:
  - "DeKosky ST et al. (GEM Study), JAMA, 2008 — PMID:19017911 (DOI:10.1001/jama.2008.683) — large dementia-PREVENTION RCT, NULL"
  - "Vellas B et al. (GuidAge), Lancet Neurol, 2012 — PMID:22959217 (DOI:10.1016/S1474-4422(12)70206-5) — large Alzheimer-PREVENTION RCT, NULL"
  - "Gauthier S, Schlaefke S, Clin Interv Aging, 2014 — PMID:25506211 (DOI:10.2147/CIA.S72728) — meta-analysis, dementia treatment, benefit at 240 mg/day"
  - "Tan MS et al., J Alzheimers Dis, 2015 — PMID:25114079 (DOI:10.3233/JAD-140837) — systematic review/meta-analysis, EGb761 240 mg/day favourable for cognition/ADL"
  - "Birks J, Grimley Evans J, Cochrane Database Syst Rev, 2009 — PMID:19160216 (DOI:10.1002/14651858.CD003120.pub3) — evidence inconsistent/unreliable for dementia & cognitive impairment"
  - "Laws KR et al., Hum Psychopharmacol, 2012 — PMID:23001963 (DOI:10.1002/hup.2259) — meta-analysis, NO cognitive enhancement in healthy individuals"
tags: [nootropic, botanical, vasoactive, antioxidant, dementia, bleeding-risk]
---

## Summary
Ginkgo biloba (standardized extract EGb 761) is one of the most heavily studied botanicals for cognition. The honest read of the literature is split by use case. For **dementia PREVENTION**, the two large, long-duration RCTs are **null**: the GEM Study (DeKosky 2008, JAMA — PMID:19017911) and GuidAge (Vellas 2012, Lancet Neurol — PMID:22959217) both failed to show reduced incidence of dementia or Alzheimer's disease. For **existing dementia / cognitive-impairment TREATMENT**, evidence is **mixed and modest**: several meta-analyses report statistically significant benefits in cognition, function (ADL), and global change, concentrated at **240 mg/day** (Gauthier & Schlaefke 2014 — PMID:25506211; Tan 2015 — PMID:25114079), while the Cochrane review judged the overall evidence **inconsistent and unreliable** (Birks & Grimley Evans 2009 — PMID:19160216). For **healthy-adult cognitive enhancement**, benefit is **largely unsupported** (Laws 2012 meta-analysis — PMID:23001963). The dominant safety concern is **bleeding-risk interaction with anticoagulants/antiplatelets**. Graded **2/4**: a defensible-but-modest treatment signal in dementia at 240 mg/day, undercut by two null prevention RCTs, a skeptical Cochrane verdict, and absent healthy-adult benefit.

## Mechanism
EGb 761 is a multi-constituent extract; its two pharmacologically defining classes are **terpene trilactones** (ginkgolides A/B/C and bilobalide) and **flavonol glycosides** (quercetin, kaempferol derivatives).
- **Cerebral blood flow (cbf) — primary putative mechanism:** ginkgolide B is a **platelet-activating-factor (PAF) antagonist**, and the extract is reported to improve microcirculation, reduce blood viscosity, and increase regional perfusion. This vasoactive/hemorheologic action is the textbook rationale, and it is also the mechanistic root of the bleeding interaction. Crucially, the cognition read-through is graded conservatively: improved perfusion did **not** prevent cognitive decline in the two large prevention RCTs.
- **Anti-inflammatory / antioxidant (inflam):** flavonoid and terpenoid constituents scavenge free radicals, reduce lipid peroxidation, and show mitochondrial-protective effects. This is predominantly **preclinical/mechanistic** and is not established as the basis of any human cognitive benefit.
- **Cholinergic (ach):** rodent data suggest enhanced hippocampal acetylcholine release and receptor modulation; there is **no human confirmation**, so this is speculative.

## Evidence
**Dementia / cognitive-decline PREVENTION — NULL (the honest headline):**
- **DeKosky ST et al., GEM Study, JAMA 2008 — PMID:19017911 (DOI:10.1001/jama.2008.683):** Randomized, double-blind, placebo-controlled trial of EGb 761 120 mg twice daily in **3,069** community-dwelling adults aged ≥75 with normal cognition or MCI, median ~6 years follow-up. Ginkgo was **not effective** in reducing the overall incidence of dementia or Alzheimer's disease (hazard ratio ~1.12, not significant). Definitive null result for primary prevention.
- **Vellas B et al., GuidAge, Lancet Neurol 2012 — PMID:22959217 (DOI:10.1016/S1474-4422(12)70206-5):** Randomized, placebo-controlled trial of EGb 761 120 mg twice daily in **2,854** adults ≥70 with memory complaints, 5-year primary analysis. Conversion to Alzheimer's disease did **not differ** from placebo (HR 0.84, 95% CI 0.60-1.18; p=0.306). Second large null prevention trial, consistent with GEM.

**Existing dementia / cognitive-impairment TREATMENT — MIXED / MODEST:**
- **Gauthier S, Schlaefke S, Clin Interv Aging 2014 — PMID:25506211 (DOI:10.2147/CIA.S72728):** Meta-analysis of randomized placebo-controlled trials; EGb 761 showed statistically significant benefit on cognition, ADL, and global clinical impression, with effects concentrated at **240 mg/day** and good tolerability, especially in patients with neuropsychiatric symptoms.
- **Tan MS et al., J Alzheimers Dis 2015 — PMID:25114079 (DOI:10.3233/JAD-140837):** Systematic review/meta-analysis; weighted mean difference favoured EGb 761 for **cognition** (WMD -2.86, 95% CI -3.18 to -2.54) and **ADL** (SMD -0.36), with benefits "mainly associated with EGb761 at a dose of 240 mg/day." Stabilization/slowed decline at 22-26 weeks.
- **Birks J, Grimley Evans J, Cochrane Database Syst Rev 2009 — PMID:19160216 (DOI:10.1002/14651858.CD003120.pub3):** The skeptical counterweight — concluded the evidence that ginkgo has predictable, clinically significant benefit for dementia or cognitive impairment is **inconsistent and unreliable**, citing heterogeneity and older positive trials not reproduced by the large recent RCT (GEM). This is why treatment is graded mixed rather than positive.

**Healthy-adult cognitive enhancement — LARGELY UNSUPPORTED:**
- **Laws KR et al., Hum Psychopharmacol 2012 — PMID:23001963 (DOI:10.1002/hup.2259):** Meta-analysis across memory, executive function, and attention domains in healthy individuals found **no ascertainable positive effect** on any targeted cognitive function; effect sizes essentially zero. Consistent with earlier "not a smart drug" reviews. No robust acute or chronic nootropic benefit in healthy people.

**Interpretation:** the strongest claim that survives scrutiny is a **modest treatment effect in established dementia at 240 mg/day** (multiple meta-analyses), heavily qualified by the Cochrane "inconsistent/unreliable" verdict. Prevention is null and healthy enhancement is unsupported. Net 2/4.

## Safety & interactions (research metadata)
- **Bleeding / anticoagulants (key safety item):** via PAF antagonism and antiplatelet activity, ginkgo carries a theoretical and case-report-documented bleeding risk. Co-use with **warfarin, DOACs, aspirin, clopidogrel**, or other antiplatelet agents/supplements may be additive; case reports include hyphema and subdural/intracerebral hemorrhage. Notably, the large prevention RCTs did not demonstrate a clear excess of major hemorrhage overall, though a hemorrhagic-stroke signal has been discussed — so the interaction is best treated as a **precaution**, strongest at the individual/perioperative level. Common guidance is to **stop ~1-2 weeks before surgery**.
- **Seizure threshold:** reports of lowered seizure threshold and seizures, attributed to **ginkgotoxin (4'-O-methylpyridoxine)** contamination (higher in seeds, present in leaf material); caution in epilepsy or with anticonvulsants.
- **Other:** generally well tolerated; mild GI upset, headache, dizziness, and allergic skin reactions are the usual adverse effects. Possible modest CYP/transporter interactions reported in vitro and in limited clinical studies.

## Open questions
- Why does documented cbf/perfusion modulation fail to translate into dementia prevention (GEM, GuidAge null)? Is the vasoactive mechanism simply insufficient, or mistimed (too late, wrong population)?
- Is the 240 mg/day treatment signal a genuine class effect or an artifact of heterogeneity and older, smaller, industry-associated trials (per Cochrane)? A definitive modern large treatment RCT at 240 mg/day is lacking.
- Real-world magnitude and clinical significance of the anticoagulant bleeding interaction, given that large RCTs did not show a clear major-hemorrhage excess — individual susceptibility vs. population risk remains unresolved.
- Whether any subgroup (e.g., dementia with prominent neuropsychiatric symptoms) derives reproducible benefit.
- Human confirmation (or refutation) of the preclinical cholinergic and antioxidant/mitochondrial mechanisms at standard doses; currently no human biomarker linkage to cognition.
