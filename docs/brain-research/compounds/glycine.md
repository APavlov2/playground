---
id: glycine
name: Glycine
aliases: [Gly, aminoacetic acid, glycocoll]
type: compound
klass: Amino acid / NMDA co-agonist
status: draft
evidence_overall: 2
onset: "Sleep effect acute (~3 g taken before bed acts the same night, core-temp/sleep-latency changes within ~1 h); NMDA co-agonist/psychiatric effects studied over weeks of chronic high-dose dosing"
half_life: "Plasma ~0.5-4 h (rapidly cleared; freely metabolized and incorporated into protein/one-carbon pool); no meaningful accumulation"
dose_range: "Sleep: ~3 g before bedtime. NMDA/schizophrenia adjunct (research only): high-dose 0.4-0.8 g/kg/day (~30-60 g/day) in divided doses"
cognitive_domains: [sleep-quality, daytime-alertness, mental-fatigue, recognition-memory, processing-speed]
channels:
  - channel: glu
    mechanism: "Glycine is an obligatory co-agonist at the strychnine-insensitive glycine modulatory site (GlyB) of the NMDA receptor; raising synaptic glycine potentiates NMDA-receptor function. Basis of the schizophrenia-adjunct hypothesis. Direction is modulate (co-agonist that gates, rather than simply driving, NMDA current); net clinical effect on cognition in healthy people is unproven"
    evidence: 2
    population: impaired
    direction: modulate
  - channel: gaba
    mechanism: "Glycine is also the major fast inhibitory neurotransmitter at strychnine-sensitive glycine receptors (GlyR, Cl- channels) in spinal cord and brainstem (grouped here under the inhibitory/gaba channel as the nearest schema fit). Relevance to oral-supplement brain effects is uncertain; the mechanistic work on glycine's sleep action specifically excluded GlyR and implicated NMDA receptors instead"
    evidence: 1
    population: preclinical
    direction: modulate
  - channel: cbf
    mechanism: "Pre-clinical (rat) work shows the sleep-promoting and hypothermic effect of oral glycine is mediated by NMDA receptors in the suprachiasmatic-nucleus shell, driving peripheral (cutaneous) vasodilation, heat loss and a core-body-temperature drop that shortens sleep-onset latency. This is the proposed mechanism for the human bedtime-sleep finding. NOT classic regional cerebral-blood-flow enhancement, and demonstrated in animals only; graded low and population preclinical. (The glymphatic channel is deliberately not used: no human glymphatic data exist for glycine; the sleep effect is via thermoregulatory peripheral vasodilation/core-temp drop, not a demonstrated glymphatic action.)"
    evidence: 1
    population: preclinical
    direction: modulate
safety:
  contraindications: []
  interactions: ["clozapine: adjunctive high-dose glycine appears to lose/blunt its efficacy on negative symptoms when added to clozapine (proposed clozapine partial action at the NMDA glycine site); studied in schizophrenia trials, not a toxicity interaction"]
  notable_risks: ["very well tolerated; mild GI upset (nausea, soft stool) mainly at high gram-per-kg research doses", "high-dose data come from supervised schizophrenia trials and should not be self-dosed"]
sources:
  - "Yamadera et al., Sleep and Biological Rhythms, 2007;5:126-131 — DOI:10.1111/j.1479-8425.2007.00262.x (crossover RCT, 3 g bedtime; subjective sleep quality + PSG; not PubMed-indexed)"
  - "Inagawa et al., Sleep and Biological Rhythms, 2006;4:75-77 — DOI:10.1111/j.1479-8425.2006.00193.x (randomized double-blind crossover, 3 g bedtime; subjective morning feeling; not PubMed-indexed)"
  - "Bannai et al., Frontiers in Neurology, 2012;3:61 — PMID:22529837 / DOI:10.3389/fneur.2012.00061 (3 g bedtime in partially sleep-restricted healthy volunteers; reduced daytime fatigue/sleepiness)"
  - "Kawai et al., Neuropsychopharmacology, 2015;40(6):1405-1416 — PMID:25533534 / DOI:10.1038/npp.2014.326 (rat mechanism: sleep-promoting & hypothermic effects via NMDA receptors in the SCN, peripheral vasodilation)"
  - "Javitt et al., Am J Psychiatry, 1994;151(8):1234-1236 — PMID:8037263 (double-blind RCT, glycine added to antipsychotics; improved negative symptoms)"
  - "Heresco-Levy et al., Arch Gen Psychiatry, 1999;56(1):29-36 — PMID:9892253 (double-blind placebo-controlled crossover, 0.8 g/kg/day; ~30% reduction in negative symptoms)"
  - "Potkin et al., Am J Psychiatry, 1999;156(1):145-147 — PMID:9892314 (high-dose glycine added to clozapine; no benefit on negative symptoms)"
  - "Evins et al., Am J Psychiatry, 2000;157(5):826-828 — PMID:10784481 (placebo-controlled glycine added to clozapine; no significant change)"
tags: [nootropic, sleep, amino-acid, nmda, glutamatergic]
---

## Summary
Glycine is the simplest amino acid, an endogenous metabolite that plays two pharmacologically distinct roles relevant to brain optimization, which should not be conflated. (1) **Sleep:** a single ~3 g dose before bed has, in small Japanese RCTs, improved subjective sleep quality, shortened sleep-onset latency, and improved next-day alertness and recognition memory in people with unsatisfactory sleep. (2) **NMDA co-agonist:** because glycine is an obligatory co-agonist at the NMDA-receptor glycine site, high-dose glycine (0.4-0.8 g/kg/day) has been tested as an adjunct in schizophrenia, with mixed results and a notable failure when combined with clozapine. The sleep evidence is consistent but rests on small studies (and the two foundational papers are not PubMed-indexed); the psychiatric evidence is mixed and pertains to an impaired population, not to enhancing healthy cognition. Glycine is generally very safe. Overall evidence for *brain optimization in healthy people* is graded **Moderate-low (2)** — promising sleep signal, small n, limited direct cognitive enhancement.

## Mechanism
**glu / NMDA co-agonist (modulate).** Glycine binds the strychnine-insensitive GlyB site of the NMDA receptor; NMDA channels require both glutamate and a co-agonist (glycine or D-serine) to open. Raising glycine availability can therefore potentiate NMDA-mediated transmission — the rationale for using it to counter the NMDA-hypofunction model of schizophrenia. Direction is **modulate**, since glycine gates rather than independently drives NMDA current, and the cognitive consequence in non-patients is unestablished.

**Sleep / thermoregulation (cbf, preclinical).** The mechanism of the human bedtime-sleep effect was worked out in rats (Kawai/Bannai group, PMID:25533534): oral glycine acts on NMDA receptors in the suprachiasmatic-nucleus shell, producing peripheral cutaneous vasodilation, heat loss, and a fall in core body temperature that promotes NREM sleep onset. The same work explicitly showed strychnine-sensitive glycine receptors (GlyR) were *not* responsible. This is why the sleep effect is mapped to a thermoregulatory/peripheral-vasodilation mechanism (cbf, graded low/preclinical) rather than to glymphatic clearance — there are no human glymphatic data for glycine.

**gaba / inhibitory GlyR.** Glycine is the principal fast inhibitory transmitter at spinal/brainstem GlyR (chloride channels); included for completeness as the nearest inhibitory-channel fit, but with low/preclinical grading because it is not the mechanism behind the oral-supplement brain effects.

## Evidence
Two separate literatures; keep them apart.

**Sleep (healthy / poor-sleepers, ~3 g):**
- Yamadera et al. 2007 (DOI:10.1111/j.1479-8425.2007.00262.x) — crossover RCT in volunteers with unsatisfactory sleep: 3 g glycine before bed improved subjective sleep quality and sleep efficacy, shortened polysomnographic latency to sleep onset and to slow-wave sleep without altering sleep architecture, and improved daytime sleepiness and a memory-recognition task. Small n; published in *Sleep and Biological Rhythms*, **not PubMed-indexed** (DOI only).
- Inagawa et al. 2006 (DOI:10.1111/j.1479-8425.2006.00193.x) — randomized double-blind crossover: 3 g before bed improved next-morning "fatigue," "liveliness/peppiness," and "clear-headedness." Small n; also **not PubMed-indexed**.
- Bannai et al. 2012 (PMID:22529837) — in partially sleep-restricted healthy volunteers, 3 g bedtime glycine reduced daytime sleepiness and fatigue versus placebo. PubMed-indexed; still modest n and largely subjective endpoints.

These are consistent and mechanistically coherent (PMID:25533534), but all small, mostly from one research group, and partly reliant on subjective scales — hence graded conservatively.

**NMDA co-agonist / schizophrenia adjunct (impaired population — mixed):**
- Javitt et al. 1994 (PMID:8037263) — double-blind RCT adding glycine to antipsychotics: significant improvement in negative symptoms.
- Heresco-Levy et al. 1999 (PMID:9892253) — double-blind placebo-controlled crossover, 0.8 g/kg/day for 6 weeks (n=22): ~30%±16% reduction in PANSS negative symptoms; low baseline serum glycine predicted response.
- Potkin et al. 1999 (PMID:9892314) and Evins et al. 2000 (PMID:10784481) — adding glycine to **clozapine** produced no benefit, the key negative/interaction signal. Larger later trials (e.g., the CONSIST trial) were also unimpressive, so the overall psychiatric picture is mixed. This evidence concerns symptom reduction in patients, not cognitive enhancement in healthy adults, and does not transfer to the optimization use-case.

Net: the relevant-to-optimization claim — 3 g at bedtime modestly improves sleep quality and next-day alertness in poor sleepers — rates **Moderate-low (2)** given small, partly non-indexed studies. The NMDA-adjunct literature is real but mixed and population-specific.

## Safety & interactions (research metadata)
Glycine is generally very safe and well tolerated; it is a normal dietary amino acid. At the ~3 g sleep dose adverse effects are minimal. High-dose research regimens (tens of grams/day) can cause mild GI upset (nausea, soft stools) and should only occur under supervision. No established contraindications at cognitive/sleep doses.

**Key interaction — clozapine:** adjunctive high-dose glycine loses or blunts its efficacy on schizophrenia negative symptoms when added to clozapine (PMID:9892314; PMID:10784481), the leading explanation being that clozapine already acts at/near the NMDA glycine site so additional glycine adds little. This is a pharmacodynamic efficacy interaction in the psychiatric context, not a toxicity interaction. This is research metadata, not medical advice.

## Open questions
- Are the bedtime-sleep benefits robust beyond the small, largely single-group, partly non-PubMed-indexed Japanese studies? Independent, larger, objective-endpoint RCTs are needed.
- Does the sleep benefit extend to healthy good-sleepers (enhancement) or is it confined to those with unsatisfactory/restricted sleep?
- Does next-day cognitive benefit (recognition memory, processing speed) reflect a direct nootropic action or simply better/recovered sleep? Current data favor the latter.
- Is the rat SCN-thermoregulation mechanism (PMID:25533534) the operative human mechanism, and does pre-bed core-temperature manipulation reproduce it?
- In the glutamatergic literature, why is the clozapine interaction so consistently null, and does it generalize to other strong NMDA-active agents? Relevance to healthy-cognition enhancement remains unproven.
