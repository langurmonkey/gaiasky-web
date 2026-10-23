#!/bin/bash
# Generates the mobile variants in sm/ (1280 px wide, Q68, metadata stripped).
# The originals are ~2560 px / up to 1.9 MB; phones download sm/ instead
# (gaiasky.css, max-width: 767px). Run from this directory.
set -euo pipefail

cd "$(dirname "$0")"
mkdir -p sm

for f in *.avif; do
  [ -f "sm/$f" ] && [ "sm/$f" -nt "$f" ] && continue
  magick "$f" -resize 1280x -quality 68 -strip "sm/$f"
done

echo "sm/: $(ls sm/*.avif | wc -l) files, $(du -ck sm/*.avif | tail -1 | cut -f1) kB"
