# Brain Optimization Research — Master Index & Status Board

A structured, literature-graded research base on optimising brain health and
performance, via compounds and habits. See [`BRIEF.md`](./BRIEF.md) for the full
workflow, [`taxonomy.md`](./taxonomy.md) for the 12 neural channels, and
[`rubric.md`](./rubric.md) for the evidence grading.

**Status legend:** `draft` → `reviewed` → `verified`
**Evidence badge:** 1 (preclinical) · 2 (emerging) · 3 (good) · 4 (strong)

## Phase progress

- [x] **Phase 0 — Scaffold.** Directory tree, taxonomy, rubric, template, this board.
- [~] **Phase 1 — Compound track** (Track A) — **63 of seed list done**, ongoing.
- [ ] **Phase 2 — Habit track** (Track B).
- [ ] **Phase 3 — Cross-link** — generate `synthesis/channel-matrix.json` + `channel-briefs.md`.
- [ ] **Phase 4 — Synthesis** — `synthesis/stacks-by-goal.md`.
- [ ] **Phase 5 — Review pass** — dedupe, verify citations, flip statuses.

## Track A — Compounds

_63 entries. All `draft` pending Phase 5 review. Evidence = `evidence_overall` badge._

| id | Name | klass | Evidence | Status | Channels (grade) |
|----|------|-------|:--------:|:------:|------------------|
| [caffeine-l-theanine](./compounds/caffeine-l-theanine.md) | Caffeine + L-theanine | Stimulant + relaxant synergy | 3 | draft | ne(3), cbf(3↓), da(2), gaba(2), glu(2) |
| [citicoline](./compounds/citicoline.md) | Citicoline (CDP-choline) | Cholinergic | 3 | draft | ach(2), ntrophic(2), da(1) |
| [creatine](./compounds/creatine.md) | Creatine monohydrate | Neuroenergetic | 3 | draft | mito(3) |
| [l-theanine](./compounds/l-theanine.md) | L-Theanine | Relaxant / glutamate analogue | 3 | draft | hpa(3), gaba(2), glu(2) |
| [alpha-gpc](./compounds/alpha-gpc.md) | Alpha-GPC | Cholinergic | 3 | draft | ach(3), ntrophic(2) |
| [bacopa-monnieri](./compounds/bacopa-monnieri.md) | Bacopa monnieri | Botanical memory | 3 | draft | ach(2), ntrophic(1), inflam(1) |
| [lions-mane](./compounds/lions-mane.md) | Lion's Mane | Botanical neurotrophic | 2 | draft | ntrophic(2), ser(1), inflam(1) |
| [omega-3-epa-dha](./compounds/omega-3-epa-dha.md) | Omega-3 (EPA/DHA) | Structural lipid / anti-inflammatory | 2 | draft | ser(3, impaired), inflam(2), ntrophic(2) |
| [rhodiola-rosea](./compounds/rhodiola-rosea.md) | Rhodiola rosea | Adaptogen | 2 | draft | hpa(2), mito(2), ser(1), da(1), ne(1) |
| [phosphatidylserine](./compounds/phosphatidylserine.md) | Phosphatidylserine | Phospholipid / cholinergic | 2 | draft | ntrophic(2), ach(2), hpa(2↓) |
| [huperzine-a](./compounds/huperzine-a.md) | Huperzine A | Cholinergic (AChE inhibitor) | 2 | draft | ach(3), glu(1↓) |
| [acetyl-l-carnitine](./compounds/acetyl-l-carnitine.md) | Acetyl-L-Carnitine (ALCAR) | Neuroenergetic | 2 | draft | mito(2), ach(2), ntrophic(1) |
| [alpha-lipoic-acid](./compounds/alpha-lipoic-acid.md) | Alpha-Lipoic Acid | Mitochondrial / antioxidant | 2 | draft | mito(2), inflam(2↓) |
| [pqq](./compounds/pqq.md) | PQQ | Mitochondrial / antioxidant | 2 | draft | mito(2), inflam(2↓), cbf(2), ntrophic(1) |
| [coq10-ubiquinol](./compounds/coq10-ubiquinol.md) | CoQ10 / Ubiquinol | Mitochondrial | 1 | draft | mito(1), inflam(1↓) |
| [dmae](./compounds/dmae.md) | DMAE | Cholinergic (disputed) | 1 | draft | ach(1) |
| [ashwagandha](./compounds/ashwagandha.md) | Ashwagandha | Adaptogen | 3 | draft | hpa(3↓), gaba(2), ntrophic(2) |
| [saffron](./compounds/saffron.md) | Saffron (Crocus sativus) | Botanical mood | 3 | draft | ser(2), inflam(2↓), da(1) |
| [panax-ginseng](./compounds/panax-ginseng.md) | Panax ginseng | Adaptogen | 2 | draft | cbf(2), ach(1), mito(1), inflam(1↓) |
| [ginkgo-biloba](./compounds/ginkgo-biloba.md) | Ginkgo biloba (EGb 761) | Botanical circulation | 2 | draft | cbf(2), inflam(1), ach(1) |
| [curcumin](./compounds/curcumin.md) | Curcumin | Polyphenol / anti-inflammatory | 2 | draft | inflam(2↓), ser(2), ntrophic(1) |
| [gotu-kola](./compounds/gotu-kola.md) | Gotu kola (Centella asiatica) | Botanical | 2 | draft | hpa(2), ntrophic(1), inflam(1↓), gaba(1) |
| [eleuthero](./compounds/eleuthero.md) | Eleuthero | Adaptogen | 2 | draft | hpa(2), mito(1) |
| [holy-basil](./compounds/holy-basil.md) | Holy basil (Tulsi) | Adaptogen | 2 | draft | hpa(2), inflam(2↓), gaba(1) |
| [l-tyrosine](./compounds/l-tyrosine.md) | L-Tyrosine (NALT) | NT precursor (catecholamine) | 3 | draft | da(3), ne(3) — conditional on acute stress |
| [l-tryptophan-5-htp](./compounds/l-tryptophan-5-htp.md) | L-Tryptophan / 5-HTP | NT precursor (serotonin) | 2 | draft | ser(2), glymph(2) |
| [taurine](./compounds/taurine.md) | Taurine | Inhibitory neuromodulator | 2 | draft | gaba(2↓), inflam(1↓) |
| [glycine](./compounds/glycine.md) | Glycine | Amino acid (sleep / NMDA) | 2 | draft | glu(2), gaba(1), cbf(1) |
| [gaba](./compounds/gaba.md) | GABA (oral) | Inhibitory (BBB-disputed) | 2 | draft | gaba(2), hpa(2↓) |
| [magnesium-l-threonate](./compounds/magnesium-l-threonate.md) | Magnesium L-threonate | Mineral | 2 | draft | glu(2), ntrophic(1), gaba(1) |
| [zinc](./compounds/zinc.md) | Zinc | Mineral (cofactor) | 2 | draft | glu(3), inflam(2↓), ser(2), ntrophic(1) |
| [b-vitamins-homocysteine](./compounds/b-vitamins-homocysteine.md) | B6 / Folate / B12 (homocysteine) | Vitamin cofactor | 2 | draft | cbf(3), inflam(2↓), mito(1) |
| [iron](./compounds/iron.md) | Iron (if deficient) | Mineral (deficiency) | 3 | draft | da(3), mito(2) |
| [vitamin-d3](./compounds/vitamin-d3.md) | Vitamin D3 | Vitamin (deficiency) | 2 | draft | ntrophic(2), inflam(2) |
| [vitamin-c](./compounds/vitamin-c.md) | Vitamin C | Vitamin / antioxidant | 2 | draft | ne(2), inflam(2), da(1) |
| [vitamin-e](./compounds/vitamin-e.md) | Vitamin E | Antioxidant | 2 | draft | inflam(2) |
| [nicotinamide-riboside](./compounds/nicotinamide-riboside.md) | Nicotinamide Riboside | NAD⁺ precursor | 2 | draft | mito(2), ntrophic(1) |
| [methylene-blue](./compounds/methylene-blue.md) | Methylene blue (low-dose) | Mitochondrial (research-grade) | 2 | draft | mito(2), cbf(2), inflam(1↓) |
| [nmn](./compounds/nmn.md) | NMN | NAD⁺ precursor | 1 | draft | mito(2), ntrophic(1) |
| [choline-bitartrate](./compounds/choline-bitartrate.md) | Choline bitartrate | Cholinergic (poor CNS delivery) | 1 | draft | ach(1), ntrophic(1) |
| [sage](./compounds/sage.md) | Sage (Salvia officinalis/lavandulaefolia) | Botanical (AChE) | 2 | draft | ach(3), inflam(1) |
| [vinpocetine](./compounds/vinpocetine.md) | Vinpocetine | Vasoactive (Rx-adjacent) | 2 | draft | cbf(2), inflam(2↓) |
| [resveratrol](./compounds/resveratrol.md) | Resveratrol | Polyphenol | 2 | draft | cbf(3), inflam(1↓), mito(1) |
| [egcg](./compounds/egcg.md) | EGCG (green tea catechin) | Polyphenol / catechin | 2 | draft | inflam(2↓), cbf(2), gaba(2), da(1) |
| [schisandra](./compounds/schisandra.md) | Schisandra chinensis | Adaptogen | 2 | draft | hpa(2), inflam(2↓), ach(2) |
| [lecithin](./compounds/lecithin.md) | Lecithin / Phosphatidylcholine | Cholinergic (dietary) | 1 | draft | ach(1), ntrophic(1) |
| [pterostilbene](./compounds/pterostilbene.md) | Pterostilbene | Polyphenol | 1 | draft | inflam(2↓), ntrophic(1) |
| [cordyceps](./compounds/cordyceps.md) | Cordyceps | Mushroom / adaptogen | 1 | draft | mito(2), inflam(2↓) |
| [aniracetam](./compounds/aniracetam.md) | Aniracetam *(research-grade)* | Racetam (AMPA PAM) | 2 | draft | glu(3), ach(2), da(2), ser(2) |
| [piracetam](./compounds/piracetam.md) | Piracetam *(research-grade)* | Racetam | 2 | draft | glu(2), cbf(2), mito(2) |
| [oxiracetam](./compounds/oxiracetam.md) | Oxiracetam *(research-grade)* | Racetam | 2 | draft | glu(2), ach(2), cbf(1) |
| [phenylpiracetam](./compounds/phenylpiracetam.md) | Phenylpiracetam *(research-grade, WADA-banned)* | Racetam (stimulant) | 2 | draft | da(2), ne(2), glu(1) |
| [noopept](./compounds/noopept.md) | Noopept *(research-grade)* | Peptide-analog nootropic | 2 | draft | ntrophic(2), glu(2), inflam(2↓) |
| [pramiracetam](./compounds/pramiracetam.md) | Pramiracetam *(research-grade)* | Racetam | 1 | draft | ach(2), glu(1) |
| [coluracetam](./compounds/coluracetam.md) | Coluracetam *(investigational)* | Racetam (HACU) | 1 | draft | ach(1) |
| [amphetamine-methylphenidate](./compounds/amphetamine-methylphenidate.md) | Amphetamine / Methylphenidate *(Rx, Schedule II)* | Stimulant | 4 | draft | da(4 imp / 3 healthy), ne(4 imp / 3 healthy) |
| [modafinil](./compounds/modafinil.md) | Modafinil *(Rx)* | Eugeroic | 3 | draft | da(3), ne(2) |
| [nicotine](./compounds/nicotine.md) | Nicotine (non-smoked) | nAChR agonist | 3 | draft | ach(4), da(4), ne(2) |
| [armodafinil](./compounds/armodafinil.md) | Armodafinil *(Rx)* | Eugeroic | 2 | draft | da(2), ne(2) |
| [adrafinil](./compounds/adrafinil.md) | Adrafinil *(research-grade, WADA)* | Eugeroic prodrug | 2 | draft | ne(2), da(2) |
| [centrophenoxine](./compounds/centrophenoxine.md) | Centrophenoxine *(research-grade)* | Cholinergic / antioxidant | 2 | draft | ach(2), inflam(2↓) |
| [krill-oil](./compounds/krill-oil.md) | Krill oil | Omega-3 (phospholipid) | 2 | draft | ntrophic(2), inflam(2↓) |
| [algal-dha](./compounds/algal-dha.md) | Algal DHA (vegan) | Omega-3 (structural) | 2 | draft | ntrophic(2), inflam(2) |

_Seed queue (remaining):_ melatonin · apigenin · spermidine · fisetin · sulforaphane · lithium ·
probiotics · prebiotic-fiber · semax · selank · cerebrolysin · dihexa · psilocybin (full set in `BRIEF.md` §8A)

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
