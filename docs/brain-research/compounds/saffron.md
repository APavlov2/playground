---
id: saffron
name: Saffron
aliases: [Crocus sativus, Crocus sativus L., crocin, crocins, safranal, affron, saffron stigma extract]
type: compound
klass: Botanical / spice-derived extract (carotenoid glycosides)
origin: natural                  # natural | semi-synthetic | synthetic (lab-only)
source: "Saffron (Crocus sativus stigmas)"
status: draft
evidence_overall: 3  # Best relevant claim = ANTIDEPRESSANT (mild-moderate depression). Multiple RCTs + several meta-analyses show benefit vs placebo and non-inferiority vs SSRIs/TCAs. Graded DOWN from 4 because most trials are small and a large share originate from a few Iranian groups (replication/geographic-bias concern). 3, not 4.
onset: "Antidepressant effect studied over ~6-8 weeks in RCTs (comparable timeframe to SSRI onset); some low-mood supplement trials report change over 4-6 weeks. Not an acute effect."
half_life: "Crocin/crocetin/safranal pharmacokinetics not well characterized in humans; crocin is poorly absorbed intact and largely hydrolyzed to crocetin. Half-life not firmly established (approximate/unsettled)."
dose_range: "Most depression and AD/MCI RCTs used 30 mg/day of standardized hydroalcoholic stigma extract (often 15 mg twice daily), typically standardized to crocin and safranal (e.g. ~1.65-1.75 mg crocin and ~0.13-0.15 mg safranal per capsule). Low-mood supplement trials commonly use ~28 mg/day affron. High doses are toxic (see Safety)."
cognitive_domains: [mood, depression, anxiety, cognition-mci, attention-adhd, well-being]
channels:
  - channel: ser
    mechanism: "Serotonergic modulation is the most-cited mechanism: crocin/safranal reported to inhibit serotonin reuptake at synapses and to modulate monoamines (with additional reported MAO-A/B inhibition and NMDA antagonism). This is the leading explanation for the antidepressant effect, but the direct reuptake-inhibition data are largely PRECLINICAL (animal/in vitro); the exact human mechanism is unconfirmed."
    evidence: 2  # human antidepressant outcome is well-replicated, but the serotonergic MECHANISM itself is preclinical -> channel grade capped at 2
    population: both  # antidepressant outcome in impaired (depressed) populations; mechanism studied preclinically
    direction: modulate
  - channel: inflam
    mechanism: "Anti-inflammatory / antioxidant activity of crocin and safranal (reduced oxidative-stress and inflammatory markers) is proposed to underlie neuroprotective and AD-adjunct effects; one adjunct AD trial reported reductions in some inflammation/oxidative-stress markers. Mostly preclinical plus limited human marker data."
    evidence: 2
    population: both
    direction: down
  - channel: da
    mechanism: "Possible dopaminergic involvement invoked for ADHD signal and mood; preclinical/mechanistic only, not established in humans."
    evidence: 1
    population: preclinical
    direction: modulate
safety:
  contraindications:
    - "Pregnancy: traditional and pharmacological evidence of uterine-stimulant / emmenagogue and abortifacient activity at higher (non-culinary) doses; therapeutic-dose supplementation should be avoided in pregnancy. Caution also with lactation (insufficient safety data)."
  interactions:
    - "Antidepressants (SSRIs/MAOIs/TCAs): potential ADDITIVE serotonergic effect given proposed serotonin-reuptake/MAO mechanism; theoretical serotonergic-excess risk when combined (mechanistically plausible; not well quantified in controlled human studies)."
    - "Antihypertensives and antiplatelet/anticoagulant agents: commonly cited theoretical additive effects (blood-pressure lowering; platelet/anticoagulant effects of saffron constituents) — not established in controlled human studies (unsourced beyond general/preclinical reports)."
  notable_risks:
    - "High-dose toxicity: saffron is generally well tolerated at studied doses (~30 mg/day) but is toxic at high doses; ~5 g is considered toxic and doses around ~12-20 g can be lethal. Therapeutic window matters."
    - "Mild adverse effects in trials: headache, nausea/GI upset, changes in appetite, sedation/anxiety reported at low rates; meta-analytic data suggest fewer adverse events than SSRIs."
tags: [botanical, antidepressant, mood, serotonergic, geographic-bias-flag]
sources:
  - "Hausenblas HA, Saha D, Dubyak PJ, Anton SD — J Integr Med (formerly J Chin Integr Med), 2013 — PMID:24299602 DOI:10.3736/jintegrmed2013056 (meta-analysis, 5 RCTs; saffron > placebo, = standard antidepressants in MDD; authors call for larger international trials)"
  - "Tóth B, Hegyi P, Lantos T, et al.; Csupor D — Planta Med, 2019 — PMID:30036891 DOI:10.1055/a-0660-9565 (meta-analysis; vs placebo Hedges g=0.891, p=0.001; vs antidepressants g=-0.246, p=0.053 i.e. non-inferior; 11 trials qualitative / 9 pooled)"
  - "Shafiee A, Jafarabady K, Seighali N, et al.; Bakhtiyari M — Nutr Rev, 2025 — PMID:38913392 DOI:10.1093/nutrit/nuae076 (meta-analysis, saffron vs SSRIs; depression SMD=0.10 [-0.09,0.29] NS, anxiety SMD=0.04 NS, fewer adverse events; Iranian-affiliated authors)"
  - "Akhondzadeh S, Shafiee Sabet M, Harirchian MH, et al. — Psychopharmacology (Berl), 2010 — PMID:19838862 DOI:10.1007/s00213-009-1706-1 (22-wk multicenter RCT; saffron 30 mg/day ~ donepezil 10 mg/day in mild-to-moderate AD)"
  - "Ayati Z, Yang G, Ayati MH, Emami SA, Chang D — BMC Complement Med Ther, 2020 — PMID:33167948 DOI:10.1186/s12906-020-03102-3 (systematic review/meta-analysis, 4 RCTs/203 pts, MCI+dementia; benefit on ADAS-cog/CDR-SB vs placebo, ~ conventional drugs; 3/4 trials from Iran, MCI trial quality 'poor'; insufficient evidence for clinical recommendation)"
  - "Baziar S, Aqamolaei A, Khadem E, et al. — J Child Adolesc Psychopharmacol, 2019 — PMID:30741567 DOI:10.1089/cap.2018.0146 (6-wk double-blind pilot RCT, n=54 children; saffron 20-30 mg/day = methylphenidate for ADHD; small pilot)"
---

## Summary
Saffron (the dried stigmas of *Crocus sativus*, with crocin and safranal as principal bioactives) is a spice-derived botanical whose strongest evidence is as an **antidepressant** in mild-to-moderate depression. Multiple randomized controlled trials and several meta-analyses report that ~30 mg/day standardized extract is significantly more effective than placebo and roughly **non-inferior to SSRIs/TCAs** (fluoxetine, imipramine, citalopram), generally with fewer adverse events (PMID:24299602; PMID:30036891; PMID:38913392). This earns a relatively high honest grade (evidence_overall 3) — but it is deliberately **graded down from 4** for two reasons: (1) most trials are small (often 6-8 weeks, dozens of participants), and (2) a large share of the trials and meta-analytic author groups originate from a few **Iranian research centers** (notably the Akhondzadeh/Tehran group), raising replication and geographic-bias concerns that independent, larger, multi-country RCTs have not yet fully resolved. Secondary signals exist for MCI/Alzheimer's disease (adjunct/standalone) and ADHD, but these are weaker, smaller, and even more geographically concentrated. The serotonergic mechanism most often invoked is largely preclinical.

## Mechanism
Saffron's bioactivity is attributed chiefly to the carotenoid glycoside **crocin** (hydrolyzed in vivo to crocetin) and the volatile **safranal**, with picrocrocin contributing to flavor. Proposed central mechanisms:

- **Serotonergic / monoaminergic (ser):** The leading antidepressant hypothesis is that saffron constituents **inhibit serotonin reuptake** at the synapse and modulate monoamines, with additional reported **MAO-A/B inhibition**, NMDA-receptor antagonism, and enhanced BDNF signaling. These are most strongly supported by **preclinical** (rodent/in vitro) work; saffron/crocin produce antidepressant-like behavior comparable to fluoxetine in animal models, but the exact human mechanism remains unconfirmed. Hence the human *outcome* is solid while the *mechanism* is preclinical — channel grade capped at 2.
- **Anti-inflammatory / antioxidant (inflam):** Crocin and safranal show antioxidant and anti-inflammatory activity (reduced oxidative-stress and inflammatory markers), proposed to underlie neuroprotection in AD/MCI. Some human marker data exist (e.g., an AD donepezil-adjunct trial reporting reductions in select inflammation/oxidative-stress markers), but the bulk is preclinical.
- **Dopaminergic (da):** Dopaminergic involvement is invoked for the ADHD signal and mood, but this is mechanistic/preclinical only (grade 1).

## Evidence
**Depression — the primary, best-supported claim (with the key honesty caveat).**
- Hausenblas 2013 (PMID:24299602): meta-analysis of 5 RCTs in MDD; saffron supplementation produced substantially larger reductions in depressive symptoms than placebo and was equivalent to standard antidepressants. High reported trial quality (mean Jadad 5), but the authors themselves call for larger trials conducted **internationally** with longer follow-up.
- Tóth 2019 (PMID:30036891), *Planta Med*: meta-analysis (11 trials qualitative, 9 pooled). Saffron vs placebo Hedges **g = 0.891 (95% CI 0.369-1.412, p = 0.001)**; saffron vs antidepressants **g = -0.246 (95% CI -0.495 to 0.004, p = 0.053)**, i.e., significantly better than placebo and **non-inferior** to comparator antidepressants, with the antidepressant comparison at borderline significance and a modest number of pooled trials.
- Shafiee 2025 (PMID:38913392), *Nutrition Reviews*: meta-analysis of saffron vs SSRIs (8 depression, 4 anxiety studies). **No significant difference** vs SSRIs for depression (SMD = 0.10; 95% CI -0.09 to 0.29) or anxiety (SMD = 0.04), and **fewer adverse events** with saffron. Authors are Iranian-affiliated and explicitly call for larger, more diverse-population studies.

**Replication / geographic-bias caveat (load-bearing).** Across these meta-analyses, a disproportionate share of primary RCTs come from a small number of Iranian groups (the Tehran/Akhondzadeh program is especially prominent), and several review author teams are themselves Iranian-affiliated. This concentration is a recognized limitation: positive findings are well-replicated *within* a narrow research ecosystem but are under-replicated by independent international groups. Trial sizes are also typically small (tens of participants, ~6-8 weeks). Treat "comparable to SSRIs" as promising-but-not-definitive; the honest compound grade is 3, not 4.

**MCI / Alzheimer's disease (secondary, weaker).**
- Akhondzadeh 2010 (PMID:19838862), *Psychopharmacology*: 22-week, multicenter, double-blind RCT; saffron 30 mg/day was **comparable to donepezil 10 mg/day** in mild-to-moderate AD, with fewer vomiting events than donepezil.
- Ayati 2020 (PMID:33167948), *BMC Complement Med Ther*: systematic review/meta-analysis of **4 RCTs (203 patients)** in MCI/dementia. Saffron showed clinically significant improvement vs placebo on ADAS-cog and CDR-SB and comparable efficacy to conventional drugs, with a favorable safety profile — **but** 3 of 4 trials were from Iran (1 from Greece), only 1 addressed MCI (rated "poor" quality), and the authors conclude there is **insufficient high-quality evidence to recommend clinical use**. So the cognitive/AD signal is real but materially weaker and more bias-prone than the depression signal.

**ADHD (exploratory).**
- Baziar 2019 (PMID:30741567), *J Child Adolesc Psychopharmacol*: 6-week double-blind pilot RCT (n=54 children/adolescents); saffron (20-30 mg/day) showed **equivalent efficacy to methylphenidate** with similar tolerability. Small pilot from an Iranian group; hypothesis-generating only. (Additional MPH-combination and affron ADHD trials exist but do not change the small-and-concentrated evidence picture.)

**Bottom line.** Replicated antidepressant effect in mild-to-moderate depression (the grade-3 anchor), undercut by small trials and geographic/replication bias; supportive but weaker AD/MCI signal; preliminary ADHD signal. Mechanistic serotonergic claims are mostly preclinical.

## Safety & interactions (research metadata)
Saffron is **generally well tolerated** at studied therapeutic doses (~30 mg/day); meta-analytic data indicate **fewer adverse events than SSRIs** (PMID:38913392), with mild effects (headache, nausea/GI upset, appetite change, sedation or anxiety) reported at low rates. Key cautions:
- **Pregnancy / uterine stimulant:** saffron has documented emmenagogue/uterine-stimulant and abortifacient activity at higher-than-culinary doses; therapeutic-dose supplementation should be avoided in pregnancy (and is cautioned in lactation for lack of data). Listed as a contraindication.
- **High-dose toxicity:** there is a defined therapeutic window — culinary/supplement doses are safe, but high doses are toxic (commonly cited: ~5 g toxic; ~12-20 g potentially lethal). This is not a "more is better" compound.
- **Additive antidepressant/serotonergic interaction:** given the proposed serotonin-reuptake/MAO mechanism, combining saffron with SSRIs/MAOIs/TCAs carries a theoretical additive serotonergic risk; mechanistically plausible but not well quantified in controlled human studies.
- **Cardiovascular/hemostatic:** theoretical additive effects with antihypertensives and antiplatelet/anticoagulant drugs are frequently cited but not established in controlled human trials (unsourced beyond general/preclinical reports).

This section is research metadata, not medical advice.

## Open questions
- **Independent international replication:** can the SSRI-comparable antidepressant effect be reproduced in large, adequately powered RCTs run *outside* the few Iranian centers that dominate the literature? This is the central unresolved question driving the grade-down to 3.
- **Mechanism confirmation:** the serotonin-reuptake / MAO-inhibition / BDNF mechanisms are preclinical — no human study links a defined molecular mechanism to the observed mood effect.
- **Standardization & pharmacokinetics:** crocin/safranal content varies by extract; crocin absorption (hydrolysis to crocetin), half-life, and dose-response in humans are poorly characterized.
- **Cognitive/AD efficacy:** MCI/AD trials are few, small, and largely single-region; whether saffron is disease-modifying vs symptomatic, and durable beyond ~22-52 weeks, is unknown.
- **Long-term safety & populations:** durability beyond a few months, healthy-population (non-depressed) effects, pediatric ADHD confirmation, and interaction risk with antidepressants all need dedicated study.
