#!/usr/bin/env python3
"""Build the Project 01 vendor questionnaire (.xlsx) from the Markdown working files.

Sources of truth (edit these, then re-run):
  01-edtech-vendor-review/working/requirements-matrix.md     requirements, basis, basis type
  01-edtech-vendor-review/working/questionnaire-rubric.md    questions, score levels, weights
  01-edtech-vendor-review/sources/source-register.md         source list
  01-edtech-vendor-review/working/evidence-notes.md          answers (evidence, source, score, follow-up)

Output:
  01-edtech-vendor-review/deliverables/1-vendor-questionnaire.xlsx

Safe to re-run: answers typed directly into an existing workbook are carried over
by question ID; rows present in evidence-notes.md take precedence.

Usage:
  .venv/bin/python tools/build_questionnaire.py
"""
import re
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
PROJ = ROOT / "01-edtech-vendor-review"
MATRIX = PROJ / "working" / "requirements-matrix.md"
RUBRIC = PROJ / "working" / "questionnaire-rubric.md"
REGISTER = PROJ / "sources" / "source-register.md"
EVIDENCE = PROJ / "working" / "evidence-notes.md"
EVIDENCE_COLS = ["What the public documents say", "Source ID + section", "Score", "Score status",
                 "Follow-up question for vendor", "Notes"]
OUT = PROJ / "deliverables" / "1-vendor-questionnaire.xlsx"

DISCLAIMER = ("Independent educational exercise, based only on public documents. Not legal advice. "
              "Not affiliated with or endorsed by Wayground. Pecan Hollow ISD is a fictional district.")
POINTS = {"A": 2, "P": 1, "D": 1, "NF": 0}  # N/A is excluded from scoring

# Questionnaire columns: (header, width, filled-by)
COLUMNS = [
    ("ID", 7, "build"), ("Domain", 22, "build"), ("Question", 50, "build"),
    ("Requirement (from matrix)", 50, "build"), ("Basis / citation", 30, "build"),
    ("Basis type", 14, "build"), ("Weight", 8, "build"), ("Vendor sources to check", 20, "build"),
    ("What the public documents say", 50, "answer"), ("Source ID + section", 18, "answer"),
    ("Score", 8, "answer"), ("Score status", 12, "answer"),
    ("Points", 8, "formula"), ("Max points", 8, "formula"),
    ("Weighted points", 10, "formula"), ("Weighted max", 10, "formula"),
    ("Follow-up question for vendor", 40, "answer"), ("Notes", 30, "answer"),
]
COL = {name: get_column_letter(i + 1) for i, (name, _, _) in enumerate(COLUMNS)}
ANSWER_COLS = [name for name, _, kind in COLUMNS if kind == "answer"]

HEADER_FILL = PatternFill("solid", fgColor="1F3A5F")
HEADER_FONT = Font(bold=True, color="FFFFFF")
ANSWER_FILL = PatternFill("solid", fgColor="FFF8E1")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def strip_md(text):
    """Remove Markdown emphasis and links for spreadsheet cells."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("**", "").replace("`", "").strip()


def table_cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_matrix():
    domains, reqs, domain = {}, [], None
    for line in MATRIX.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### (D\d+)\. (.+)$", line)
        if m:
            domain = m.group(1)
            domains[domain] = m.group(2).strip()
            continue
        if re.match(r"^\| D\d+\.\d+ \|", line):
            c = table_cells(line)
            reqs.append({"id": c[0], "domain": domain, "requirement": strip_md(c[1]),
                         "basis": strip_md(c[2]), "type": strip_md(c[3]), "vendor": strip_md(c[4])})
    return domains, reqs


def parse_rubric():
    text = RUBRIC.read_text(encoding="utf-8")
    questions = {m.group(1): strip_md(m.group(2))
                 for m in re.finditer(r"^- \*\*(D\d+\.\d+)\*\* (.+)$", text, re.M)}
    weights, levels = {}, []
    section = None
    for line in text.splitlines():
        if line.startswith("## "):
            section = line
        elif section and section.startswith("## Weighting") and line.startswith("| ") \
                and not line.startswith("| Basis type") and not line.startswith("|---"):
            c = table_cells(line)
            n = re.match(r"(\d+)", c[1])
            if n:
                weights[c[0]] = int(n.group(1))
        elif section and section.startswith("## Score levels") and re.match(r"^\| \*\*", line):
            c = table_cells(line)
            levels.append([strip_md(x) for x in c])
    return questions, weights, levels


def parse_register():
    rows = []
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\| S\d+ \|", line):
            c = table_cells(line)
            rows.append([strip_md(x) for x in (c[0], c[1], c[2], c[3], c[4], c[5], c[7])])
    return rows


def parse_evidence():
    """Answer columns from working/evidence-notes.md (Markdown wins over the workbook)."""
    if not EVIDENCE.exists():
        return {}
    rows = {}
    for line in EVIDENCE.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\| D\d+\.\d+ \|", line):
            c = table_cells(line)
            if len(c) != 7:
                sys.exit(f"evidence-notes.md row {c[0]}: expected 7 columns, found {len(c)}")
            rows[c[0]] = {k: (None if strip_md(v) in ("", "—") else strip_md(v))
                          for k, v in zip(EVIDENCE_COLS, c[1:])}
            if rows[c[0]]["Score"] not in (None, "A", "P", "D", "NF", "N/A"):
                sys.exit(f"evidence-notes.md row {c[0]}: invalid score {rows[c[0]]['Score']!r}")
    return rows


def existing_answers():
    """Carry over answer columns from a previously built workbook, keyed by ID."""
    if not OUT.exists():
        return {}
    ws = load_workbook(OUT)["Questionnaire"]
    headers = [c.value for c in ws[1]]
    saved = {}
    for row in ws.iter_rows(min_row=2, values_only=True):
        if not row[0]:
            continue
        rec = {h: row[headers.index(h)] for h in ANSWER_COLS if h in headers}
        if any(v not in (None, "") for v in rec.values()):
            saved[row[0]] = rec
    return saved


def style_header(ws, row=1):
    for cell in ws[row]:
        cell.fill, cell.font, cell.alignment, cell.border = HEADER_FILL, HEADER_FONT, WRAP, BORDER


def build():
    domains, reqs = parse_matrix()
    questions, weights, levels = parse_rubric()
    register = parse_register()
    saved = existing_answers()
    evidence = parse_evidence()
    for qid, rec in evidence.items():
        saved.setdefault(qid, {}).update(rec)

    problems = [f"{r['id']}: no question in rubric" for r in reqs if r["id"] not in questions]
    problems += [f"{r['id']}: basis type '{r['type']}' has no weight" for r in reqs if r["type"] not in weights]
    problems += [f"{q}: question has no requirement in matrix" for q in questions
                 if q not in {r["id"] for r in reqs}]
    if problems:
        sys.exit("Cannot build; fix the Markdown first:\n  " + "\n  ".join(problems))

    wb = Workbook()

    # --- Instructions ---
    ws = wb.active
    ws.title = "Instructions"
    lines = [
        ("Vendor Privacy Questionnaire — Wayground (formerly Quizizz)", Font(bold=True, size=14)),
        ("Reviewing organization: Pecan Hollow ISD (FICTIONAL)", Font(bold=True)),
        (DISCLAIMER, Font(italic=True)),
        ("", None),
        ("How this questionnaire works", Font(bold=True)),
        ("The vendor does not answer this questionnaire. The analyst answers each question from the vendor's "
         "public documents only, citing a source ID and section from the Sources sheet.", None),
        ("When the public documents are silent, the score is NF = 'Not found in public documentation'. That is a "
         "finding about the documents, not about the vendor's practices; it becomes a follow-up question.", None),
        ("Yellow columns are filled in by the analyst. Points and Domain Scores calculate automatically.", None),
        ("Scores stay 'PROPOSED' in the Score status column until Brittany confirms them.", None),
        ("The score is not the risk rating. Risk ratings (likelihood x impact) are assigned separately in the "
         "risk assessment.", None),
        ("", None),
        ("Built by tools/build_questionnaire.py from working/requirements-matrix.md and "
         "working/questionnaire-rubric.md. Edit those files and re-run; entered answers are kept.", Font(italic=True, color="666666")),
    ]
    for i, (text, font) in enumerate(lines, start=1):
        cell = ws.cell(row=i, column=1, value=text)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        if font:
            cell.font = font
    ws.column_dimensions["A"].width = 110

    # --- Questionnaire ---
    ws = wb.create_sheet("Questionnaire")
    ws.append([h for h, _, _ in COLUMNS])
    style_header(ws)
    for i, (_, width, _) in enumerate(COLUMNS, start=1):
        ws.column_dimensions[get_column_letter(i)].width = width

    for r, req in enumerate(reqs, start=2):
        values = {
            "ID": req["id"], "Domain": f"{req['domain']}. {domains[req['domain']]}",
            "Question": questions[req["id"]], "Requirement (from matrix)": req["requirement"],
            "Basis / citation": req["basis"], "Basis type": req["type"], "Weight": weights[req["type"]],
            "Vendor sources to check": req["vendor"],
        }
        values.update(saved.get(req["id"], {}))
        s, w = f"{COL['Score']}{r}", f"{COL['Weight']}{r}"
        values["Points"] = f'=IF({s}="A",2,IF(OR({s}="P",{s}="D"),1,IF({s}="NF",0,"")))'
        values["Max points"] = f'=IF(OR({s}="",{s}="N/A"),"",2)'
        values["Weighted points"] = f'=IF({COL["Points"]}{r}="","",{COL["Points"]}{r}*{w})'
        values["Weighted max"] = f'=IF({COL["Max points"]}{r}="","",{COL["Max points"]}{r}*{w})'
        for c, (name, _, kind) in enumerate(COLUMNS, start=1):
            cell = ws.cell(row=r, column=c, value=values.get(name))
            cell.alignment, cell.border = WRAP, BORDER
            if kind == "answer":
                cell.fill = ANSWER_FILL
    last = len(reqs) + 1

    dv_score = DataValidation(type="list", formula1='"A,P,D,NF,N/A"', allow_blank=True,
                              errorTitle="Score", error="Use A, P, D, NF, or N/A (see Rubric sheet).")
    dv_status = DataValidation(type="list", formula1='"PROPOSED,Confirmed"', allow_blank=True)
    ws.add_data_validation(dv_score)
    ws.add_data_validation(dv_status)
    dv_score.add(f"{COL['Score']}2:{COL['Score']}{last}")
    dv_status.add(f"{COL['Score status']}2:{COL['Score status']}{last}")

    score_range = f"{COL['Score']}2:{COL['Score']}{last}"
    for code, color in (("A", "C8E6C9"), ("P", "FFF59D"), ("D", "FFE0B2"), ("NF", "FFCDD2"), ("N/A", "E0E0E0")):
        ws.conditional_formatting.add(score_range, CellIsRule(operator="equal", formula=[f'"{code}"'],
                                                              fill=PatternFill("solid", fgColor=color)))
    ws.freeze_panes = "D2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(COLUMNS))}{last}"

    # --- Domain Scores ---
    ds = wb.create_sheet("Domain Scores")
    ds.append(["Domain", "Questions", "Scored", "Weighted points", "Weighted max", "Domain %",
               "A", "P", "D", "NF", "N/A"])
    style_header(ds)
    q = "Questionnaire!"
    dom_rng = f"{q}${COL['Domain']}$2:${COL['Domain']}${last}"
    sc_rng = f"{q}${COL['Score']}$2:${COL['Score']}${last}"
    for i, (d, name) in enumerate(domains.items(), start=2):
        label = f"{d}. {name}"
        ds.append([
            label,
            f'=COUNTIF({dom_rng},A{i})',
            f'=COUNTIFS({dom_rng},A{i},{sc_rng},"<>")-COUNTIFS({dom_rng},A{i},{sc_rng},"N/A")',
            f'=SUMIF({dom_rng},A{i},{q}${COL["Weighted points"]}$2:${COL["Weighted points"]}${last})',
            f'=SUMIF({dom_rng},A{i},{q}${COL["Weighted max"]}$2:${COL["Weighted max"]}${last})',
            f'=IF(E{i}=0,"not yet scored",D{i}/E{i})',
        ] + [f'=COUNTIFS({dom_rng},A{i},{sc_rng},"{code}")' for code in ("A", "P", "D", "NF", "N/A")])
        ds[f"F{i}"].number_format = "0%"
        for cell in ds[i]:
            cell.border, cell.alignment = BORDER, WRAP
    ds.column_dimensions["A"].width = 44
    for col in "BCDEFGHIJK":
        ds.column_dimensions[col].width = 11
    note_row = len(domains) + 3
    ds.cell(row=note_row, column=1, value=(
        "Domain % = weighted points / weighted max for scored questions (N/A excluded). "
        "No overall score is reported, by design (rubric decision 2026-11-03).")).font = Font(italic=True)
    ds.freeze_panes = "B2"

    # --- Rubric ---
    rb = wb.create_sheet("Rubric")
    rb.append(["Code", "Level", "Meaning", "Points"])
    style_header(rb)
    for row in levels:
        rb.append(row[:4])
    rb.append([])
    start = rb.max_row + 1
    rb.append(["Basis type", "Weight"])
    style_header(rb, start)
    for k, v in weights.items():
        rb.append([k, v])
    for col, width in zip("ABCD", (16, 30, 80, 10)):
        rb.column_dimensions[col].width = width
    for row in rb.iter_rows():
        for cell in row:
            cell.alignment = WRAP

    # --- Sources ---
    so = wb.create_sheet("Sources")
    so.append(["ID", "Title", "Publisher", "URL", "Version / last updated", "Date accessed", "Type"])
    style_header(so)
    for row in register:
        so.append(row)
    for col, width in zip("ABCDEFG", (6, 50, 28, 60, 40, 14, 24)):
        so.column_dimensions[col].width = width
    for row in so.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = WRAP

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(reqs)} questions, {len(domains)} domains, "
          f"{len(register)} sources, {len(evidence)} rows from evidence-notes.md, "
          f"{len(set(saved) - set(evidence))} other answered rows carried over")


if __name__ == "__main__":
    build()
