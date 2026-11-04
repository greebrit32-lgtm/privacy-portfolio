#!/usr/bin/env python3
"""Size Markdown table columns for PDF export.

Pandoc sets relative column widths from the dashes in each table's separator row
(|---|-----|). This rewrites every separator row so each column's dash count is
proportional to its typical content length. GitHub ignores dash counts, so the
on-GitHub rendering is unchanged.

Usage:
  python3 tools/fit_tables.py FILE.md [FILE.md ...]
"""
import re
import statistics
import sys

TOTAL = 100   # total dashes per separator row (only proportions matter)
MIN = 7       # minimum dashes per column (keeps short ID columns like "D-1" on one line)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def fit(text):
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if i + 1 < len(lines) and re.match(r"^\|(\s*:?-{3,}:?\s*\|)+\s*$", lines[i + 1]) \
                and lines[i].lstrip().startswith("|"):
            header = cells(lines[i])
            body = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                body.append(cells(lines[j]))
                j += 1
            n = len(header)
            weights = []
            for c in range(n):
                lens = [len(re.sub(r"\*\*|`|\[([^\]]*)\]\([^)]*\)", r"\1", r[c])) for r in body if c < len(r)]
                typical = statistics.median(lens) if lens else 0
                weights.append(max(len(header[c]), typical, 3) ** 0.85)
            total = sum(weights)
            dashes = [max(MIN, round(TOTAL * w / total)) for w in weights]
            lines[i + 1] = "|" + "|".join("-" * d for d in dashes) + "|"
            i = j
        else:
            i += 1
    return "\n".join(lines)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        src = open(path, encoding="utf-8").read()
        out = fit(src)
        if out != src:
            open(path, "w", encoding="utf-8").write(out)
            print(f"fitted tables: {path}")
        else:
            print(f"unchanged: {path}")
