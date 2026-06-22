---
id: psilocybin-microdosing
name: Psilocybin (microdosing)
aliases: [psilocybin microdose, "4-PO-DMT", psilocin (active metabolite), "magic mushroom microdose", "Psilocybe microdose", "sub-perceptual psilocybin"]
type: compound
klass: "Serotonergic (classic) psychedelic — tryptamine 5-HT2A agonist; sub-perceptual MICRODOSING regimen (distinct from macrodose/therapeutic dosing). Schedule I controlled substance."
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Psilocybe mushrooms; can also be synthesized"
status: draft
evidence_overall: 1  # MICRODOSING cognition. The best-controlled designs (self-blinding and double-blind placebo-controlled RCTs: Szigeti 2021 PMID:33648632; Cavanna/van Elk 2022 PMID:35918311) are essentially NULL vs placebo for cognitive enhancement, with reported benefits explained by EXPECTANCY/unblinding. Open-label/observational reports are positive but confounded. Graded 1 (lowest), leaning null. NOTE: this entry is microdosing-for-cognition ONLY — it does NOT grade macrodose psilocybin-assisted therapy for depression, which is a separate and stronger evidence base.
onset: "Microdose regimens are taken on an intermittent schedule (commonly every ~3rd day) rather than for an acute effect; doses are deliberately SUB-perceptual. Any acute pharmacological onset of psilocin is ~20-40 min after oral psilocybin, but the microdosing claim is about cumulative/sub-perceptual benefit, which controlled trials do not support."
half_life: "Psilocybin is a prodrug rapidly dephosphorylated to psilocin; psilocin plasma half-life ~1.5-3 h (subjective effects ~4-6 h at full doses). Half-life is for the active psilocin; sub-perceptual microdoses are below the threshold for typical subjective effects."
dose_range: "Typical self-reported microdose ~0.1-0.5 g dried Psilocybe mushroom (~roughly 1-3 mg psilocybin), about one-tenth of a full/'macro' dose, taken intermittently. Doses and potency are highly variable and unstandardized; 'macrodose' therapeutic studies use ~25 mg synthetic psilocybin and are a SEPARATE regimen not covered by this grade."
cognitive_domains: [creativity, attention, mood, well-being, processing-speed, executive-function]
channels:
  - channel: ser
    mechanism: "Primary pharmacology: psilocin is an agonist at serotonin 5-HT2A receptors (with activity at other 5-HT subtypes incl. 5-HT2C, 5-HT1A). 5-HT2A agonism is the established receptor mechanism for classic psychedelics. At MICRODOSES the question is whether sub-perceptual 5-HT2A engagement yields cognitive benefit — controlled human trials do not demonstrate a reliable cognitive effect over placebo, so the human cognitive-OUTCOME grade is low even though the receptor mechanism itself is well characterized."
    evidence: 2  # 5-HT2A agonism is a real, well-established mechanism (preclinical/pharmacological), but at microdose the human cognitive translation is largely null -> capped at 2
    population: healthy  # microdosing is studied predominantly in healthy adults seeking enhancement
    direction: modulate
  - channel: ntrophic
    mechanism: "Psychedelics act as 'psychoplastogens': 5-HT2A activation (incl. intracellular 5-HT2A) drives BDNF-TrkB and mTOR signaling and rapid/persistent dendritic spine growth in rodent frontal cortex (Shao 2021 PMID:34228959). CRITICAL caveat: these neuroplasticity signals are mostly ACUTE and PRECLINICAL, and largely demonstrated at full/MACRO doses, not at sub-perceptual human microdoses. Translation of a neuroplasticity signal into microdose cognitive enhancement in humans is unproven."
    evidence: 1  # neuroplasticity is acute/preclinical and mostly macrodose; microdose human translation unproven -> 1
    population: preclinical
    direction: up
safety:
  contraindications:
    - "Personal or family history of psychotic-spectrum disorders (schizophrenia, schizoaffective) or bipolar disorder: classic psychedelics are generally contraindicated due to risk of precipitating or worsening psychosis/mania (theoretical even at microdose; conservative exclusion in research)."
    - "Pregnancy and breastfeeding: insufficient safety data; avoided in research settings."
  interactions:
    - "Serotonergic agents (SSRIs/SNRIs/MAOIs, lithium, tramadol): theoretical additive serotonergic effect. MAOIs and especially lithium are flagged in the literature as higher-concern combinations with psychedelics (lithium associated with seizures/adverse events in case reports); SSRIs may blunt subjective effects via 5-HT2A downregulation. Quantitative microdose-specific interaction data are limited."
    - "Other 5-HT2A-active or serotonergic drugs and stimulants: theoretical additive/pharmacodynamic interactions; not well characterized at microdose."
  notable_risks:
    - "Legal: psilocybin is Schedule I in the United States (federal) and a controlled/illegal substance in most jurisdictions; possession and use are illegal in most places. This is a prominent legal-status flag, not legal advice."
    - "Cardiac valvulopathy (theoretical, chronic): 5-HT2B-receptor agonism is the mechanism linked to drug-induced valvular heart disease (as seen with fenfluramine/pergolide); classic psychedelics have 5-HT2B affinity, raising a THEORETICAL concern with frequent/chronic microdosing. Direct human evidence of valvulopathy from psilocybin microdosing is lacking; flagged as a plausibility-based risk."
    - "Psychiatric: possible anxiety, mood destabilization, or perceptual effects if a 'microdose' is unintentionally perceptual (potency is unstandardized); risk of precipitating psychosis/mania in susceptible individuals."
    - "Unstandardized product: mushroom potency varies widely, so 'sub-perceptual' dosing is unreliable; misidentification of wild mushrooms carries poisoning risk."
tags: [schedule-i, psychedelic, serotonergic, microdosing, 5-ht2a, null-or-placebo-flag, expectancy-confound, legal-status-flag]
sources:
  - "Szigeti B, Kartner L, Blemings A, Rosas F, Feilding A, Nutt DJ, Carhart-Harris RL, Erritzoe D — eLife, 2021 — PMID:33648632 DOI:10.7554/eLife.62878 (self-blinding citizen-science RCT, n=191 completers; microdosers improved on psychological outcomes but so did placebo group — NO significant between-group difference once blinding/expectancy modeled; benefits explained by placebo)"
  - "Cavanna F, Muller S, de la Fuente LA, Zamberlan F, Palmucci M, Janeckova L, Kuchar M, Pallavicini C, Tagliazucchi E — Transl Psychiatry, 2022 — PMID:35918311 DOI:10.1038/s41398-022-02039-0 (van Elk-affiliated double-blind placebo-controlled study, 0.5 g dried psilocybin mushrooms; no enhancement of well-being/creativity/cognition over placebo — a few small changes toward cognitive impairment; acute effects intense only in those who correctly guessed condition = expectancy/unblinding)"
  - "Polito V, Liknaitzky P — J Psychopharmacol, 2024 — PMID:38877715 DOI:10.1177/02698811241254831 (rapid review of 19 placebo-controlled low-dose LSD/psilocybin studies; concludes much of the reported microdosing benefit is consistent with a placebo explanation)"
  - "Bershad AK, Schepers ST, Bremmer MP, Lee R, de Wit H — Biol Psychiatry, 2019 — PMID:31331617 DOI:10.1016/j.biopsych.2019.05.019 (double-blind placebo-controlled LSD microdose, n=20 healthy adults, 0/6.5/13/26 µg; orderly dose-related subjective effects but no clear cognitive enhancement — a microdose-paradigm reference for the de Wit lab's controlled work)"
  - "Shao LX, Liao C, Gregg I, Davoudian PA, Savalia NK, Delagarza K, Kwan AC — Neuron, 2021 — PMID:34228959 DOI:10.1016/j.neuron.2021.06.008 (preclinical: single psilocybin dose induces rapid, persistent dendritic spine growth in mouse frontal cortex — ACUTE, MACRO-dose, animal; mechanism/neuroplasticity context only, not a microdose-cognition result)"
---

## Summary
Psilocybin **microdosing** — taking deliberately **sub-perceptual** doses (roughly one-tenth of a full dose, ~1-3 mg, on an intermittent schedule) — is a popular self-enhancement practice claimed to improve mood, creativity, focus, and well-being. The honest assessment of the controlled literature is that **the best-designed studies are largely null for cognitive enhancement**: self-blinding and double-blind placebo-controlled RCTs find that microdosers improve, but **placebo groups improve just as much**, and the apparent benefits are largely explained by **expectancy and breaking blind** (Szigeti 2021, PMID:33648632; Cavanna/van Elk 2022, PMID:35918311; reviewed by Polito & Liknaitzky 2024, PMID:38877715). Open-label and observational studies report positive effects, but they are **confounded** by expectancy, self-selection, and lack of blinding. This entry therefore grades **microdosing-for-cognition** at the lowest level (evidence_overall 1, leaning null).

**Two critical distinctions and a legal flag.** (1) This entry covers **microdosing for cognitive enhancement only**. It does **not** assess **macrodose / psilocybin-assisted therapy for depression**, which is a separate and substantially stronger evidence base and should not be conflated with microdosing claims. (2) The neuroplasticity story ("psychoplastogen") is real but mostly **acute and preclinical at full doses**, not a demonstrated microdose effect in humans. (3) Psilocybin is **Schedule I** in the United States and illegal in most jurisdictions — flagged prominently below. Tone here is neutral and non-advisory; this is research metadata, not medical, legal, or usage advice.

## Mechanism
- **Serotonin 5-HT2A agonism (ser) — primary.** Psilocybin is a prodrug rapidly dephosphorylated to **psilocin**, an agonist at **5-HT2A** receptors (with additional activity at 5-HT2C, 5-HT1A, and affinity at 5-HT2B). 5-HT2A agonism is the well-established receptor mechanism of classic psychedelics. The open question for microdosing is whether **sub-perceptual** 5-HT2A engagement produces measurable cognitive benefit — and controlled human trials do not show a reliable effect over placebo. So while the *receptor mechanism* is well characterized, the *human cognitive outcome* at microdose is low/null (channel grade capped at 2).
- **Neuroplasticity / neurotrophic signaling (ntrophic) — acute, preclinical, mostly macrodose.** Psychedelics are described as **psychoplastogens**: 5-HT2A activation (including intracellular 5-HT2A) engages **BDNF-TrkB** and **mTOR** signaling and induces **rapid, persistent dendritic spine growth** in rodent frontal cortex (Shao 2021, PMID:34228959). This is compelling preclinical biology, **but it is an acute response demonstrated largely at full/macro doses in animals**; there is no established translation to sub-perceptual human microdosing or to durable cognitive enhancement. Hence channel grade 1 and population: preclinical.

## Evidence
**Best-controlled microdosing RCTs — largely NULL (the anchor for grade 1).**
- **Szigeti 2021** (PMID:33648632), *eLife* — the largest placebo-controlled psychedelic microdosing study to date (n=191 completers), using an innovative **self-blinding citizen-science** design where participants placebo-controlled themselves. All psychological outcomes improved from baseline in the microdose group — **but the placebo group improved just as much**, and **no significant between-group differences** remained once blinding and expectancy were modeled. Conclusion: anecdotal microdosing benefits are consistent with a **placebo effect**.
- **Cavanna / van Elk-affiliated 2022** (PMID:35918311), *Translational Psychiatry* — double-blind placebo-controlled study of 0.5 g dried psilocybin mushrooms on subjective experience, behavior, creativity, perception, cognition, and brain activity. **No evidence** that low doses enhanced well-being, creativity, or cognitive function; a few small changes trended **toward cognitive impairment**. Acute effects were more intense **only in participants who correctly identified their condition**, underscoring **expectancy/unblinding** as the driver.
- **Polito & Liknaitzky 2024** (PMID:38877715), *J Psychopharmacol* — rapid review of **19 placebo-controlled** low-dose LSD/psilocybin studies, framed around the question "is microdosing a placebo?"; the controlled evidence is broadly consistent with a **placebo explanation** for the subjective/affective/cognitive benefits people report.

**Controlled microdose paradigm (LSD, de Wit lab) — supportive of the null-for-enhancement picture.**
- **Bershad 2019** (PMID:31331617), *Biological Psychiatry* — double-blind placebo-controlled LSD microdose study (n=20 healthy adults; 0 / 6.5 / 13 / 26 µg). Produced **orderly, dose-related subjective effects** (confirming the doses were pharmacologically active) but **no clear cognitive enhancement**. Included as a rigorous controlled-microdose reference; it is **LSD, not psilocybin**, but reinforces that controlled microdose paradigms do not deliver the cognitive gains claimed in open-label settings.

**Open-label / observational reports — positive but CONFOUNDED.** Large naturalistic and open-label surveys report improved mood, focus, and creativity with microdosing. These are **not blinded**, are subject to strong **expectancy, self-selection, and reporting biases**, and consistently fail to survive placebo control. They do not raise the grade.

**Macrodose psilocybin therapy — SEPARATE, do not conflate.** Full-dose ("macro") psilocybin-assisted therapy for depression is a distinct regimen with its own (stronger) clinical evidence base and is **explicitly out of scope** for this microdosing entry. The neuroplasticity preclinical work (Shao 2021, PMID:34228959) likewise pertains to full doses/acute biology, not microdose cognition.

**Bottom line.** For **cognitive enhancement via microdosing**, the best-controlled human evidence is **essentially null and largely explained by placebo/expectancy**. Grade: evidence_overall 1 (leaning null).

## Safety & interactions (research metadata)
This section is neutral research metadata, not medical, legal, or usage advice.
- **Legal status — Schedule I (prominent flag).** Psilocybin is a **Schedule I** controlled substance under US federal law and is **illegal in most jurisdictions worldwide**; possession, manufacture, and use are generally criminal offenses. A small number of localities have decriminalized or created supervised frameworks, but this does not change the broad illegality. Treat legal status as the foremost consideration.
- **Cardiac / valvulopathy (theoretical, chronic use).** Drug-induced **valvular heart disease** is mechanistically tied to **5-HT2B agonism** (the fenfluramine/pergolide precedent). Classic psychedelics have 5-HT2B affinity, so **frequent/chronic microdosing** carries a **theoretical** valvulopathy concern. Direct human evidence of psilocybin-microdosing valvulopathy is lacking; this is a plausibility-based flag, not a documented outcome.
- **Psychiatric.** Contraindicated (conservatively) in personal/family history of **psychotic-spectrum or bipolar disorder** due to risk of precipitating psychosis/mania. Even at "microdose," unstandardized potency can make a dose unintentionally perceptual, with possible anxiety or mood destabilization.
- **Serotonergic drug interactions.** Theoretical additive serotonergic effects with **SSRIs/SNRIs/MAOIs, lithium, tramadol**, and other serotonergic agents. **Lithium** (case-report seizures/adverse events) and **MAOIs** are higher-concern combinations cited in the literature; **SSRIs** may blunt psychedelic subjective effects via 5-HT2A downregulation. Microdose-specific interaction data are limited.
- **Product variability.** Mushroom potency is highly variable and unregulated, so reliable "sub-perceptual" dosing is difficult; wild-mushroom misidentification carries poisoning risk.

## Open questions
- **Is there any real signal beyond placebo?** Across the best designs the answer is largely no for cognition — can any adequately powered, expectancy-controlled study isolate a genuine, non-placebo cognitive or mood benefit of microdosing?
- **Expectancy modeling.** Self-blinding and unblinding analyses suggest most benefit is expectancy-driven; how much, if any, residual pharmacological effect remains after rigorous expectancy control?
- **Neuroplasticity translation.** Do the preclinical/macrodose psychoplastogen effects (5-HT2A → BDNF/mTOR → spine growth) occur at all at **sub-perceptual human doses**, and do they translate to durable functional/cognitive change? Currently unproven.
- **Chronic safety.** Long-term cardiac (5-HT2B/valvulopathy) and psychiatric safety of repeated microdosing is uncharacterized in humans.
- **Standardization.** Without standardized, quantified dosing, "microdose" is an imprecise exposure, complicating both efficacy and safety conclusions.
- **Scope boundary.** Macrodose psilocybin-assisted therapy (e.g., for depression) is a separate evidence base and is intentionally not graded here.
