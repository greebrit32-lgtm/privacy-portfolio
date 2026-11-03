#!/usr/bin/env python3
"""Build the Project 02 data inventory (.xlsx) from the Markdown working files.

Sources of truth (edit these, then re-run):
  02-pia-data-map/working/system-description.md   systems, data elements, features (product design)
  02-pia-data-map/working/inventory-notes.md      analyst columns (sensitivity, TDPSA category, ...)
  02-pia-data-map/sources/source-register.md      source list

Output:
  02-pia-data-map/deliverables/1-data-inventory.xlsx

Usage:
  .venv/bin/python tools/build_inventory.py
"""
import re
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# Shared helpers from the Project 01 builder (same Markdown conventions and styling).
from build_questionnaire import (ANSWER_FILL, BORDER, WRAP, strip_md, style_header,
                                 table_cells)

ROOT = Path(__file__).resolve().parent.parent
PROJ = ROOT / "02-pia-data-map"
SYSDESC = PROJ / "working" / "system-description.md"
NOTES = PROJ / "working" / "inventory-notes.md"
REGISTER = PROJ / "sources" / "source-register.md"
OUT = PROJ / "deliverables" / "1-data-inventory.xlsx"

DISCLAIMER = ("Independent educational exercise. Mesquite Lantern Co. and Lantern Local are fictional; "
              "all data is described by type only. Not legal advice.")
ANALYST_COLS = ["Sensitivity", "TDPSA category", "§541.105 assessment trigger(s)",
                "Consent / legal basis", "FIPPs concerns", "Analyst notes"]
SENSITIVITY = ("High", "Medium", "Low")
TDPSA_CATS = ("Sensitive data", "Personal data", "Pseudonymous data", "Deidentified data", "Not personal data")


def section(text, heading):
    """Lines under a '## <heading>' up to the next '## '."""
    m = re.search(rf"^## {re.escape(heading)}.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        sys.exit(f"system-description.md: section '## {heading}' not found")
    return m.group(1).splitlines()


def element_ids(text):
    """DE IDs mentioned in text, expanding ranges like 'DE-01–06' or 'DE-01-DE-06'."""
    ids = set()
    for a, b in re.findall(r"DE-(\d+)\s*[–-]\s*(?:DE-)?(\d+)", text):
        ids.update(f"DE-{n:02d}" for n in range(int(a), int(b) + 1))
    ids.update(re.findall(r"DE-\d+", text))
    return ids


def rows(lines, id_pattern):
    return [table_cells(l) for l in lines if re.match(rf"^\| {id_pattern} ", l)]


def parse_sysdesc():
    text = SYSDESC.read_text(encoding="utf-8")
    systems = {c[0]: {"name": strip_md(c[1]), "operator": strip_md(c[2]), "notes": strip_md(c[3])}
               for c in rows(section(text, "1. Systems"), r"(SYS|TP)-\d+")}
    elements = {}
    for c in rows(section(text, "2. Data elements"), r"DE-\d+"):
        recips = [r.strip() for r in c[4].split(",") if r.strip()]
        elements[c[0]] = {"name": strip_md(c[1]), "source": strip_md(c[2]),
                          "collected_by": strip_md(c[3]), "recipients": recips}
    features = {}
    for c in rows(section(text, "3. Feature-by-feature design"), r"\*\*F-\d+"):
        fid = re.match(r"\*\*(F-\d+)", c[0]).group(1)
        features[fid] = {"name": strip_md(c[0]), "collected": strip_md(c[1]), "purpose": strip_md(c[2]),
                         "where": strip_md(c[3]), "retention": strip_md(c[4]), "notice": strip_md(c[5]),
                         "elements": element_ids(c[1])}
    return systems, elements, features


def parse_notes():
    if not NOTES.exists():
        return {}
    out = {}
    for line in NOTES.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\| DE-\d+ \|", line):
            c = table_cells(line)
            if len(c) != 1 + len(ANALYST_COLS):
                sys.exit(f"inventory-notes.md row {c[0]}: expected {1 + len(ANALYST_COLS)} columns, found {len(c)}")
            out[c[0]] = {k: (None if strip_md(v) in ("", "—") else strip_md(v))
                         for k, v in zip(ANALYST_COLS, c[1:])}
    return out


def parse_register():
    return [[strip_md(x) for x in (c[0], c[1], c[2], c[3], c[4], c[5], c[7])]
            for c in (table_cells(l) for l in REGISTER.read_text(encoding="utf-8").splitlines()
                      if re.match(r"^\| S\d+ \|", l))]


def validate(systems, elements, features, notes):
    problems = []
    for de, e in elements.items():
        problems += [f"{de}: unknown recipient {r}" for r in e["recipients"] if r not in systems]
        problems += [f"{de}: unknown feature {f}" for f in re.findall(r"F-\d+", e["collected_by"])
                     if f not in features]
    for fid, f in features.items():
        problems += [f"{fid}: mentions unknown {d}" for d in f["elements"] if d not in elements]
    for de, n in notes.items():
        if de not in elements:
            problems.append(f"inventory-notes.md: {de} not in system description")
        if n["Sensitivity"] not in (None,) + SENSITIVITY:
            problems.append(f"inventory-notes.md {de}: sensitivity {n['Sensitivity']!r}")
        if n["TDPSA category"] not in (None,) + TDPSA_CATS:
            problems.append(f"inventory-notes.md {de}: TDPSA category {n['TDPSA category']!r}")
    if problems:
        sys.exit("Cannot build; fix the Markdown first:\n  " + "\n  ".join(problems))


def write_table(ws, headers, data, widths, answer_from=None):
    ws.append(headers)
    style_header(ws)
    for r in data:
        ws.append(r)
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment, cell.border = WRAP, BORDER
            if answer_from and cell.column >= answer_from:
                cell.fill = ANSWER_FILL
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{ws.max_row}"


def build():
    systems, elements, features = parse_sysdesc()
    notes = parse_notes()
    register = parse_register()
    validate(systems, elements, features, notes)

    used_in = {de: sorted((f for f, v in features.items() if de in v["elements"]),
                          key=lambda x: int(x[2:])) for de in elements}

    def per_feature(de, key):
        return "\n".join(f"{f}: {features[f][key]}" for f in used_in[de]) or "—"

    wb = Workbook()

    # Instructions
    ws = wb.active
    ws.title = "Instructions"
    for i, (text, font) in enumerate([
        ("Data Inventory — Lantern Local (Mesquite Lantern Co.)", Font(bold=True, size=14)),
        ("FICTIONAL company, product, and data. Data is listed by type only, never as records.", Font(bold=True)),
        (DISCLAIMER, Font(italic=True)),
        ("", None),
        ("Inventory: one row per data element (DE-xx). Grey columns come from the product team's design "
         "(working/system-description.md). Yellow columns are the analyst's assessment "
         "(working/inventory-notes.md).", None),
        ("Data × Recipients: which systems and third parties receive each data element. This is the basis "
         "for the data-flow map.", None),
        ("Built by tools/build_inventory.py. Edit the Markdown files and re-run.", Font(italic=True, color="666666")),
    ], start=1):
        c = ws.cell(row=i, column=1, value=text)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if font:
            c.font = font
    ws.column_dimensions["A"].width = 110

    # Inventory
    ws = wb.create_sheet("Inventory")
    headers = ["ID", "Data element (type)", "Source", "Collected by", "Used in features",
               "Purpose (as designed)", "Systems and recipients", "Retention (as proposed)",
               "Notice / choice (as designed)"] + ANALYST_COLS
    data = []
    for de, e in elements.items():
        n = notes.get(de, {})
        data.append([de, e["name"], e["source"], e["collected_by"], ", ".join(used_in[de]) or "—",
                     per_feature(de, "purpose"),
                     "\n".join(f"{r} {systems[r]['name']}" for r in e["recipients"]),
                     per_feature(de, "retention"), per_feature(de, "notice")]
                    + [n.get(k) for k in ANALYST_COLS])
    write_table(ws, headers, data, [8, 30, 18, 12, 14, 40, 34, 34, 40, 11, 16, 24, 28, 28, 30],
                answer_from=len(headers) - len(ANALYST_COLS) + 1)
    last = ws.max_row
    sens_col = get_column_letter(headers.index("Sensitivity") + 1)
    cat_col = get_column_letter(headers.index("TDPSA category") + 1)
    for col, opts in ((sens_col, SENSITIVITY), (cat_col, TDPSA_CATS)):
        dv = DataValidation(type="list", formula1='"' + ",".join(opts) + '"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{col}2:{col}{last}")
    for value, color in (("High", "FFCDD2"), ("Medium", "FFF59D"), ("Low", "C8E6C9")):
        ws.conditional_formatting.add(f"{sens_col}2:{sens_col}{last}", CellIsRule(
            operator="equal", formula=[f'"{value}"'], fill=PatternFill("solid", fgColor=color)))

    # Data × Recipients matrix
    mx = wb.create_sheet("Data x Recipients")
    sys_ids = list(systems)
    mx.append(["ID", "Data element"] + [f"{s}\n{systems[s]['name']}" for s in sys_ids] + ["# recipients"])
    style_header(mx)
    for de, e in elements.items():
        mx.append([de, e["name"]] + ["●" if s in e["recipients"] else "" for s in sys_ids]
                  + [len(e["recipients"])])
    mx.column_dimensions["A"].width = 8
    mx.column_dimensions["B"].width = 34
    for i in range(3, 3 + len(sys_ids) + 1):
        mx.column_dimensions[get_column_letter(i)].width = 11
    mx.row_dimensions[1].height = 75
    for row in mx.iter_rows(min_row=2):
        for cell in row:
            cell.border = BORDER
            cell.alignment = Alignment(horizontal="center" if cell.column > 2 else "left",
                                       vertical="top", wrap_text=True)
    tp_fill = PatternFill("solid", fgColor="FFF3E0")
    for i, s in enumerate(sys_ids, start=3):
        if s.startswith("TP-"):
            for r in range(2, mx.max_row + 1):
                if mx.cell(r, i).value:
                    mx.cell(r, i).fill = tp_fill
    mx.freeze_panes = "C2"

    # Features
    write_table(wb.create_sheet("Features"),
                ["Feature", "Collected (and when)", "Purpose", "Where it goes", "Retention", "Notice / choice"],
                [[f["name"], f["collected"], f["purpose"], f["where"], f["retention"], f["notice"]]
                 for f in features.values()],
                [24, 40, 34, 30, 30, 44])

    # Systems & recipients
    write_table(wb.create_sheet("Systems & Recipients"), ["ID", "System / recipient", "Operated by", "Notes"],
                [[k, v["name"], v["operator"], v["notes"]] for k, v in systems.items()], [8, 40, 40, 60])

    # Sources
    write_table(wb.create_sheet("Sources"),
                ["ID", "Title", "Publisher", "URL", "Version / last updated", "Date accessed", "Type"],
                register, [6, 50, 28, 60, 40, 14, 24])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(elements)} data elements, {len(features)} features, "
          f"{len(systems)} systems/recipients, {len(notes)} analyst rows, {len(register)} sources")


if __name__ == "__main__":
    build()
