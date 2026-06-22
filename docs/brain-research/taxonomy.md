# Neural-Channel Taxonomy (12)

The shared vocabulary for this study. Every effect — from a compound or a habit —
is mapped to one or more of these **channels**. The `channel` ids below are the
single source of truth: they must match the `channels[].channel` ids in every
entry's frontmatter and the keys in `synthesis/channel-matrix.json`.

Channels are intentionally *orthogonal-ish*. Overlap is expected and is itself the
signal — when a potent habit and a well-evidenced compound both drive the same
channel, that convergence is the real output of the study (see Phase 3).

| id | Channel | Cognitive / functional domain |
|----|---------|-------------------------------|
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

## Channel notes

- **`ach` — Cholinergic.** The acetylcholine system. Core to encoding new
  information, sustained attention, and memory consolidation. Targeted by choline
  donors, acetylcholinesterase inhibitors, and muscarinic/nicotinic modulators.
- **`da` — Dopaminergic.** Drives motivation, reward prediction, working memory,
  and executive control. Precursors, reuptake inhibitors, and tyrosine availability
  act here.
- **`ser` — Serotonergic.** Mood, affect regulation, satiety, impulse control.
  Tryptophan/5-HTP availability and receptor modulation act here.
- **`glu` — Glutamatergic / NMDA.** The primary excitatory system; the substrate
  of long-term potentiation (LTP) and learning. Over-activity is excitotoxic, so
  `direction` matters — `modulate` is often the goal, not `up`.
- **`gaba` — GABAergic.** The primary inhibitory system. Calm, anxiolysis, sleep
  onset, and the inhibitory tone that lets signal stand out from noise.
- **`ne` — Noradrenergic.** Arousal, vigilance, alertness, the "gain" on attention.
  Stimulants and adaptogens frequently act here.
- **`cbf` — Cerebral blood flow.** Perfusion that delivers oxygen and nutrients.
  Vasoactive compounds and aerobic exercise act here.
- **`mito` — Mitochondrial / bioenergetic.** ATP supply and metabolic resilience.
  Creatine, ALCAR, CoQ10, and Zone-2 exercise act here.
- **`ntrophic` — Neurotrophic / neurogenesis.** BDNF/NGF-mediated growth, synapse
  formation, and repair. This is where the established #1 lever (strength training)
  lives, alongside Lion's Mane and others.
- **`inflam` — Neuroinflammation / oxidative.** Microglial tone and ROS control.
  Omega-3s, polyphenols, and sleep act here. `direction: down` is usually the win.
- **`glymph` — Glymphatic / sleep clearance.** The night-time waste-clearance
  system (amyloid/tau). Almost entirely driven by deep sleep.
- **`hpa` — HPA axis / stress.** Cortisol regulation and allostatic load.
  Adaptogens, meditation, and breathwork act here; chronic over-activation is
  corrosive to the other channels.

> Keep this list and the ids frozen once Phase 1 begins. If a genuinely new channel
> is needed, add it here first, then propagate to entries and the matrix.
