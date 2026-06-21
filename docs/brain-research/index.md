# Brain Optimization Research — Master Index & Status Board

A structured, literature-graded research base on optimising brain health and
performance, via compounds and habits. See [`BRIEF.md`](./BRIEF.md) for the full
workflow, [`taxonomy.md`](./taxonomy.md) for the 12 neural channels, and
[`rubric.md`](./rubric.md) for the evidence grading.

**Status legend:** `draft` → `reviewed` → `verified`
**Evidence badge:** 1 (preclinical) · 2 (emerging) · 3 (good) · 4 (strong)

## Phase progress

- [x] **Phase 0 — Scaffold.** Directory tree, taxonomy, rubric, template, this board.
- [~] **Phase 1 — Compound track** (Track A) — **8 of seed list done**, ongoing.
- [ ] **Phase 2 — Habit track** (Track B).
- [ ] **Phase 3 — Cross-link** — generate `synthesis/channel-matrix.json` + `channel-briefs.md`.
- [ ] **Phase 4 — Synthesis** — `synthesis/stacks-by-goal.md`.
- [ ] **Phase 5 — Review pass** — dedupe, verify citations, flip statuses.

## Track A — Compounds

_8 entries. All `draft` pending Phase 5 review. Evidence = `evidence_overall` badge._

| id | Name | klass | Evidence | Status | Channels (grade) |
|----|------|-------|:--------:|:------:|------------------|
| [caffeine-l-theanine](./compounds/caffeine-l-theanine.md) | Caffeine + L-theanine | Stimulant + relaxant synergy | 3 | draft | ne(3), cbf(3↓), da(2), gaba(2), glu(2) |
| [citicoline](./compounds/citicoline.md) | Citicoline (CDP-choline) | Cholinergic | 3 | draft | ach(2), ntrophic(2), da(1) |
| [creatine](./compounds/creatine.md) | Creatine monohydrate | Neuroenergetic | 3 | draft | mito(3) |
| [l-theanine](./compounds/l-theanine.md) | L-Theanine | Relaxant / glutamate analogue | 3 | draft | hpa(3), gaba(2), glu(2) |
| [bacopa-monnieri](./compounds/bacopa-monnieri.md) | Bacopa monnieri | Botanical memory | 3 | draft | ach(2), ntrophic(1), inflam(1) |
| [lions-mane](./compounds/lions-mane.md) | Lion's Mane | Botanical neurotrophic | 2 | draft | ntrophic(2), ser(1), inflam(1) |
| [omega-3-epa-dha](./compounds/omega-3-epa-dha.md) | Omega-3 (EPA/DHA) | Structural lipid / anti-inflammatory | 2 | draft | ser(3, impaired), inflam(2), ntrophic(2) |
| [rhodiola-rosea](./compounds/rhodiola-rosea.md) | Rhodiola rosea | Adaptogen | 2 | draft | hpa(2), mito(2), ser(1), da(1), ne(1) |

_Seed queue (next):_ alpha-gpc · phosphatidylserine · ginkgo-biloba · panax-ginseng ·
ashwagandha · acetyl-l-carnitine · l-tyrosine · magnesium-l-threonate · huperzine-a ·
vitamin-d3 · b-vitamins (B6/folate/B12) · curcumin · … (full set in `BRIEF.md` §8A)

## Track B — Habits

_No entries yet._

| id | Name | klass | Evidence | Status | Channels |
|----|------|-------|:--------:|:------:|----------|
| –  | –    | –     | –        | –      | –        |

## Synthesis artifacts

| File | Purpose | Status |
|------|---------|:------:|
| `synthesis/channel-matrix.json` | Aggregated agent×channel — regenerates the Atlas | pending |
| `synthesis/channel-briefs.md` | Per-channel: what moves it, ranked; convergence + gaps | pending |
| `synthesis/stacks-by-goal.md` | Minimum-effective levers per goal | pending |
