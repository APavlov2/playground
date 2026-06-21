---
id: apigenin
name: Apigenin
aliases:
  - "4',5,7-trihydroxyflavone"
  - apigenine
  - chamomile flavone
type: compound
klass: flavonoid (flavone aglycone)
status: draft
evidence_overall: 1
onset: "not established for isolated apigenin in humans (unsourced); preclinical anxiolytic effects acute (i.p. dosing in rodents, PMID 7617761), neurogenesis/BDNF effects over ~10+ days of dosing in mice (PMID 37101380)"
half_life: "human pharmacokinetics of isolated oral apigenin poorly characterized; absorption is low and the aglycone is rapidly conjugated/metabolized (unsourced for a precise human half-life)"
dose_range: "no validated human cognitive/anxiety dose for isolated apigenin (unsourced). Rodent anxiolytic doses ~3 mg/kg i.p. in mice (PMID 7617761); supplement market doses (~50 mg) are extrapolated, not trial-validated"
cognitive_domains:
  - anxiety / affect (preclinical only)
  - memory (preclinical, disease/kindling models only)
channels:
  - channel: gaba
    mechanism: "Competitive ligand at the central benzodiazepine (BZD) site of the GABA-A receptor (inhibits flunitrazepam binding, Ki ~4 uM); behaves as a weak partial/low-efficacy modulator with anxiolytic and slight sedative but not anticonvulsant or myorelaxant effects in mice. Profile is complex and species-dependent (anxiolytic in mice; inverse-agonist-like/sedative in some rat work). Preclinical only."
    evidence: 2
    population: preclinical
    direction: modulate
  - channel: inflam
    mechanism: "Antioxidant and anti-neuroinflammatory actions in cell and rodent models: scavenges ROS, inhibits NF-kB activation, lowers pro-inflammatory cytokines, attenuates microglial activation, downregulates NLRP3/iNOS/COX-2. No human brain confirmation. Preclinical only."
    evidence: 2
    population: preclinical
    direction: down
  - channel: ntrophic
    mechanism: "Increases hippocampal BDNF/CREB signaling and reportedly potentiates BDNF-TrkB receptor signaling (direct apigenin-BDNF binding in vitro); increased hippocampal neurogenesis and improved memory in mice. All preclinical."
    evidence: 1
    population: preclinical
    direction: up
safety:
  contraindications:
    - "known hypersensitivity to apigenin or to Asteraceae/Compositae botanicals (chamomile, ragweed) as a practical source caution"
    - "pregnancy/lactation — avoid; insufficient human safety data and theoretical estrogenic/uterine activity (unsourced for clinical risk)"
  interactions:
    - "CNS depressants (benzodiazepines, Z-drugs, alcohol, barbiturates, sedating antihistamines) — theoretical additive sedation via BZD-site/GABA-A activity (mechanism preclinical, PMID 7617761; human magnitude unsourced)"
    - "flumazenil — may antagonize the BZD-site component of apigenin's GABA-A effect (preclinical, PMID 7617761)"
    - "CYP3A4 / CYP2C9 / CYP1A2 substrates — apigenin inhibits these enzymes in vitro and could raise levels of co-administered drugs (PMID 27933871, PMID 30301254); clinical relevance unsourced"
    - "drugs with narrow therapeutic index metabolized hepatically — caution by extension of CYP inhibition above (unsourced for clinical events)"
  notable_risks:
    - "sedation / drowsiness — plausible from GABA-A BZD-site activity, but documented in rodents not in controlled human trials of isolated apigenin (unsourced)"
    - "estrogenic activity — apigenin is a phytoestrogen in vitro; theoretical concern in hormone-sensitive conditions (unsourced for clinical effect)"
    - "thyroid — flavonoids as a class can inhibit thyroid peroxidase; not specifically established for apigenin in humans (unsourced)"
    - "isolated-apigenin human safety database is essentially empty; most human exposure data come from whole chamomile/dietary matrices, not the purified compound (unsourced)"
sources:
  - "Viola H, et al. Apigenin, a component of Matricaria recutita flowers, is a central benzodiazepine receptors-ligand with anxiolytic effects. Planta Med. 1995;61(3):213-216. PMID: 7617761. DOI: 10.1055/s-2006-958058"
  - "Gao L, et al. The neurotrophic activities of brain-derived neurotrophic factor are potentiated by binding with apigenin, a common flavone in vegetables, in stimulating the receptor signaling. CNS Neurosci Ther. 2023;29(10):2787-2799. PMID: 37101380. DOI: 10.1111/cns.14230"
  - "Sharma P, et al. Apigenin reverses behavioural impairments and cognitive decline in kindled mice via CREB-BDNF upregulation in the hippocampus. Nutr Neurosci. 2020;23(2):118-127. PMID: 29847220. DOI: 10.1080/1028415X.2018.1478653"
  - "Studies on Apigenin and Its Biological and Pharmacological Activity in Brain Disorders. Adv Pharm Bull. 2022;12(4):645-648. PMID: 36415642. DOI: 10.34172/apb.2022.068"
  - "Exploring the Role of Apigenin in Neuroinflammation: Insights and Implications. Int J Mol Sci. 2024;25(9):5041. PMID: 38732259. DOI: 10.3390/ijms25095041"
  - "Zick SM, et al. Preliminary examination of the efficacy and safety of a standardized chamomile extract for chronic primary insomnia: a randomized placebo-controlled pilot study. BMC Complement Altern Med. 2011;11:78. PMID: 21939549. DOI: 10.1186/1472-6882-11-78 (chamomile matrix, NOT isolated apigenin)"
  - "Quintieri L, et al. Flavonoids diosmetin and luteolin inhibit midazolam metabolism by human liver microsomes and recombinant CYP3A4 — context for apigenin CYP3A4 inhibition. (CYP3A4 flavonoid inhibition) PMID: 30301254. DOI: 10.3390/molecules23102553"
  - "Apigenin inhibits the cytochrome P450 monooxygenase branch of the arachidonic acid cascade (CYP4F2 / 20-HETE). J Agric Food Chem. 2016. PMID: 27933871. DOI: 10.1021/acs.jafc.6b04501"
tags:
  - flavonoid
  - flavone
  - gaba-a-bzd-site
  - anxiolytic-candidate
  - anti-inflammatory
  - preclinical
  - low-evidence
  - draft
---

## Summary

Apigenin is a dietary flavone (flavonoid aglycone) found in chamomile,
parsley, celery, and other plants. Its plausible brain mechanisms are
biologically interesting but the human evidence base for **isolated** apigenin
as a cognitive or anxiolytic agent is **essentially absent**. Overall grade is
**1 (LOW)**: nearly all neuro-relevant data are **preclinical** (cell culture
and rodent), and the most-cited human "apigenin" data actually come from whole
**chamomile** preparations — a confounded, multi-constituent matrix that cannot
be attributed to apigenin.

Three preclinical signals are reasonably reproducible: (1) **gaba** — apigenin
binds the benzodiazepine site of the GABA-A receptor as a weak/partial
modulator with anxiolytic-like effects in mice (PMID 7617761); (2) **inflam** —
antioxidant and anti-neuroinflammatory actions (NF-kB/NLRP3 inhibition, reduced
microglial activation) in models (PMID 38732259, PMID 36415642); and
(3) **ntrophic** — increased hippocampal BDNF/CREB signaling and neurogenesis
in mice (PMID 37101380, PMID 29847220). None has been demonstrated for purified
apigenin in a human RCT. Treat all clinical claims as unproven.

## Mechanism

- **gaba (BZD-site partial modulator):** Apigenin competitively inhibits
  flunitrazepam binding at the central benzodiazepine site (Ki ~4 uM) and
  produces anxiolytic and slight sedative effects in mice without anticonvulsant
  or myorelaxant action — a low-efficacy/partial profile distinct from classical
  full BZD agonists (PMID 7617761). The pharmacology is **complex and
  species-dependent**: in some rat studies apigenin behaves more like an inverse
  agonist (sedative, mildly proconvulsant, not anxiolytic), and both
  flumazenil-sensitive and -insensitive components have been reported. Preclinical.
- **inflam (antioxidant / anti-neuroinflammatory):** In vitro and in rodents,
  apigenin scavenges ROS and inhibits NF-kB, lowering pro-inflammatory cytokines,
  microglial activation, NLRP3 inflammasome, iNOS and COX-2 (PMID 38732259,
  PMID 36415642). Mechanistically the most broadly documented action, but at
  exposures human oral dosing may not reach. Preclinical.
- **ntrophic (BDNF/CREB, neurogenesis):** Apigenin raises hippocampal BDNF and
  CREB phosphorylation and reportedly binds BDNF directly to potentiate
  TrkB-receptor signaling, increasing neurogenesis and memory in mice
  (PMID 37101380, PMID 29847220). Preclinical; lowest channel grade because the
  effect is the least mechanistically settled and entirely animal-based.

## Evidence

**GABA-A / anxiolytic (preclinical).** Viola et al. 1995 is the foundational
work: apigenin isolated from *Matricaria recutita* competitively inhibited
flunitrazepam binding (Ki ~4 uM) and was anxiolytic in the mouse elevated
plus-maze at ~3 mg/kg i.p., without sedation/myorelaxation at BZD-comparable
doses and without anticonvulsant activity (PMID 7617761). Subsequent work
showed the GABA-A interaction is complex and not uniformly anxiolytic across
species/doses. All animal; no isolated-apigenin human anxiety RCT exists
**(unsourced)**.

**Neuroinflammation / antioxidant (preclinical).** Reviews compile numerous
cell and rodent studies of apigenin attenuating neuroinflammation via
NF-kB/NLRP3 inhibition, reduced microglial activation, and Nrf2-linked
antioxidant signaling across models of neurodegeneration, epilepsy, and
depression (PMID 38732259; PMID 36415642). These are mechanistic/disease-model
data, not human cognition outcomes.

**BDNF / neurogenesis (preclinical).** Gao et al. 2023 report direct
apigenin-BDNF binding (ultrafiltration/Biacore) that potentiates TrkB
autophosphorylation and BDNF-induced neurogenesis in cultured neurons; in
normal mice ~25 mg/kg for 10 days improved memory and increased hippocampal
neurogenesis (PMID 37101380). Sharma et al. 2020 found apigenin reversed
cognitive decline in kindled mice with hippocampal CREB-BDNF upregulation
(PMID 29847220). Both are rodent/disease-model studies.

**The chamomile confound (key honesty point).** The human trials people cite
for "apigenin" actually test **chamomile extract**, a multi-constituent matrix.
Zick et al. 2011 (chronic primary insomnia, standardized chamomile extract
270 mg twice daily) was a small pilot with no significant sleep efficacy and
explicitly tested chamomile, **not isolated apigenin** (PMID 21939549). Any
effect cannot be attributed to apigenin specifically, and apigenin content of
such extracts is low. Chamomile anxiety/sleep trials are therefore **not**
evidence for the isolated compound.

**Isolated-apigenin human cognition/anxiety RCT evidence: ABSENT
(unsourced).** No identified randomized controlled trial tests purified
apigenin for cognition or anxiety in humans. This gap is the central reason for
the overall grade of 1.

## Safety & interactions

- **Additive sedation (CNS depressants):** Given BZD-site/GABA-A activity, there
  is a theoretical additive sedative interaction with benzodiazepines, Z-drugs,
  alcohol, barbiturates, and sedating antihistamines (mechanism preclinical,
  PMID 7617761; human magnitude **unsourced**). Flumazenil may blunt the
  BZD-site component.
- **CYP inhibition:** Apigenin inhibits CYP1A2, CYP2C9, and CYP3A4 in vitro
  (PMID 30301254) and the CYP4F2/20-HETE pathway (PMID 27933871), so it could
  theoretically raise levels of hepatically metabolized co-medications, including
  narrow-therapeutic-index drugs; clinical drug-drug interaction events are
  **unsourced**.
- **Estrogenic activity:** Apigenin shows phytoestrogenic activity in vitro;
  caution is reasonable in hormone-sensitive conditions, though clinical effect
  is **unsourced**.
- **Thyroid:** Flavonoids as a class can inhibit thyroid peroxidase; not
  specifically demonstrated for apigenin in humans **(unsourced)**.
- **Source caution:** Avoid with Asteraceae/Compositae (chamomile, ragweed)
  hypersensitivity. Avoid in pregnancy/lactation pending data **(unsourced)**.
- **Overall:** The isolated-apigenin human safety database is essentially empty;
  most tolerability impressions derive from dietary/chamomile exposure, not the
  purified compound **(unsourced)**.

## Open questions

- Is there ANY randomized human trial of isolated apigenin for cognition or
  anxiety? Currently none identified — the headline gap.
- Does orally dosed apigenin reach brain concentrations near the uM-range needed
  for its GABA-A and anti-inflammatory effects, given low absorption and rapid
  conjugation? Human pharmacokinetics are poorly characterized **(unsourced)**.
- Is the GABA-A effect anxiolytic, sedative, or inverse-agonist-like in humans?
  Rodent data conflict by species and dose.
- Can chamomile trial signals be cleanly attributed to apigenin, or are they
  driven by other constituents (apigenin-7-glucoside, bisabolol, other flavones)?
- Are the in-vitro estrogenic, thyroid-peroxidase, and CYP-inhibition signals
  clinically meaningful at realistic supplement doses?
