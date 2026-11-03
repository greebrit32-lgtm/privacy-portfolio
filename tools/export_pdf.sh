#!/usr/bin/env bash
# Export a Markdown file to PDF: pandoc (Markdown -> styled HTML) then headless Chrome (HTML -> PDF).
# Usage: tools/export_pdf.sh path/to/file.md [output-dir]
# Default output dir: <file's folder>/pdf
set -euo pipefail

src="${1:?Usage: tools/export_pdf.sh file.md [output-dir]}"
outdir="${2:-$(dirname "$src")/pdf}"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
here="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$outdir"
base="$(basename "$src" .md)"
html="$outdir/$base.tmp.html"
pdf="$outdir/$base.pdf"

pandoc "$src" --standalone --embed-resources \
  --css "$here/pdf-style.css" \
  --metadata title="$base" --variable pagetitle="$base" \
  -o "$html"

"$chrome" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$pdf" "file://$(cd "$(dirname "$html")" && pwd)/$(basename "$html")" 2>/dev/null

rm -f "$html"
pages=$(python3 -c "import re,sys;d=open(sys.argv[1],'rb').read();m=re.search(rb'/Type\s*/Pages\b.*?/Count\s+(\d+)',d,re.S);print(m.group(1).decode() if m else '?')" "$pdf")
echo "Wrote $pdf (${pages} pages)"
