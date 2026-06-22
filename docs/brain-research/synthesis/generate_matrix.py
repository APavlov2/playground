#!/usr/bin/env python3
"""
Phase 3 generator — aggregates every entry's `channels[]` frontmatter block into
the Atlas data (`channel-matrix.json`) and the per-channel ranking (`channel-briefs.md`).

Single source of truth = the YAML frontmatter of each file in compounds/ and habits/.
Re-run after adding or editing entries:

    python3 docs/brain-research/synthesis/generate_matrix.py

No third-party deps beyond PyYAML.
"""
import json, glob, os, collections
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "synthesis")

# 12-channel taxonomy — id, display name, functional domain, Atlas colour.
# Keep ids in sync with taxonomy.md.
CHANNELS = [
    ("ach",      "Cholinergic (ACh)",            "Encoding, attention, memory",        "#F4B63A"),
    ("da",       "Dopaminergic",                 "Drive, working memory, executive",   "#E0533D"),
    ("ser",      "Serotonergic",                 "Mood, affect, impulse control",      "#7FB069"),
    ("glu",      "Glutamatergic / NMDA",         "Plasticity, LTP, learning",          "#5B8DEF"),
    ("gaba",     "GABAergic",                    "Inhibition, calm, anxiolysis",       "#9B6BDF"),
    ("ne",       "Noradrenergic",                "Arousal, vigilance, alertness",      "#E08A3C"),
    ("cbf",      "Cerebral blood flow",          "Perfusion, O2 & nutrient delivery",  "#D94F70"),
    ("mito",     "Mitochondrial / bioenergetic", "ATP supply, metabolic resilience",   "#46B5A4"),
    ("ntrophic", "Neurotrophic / neurogenesis",  "BDNF/NGF, growth & repair",          "#56A86C"),
    ("inflam",   "Neuroinflammation / oxidative","Microglial tone, ROS control",       "#C8923A"),
    ("glymph",   "Glymphatic / sleep clearance", "Waste, amyloid/tau clearance",       "#4C6EDB"),
    ("hpa",      "HPA axis / stress",            "Cortisol regulation, allostatic load","#B5566E"),
]
CH_IDS = [c[0] for c in CHANNELS]
CH_NAME = {c[0]: c[1] for c in CHANNELS}

EV_LABEL = {4: "Strong", 3: "Good", 2: "Emerging", 1: "Preclinical/anecdotal"}
DIR_ARROW = {"up": "↑", "down": "↓", "modulate": "↕"}


def load_entries():
    entries = []
    for sub in ("compounds", "habits"):
        for f in sorted(glob.glob(os.path.join(ROOT, sub, "*.md"))):
            txt = open(f).read()
            if not txt.startswith("---"):
                continue
            fm = yaml.safe_load(txt.split("---", 2)[1])
            entries.append(fm)
    return entries


def collapse_channels(fm):
    """One record per channel id. If an entry lists a channel twice (e.g. different
    populations), merge: max evidence, union of populations, mechanisms joined."""
    by_id = collections.OrderedDict()
    for c in fm.get("channels", []) or []:
        cid = c["channel"]
        if cid not in CH_IDS:
            raise ValueError(f"{fm['id']}: unknown channel id {cid!r}")
        if cid in by_id:
            prev = by_id[cid]
            prev["evidence"] = max(prev["evidence"], c["evidence"])
            pops = {prev["population"], c["population"]}
            prev["population"] = "both" if pops >= {"healthy", "impaired"} else prev["population"]
            if c["mechanism"] not in prev["mechanism"]:
                prev["mechanism"] = prev["mechanism"].rstrip(".") + "; " + c["mechanism"]
            if prev["direction"] != c["direction"]:
                prev["direction"] = "modulate"
        else:
            by_id[cid] = dict(channel=cid, mechanism=c["mechanism"],
                              evidence=c["evidence"], population=c["population"],
                              direction=c["direction"])
    return list(by_id.values())


def build():
    entries = load_entries()
    agents = []
    # per-channel index for the briefs
    bychan = {cid: [] for cid in CH_IDS}
    for fm in entries:
        chans = collapse_channels(fm)
        ch_map = {c["channel"]: c["mechanism"] for c in chans}
        agents.append(dict(
            id=fm["id"], name=fm["name"], type=fm["type"],
            klass=fm.get("klass", ""), origin=fm.get("origin", ""),
            source=fm.get("source", ""), ev=fm["evidence_overall"], ch=ch_map,
        ))
        for c in chans:
            bychan[c["channel"]].append(dict(
                id=fm["id"], name=fm["name"], type=fm["type"], klass=fm.get("klass", ""),
                origin=fm.get("origin", ""),
                overall=fm["evidence_overall"], ev=c["evidence"],
                population=c["population"], direction=c["direction"], mechanism=c["mechanism"],
            ))

    matrix = {
        "channels": [dict(id=i, name=n, domain=d, color=col) for (i, n, d, col) in CHANNELS],
        "agents": agents,
        "meta": {
            "n_agents": len(agents),
            "n_compounds": sum(1 for a in agents if a["type"] == "compound"),
            "n_habits": sum(1 for a in agents if a["type"] == "habit"),
            "by_origin": dict(collections.Counter(a["origin"] for a in agents if a["origin"])),
            "note": "Generated by generate_matrix.py from entry frontmatter. Do not hand-edit.",
        },
    }
    with open(os.path.join(OUT, "channel-matrix.json"), "w") as fh:
        json.dump(matrix, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    write_briefs(bychan, matrix["meta"])
    return matrix, bychan


def write_briefs(bychan, meta):
    L = []
    L.append("# Channel Briefs — what moves each neural channel\n")
    L.append("> Auto-generated by `generate_matrix.py` from entry frontmatter. "
             "For each of the 12 channels: every agent that acts on it, ranked by "
             "**per-channel** evidence (then overall badge). Direction ↑ up · ↓ down · ↕ modulate.\n")
    L.append(f"> **Coverage so far:** {meta['n_compounds']} compounds, {meta['n_habits']} habits "
             f"({meta['n_agents']} agents total).\n")
    if meta["n_habits"] == 0:
        L.append("> ⚠ **Habit track (Phase 2) not yet done.** Convergence flags below are therefore "
                 "*compound-only* and provisional — several channels whose strongest real-world lever "
                 "is a habit (e.g. `ntrophic`←resistance training, `glymph`←deep sleep, `mito`←Zone-2, "
                 "`hpa`←meditation) will shift once habits are added. Treat 'gaps' as *compound-coverage* gaps.\n")

    # ranking helper
    def rank(rows):
        return sorted(rows, key=lambda r: (-r["ev"], -r["overall"], r["id"]))

    # origin breakdown
    allrows = [r for rows in bychan.values() for r in rows]
    origins = collections.Counter()
    seen = set()
    for r in allrows:
        if r["id"] not in seen:
            seen.add(r["id"]); origins[r["origin"] or "—"] += 1
    L.append("## Origin breakdown\n")
    L.append("_How the agents split by where the molecule comes from "
             "(`natural` = in food/plants/the body · `semi-synthetic` = derived from a natural precursor "
             "· `synthetic` = lab-only). See each entry's `origin`/`source` fields._\n")
    L.append("| Origin | Agents |")
    L.append("|--------|:------:|")
    for k in ("natural", "semi-synthetic", "synthetic", "—"):
        if origins.get(k):
            L.append(f"| {k} | {origins[k]} |")
    L.append("")

    OICON = {"natural": "🌿", "semi-synthetic": "⚗", "synthetic": "🧪"}

    # summary table
    L.append("## Coverage at a glance\n")
    L.append("| Channel | Agents | Best per-channel evidence | Top agent(s) |")
    L.append("|---------|:------:|:-------------------------:|--------------|")
    for cid in CH_IDS:
        rows = rank(bychan[cid])
        if not rows:
            L.append(f"| `{cid}` {CH_NAME[cid]} | 0 | – | — |")
            continue
        best = rows[0]["ev"]
        tops = [r for r in rows if r["ev"] == best][:3]
        topnames = ", ".join(f"{r['name']} ({r['ev']})" for r in tops)
        L.append(f"| `{cid}` {CH_NAME[cid]} | {len(rows)} | {best} ({EV_LABEL[best]}) | {topnames} |")
    L.append("")

    # per-channel detail
    for cid in CH_IDS:
        rows = rank(bychan[cid])
        L.append(f"\n## `{cid}` — {CH_NAME[cid]}\n")
        if not rows:
            L.append("_No agents map to this channel yet — **coverage gap.**_\n")
            continue
        strong = [r for r in rows if r["ev"] >= 3]
        flag = []
        if strong:
            flag.append(f"**{len(strong)}** agent(s) at evidence ≥3")
        else:
            flag.append("⚠ **thin** — no agent reaches evidence ≥3 (compound-only)")
        L.append(f"_{len(rows)} agents · {', '.join(flag)}._\n")
        L.append("| Agent | Origin | Overall | Channel ev | Dir | Population | Mechanism |")
        L.append("|-------|--------|:-------:|:----------:|:---:|------------|-----------|")
        for r in rows:
            mech = r["mechanism"].replace("|", "\\|")
            if len(mech) > 130:
                mech = mech[:127] + "…"
            org = f"{OICON.get(r['origin'], '')} {r['origin']}".strip()
            L.append(f"| [{r['name']}](../{r['type']}s/{r['id']}.md) | {org} | {r['overall']} "
                     f"| **{r['ev']}** | {DIR_ARROW.get(r['direction'], r['direction'])} "
                     f"| {r['population']} | {mech} |")
        L.append("")

    with open(os.path.join(OUT, "channel-briefs.md"), "w") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    matrix, bychan = build()
    print(f"channel-matrix.json: {matrix['meta']['n_agents']} agents "
          f"({matrix['meta']['n_compounds']} compounds, {matrix['meta']['n_habits']} habits)")
    print("per-channel counts:")
    for cid in CH_IDS:
        print(f"  {cid:9s} {len(bychan[cid]):3d}")
