---
id: l-tryptophan-5-htp
name: L-Tryptophan and 5-HTP
aliases:
  - L-tryptophan
  - tryptophan
  - 5-HTP
  - 5-hydroxytryptophan
  - oxitriptan
  - L-5-hydroxytryptophan
type: compound
klass: serotonin precursor (amino acid / amino-acid metabolite)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Tryptophan from dietary protein; 5-HTP from Griffonia simplicifolia seeds"
status: draft
evidence_overall: 2
onset: "L-tryptophan sleep effect can take several nights of repeated dosing in chronic insomniacs (latency reduction appeared on nights 4-6, not nights 1-3); 5-HTP absorbed and decarboxylated to serotonin within ~1-2 h"
half_life: "L-tryptophan plasma half-life roughly 2 h; 5-HTP plasma half-life roughly 2-7 h (peripheral; carbidopa co-administration prolongs)"
dose_range: "L-tryptophan: ~1-15 g for sleep (most trials 1-4 g). 5-HTP: commonly 100 mg three times daily in depression/fibromyalgia trials; ranges 150-3000 mg/day reported"
cognitive_domains:
  - mood
  - sleep
  - none-cognitive-direct
channels:
  - channel: ser
    mechanism: "Both are direct serotonin precursors. L-tryptophan is the rate-limiting dietary precursor converted by tryptophan hydroxylase to 5-HTP, then decarboxylated to serotonin (5-HT); 5-HTP bypasses the rate-limiting hydroxylation step and crosses the blood-brain barrier without a transporter, raising central 5-HT synthesis. Rationale is biochemically sound; human clinical efficacy data are old, small, and low-quality."
    evidence: 2
    population: impaired
    direction: up
  - channel: glymph
    mechanism: "Serotonin is a precursor to melatonin (via N-acetylserotonin), providing a plausible sleep/circadian pathway. L-tryptophan reduced sleep-onset latency in small insomnia trials, but direct evidence for melatonin-mediated or glymphatic effects in humans is absent. (unsourced for glymphatic clearance specifically)"
    evidence: 2
    population: impaired
    direction: modulate
safety:
  contraindications:
    - "Concurrent MAOI use (risk of serotonin syndrome / hypertensive reaction)"
    - "Concurrent serotonergic antidepressant therapy without medical supervision (SSRIs, SNRIs, TCAs)"
    - "History of eosinophilia-myalgia syndrome (EMS) or scleroderma-like illness associated with prior tryptophan use"
  interactions:
    - "SSRIs / SNRIs: additive serotonergic load; theoretical serotonin syndrome risk"
    - "MAOIs: serotonin syndrome and case-reported precipitation of mania"
    - "Other serotonergic agents: tramadol, triptans, dextromethorphan, St John's wort, lithium"
    - "Carbidopa (peripheral decarboxylase inhibitor): increases central availability of 5-HTP but historically linked to scleroderma-like reactions"
  notable_risks:
    - "Eosinophilia-myalgia syndrome (EMS): 1989 epidemic of >1500 cases and >30 deaths linked to contaminated L-tryptophan from a single manufacturer (Showa Denko); causally tied to a manufacturing-process contaminant (peak E), with post-epidemic cases still reported"
    - "Serotonin syndrome when combined with serotonergic drugs"
    - "Gastrointestinal effects: nausea, diarrhea, dizziness (dose-related, more common with 5-HTP)"
    - "Quality/purity of supplements is a persistent concern given the EMS contaminant history"
sources:
  - "Shaw K, Turner J, Del Mar C. Tryptophan and 5-hydroxytryptophan for depression. Cochrane Database Syst Rev. 2002;(1):CD003198. PMID: 11869656. DOI: 10.1002/14651858.CD003198"
  - "Belongia EA, Hedberg CW, Gleich GJ, et al. An investigation of the cause of the eosinophilia-myalgia syndrome associated with tryptophan use. N Engl J Med. 1990;323(6):357-365. PMID: 2370887. DOI: 10.1056/NEJM199008093230601"
  - "Allen JA, Peterson A, Sufit R, et al. Post-epidemic eosinophilia-myalgia syndrome associated with L-tryptophan. Arthritis Rheum. 2011;63(11):3633-3639. PMID: 21702023"
  - "Spinweber CL. L-tryptophan administered to chronic sleep-onset insomniacs: late-appearing reduction of sleep latency. Psychopharmacology (Berl). 1986;90(2):151-155. PMID: 3097693"
  - "Caruso I, Sarzi Puttini P, Cazzola M, Azzolini V. Double-blind study of 5-hydroxytryptophan versus placebo in the treatment of primary fibromyalgia syndrome. J Int Med Res. 1990;18(3):201-209. PMID: 2193835"
tags:
  - serotonin
  - serotonin-precursor
  - amino-acid
  - mood
  - sleep
  - depression
  - safety-critical
  - EMS
  - serotonin-syndrome
---

## Summary

L-Tryptophan (an essential amino acid) and 5-HTP (5-hydroxytryptophan, its downstream metabolite) are direct precursors of serotonin. The biochemical rationale for a mood- and sleep-supporting effect is sound: both feed central serotonin synthesis, and 5-HTP additionally bypasses the rate-limiting hydroxylation step and crosses the blood-brain barrier freely. However, the human efficacy evidence is old, small, and methodologically weak. The Cochrane review (Shaw 2002) screened 108 studies and found only 2 of adequate quality (64 participants total). Overall evidence is graded modestly (2/4), and safety dominates the assessment: L-tryptophan caused a fatal eosinophilia-myalgia syndrome (EMS) epidemic in 1989, and both compounds carry serotonin-syndrome risk when combined with serotonergic drugs.

This entry treats the two together because they share the serotonin-precursor mechanism, but distinguishes them where it matters: EMS is historically tied to L-tryptophan specifically (a manufacturing contaminant), while 5-HTP has the larger, though still weak, depression/fibromyalgia trial base and a higher rate of GI side effects.

## Mechanism

- L-tryptophan -> (tryptophan hydroxylase, rate-limiting) -> 5-HTP -> (aromatic L-amino-acid decarboxylase) -> serotonin (5-HT) -> (via N-acetylserotonin) -> melatonin.
- L-tryptophan competes with other large neutral amino acids for the same blood-brain-barrier transporter; central uptake is therefore diet- and competition-dependent.
- 5-HTP bypasses the rate-limiting hydroxylation step and crosses the blood-brain barrier without requiring a transporter, so it raises central serotonin synthesis more directly. Peripheral decarboxylation also raises systemic serotonin, which contributes to GI side effects.
- Channel mapping: ser is the primary and best-justified channel (direction up, population impaired/deficient most relevant). A secondary glymph/sleep link is plausible through the serotonin-to-melatonin pathway, but human glymphatic-clearance evidence is absent (direction modulate, low confidence).

## Evidence

Depression (primary efficacy question):
- Shaw 2002 (Cochrane, PMID 11869656; DOI 10.1002/14651858.CD003198): of 108 identified trials, only 2 met quality criteria (64 participants). Pooled effect favored tryptophan/5-HTP over placebo (Peto OR 4.10; 95% CI 1.28-13.15), but the authors judged the evidence insufficient to be conclusive and flagged the EMS safety concern. This is the central reason efficacy is graded down rather than up.

Sleep / insomnia:
- Spinweber 1986 (PMID 3097693): in chronic sleep-onset insomniacs, 3 g L-tryptophan did NOT reduce sleep latency on nights 1-3 but significantly reduced it on nights 4-6, without altering sleep architecture, performance, or waking EEG. This "late-appearing" effect informs the onset note. Several other small trials (1-4 g) report sleep-latency reductions, but they are small, old, and heterogeneous.

Fibromyalgia (often cited but not cognitive):
- Caruso 1990 (PMID 2193835): double-blind RCT, 50 patients, 5-HTP 100 mg three times daily vs placebo; all clinical parameters improved with mild/transient side effects. Small and single-center; included for context on dosing and tolerability, not as cognitive evidence.

Cognition in healthy adults: no good evidence of direct cognitive enhancement in healthy, non-deficient individuals (unsourced for a healthy-cognition benefit). Effects are mood/sleep-oriented and most relevant in impaired or deficient populations.

## Safety & interactions

Eosinophilia-myalgia syndrome (EMS) - the defining safety event:
- In 1989, an epidemic of EMS (>1500 cases, >30 deaths) was linked to L-tryptophan supplements. Belongia 1990 (NEJM, PMID 2370887; DOI 10.1056/NEJM199008093230601) traced the outbreak to a chemical contaminant ("peak E") associated with specific manufacturing conditions at a single producer (Showa Denko), rather than to tryptophan itself. The FDA recalled and largely banned tryptophan sales (1989-1990; restrictions later eased).
- EMS is not purely historical: Allen 2011 (PMID 21702023) documented a post-epidemic, L-tryptophan-associated EMS case after the ban was eased, underscoring ongoing product-purity risk.

Serotonin syndrome and drug interactions:
- Combining either compound with SSRIs, SNRIs, TCAs, MAOIs, tramadol, triptans, dextromethorphan, St John's wort, or lithium increases serotonergic load and carries a theoretical-to-real serotonin syndrome risk. A case report describes 5-HTP precipitating mania when added to an MAOI. Clinical-grade serotonin syndrome from 5-HTP alone in humans is rarely documented, but co-administration with serotonergic drugs is the principal interaction concern and warrants medical supervision or avoidance.

Other:
- GI effects (nausea, diarrhea, dizziness) are dose-related and more common with 5-HTP due to peripheral serotonin formation.
- Supplement purity remains a real concern given the EMS contaminant precedent; this is a quality-control rather than an intrinsic-pharmacology risk.

## Open questions

- Is the modest Cochrane efficacy signal real, or an artifact of small, low-quality, old trials? No modern, adequately powered RCT has settled this.
- Does the EMS risk reside entirely in contaminants, or is there any intrinsic tryptophan/metabolite contribution? The contaminant hypothesis is strongly supported but the precise causative agent remains not fully elucidated.
- Are there any cognitive (as opposed to mood/sleep) benefits in healthy, non-deficient adults? Currently unsupported.
- What is the true serotonin-syndrome risk of 5-HTP at supplement doses alongside common serotonergic medications, beyond theoretical/case-report level?
- Is there any genuine melatonin- or glymphatic-mediated sleep benefit, or are sleep effects fully explained by serotonergic mechanisms? Glymphatic involvement is unsourced.
