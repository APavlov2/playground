# Metabolic–Cardiac Channel Taxonomy (12)

The shared vocabulary for this study, mirroring the brain study's neural-channel
approach. Every effect — from a supplement or a habit — maps to one or more of
these **channels**. The `channel` ids below are the single source of truth: they
must match the `channels[].channel` ids in every entry's frontmatter and the keys
in `synthesis/channel-matrix.json`.

The thesis of [`PLAN.md`](./PLAN.md) is that fatty liver, insulin resistance,
obesity, and heart health are **one connected problem**. These channels make that
connectedness explicit — and the last two rows (`rhythm`, `bp`) carry the
**cardiac-safety constraint** that shapes the whole study.

| id | Channel | Domain |
|----|---------|--------|
| `insulin` | Insulin sensitivity / glucose handling | IR reversal, GLUT4, glycemic control |
| `liver` | Hepatic fat / MASLD | De novo lipogenesis, liver enzymes, fibrosis |
| `lipid` | Lipids | Triglycerides, LDL/HDL, atherogenic load |
| `bp` | Blood pressure / vascular tone | Hypertension, BP response to exertion |
| `rhythm` | Cardiac rhythm / autonomic | PVC burden, vagal tone, palpitations |
| `ampk` | AMPK / cellular energy sensing | Fuel switching, "natural-metformin" axis |
| `mito` | Mitochondrial / fat oxidation | ATP, fat-burning capacity, metabolic flexibility |
| `inflam` | Inflammation / oxidative stress | Systemic inflammation, ROS, hepatic injury |
| `adipos` | Adiposity / visceral fat | Energy balance, the master lever |
| `muscle` | Muscle mass / glucose disposal | Lean mass, the glucose "sink", resting metabolism |
| `circadian` | Sleep / circadian / recovery | Sleep quality, apnea, recovery-driven insulin sensitivity |
| `stress` | Stress / vagal load | Autonomic balance, cortisol, PVC triggers |

## Channel notes

- **`insulin`.** The hinge of the whole cluster. Improved when visceral fat falls,
  muscle grows, and post-meal glucose spikes are blunted. Most levers here route
  through it.
- **`liver`.** Hepatic fat and the de novo lipogenesis pathway that fructose feeds
  directly. The plan's single biggest dietary target (cut added sugar). Track via
  liver enzymes and waist.
- **`lipid`.** Triglycerides and cholesterol fractions. Omega-3 and berberine act
  here; refined carbs worsen it.
- **`bp`. ⚠ cardiac-safety channel.** Blood pressure and the *exaggerated BP
  response to exertion* flagged on the stress test. `direction: down` is the goal,
  but **additive** BP-lowering with nebivolol (e.g. berberine) is itself a flagged
  interaction — record it in `cardiac_safety`, not just as a benefit. Excess salt
  and Valsalva strength reps push this the wrong way.
- **`rhythm`. ⚠ cardiac-safety channel.** PVC burden and autonomic/vagal tone.
  Magnesium may reduce PVC frequency; stimulants, high-dose caffeine, and poor sleep
  provoke them. Any rhythm signal — in either direction — belongs in `cardiac_safety`.
- **`ampk`.** Cellular energy sensing — the "natural metformin" axis. Activated by
  berberine, fasting/time-restricted eating, and exercise. Drives fat oxidation and
  insulin sensitivity.
- **`mito`.** Mitochondrial density and fat-oxidation capacity. Zone-2 cardio is the
  flagship lever; creatine and CoQ10 are adjacent.
- **`inflam`.** Systemic inflammation and oxidative stress that link MASLD to
  cardiovascular risk. Omega-3, polyphenols, and the Mediterranean pattern act here;
  ultra-processed foods and alcohol worsen it.
- **`adipos`. The master lever.** Visceral fat / energy balance. Losing 5–10% body
  weight is the upstream move that improves nearly every other channel. Most habits
  ultimately serve this.
- **`muscle`.** Lean mass as a glucose sink and resting-metabolism driver. Built by
  strength training (Valsalva-free) and supported by adequate protein + creatine.
- **`circadian`.** Sleep quality and circadian regularity — poor sleep wrecks
  insulin sensitivity and triggers PVCs. Sleep-apnea screening sits here and bridges
  to `rhythm`.
- **`stress`.** Stress / vagal load — the autonomic input to PVC triggers and
  cortisol-driven insulin resistance. Managed by stress reduction, not
  over-caffeinating, and avoiding late-night spikes.

> Keep this list and the ids frozen once Phase 1 begins. If a genuinely new channel
> is needed, add it here first, then propagate to entries and the matrix.
