# Metabolic + Cardiac Recovery — Research Workflow Brief

> **How to use this file**
> This brief turns the personal [`PLAN.md`](./PLAN.md) into a structured,
> literature-graded research base, using the same methodology as the
> sibling `docs/brain-research/` study. Open Claude Code with:
> *"Read `docs/recovery-plan/BRIEF.md` and start Phase 1."*

---

## 1. Objective & scope

Build a structured, evidence-graded research base on **reversing the connected
cluster of fatty liver (MASLD) → insulin resistance → obesity → cardiovascular
risk**, through supplementation and lifestyle — *while staying safe for a specific
cardiac picture* (beta-blockade with nebivolol, monomorphic PVCs, exaggerated BP
response to exertion).

This is a **research study built around an existing personal plan** ([`PLAN.md`](./PLAN.md)),
not new medical advice. Optimise for *completeness first*, then mechanism clarity,
then honest evidence grading. The master lever — **visceral fat loss** — is taken
as established; the study maps every supporting lever around it: the metabolic /
cardiac pathway each acts through, how strong the evidence is, and **its cardiac
safety profile under these specific constraints**.

Two tracks, worked **in parallel and cross-linked**:
- **Track A — Compounds** (supplements; prescription items such as GLP-1 agonists
  flagged as such)
- **Track B — Habits** (diet, activity, sleep, stress, daily movement)

The point of cross-linking is the synthesis: many habits and compounds converge on
the *same* metabolic/cardiac channels. That convergence map — and the **cardiac
safety overlay** — is the real output.

---

## 2. Operating principles (research stance)

1. **Mechanism-first.** Every entry names the molecular/physiological pathway
   (e.g. AMPK activation, hepatic de novo lipogenesis, GLUT4 translocation), not
   just the claimed benefit.
2. **Evidence-graded, honestly.** Use the rubric in `rubric.md`. Preclinical stays
   preclinical. "Popular" is not evidence.
3. **Cardiac-safety overlay is first-class.** Every entry carries a `cardiac_safety`
   field: interactions with nebivolol/beta-blockade, BP effects, rhythm/PVC signals,
   and hepatic load. This is the constraint that makes this study different from a
   generic metabolic one.
4. **Population matters.** Distinguish effects in the target picture (MASLD +
   insulin resistance + obesity) from effects in already-healthy subjects.
5. **Cite real sources.** Prefer meta-analyses, RCTs, and primary literature. No
   invented citations — mark unsupported claims `unsourced` and move on.
6. **Single source of truth.** The structured `channels[]` blocks across all
   entries regenerate the **Metabolic–Cardiac Atlas** visualisation. Keep `channel`
   ids in sync with `taxonomy.md`.

> This is a literature study layered on a personal plan. It does **not** replace the
> cardiologist sign-off the plan itself calls for — safety fields are research
> metadata, not clearance.

---

## 3. The metabolic–cardiac channel taxonomy (12)

See [`taxonomy.md`](./taxonomy.md) for the full list and notes. Every effect maps
to one or more of: `insulin`, `liver`, `lipid`, `bp`, `rhythm`, `ampk`, `mito`,
`inflam`, `adipos`, `muscle`, `circadian`, `stress`. Use these exact ids.

---

## 4. Entry schema

One markdown file per lever (YAML frontmatter + body). Frontmatter is the
machine-readable layer; the body is the human reading layer with prose + citations.
See [`_template.md`](./_template.md) for the blank entry. The schema mirrors the
brain study's, **plus** a `cardiac_safety` block and a `tier` field (1 / 2 /
optional / avoid) that maps to the plan's own tiering.

---

## 5. Evidence rubric (1–4)

Identical scale to the brain study — see [`rubric.md`](./rubric.md). Grade **per
channel** in `channels[].evidence`; set `evidence_overall` to the best-supported,
most relevant claim. When in doubt, grade down and say why.

---

## 6. Repository structure

```
docs/recovery-plan/
├── PLAN.md                 # the source personal plan (seed content)
├── BRIEF.md                # this file
├── taxonomy.md             # the 12 metabolic-cardiac channels
├── rubric.md               # the evidence rubric
├── _template.md            # the schema as a blank entry
├── compounds/              # Track A — one file per supplement / Rx item
│   ├── berberine.md
│   ├── omega-3.md
│   └── ...
├── habits/                 # Track B — one file per habit
│   ├── zone-2-cardio.md
│   ├── post-meal-walks.md
│   └── ...
├── synthesis/
│   ├── channel-matrix.json # aggregated lever×channel — regenerates the Atlas
│   ├── channel-briefs.md   # per-channel: what moves it, ranked
│   ├── cardiac-safety.md   # the safety overlay: what needs sign-off and why
│   └── plan-by-phase.md    # Week 1 / Tier 1 / Tier 2 sequencing, evidence-ranked
└── index.md                # master list + status board
```

`synthesis/channel-matrix.json` mirrors the brain study's shape: a `channels[]`
array (id/name/domain/color) and an `agents[]` array, each with `id`, `name`,
`type`, `tier`, `ev`, and a `ch` map of channel→mechanism.

---

## 7. Workflow phases

**Phase 0 — Scaffold.** *(done)* Directory tree, `PLAN.md`, `taxonomy.md`,
`rubric.md`, `_template.md`, empty `index.md` status board.

**Phase 1 — Compound track.** Work the seed list (§8 A) **one lever at a time**.
For each: search primary literature → populate the schema → grade every channel
with a citation → fill `cardiac_safety` → write the body. Commit per entry. Keep
`index.md` updated.

**Phase 2 — Habit track.** Same process for §8 B. Habits here often have the
stronger evidence (Mediterranean diet, Zone-2, post-meal walks) — grade accordingly.

**Phase 3 — Cross-link.** Generate `synthesis/channel-matrix.json`; in
`channel-briefs.md`, for each channel list every lever that hits it, ranked by
evidence, flagging **convergence** and **gaps**. Build `cardiac-safety.md` as the
overlay: every lever with a BP / rhythm / hepatic / beta-blocker interaction.

**Phase 4 — Synthesis.** Write `plan-by-phase.md`: the minimum-effective,
evidence-ranked sequence — Week 1 wins, then Tier 1, then Tier 2 (sign-off-gated) —
habits first.

**Phase 5 — Review pass.** Dedupe, verify every citation resolves, downgrade
unsupported claims, sanity-check dose ranges, flip `status` to `reviewed`/`verified`.

---

## 8. Seed catalog

Starting set from `PLAN.md`. Add to it; don't treat as exhaustive.

### A. Compounds

**Tier 1 (foundational)** — Magnesium (glycinate/citrate), Omega-3 (EPA/DHA),
Vitamin D3

**Tier 2 (sign-off required)** — Berberine, Myo-inositol

**Optional (training)** — Creatine monohydrate, Coffee (black)

**Prescription (doctor's call)** — GLP-1 agonists

**Avoid / caution** — High-dose green tea extract (EGCG), stimulant fat-burners /
high-caffeine pre-workouts, licorice root, ashwagandha

### B. Habits / lifestyle

**Diet** — Mediterranean base, high protein, whole intact grains, legumes; avoid
added sugar/fructose, refined carbs, ultra-processed foods, alcohol, excess salt,
processed/cured meats

**Activity** — Zone-2 cardio (RPE/talk-test, not HR), post-meal walks, full-body
strength (no Valsalva), daily movement / step target; HIIT *only after clearance*

**Supporting pillars** — Sleep quality + sleep-apnea screening, stress / vagal-load
management, hydration

**Tracking** — Weekly weight + waist + resting BP + training RPE; periodic liver
enzymes + metabolic panel; Holter-set intensity ceiling

---

## 9. Definition of done (per entry)

- [ ] Frontmatter complete and valid; `channel` ids match `taxonomy.md`
- [ ] Every `channels[]` entry has a mechanism, an evidence score, and a population
- [ ] `cardiac_safety` filled: BP / rhythm / hepatic / beta-blocker interaction (or `none known`)
- [ ] `tier` set (1 | 2 | optional | rx | avoid)
- [ ] At least one real, resolvable source per non-trivial claim (or `unsourced`)
- [ ] `status` advanced and `index.md` updated

---

## 10. Guardrails

- This is a **literature study layered on a personal plan**. It does not replace the
  cardiologist sign-off the plan calls for, and is not generic medical advice.
- The **cardiac constraints are load-bearing**: never grade a lever "safe" without
  addressing BP, rhythm/PVC, hepatic load, and the nebivolol interaction.
- Grade evidence **down** under uncertainty and state the reason.
- Never fabricate citations, PMIDs, or effect sizes. Missing support → mark it.
- Keep prescription / sign-off-gated items clearly labelled as such throughout.
