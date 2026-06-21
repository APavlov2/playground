---
id: amphetamine-methylphenidate
name: "Prescription stimulants (amphetamines & methylphenidate)"
aliases:
  - amphetamine
  - dextroamphetamine
  - "mixed amphetamine salts"
  - Adderall
  - lisdexamfetamine
  - Vyvanse
  - methylphenidate
  - Ritalin
  - Concerta
  - "MPH"
  - "d-amphetamine"
type: compound
klass: "psychostimulant (CNS stimulant, Schedule II controlled substance)"
status: draft
evidence_overall: 4
onset: "IR ~20-60 min; XR/prodrug formulations slower and more gradual"
half_life: "amphetamine ~9-14 h; methylphenidate ~2-4 h (parent); lisdexamfetamine prodrug converts to d-amphetamine"
dose_range: "Clinical, ADHD only, set by prescriber (e.g., methylphenidate ~5-72 mg/day; mixed amphetamine salts ~5-40 mg/day; lisdexamfetamine ~30-70 mg/day). Not a self-administration recommendation."
cognitive_domains:
  - attention
  - "inhibitory control"
  - "working memory"
  - "episodic memory (delayed)"
  - "arousal/wakefulness"
  - "effort/motivation"
channels:
  - channel: da
    mechanism: "Increases synaptic dopamine: amphetamines reverse DAT and promote vesicular release (also VMAT2/MAO effects); methylphenidate blocks DAT reuptake. Drives arousal and executive/striatal-prefrontal signaling."
    evidence: 4
    population: impaired
    direction: up
  - channel: da
    mechanism: "In healthy non-ADHD users, dopaminergic up-modulation yields modest, inconsistent cognitive effects with an inverted-U dependence on baseline performance (low performers gain more; high performers may show no change or decrement)."
    evidence: 3
    population: healthy
    direction: modulate
  - channel: ne
    mechanism: "Increases synaptic norepinephrine via NET blockade (methylphenidate) and reverse transport/release (amphetamines); contributes to prefrontal arousal, alertness, and sympathetic activation."
    evidence: 4
    population: impaired
    direction: up
  - channel: ne
    mechanism: "Noradrenergic arousal contributes to subjective alertness/energy in healthy users; objective cognitive benefit is modest and task-dependent."
    evidence: 3
    population: healthy
    direction: modulate
safety:
  contraindications:
    - "Known hypersensitivity to amphetamine or methylphenidate products"
    - "Concurrent or recent (within 14 days) monoamine oxidase inhibitor (MAOI) use"
    - "Symptomatic cardiovascular disease, structural cardiac abnormalities, advanced arteriosclerosis, or moderate-to-severe hypertension"
    - "Hyperthyroidism"
    - "Glaucoma (per label warnings)"
    - "History of, or current, psychosis or mania (risk of exacerbation)"
    - "History of stimulant/substance use disorder (high abuse/dependence risk)"
  interactions:
    - "MAOIs: risk of hypertensive crisis; combination contraindicated (14-day washout)"
    - "Serotonergic agents (SSRIs, SNRIs, triptans, tramadol): potential serotonin syndrome with amphetamines"
    - "Other sympathomimetics/decongestants: additive cardiovascular stimulation"
    - "Antihypertensives: may reduce their efficacy"
    - "Urinary pH modifiers (acidifying/alkalinizing agents): alter amphetamine excretion and exposure"
    - "Methylphenidate may inhibit metabolism of some anticonvulsants, warfarin, and tricyclic antidepressants (label caution)"
    - "QT-prolonging drugs: additive cardiac risk"
  notable_risks:
    - "Schedule II controlled substance: high potential for misuse, abuse, dependence, and diversion (boxed warning)"
    - "Cardiovascular: increased heart rate and blood pressure; rare reports of serious cardiac events; caution with pre-existing cardiac disease"
    - "Psychiatric: anxiety, irritability, insomnia; new or worsened psychosis/mania; aggression"
    - "Appetite suppression, weight loss; growth monitoring in children"
    - "Sleep disruption"
    - "Peripheral vasculopathy/Raynaud's phenomenon"
    - "Tolerance and withdrawal (fatigue, dysphoria) on discontinuation of heavy/non-prescribed use"
    - "Priapism (rare); seizure threshold lowering"
sources:
  - "Cortese S, et al. Comparative efficacy and tolerability of medications for attention-deficit hyperactivity disorder in children, adolescents, and adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2018;5(9):727-738. PMID: 30097390. DOI: 10.1016/S2215-0366(18)30269-4"
  - "Farhat LC, et al. Comparative cardiovascular safety of medications for attention-deficit hyperactivity disorder in children, adolescents, and adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2025;12(5):e1. PMID: 40203844. DOI: 10.1016/S2215-0366(25)00062-8"
  - "Ilieva IP, Hook CJ, Farah MJ. Prescription Stimulants' Effects on Healthy Inhibitory Control, Working Memory, and Episodic Memory: A Meta-analysis. J Cogn Neurosci. 2015;27(6):1069-1089. PMID: 25591060. DOI: 10.1162/jocn_a_00776"
  - "Repantis D, Schlattmann P, Laisney O, Heuser I. Modafinil and methylphenidate for neuroenhancement in healthy individuals: a systematic review. Pharmacol Res. 2010;62(3):187-206. PMID: 20416377. DOI: 10.1016/j.phrs.2010.04.002"
  - "Marraccini ME, Weyandt LL, Rossi JS, Gudmundsdottir BG. Neurocognitive Enhancement or Impairment? A Systematic Meta-Analysis of Prescription Stimulant Effects on Processing Speed, Decision-Making, Planning, and Cognitive Perseveration. Exp Clin Psychopharmacol. 2016;24(4):269-284. PMID: 27454675. DOI: 10.1037/pha0000079"
  - "Smith ME, Farah MJ. Are prescription stimulants 'smart pills'? The epidemiology and cognitive neuroscience of prescription stimulant use by normal healthy individuals. Psychol Bull. 2011;137(5):717-741. PMID: 21859174. DOI: 10.1037/a0023825"
tags:
  - prescription
  - controlled-substance
  - schedule-ii
  - stimulant
  - adhd
  - dopamine
  - norepinephrine
  - cognitive-enhancement
---

## Summary

Prescription stimulants comprise two principal drug classes: amphetamines (e.g., dextroamphetamine, mixed amphetamine salts/Adderall, and the prodrug lisdexamfetamine/Vyvanse) and methylphenidate (Ritalin, Concerta). Both are **Schedule II controlled substances** in the United States, carrying a boxed warning for **high potential for abuse, dependence, and diversion**. This entry treats them as a single Rx-stimulant class and distinguishes the two agents where mechanism or evidence differs.

The evidence base is asymmetric and must be read carefully. For **attention-deficit/hyperactivity disorder (ADHD)**, efficacy is **strong and well replicated** across large network meta-analyses (the basis for the `evidence_overall: 4` rating — this rating reflects ADHD efficacy, not enhancement in healthy people). For **cognitive "enhancement" in healthy, non-ADHD adults**, effects are **modest, inconsistent, and act largely on arousal, effort, and motivation rather than on raw cognitive capacity**. Some studies show no benefit, and complex or already-optimal performance can be unchanged or impaired (an inverted-U pattern in which lower baseline performers benefit more). This entry is descriptive and non-advisory; it is not medical advice and does not endorse non-prescribed use.

## Mechanism

Both classes increase synaptic monoamines but by partly different routes:

- **Amphetamines** are substrates that promote release of dopamine (DA) and norepinephrine (NE): they enter via and reverse the dopamine transporter (DAT) and norepinephrine transporter (NET), redistribute monoamines from vesicles (via VMAT2), and weakly inhibit monoamine oxidase (MAO). The net effect is elevated extracellular DA and NE independent of neuronal firing.
- **Methylphenidate** is primarily a **reuptake blocker** of DAT and NET, raising synaptic DA/NE in a more firing-dependent manner.

The therapeutic and arousal-promoting effects are attributed mainly to **dopaminergic (`da`) and noradrenergic (`ne`)** potentiation of striatal-prefrontal circuits supporting attention, inhibitory control, and arousal. A central pharmacodynamic concept is the **inverted-U**: catecholamine signaling in prefrontal cortex has an optimum, so individuals (or task states) below optimum may improve while those at or above optimum may not change or may worsen. This underlies the population-dependent grading: clearer benefit in impaired/deficient states, modulatory and variable effects in healthy individuals.

## Evidence

### ADHD (impaired population) — strong

Cortese et al. (2018), a network meta-analysis informing international ADHD guidelines, found methylphenidate and amphetamines efficacious versus placebo on short-term symptom reduction, with methylphenidate favored as first choice in children/adolescents and amphetamines in adults on the balance of efficacy and tolerability (PMID: 30097390). This large, consistent evidence base is the basis for the overall evidence rating.

### Healthy "cognitive enhancement" — modest and inconsistent

- **Ilieva, Hook & Farah (2015)** meta-analyzed 48 studies (n = 1,409) of methylphenidate and amphetamine in healthy adults: effects on inhibitory control and short-term episodic memory were **small but significant**, working memory effects small, and delayed episodic memory medium-sized — but the authors concluded the overall effect on healthy cognition is **"probably modest,"** qualified by publication bias, and suggested users may value **energy and motivation more than cognition** (PMID: 25591060).
- **Repantis et al. (2010)** systematic review found, for methylphenidate, an improvement in memory but **no consistent evidence** for other enhancing effects in healthy individuals, and noted that expectations exceed measured effects (PMID: 20416377).
- **Marraccini et al. (2016)** meta-analysis found a small significant gain only in processing-speed accuracy and **no significant effect** on decision-making, planning, or cognitive perseveration — i.e., higher-order/complex executive functions were not enhanced (PMID: 27454675).
- **Smith & Farah (2011)** reviewed >40 laboratory studies, documenting small and variable enhancement concentrated in lower-baseline performers and consistent with an **inverted-U** dependence on baseline ability (PMID: 21859174).

Taken together: in healthy people the signal is small, domain-specific, sensitive to baseline performance, and weighted toward **arousal/effort/motivation** rather than fundamental cognitive capacity. Complex tasks may show no benefit or impairment.

## Safety & interactions

- **Controlled-substance / addiction (prominent):** Schedule II classification reflects high abuse and dependence liability; boxed warnings address misuse, dependence, and diversion. Non-prescribed and high-dose use carries substantial addiction risk; tolerance and withdrawal (fatigue, dysphoria) can occur.
- **Cardiovascular:** Stimulants raise heart rate and blood pressure. Farhat et al. (2025) network meta-analysis quantified small but consistent increases in pulse and blood pressure across ADHD medications, supporting baseline cardiac assessment and monitoring; serious cardiac events are rare but reported (PMID: 40203844). Contraindicated in symptomatic cardiovascular disease and serious structural cardiac abnormalities.
- **MAOI interaction:** Co-administration with, or use within 14 days of, an MAOI risks **hypertensive crisis** and is contraindicated.
- **Psychiatric:** Can precipitate or worsen **psychosis or mania**; associated with anxiety, irritability, insomnia, and aggression.
- **Serotonergic agents:** Amphetamines combined with serotonergic drugs carry a serotonin-syndrome risk.
- **Other:** Appetite suppression and weight loss (growth monitoring in children), sleep disruption, peripheral vasculopathy/Raynaud's, rare priapism, and seizure-threshold lowering.

This section is informational and not a substitute for prescriber and pharmacist review.

## Open questions

- How large and durable are healthy-enhancement effects once publication bias and expectancy/placebo effects are removed, and do any survive on complex, ecologically valid tasks?
- To what extent does baseline performance (inverted-U) predict who benefits versus who is impaired, and can it be measured prospectively?
- Differential profiles of amphetamines vs methylphenidate for cognition, abuse liability, and cardiovascular load at equivalent clinical effect.
- Long-term cognitive, cardiovascular, and dependence outcomes of sustained non-medical use in healthy adults (largely unstudied) (unsourced).
- Whether motivation/effort enhancement is mechanistically separable from "cognitive" enhancement in measurement terms.
