#!/usr/bin/env python3
"""Build the Project 02 data-flow map (Mermaid) from the same Markdown as the inventory.

Reads:   02-pia-data-map/working/system-description.md  (data elements and their recipients)
         02-pia-data-map/working/inventory-notes.md     (TDPSA category, to highlight sensitive flows)
Writes:  02-pia-data-map/deliverables/2-data-flow-map.md   (GitHub renders the Mermaid block)
         02-pia-data-map/deliverables/pdf/2-data-flow-map.pdf (with --pdf; headless Chrome + Mermaid)

Usage:
  .venv/bin/python tools/build_dataflow.py [--pdf]
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from build_inventory import ROOT, parse_notes, parse_sysdesc

PROJ = ROOT / "02-pia-data-map"
OUT_MD = PROJ / "deliverables" / "2-data-flow-map.md"
OUT_PDF = PROJ / "deliverables" / "pdf" / "2-data-flow-map.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
MERMAID_JS = "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"

# Presentation only: readable groups of data elements (IDs come from system-description.md).
GROUPS = {
    "Account": ["DE-01", "DE-02", "DE-03", "DE-04", "DE-05", "DE-06"],
    "Precise location": ["DE-07", "DE-08", "DE-09"],
    "Coarse location": ["DE-24"],
    "Interests & profile": ["DE-11", "DE-12"],
    "App activity": ["DE-13"],
    "Check-ins & tickets": ["DE-14", "DE-15"],
    "Card data": ["DE-16"],
    "Device & ad IDs": ["DE-10", "DE-17", "DE-18", "DE-19", "DE-20"],
    "Segments & ad data": ["DE-21", "DE-22"],
    "Choices": ["DE-23"],
}
# Short labels for arrows (full names appear in the legend table).
SHORT = {"Account": "Account", "Precise location": "Location", "Coarse location": "Coarse loc.",
         "Interests & profile": "Profile", "App activity": "Activity", "Check-ins & tickets": "Check-ins",
         "Card data": "Card", "Device & ad IDs": "Device IDs", "Segments & ad data": "Ad data",
         "Choices": "Choices"}
# Where each recipient receives data from (one hop upstream), as designed in system-description.md.
UPSTREAM = {
    "SYS-1": ["USER"], "SYS-2": ["SYS-1"], "SYS-3": ["SYS-2"], "SYS-4": ["SYS-2", "SYS-3", "TP-2"],
    "SYS-5": ["SYS-4"], "SYS-6": ["SYS-2"], "TP-1": ["SYS-1"], "TP-2": ["SYS-1", "SYS-3"],
    "TP-3": ["SYS-2"], "TP-4": ["SYS-1"], "TP-5": ["SYS-6"], "TP-6": ["SYS-5"],
}
# Role of each outside party for the map (TP-1 is not stated in the design; flagged for S7).
PROCESSORS = ["TP-3", "TP-4"]
THIRD_PARTIES = ["TP-2", "TP-5", "TP-6"]
ROLE_UNCLEAR = ["TP-1"]


def node_id(x):
    return x.replace("-", "")


def build():
    systems, elements, _ = parse_sysdesc()
    notes = parse_notes()
    grouped = {de for ids in GROUPS.values() for de in ids}
    missing = sorted(set(elements) - grouped) + sorted(grouped - set(elements))
    if missing or set(UPSTREAM) != set(systems):
        sys.exit(f"build_dataflow: groups/recipients out of sync with system description: {missing}")
    sensitive = {de for de, n in notes.items() if n.get("TDPSA category") == "Sensitive data"}
    group_of = {de: g for g, ids in GROUPS.items() for de in ids}

    # Edges: data element flows from u to r if r receives it and u is the user or also holds it.
    edges = {}
    for r, ups in UPSTREAM.items():
        for u in ups:
            des = sorted(de for de, e in elements.items()
                         if r in e["recipients"] and (u == "USER" or u in e["recipients"])
                         # data flows *out of* a third party only if that party is its source
                         and (not u.startswith("TP-") or u in e["source"]))
            if des:
                edges[(u, r)] = des

    def label(r):
        return f"{r}<br/>{systems[r]['name']}"

    lines = ["flowchart TB",
             '  USER(["Users 18+ in Texas"])',
             '  subgraph ML["Mesquite Lantern Co. (controller)"]',
             "    direction TB"]
    lines += [f'    {node_id(s)}["{label(s)}"]' for s in systems if s.startswith("SYS-")]
    lines += ["  end"]
    role = {**{s: "processor" for s in PROCESSORS}, **{s: "third party" for s in THIRD_PARTIES},
            **{s: "role to confirm" for s in ROLE_UNCLEAR}}
    lines += [f'  {node_id(s)}["{s}<br/>{systems[s]["name"]}<br/>({role[s]})"]' for s in role]
    red = []
    for i, ((u, r), des) in enumerate(edges.items()):
        groups = []
        for de in des:
            if group_of[de] not in groups:
                groups.append(group_of[de])
        groups = [SHORT[g] + (" ⚠" if any(d in sensitive for d in des if group_of[d] == g) else "") for g in groups]
        lines.append(f'  {node_id(u)} -->|"{", ".join(groups)}"| {node_id(r)}')
        if any(de in sensitive for de in des):
            red.append(str(i))
    lines += ["  classDef tp fill:#fff3e0,stroke:#e65100",
              "  classDef proc fill:#e3f2fd,stroke:#1565c0",
              "  classDef unk fill:#f3e5f5,stroke:#6a1b9a,stroke-dasharray: 4 3",
              f"  class {','.join(node_id(s) for s in THIRD_PARTIES)} tp",
              f"  class {','.join(node_id(s) for s in PROCESSORS)} proc",
              f"  class {','.join(node_id(s) for s in ROLE_UNCLEAR)} unk"]
    if red:
        lines.append(f"  linkStyle {','.join(red)} stroke:#c62828,stroke-width:2.5px")
    mermaid = "\n".join(lines)

    table = ["| From | To | Data elements | Sensitive data? |", "|---|---|---|---|"]
    for (u, r), des in edges.items():
        frm = "Users" if u == "USER" else f"{u} {systems[u]['name']}"
        sens = [d for d in des if d in sensitive]
        table.append(f"| {frm} | {r} {systems[r]['name']} | {', '.join(des)} | "
                     f"{'**Yes:** ' + ', '.join(sens) if sens else 'No'} |")
    group_table = ["| Arrow label | Group | Data elements |", "|---|---|---|"]
    group_table += [f"| {SHORT[g]} | {g} | " + ", ".join(f"{de} {elements[de]['name']}" for de in ids) + " |"
                    for g, ids in GROUPS.items()]

    md = f"""# Data-Flow Map — Lantern Local (as designed, pre-review)

> **FICTIONAL** company, product, vendors, and data. Data is shown by **type** only. Generated by `tools/build_dataflow.py` from [`working/system-description.md`](../working/system-description.md) and [`working/inventory-notes.md`](../working/inventory-notes.md). Edit those files and re-run; do not edit this file by hand.

**How to read it:** arrows show which data groups move between parties. **Red arrows and ⚠** carry data the inventory classifies as Texas "sensitive data" (Tex. Bus. & Com. Code §541.001(29) [S01]). Orange boxes are independent third parties, blue boxes are processors, and the dashed purple box is a party whose role is not yet established. This map shows the **pre-review design**. Changes recommended by the PIA appear in the PIA report.

```mermaid
{mermaid}
```

## Flows ({len(edges)} arrows)

{chr(10).join(table)}

## Data groups used in the map

{chr(10).join(group_table)}

## Observations for the PIA (facts from the map; assessed in S7)
- **{sum(1 for k, v in edges.items() if any(d in sensitive for d in v))} of {len(edges)} flows carry sensitive data.** Sensitive data leaves Mesquite Lantern's own systems on these flows: {", ".join(f"{u}→{r}" for (u, r), v in edges.items() if r.startswith("TP-") and any(d in sensitive for d in v)) or "none"}.
- **Embedded SDKs (TP-1 analytics, TP-2 ad network) receive data directly from the app**, not through Mesquite Lantern's servers, so Mesquite Lantern's backend controls do not apply to those flows.
- **TP-1's role (processor or third party) is not stated in the design.** Under Texas law, a processor acts "on behalf of a controller" (§541.001(23) [S01]) and must be under contract (§541.104(b) [S01]).

_Independent educational exercise. Fictional organization and data. Not legal advice._
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}: {len(edges)} flows, {len(red)} carrying sensitive data")
    return mermaid


def render_pdf(mermaid):
    page = f"""<!doctype html><html><head><meta charset="utf-8"><title>Data-Flow Map</title>
<style>@page {{ size: Letter; margin: 0.4in; }}
body {{ font-family: -apple-system, Helvetica, Arial, sans-serif; margin: 0; }}
h1 {{ font-size: 15pt; color: #1f4e79; margin: 0 0 4px; }} p {{ font-size: 9pt; margin: 2px 0 8px; color: #333; }}
.mermaid svg {{ max-width: 100%; height: auto; }}</style>
<script src="{MERMAID_JS}"></script></head><body>
<h1>Data-Flow Map — Lantern Local (as designed, pre-review)</h1>
<p>FICTIONAL company, product, and data; data shown by type only. Red arrows / ⚠ = Texas "sensitive data" (Tex. Bus. &amp; Com. Code §541.001(29)). Orange = independent third parties; blue = processors; dashed = role to confirm. Not legal advice.</p>
<pre class="mermaid">{html.escape(mermaid)}</pre>
<script>mermaid.initialize({{startOnLoad: true, securityLevel: "loose", flowchart: {{htmlLabels: true, useMaxWidth: true, nodeSpacing: 30, rankSpacing: 45}}}});</script>
</body></html>"""
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "map.html"
        src.write_text(page, encoding="utf-8")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=10000", f"--print-to-pdf={OUT_PDF}", src.as_uri()],
                       check=True, stderr=subprocess.DEVNULL)
    print(f"Wrote {OUT_PDF.relative_to(ROOT)}")


if __name__ == "__main__":
    m = build()
    if "--pdf" in sys.argv:
        render_pdf(m)
