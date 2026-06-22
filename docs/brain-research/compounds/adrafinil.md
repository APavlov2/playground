---
id: adrafinil
name: Adrafinil
aliases:
  - "CRL-40028"
  - "Olmifon"
  - "(diphenylmethyl)sulfinyl-2-acetohydroxamic acid"
type: compound
klass: "eugeroic (wakefulness-promoting); prodrug of modafinil"
origin: synthetic                  # natural | semi-synthetic | synthetic (lab-only)
source: "Lab-synthesized prodrug of modafinil (no natural source)"
status: draft
evidence_overall: 2
onset: "Slower than modafinil because hepatic conversion is required; clinical effect over ~1 h but delayed relative to direct modafinil (mechanistic; exact human onset unsourced)"
half_life: "Adrafinil itself is short-lived; activity tracks the modafinil metabolite (R-modafinil ~12-15 h, S-modafinil ~4-5 h). Adrafinil's own half-life (unsourced for a precise human value)"
dose_range: "Historical/labelled use (Olmifon): ~600-900 mg/day. No validated healthy-adult cognitive-enhancement dose (unsourced)"
cognitive_domains:
  - alertness / vigilance (wakefulness)
  - attention
  - processing speed (read-across from modafinil)
  - executive function (read-across from modafinil)
channels:
  - channel: ne
    mechanism: "Adrafinil/modafinil increase noradrenergic / catecholaminergic tone and arousal; early pharmacology described an alpha-adrenergic component. Net wake-promoting effect is adrenergic-dependent. Direct human noradrenergic data for adrafinil are sparse; largely read-across from modafinil"
    evidence: 2
    population: both
    direction: up
  - channel: da
    mechanism: "Acts via its metabolite modafinil, a weak/atypical dopamine transporter (DAT) blocker that raises extracellular dopamine including nucleus accumbens (Volkow 2009, PMID: 19293415). Adrafinil-specific human dopamine data are essentially absent; inferred from modafinil"
    evidence: 2
    population: both
    direction: up
safety:
  contraindications:
    - "Pre-existing hepatic impairment or elevated liver enzymes (prodrug requires hepatic conversion; hepatic loading risk)"
    - "Cardiovascular disease / uncontrolled hypertension or arrhythmia (sympathomimetic/arousal effects; mechanistic caution by class)"
    - "Pregnancy/lactation: no adequate safety data; avoid"
    - "History of psychosis, severe anxiety, or stimulant misuse (class caution)"
  interactions:
    - "Other hepatotoxic agents or heavy alcohol use: additive liver burden (mechanistic caution)"
    - "Modafinil is a CYP3A4 inducer and may lower efficacy of hormonal contraceptives and some CYP3A4 substrates; same interaction expected via the modafinil metabolite (read-across; adrafinil-specific data unsourced)"
    - "Additive stimulant/sympathomimetic effects with caffeine, amphetamines, methylphenidate (mechanistic)"
  notable_risks:
    - "HEPATOTOXICITY: chronic use associated with elevated serum transaminases (ALT/AST); this hepatic-loading risk is the key safety differentiator from modafinil and is plausibly worse than direct modafinil because adrafinil must be hepatically converted"
    - "WADA-banned (prohibited in sport as a stimulant/eugeroic, same class as modafinil)"
    - "Headache, insomnia, anxiety, palpitations, GI upset (eugeroic class effects)"
    - "Unapproved/unregulated in the US (not FDA-approved); branded product Olmifon was withdrawn in France (2011). Consumer research-grade purity not assured"
    - "Rare but serious skin reactions reported for modafinil class (e.g. severe rash); read-across caution"
sources:
  - "Volkow ND, et al. Effects of modafinil on dopamine and dopamine transporters in the male human brain: clinical implications. JAMA. 2009;301(11):1148-54. PMID: 19293415"
  - "Minzenberg MJ, Carter CS. Modafinil: a review of neurochemical actions and effects on cognition. Neuropsychopharmacology. 2008;33(7):1477-502. PMID: 17712350"
  - "Battleday RM, Brem AK. Modafinil for cognitive neuroenhancement in healthy non-sleep-deprived subjects: A systematic review. Eur Neuropsychopharmacol. 2015;25(11):1865-81. PMID: 26381811"
  - "Repantis D, Schlattmann P, Laisney O, Heuser I. Modafinil and methylphenidate for neuroenhancement in healthy individuals: a systematic review. Pharmacol Res. 2010;62(3):187-206. PMID: 20416377"
  - "Milgram NW, et al. (adrafinil pharmacology) [A unique psychopharmacologic profile of adrafinil in mice]. J Pharmacol. 1986. PMID: 3713198"
  - "Milgram NW, et al. Adrafinil disrupts performance on a delayed nonmatching-to-position task in aged beagle dogs. Pharmacol Biochem Behav. 2003;76(2):245-52. PMID: 13679229"
tags:
  - eugeroic
  - prodrug
  - research-grade
  - wakefulness
  - wada-banned
  - unapproved-supplement
  - hepatotoxicity-risk
  - low-evidence
---

## Summary

Adrafinil is a wakefulness-promoting agent (eugeroic) that is a **prodrug of modafinil** — it is metabolized in the liver to modafinil (and modafinilic acid), and its effects are essentially **those of modafinil acting indirectly**. The two practically meaningful differences from modafinil are (1) **slower/less reliable onset**, because hepatic conversion is required, and (2) **hepatic loading**: chronic use is associated with elevated liver enzymes, a safety differentiator that modafinil does not share to the same degree.

**Flags:** prodrug of a Schedule IV drug (modafinil); **not FDA-approved** and sold unregulated as a research-grade supplement in the US; the branded product Olmifon was withdrawn from the French market; **WADA-banned** (same eugeroic/stimulant class as modafinil).

Evidence honesty: **direct human cognition trials of adrafinil are old and sparse** (mostly 1980s-1990s French studies in elderly populations, much of it poorly indexed and not retrievable on modern PubMed), and the cleaner controlled cognitive evidence is for **modafinil**, applied here as read-across. Grade is **LOW (evidence_overall = 2)** — modest, leaning on modafinil rather than direct adrafinil data, and discounted further for the liver risk and the prodrug uncertainty.

## Mechanism (prodrug → modafinil)

- **Conversion:** Adrafinil has little intrinsic activity; it is **hepatically converted to modafinil**, the active eugeroic. Onset is therefore slower than direct modafinil, and inter-individual hepatic metabolism adds variability. The price of this route is repeated first-pass hepatic processing, the basis of the hepatic-loading concern.
- **Dopamine (da):** Via modafinil, it acts as a **weak/atypical dopamine transporter (DAT) blocker**, raising extracellular dopamine including in the nucleus accumbens (Volkow 2009, PMID: 19293415; reviewed Minzenberg & Carter 2008, PMID: 17712350). This is the read-across basis for arousal/abuse-potential considerations. **Adrafinil-specific human dopamine data are essentially absent.**
- **Noradrenergic / catecholaminergic (ne):** Wake promotion is **adrenergic-dependent**; early adrafinil pharmacology (PMID: 3713198) described an alpha-adrenergic / catecholaminergic component, and modafinil's wake effects involve noradrenergic and downstream orexinergic/histaminergic systems (Minzenberg & Carter 2008, PMID: 17712350). Graded modestly; direct adrafinil human data sparse.
- Both channels are graded conservatively (evidence 2) because the human-confirmed mechanism is for the **metabolite (modafinil)**, not adrafinil per se.

## Evidence

**Direct adrafinil (old, sparse, mostly elderly):**

- The substantive adrafinil human literature is **1980s-1990s French clinical work in elderly/aged patients** (vigilance, attention, memory, mild depressive symptoms). Much of this is **not indexed in PubMed** and cannot be independently verified here — treat as **(unsourced)** at the level of specific quantitative claims.
- Preclinical/animal: adrafinil's distinctive psychopharmacologic profile in mice (PMID: 3713198). Notably, in **aged beagle dogs, 20 mg/kg adrafinil impaired working memory** on a delayed nonmatching-to-position task (PMID: 13679229) — i.e., the cognitive read is not uniformly positive even in animals, attributed to excess prefrontal noradrenergic activity.

**Modafinil read-across (the cleaner controlled evidence):**

- Battleday & Brem 2015 (PMID: 26381811) — systematic review in healthy non-sleep-deprived subjects: with more complex tasks, modafinil showed reasonably **consistent enhancement of attention, executive function, and learning**, though effects on simpler tasks were mixed and a few studies showed reduced creativity.
- Repantis et al. 2010 (PMID: 20416377) — systematic review/meta-analysis: modafinil **improved attention in well-rested individuals**, with more modest/inconsistent effects on memory and executive function; concluded expectations exceed actual effects.
- Minzenberg & Carter 2008 (PMID: 17712350) — neurochemical review supporting the catecholaminergic mechanism above.

Net read: the **wakefulness/attention signal is genuine but modest and belongs to modafinil**; adrafinil inherits it indirectly while adding slower onset and a liver-burden cost. Healthy-adult cognitive enhancement specifically from adrafinil (as opposed to modafinil) is **(unsourced)**.

**Gaps (unsourced):** modern adrafinil RCTs of any kind; head-to-head adrafinil vs modafinil cognition/PK; precise human adrafinil half-life and onset; adrafinil-specific dopamine/noradrenaline human data; quantified incidence/threshold of liver-enzyme elevation; long-term safety; validated healthy-adult dose.

## Safety & interactions

- **HEPATOTOXICITY / liver enzymes (key differentiator):** Chronic adrafinil use is associated with **elevated serum transaminases (ALT/AST)**, and the prodrug's reliance on hepatic conversion makes hepatic loading a more salient concern than with direct modafinil. Liver-function monitoring is advisable with sustained use; avoid in pre-existing hepatic impairment and with other hepatotoxic exposures (including heavy alcohol). This is the main reason to **prefer modafinil over adrafinil** on a safety basis where a choice exists.
- **Same class as modafinil:** expect the modafinil side-effect and interaction profile via the metabolite — headache, insomnia, anxiety, palpitations, GI upset; **CYP3A4 induction** can reduce hormonal contraceptive efficacy and lower levels of some CYP3A4 substrates (read-across; adrafinil-specific data unsourced). Rare serious dermatologic reactions are a class caution.
- **Cardiovascular / psychiatric caution:** sympathomimetic arousal — caution in cardiovascular disease, uncontrolled hypertension/arrhythmia, psychosis, severe anxiety, or stimulant-misuse history.
- **WADA:** **banned in sport** as a stimulant/eugeroic (same class as modafinil).
- **Regulatory/quality flag:** **not FDA-approved**; unregulated research-grade supplement in the US; Olmifon withdrawn in France; consumer-grade purity not assured. (Modafinil itself is a Schedule IV controlled substance.)

## Open questions

- Does adrafinil offer **any advantage over modafinil**, or is it strictly inferior (slower onset + liver burden) for the same downstream effect?
- What is the true **incidence, dose-threshold, and reversibility** of adrafinil-associated liver-enzyme elevation? (unsourced)
- Are the old French elderly trials replicable under modern RCT standards, and do any effects extend to **healthy adults** specifically from adrafinil (vs modafinil)? Currently unsupported.
- Precise human **pharmacokinetics of adrafinil itself** (half-life, conversion efficiency, onset) remain poorly characterized (unsourced).
