#!/bin/bash
# calendar_html2 で作ったHTMLを docs/index.html に出力し、コミット・pushする。使い方: gh-deploy.sh [YEAR]
# GitHub Pages は Source を「master / docs」にして公開する。
set -euo pipefail

year=${1:-$(date +%Y)}
cd "$(git rev-parse --show-toplevel)"
mkdir -p docs

{
  echo '<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8">'
  echo "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>${year}-$((year + 1)) カレンダー</title></head><body>"
  uv run python -c "from jcal.html import calendar_html2; print(calendar_html2($year, $((year + 1))))"
  echo '</body></html>'
} >docs/index.html

git add docs/index.html
if git diff --cached --quiet -- docs/index.html; then
  echo "no changes"
else
  git commit -q -m "deploy: calendar $year-$((year + 1))" -- docs/index.html
  git push
fi
