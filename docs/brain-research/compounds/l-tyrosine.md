---
id: l-tyrosine
name: L-Tyrosine
aliases: [tyrosine, L-tyr, "N-acetyl-L-tyrosine", NALT, "N-acetyltyrosine", TYR]
type: compound
klass: Amino acid (catecholamine precursor)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Dietary protein (cheese, meat, soy); endogenous amino acid"
status: draft
evidence_overall: 3  # Multiple RCTs + a focused review show a REPLICATED, mechanism-consistent benefit, but ONLY under acute catecholamine-depleting stressors (cold, sleep loss, multitasking load). No reliable baseline cognitive boost in rested/unstressed people. Conditional grade 3; would be 1-2 for the unstressed-healthy claim.
onset: "Acute. Plasma tyrosine peaks ~1-2 h after an oral dose; behavioral effects in RCTs are measured single-dose, same-session (typically ~1 h post-dose) under an active stressor"
half_life: "Plasma tyrosine elimination roughly 2-3 h after oral L-tyrosine (approximate; precise human half-life not firmly characterized for nootropic dosing)"
dose_range: "Single acute doses of ~100-150 mg/kg in cognitive RCTs (~2 g fixed in the Deijen combat-course trial; up to ~300 mg/kg in cold-immersion work). No established chronic nootropic dose"
cognitive_domains: [working-memory, cognitive-control, attention, vigilance, psychomotor, task-switching]
channels:
  - channel: da
    mechanism: "Tyrosine is the rate-limited precursor for dopamine synthesis (tyrosine -> L-DOPA via tyrosine hydroxylase -> dopamine). Supplying substrate supports catecholamine synthesis specifically when neurons fire at high rates and deplete stores; under those demand conditions tyrosine repletes dopamine-dependent cognitive-control functions (e.g. N-back updating). Does NOT force-feed dopamine at rest"
    evidence: 3
    population: healthy  # benefit shown in healthy adults, but conditional on acute demand/stress
    direction: up
  - channel: ne
    mechanism: "Same precursor pathway continues: dopamine -> norepinephrine via dopamine beta-hydroxylase. Acute stressors (cold, sleep deprivation, military stress) drive high noradrenergic output and deplete brain catecholamines in animal models; tyrosine prevents the associated cognitive/psychomotor decrement and lowers stress-related blood-pressure rise in one military trial"
    evidence: 3
    population: healthy  # conditional on acute catecholamine-depleting stress
    direction: up
safety:
  contraindications:
    - "Hyperthyroidism / thyrotoxicosis (theoretical: tyrosine is a precursor to thyroid hormone) (unsourced beyond mechanistic rationale)"
    - "Concurrent MAO-inhibitor therapy (theoretical pressor/catecholamine concern) (unsourced beyond mechanistic rationale)"
  interactions:
    - "MAO inhibitors: theoretical additive catecholamine/pressor effect (mechanistic, not established in controlled human trials)"
    - "Levodopa: large neutral amino acids including tyrosine compete with L-DOPA for intestinal and blood-brain-barrier LAT1 transport and may blunt levodopa absorption (mechanistic/pharmacokinetic rationale; not characterized in dedicated tyrosine-supplement trials)"
    - "Thyroid hormone synthesis: precursor relationship is theoretical for supplement doses (unsourced)"
  notable_risks:
    - "One acute high-dose study reported INCREASED self-rated anger during severe psychological stress, i.e. effects on affect are not uniformly positive (Tumilty/related work — see sources; treat as a caution, not established harm)"
    - "Generally well tolerated at studied single doses; long-term safety of repeated high-dose use is not characterized (unsourced)"
    - "N-acetyl-L-tyrosine (NALT) is a POOR tyrosine source: in humans it raises plasma tyrosine minimally and is largely excreted unchanged in urine — see Evidence and sources"
tags: [amino-acid, catecholamine-precursor, stress, sleep-deprivation, conditional-effect]
sources:
  - "Jongkees BJ, Hommel B, Kühn S, Colzato LS — J Psychiatr Res, 2015 — PMID:26424423 (focused review: tyrosine benefits cognition under stress/high demand; effects are conditional, not a general enhancer)"
  - "Neri DF, Wiegmann D, Stanny RR, Shappell SA, McCardie A, McKay DL — Aviat Space Environ Med, 1995 — PMID:7794222 (overnight sleep loss / extended wakefulness; tyrosine attenuated psychomotor decline and vigilance lapses)"
  - "Mahoney CR, Castellani J, Kramer FM, Young A, Lieberman HR — Physiol Behav, 2007 — PMID:17078981 (cold-water immersion body cooling; tyrosine preserved match-to-sample working memory and marksmanship)"
  - "Mahoney CR, et al. — (cold/working memory) — PMID:17585971 (tyrosine mitigates working-memory decrements during cold exposure)"
  - "Deijen JB, Wientjes CJ, Vullinghs HF, Cloin PA, Langefeld JJ — Brain Res Bull, 1999 — PMID:10230711 (military combat-training course; 2 g/day tyrosine improved memory/tracking, reduced systolic BP)"
  - "Thomas JR, Lockwood PA, Singh A, Deuster PA — Pharmacol Biochem Behav, 1999 — PMID:10548261 (demanding multitasking environment; 150 mg/kg tyrosine improved working memory)"
  - "Colzato LS, Jongkees BJ, Sellaro R, Hommel B — Front Behav Neurosci, 2013 — PMID:24379768 / DOI:10.3389/fnbeh.2013.00200 (N-back: tyrosine repleted updating in the demanding 2-back but not the easy 1-back)"
  - "Magnusson I, Ekman L, Wångdahl M, Wahren J — Metabolism, 1989 — PMID:2507878 (humans, IV: N-acetyl-L-tyrosine raised plasma tyrosine only ~25% and ~56% was excreted unchanged in urine in 4 h — NALT is a poor tyrosine source)"
---

## Summary
L-Tyrosine is a large neutral amino acid and the rate-limited dietary precursor of the catecholamines dopamine and norepinephrine. Its honest, defensible claim is narrow: tyrosine **restores cognitive and psychomotor performance under acute stressors that deplete brain catecholamines** — sleep deprivation/extended wakefulness, cold exposure, demanding multitasking, and acute military/psychological stress. In those conditions multiple RCTs and a focused review report a replicated, mechanism-consistent benefit, supporting a conditional evidence grade of 3 (Jongkees 2015 — PMID:26424423).

The centerpiece caveat: tyrosine does **NOT** reliably boost baseline cognition in rested, unstressed, well-fed people. The benefit appears only when high neuronal firing outpaces endogenous catecholamine synthesis; at rest there is no substrate bottleneck to relieve. For the "general nootropic in a calm, rested person" claim the honest grade is 1-2, not 3.

A practical formulation note: **N-acetyl-L-tyrosine (NALT) is a poor tyrosine source** — in humans it raises plasma tyrosine minimally and most of it is excreted unchanged in urine (Magnusson 1989 — PMID:2507878).

## Mechanism
Catecholamine synthesis proceeds: tyrosine → L-DOPA (tyrosine hydroxylase, the rate-limiting step) → dopamine (DA, da channel) → norepinephrine (NE, ne channel, via dopamine beta-hydroxylase). Under ordinary resting conditions tyrosine hydroxylase is saturated and end-product-inhibited, so adding substrate does little. The leverage point is **demand**: when neurons fire rapidly — as during cold stress, sleep loss, or heavy cognitive load — synthesis can outstrip supply and intracellular tyrosine becomes limiting. Supplemental tyrosine then supports continued catecholamine output and prevents the performance decrement (Jongkees 2015 — PMID:26424423). This "substrate under demand" model explains why benefits are stressor- and load-gated rather than general.

- **Dopamine (da):** Cognitive-control / working-memory effects track dopaminergic demand. In the N-back task tyrosine improved performance specifically in the demanding 2-back updating condition but not the easy 1-back (Colzato 2013 — PMID:24379768), consistent with a substrate effect that only surfaces when control demand is high.
- **Norepinephrine (ne):** Acute physical/psychological stressors strongly engage the noradrenergic system; in the combat-training trial tyrosine improved memory/tracking and reduced systolic blood pressure, consistent with supporting (and buffering the consequences of) high noradrenergic drive (Deijen 1999 — PMID:10230711).

Both channels are graded 3 and population **healthy-but-conditional-on-acute-demand**; this is not a preclinical-only mechanism (human behavioral RCTs exist) but it is not an unconditional enhancement either.

## Evidence
**Conditional benefit under acute stressors (the robust finding).**
- **Sleep deprivation / extended wakefulness — Neri 1995 (PMID:7794222):** during ~24+ h continuous nighttime work with one night of sleep loss, tyrosine significantly attenuated the usual decline on a psychomotor task and reduced lapse probability on a high-event-rate vigilance task. A within-stressor rescue effect, not a baseline boost.
- **Cold exposure — Mahoney 2007 (PMID:17078981) and PMID:17585971:** with cold-water immersion lowering core temperature, placebo produced an ~18% drop in match-to-sample working memory and ~14% drop in marksmanship vs warm control, whereas the tyrosine condition did not differ from control — i.e. tyrosine prevented the cold-induced decrement. The companion work likewise shows tyrosine mitigates cold-induced working-memory decrements.
- **Acute military stress — Deijen 1999 (PMID:10230711):** 21 cadets during a demanding combat-training week; 2 g/day tyrosine vs isocaloric carbohydrate. The tyrosine group performed better on memory and tracking tasks and showed lower systolic blood pressure.
- **High cognitive load / multitasking — Thomas 1999 (PMID:10548261):** 150 mg/kg tyrosine improved working memory in a demanding multitasking environment, where the cognitive load itself (not an external physical stressor) is the depleting condition.
- **Demanding cognitive control — Colzato 2013 (PMID:24379768):** tyrosine helped the demanding 2-back but not the undemanding 1-back, a clean demonstration that the effect is load-gated.

**Null / no reliable effect in unstressed, rested people.** The Jongkees 2015 review (PMID:26424423) frames tyrosine's effects as appearing under stress or high cognitive demand and counteracting decrements in neurotransmitter function — not as a general cognitive enhancer for calm, rested, well-nourished individuals. Where demand is low, the substrate is not limiting and no benefit is expected or reliably observed. This stressed/depleted-vs-rested distinction is the single most important honesty point for grading.

**NALT caveat (formulation).** N-acetyl-L-tyrosine is marketed as a more soluble tyrosine, but in humans Magnusson 1989 (PMID:2507878) found IV NALT raised plasma tyrosine by only ~25% while ~56% of the dose was excreted unchanged in urine within 4 h, indicating incomplete deacetylation and poor bioavailability. NALT is therefore an inferior way to raise tyrosine relative to L-tyrosine itself.

**Bottom line:** Replicated, mechanism-consistent rescue of cognition/psychomotor performance under acute catecholamine-depleting stress justifies evidence_overall 3 for that conditional claim. The unstressed-healthy "nootropic" claim is not supported (grade 1-2). NALT should not be assumed equivalent to L-tyrosine.

## Safety & interactions (research metadata)
Single acute doses in the cited RCTs (≈100-300 mg/kg) were generally well tolerated. Affective effects are not uniformly positive: at least one acute high-dose study reported increased self-rated anger during severe psychological stress, so tyrosine is not purely benign on mood under extreme stress. Key theoretical interaction/contraindication concerns are mechanistic rather than trial-established:
- **Thyroid (hyperthyroidism):** tyrosine is a precursor to thyroid hormone; caution is theoretical (unsourced beyond mechanism).
- **MAO inhibitors:** theoretical additive catecholamine/pressor effect (not established in controlled human studies).
- **Levodopa:** tyrosine is a large neutral amino acid and competes with L-DOPA for LAT1 transport at the gut and blood-brain barrier, potentially reducing levodopa efficacy (pharmacokinetic rationale; not characterized in dedicated supplement trials).
Long-term safety of repeated high-dose use is not characterized. This section is research metadata, not medical advice.

## Open questions
- **Threshold of "stress" required:** how much catecholamine demand (load, sleep debt, cold) is needed before tyrosine helps? The boundary between "demanding enough to benefit" and "too rested to matter" is not quantified.
- **Individual differences / dopamine baseline:** effects may depend on baseline dopamine function and genotype (e.g. DRD2); some work even reports tyrosine impairing flexible behavior under certain demanding conditions, so direction may not be uniformly positive.
- **Chronic dosing:** essentially all positive cognitive data are single-dose/acute; whether repeated supplementation helps, does nothing, or down-regulates anything is untested.
- **Dose-response and timing:** optimal mg/kg, timing relative to the stressor, and whether protein-containing meals (competing LNAAs) blunt the effect are not well established.
- **NALT in oral nootropic use:** human oral (not IV) bioavailability of NALT at supplement doses is poorly quantified; the IV data (Magnusson 1989) strongly suggest inferiority but oral kinetics deserve direct study.
