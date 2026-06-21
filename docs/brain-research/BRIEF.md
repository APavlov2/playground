# Brain Optimization Research — Claude Code Workflow Brief

> **How to use this file**
> Save it as `docs/brain-research/BRIEF.md` in a repo and open Claude Code with:
> *"Read `docs/brain-research/BRIEF.md` and start Phase 0."*
> Or paste the whole thing as your opening message. It is the portable context + workflow handoff from the planning session.

---

## 1. Objective & scope

Build a structured, literature-graded research base on **how to optimise brain health and keep the brain performing at its best** — through both supplementation and lifestyle. This is a **research study**, not a personal protocol. Optimise for *completeness first*, then mechanism clarity, then honest evidence grading.

Strength training is taken as the established #1 lever (neurogenesis via BDNF/IGF-1). The study maps everything *around and beyond* that: the full landscape of compounds and habits, the neural pathway each acts through, and how strong the evidence actually is.

Two tracks, worked **in parallel and cross-linked**:
- **Track A — Compounds** (supplements, nutrients, and research/Rx nootropics, flagged as such)
- **Track B — Habits** (exercise, sleep, diet, hormetic, cognitive, environmental, device-based)

The point of cross-linking is the synthesis: many habits and compounds converge on the *same* neural channels. That convergence map is the real output.

---

## 2. Operating principles (research stance)

1. **Mechanism-first.** Every entry must name the molecular/physiological pathway, not just the claimed benefit.
2. **Evidence-graded, honestly.** Use the rubric in §6. Do not inflate. Preclinical stays preclinical. "Popular" is not evidence.
3. **Population matters.** Distinguish effects in *healthy/optimising* subjects vs *deficient/impaired* subjects — many compounds only help when correcting a deficit.
4. **Cite real sources.** Prefer meta-analyses, RCTs, and primary literature over blog roundups. No invented citations — if you can't find support, mark the claim `unsourced` and move on.
5. **Neutral and complete.** Include prescription and research-grade compounds for completeness, clearly flagged. Safety/interaction fields are *research metadata*, not medical advice.
6. **Single source of truth.** The structured `channels[]` blocks across all entries (see §5) are the data that regenerates the **Neural Effects Atlas** visualisation. Keep `channel` ids in sync with §4.

---

## 3. The neural-channel taxonomy (12) — shared with the Atlas

Every effect is mapped to one or more of these channels. Use these exact ids.

| id | Channel | Cognitive/functional domain |
|----|---------|------------------------------|
| `ach` | Cholinergic (ACh) | Encoding, attention, memory |
| `da` | Dopaminergic | Drive, working memory, executive function |
| `ser` | Serotonergic | Mood, affect, impulse control |
| `glu` | Glutamatergic / NMDA | Synaptic plasticity, LTP, learning |
| `gaba` | GABAergic | Inhibition, calm, anxiolysis |
| `ne` | Noradrenergic | Arousal, vigilance, alertness |
| `cbf` | Cerebral blood flow | Perfusion, O₂ & nutrient delivery |
| `mito` | Mitochondrial / bioenergetic | ATP supply, metabolic resilience |
| `ntrophic` | Neurotrophic / neurogenesis | BDNF/NGF, growth & repair |
| `inflam` | Neuroinflammation / oxidative | Microglial tone, ROS control |
| `glymph` | Glymphatic / sleep clearance | Waste, amyloid/tau clearance |
| `hpa` | HPA axis / stress | Cortisol regulation, allostatic load |

> Channels are intentionally orthogonal-ish but overlap is expected (e.g. exercise hits `ntrophic` + `mito` + `cbf`). That overlap is the signal.

---

## 4. Entry schema

One markdown file per agent, in YAML frontmatter + body. Frontmatter is the machine-readable layer (feeds retrieval + regenerates the Atlas); the body is the human reading layer with prose + citations.

```yaml
---
id: citicoline                 # slug, unique
name: Citicoline (CDP-choline)
aliases: [cytidine diphosphate-choline]
type: compound                 # compound | habit
klass: Cholinergic             # short category label
status: draft                  # draft | reviewed | verified
evidence_overall: 3            # 1–4, see rubric; the badge value
onset: "1–3 hours (acute); weeks (cumulative)"
half_life: "~varies"
dose_range: "250–500 mg/day"
cognitive_domains: [attention, memory, processing-speed]
channels:                      # SOURCE OF TRUTH for the Atlas
  - channel: ach
    mechanism: "Donates choline for acetylcholine synthesis"
    evidence: 3
    population: both           # healthy | deficient | impaired | both
    direction: up              # up | down | modulate
  - channel: ntrophic
    mechanism: "Supplies phosphatidylcholine for membrane repair"
    evidence: 2
    population: both
    direction: up
safety:
  contraindications: []
  interactions: []
  notable_risks: []
sources:                       # real refs only
  - "Author et al., Journal, Year — PMID/DOI"
tags: [nootropic, choline]
---

## Summary
2–4 sentences: what it is, primary effect, who it helps.

## Mechanism
Per-channel detail, expanded from the frontmatter.

## Evidence
What the human literature actually shows. Note study quality, population, effect size, and where it's preclinical-only.

## Safety & interactions (research metadata)
Contraindications, known interactions, notable signals.

## Open questions
What's unresolved / worth a deeper dive.
```

---

## 5. Evidence rubric (1–4)

| Score | Label | Bar |
|-------|-------|-----|
| **4** | Strong | Consistent meta-analyses / well-established human effect |
| **3** | Good | Multiple human RCTs pointing the same way |
| **2** | Emerging | Limited/mixed human data **or** strong preclinical only |
| **1** | Preclinical / anecdotal | Mechanistic, animal, or anecdotal; minimal human support |

Grade **per channel** in `channels[].evidence`, and set `evidence_overall` to the agent's best-supported, most relevant claim (this drives the Atlas badge). When in doubt, grade down and say why in the body.

---

## 6. Repository structure

```
docs/brain-research/
├── BRIEF.md                 # this file
├── taxonomy.md              # the 12 channels (§3), expanded
├── rubric.md                # the evidence rubric (§5)
├── _template.md             # the schema (§4) as a blank entry
├── compounds/               # Track A — one file per agent
│   ├── creatine.md
│   ├── citicoline.md
│   └── ...
├── habits/                  # Track B — one file per agent
│   ├── resistance-training.md
│   └── ...
├── synthesis/
│   ├── channel-matrix.json  # aggregated agent×channel — regenerates the Atlas
│   ├── channel-briefs.md    # per-channel: what moves it, ranked
│   └── stacks-by-goal.md    # memory / focus / mood / resilience / neuroprotection
└── index.md                 # master list + status board
```

`synthesis/channel-matrix.json` shape (this is what the Atlas reads):

```json
{
  "channels": [{ "id": "ach", "name": "...", "domain": "...", "color": "#F4B63A" }],
  "agents": [
    {
      "id": "citicoline", "name": "Citicoline (CDP-choline)",
      "type": "compound", "klass": "Cholinergic", "ev": 3,
      "ch": { "ach": "Donates choline for ACh synthesis", "ntrophic": "..." }
    }
  ]
}
```

---

## 7. Workflow phases

**Phase 0 — Scaffold.** Create the directory tree, `taxonomy.md`, `rubric.md`, `_template.md`, and an empty `index.md` status board. Confirm structure, then stop for review.

**Phase 1 — Compound track.** Work the seed list (§8 A) **one agent at a time**. For each: search primary literature → populate the schema → grade every channel with a citation → write the body. Commit per agent. Keep `index.md` updated.

**Phase 2 — Habit track.** Same process for §8 B. Habits often have stronger human/epidemiological evidence — grade accordingly.

**Phase 3 — Cross-link.** Generate `synthesis/channel-matrix.json` by aggregating all `channels[]` blocks. Then in `channel-briefs.md`, for each of the 12 channels list every agent that hits it, ranked by evidence — and flag **convergence** (channels driven by *both* a potent habit and a well-evidenced compound) and **gaps** (channels with thin coverage).

**Phase 4 — Synthesis.** Write `stacks-by-goal.md`: for each goal (memory, focus/executive, mood, stress-resilience, long-term neuroprotection), the minimum-effective set of levers ranked by evidence-adjusted impact, habits first.

**Phase 5 — Review pass.** Dedupe, verify every citation resolves, downgrade unsupported claims, sanity-check dose ranges, flip `status` to `reviewed`/`verified`.

---

## 8. Seed catalog

Starting set from the planning session. Add to it; don't treat as exhaustive.

### A. Compounds

**Cholinergics** — Citicoline (CDP-choline), Alpha-GPC, Choline bitartrate, Phosphatidylcholine/lecithin, Phosphatidylserine, Huperzine A, DMAE, Centrophenoxine, Nicotine (non-smoked)

**Racetams & synthetics** *(research-grade)* — Piracetam, Aniracetam, Oxiracetam, Pramiracetam, Phenylpiracetam, Noopept, Coluracetam

**Eugeroics** *(Rx)* — Modafinil, Armodafinil, Adrafinil

**Stimulants** — Caffeine (+ L-theanine), Amphetamines/methylphenidate *(Rx)*

**Adaptogens** — Rhodiola rosea, Ashwagandha, Panax ginseng, Eleuthero, Holy basil, Schisandra, Cordyceps

**Botanical memory/circulation** — Bacopa monnieri, Ginkgo biloba, Lion's Mane, Gotu kola, Vinpocetine, Sage, Saffron, Curcumin, Resveratrol, Pterostilbene, EGCG

**Neurotransmitter precursors** — L-Tyrosine/NALT, L-Theanine, L-Tryptophan/5-HTP, Taurine, Glycine, GABA

**Neuroenergetics / mitochondrial** — Creatine, Acetyl-L-Carnitine (ALCAR), CoQ10/Ubiquinol, PQQ, Alpha-Lipoic Acid, NMN, Nicotinamide Riboside, Methylene blue (low-dose)

**Omega-3 / structural lipids** — EPA/DHA (fish oil), Krill oil, Algal DHA

**Vitamins / minerals (cofactors)** — B6, Folate, B12 (homocysteine), Vitamin D3, Magnesium (esp. L-threonate), Zinc, Iron (if deficient), Vitamin E, Vitamin C

**Longevity-adjacent** — Spermidine, Fisetin, Sulforaphane, Lithium (low-dose)

**Sleep / circadian** — Melatonin, Apigenin, Glycine, Magnesium

**Gut-brain** — Probiotics (psychobiotics), Prebiotic fiber

**Emerging / experimental** *(research-only, varying legality)* — Semax, Selank, Cerebrolysin, Dihexa, Psilocybin (microdosing)

### B. Habits / lifestyle

**Exercise** — Resistance training, Zone 2 aerobic, HIIT, Skill/coordination-based

**Sleep** — Duration & quality, Deep (slow-wave) sleep, Circadian consistency

**Diet** — Mediterranean/MIND, Time-restricted eating/fasting, Ketogenic, Polyphenol-rich intake

**Cognitive/neuroplastic** — Novel skill acquisition, Language/instrument, Cognitive challenge & novelty

**Stress/mental** — Meditation, Breathwork, Nature exposure, Social connection

**Hormetic/environmental** — Sunlight & circadian light, Sauna/heat, Cold exposure, Hydration, Avoiding neurotoxins (alcohol, smoking), Treating hearing loss

**Devices/modalities** — Photobiomodulation (red/NIR), tDCS/tACS, TMS, Neurofeedback, Vagus nerve stimulation

---

## 9. Definition of done (per entry)

- [ ] Frontmatter complete and valid; `channel` ids match §3
- [ ] Every `channels[]` entry has a mechanism, an evidence score, and a population
- [ ] At least one real, resolvable source per non-trivial claim (or `unsourced` flag)
- [ ] Body distinguishes healthy-subject vs deficiency-correction effects
- [ ] Safety/interaction metadata filled (or explicitly `none known`)
- [ ] `status` advanced and `index.md` updated

---

## 10. Guardrails

- This is a **literature study**. Do not frame output as personal medical advice or a recommended regimen for any individual.
- Grade evidence **down** under uncertainty and state the reason.
- Never fabricate citations, PMIDs, or effect sizes. Missing support → mark it missing.
- Keep prescription/research-grade compounds clearly labelled as such throughout.
