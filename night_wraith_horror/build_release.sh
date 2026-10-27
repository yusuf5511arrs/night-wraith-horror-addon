#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/generate_placeholder_assets.py
python3 - <<'PY'
import os, zipfile, pathlib
base = pathlib.Path('.').resolve()
# Build archive from the two pack roots; user can rename .zip to .mcaddon manually.
out = base / 'night_wraith_horror_release.zip'
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for folder in ['behavior_pack', 'resource_pack']:
        root = base / folder
        for file in root.rglob('*'):
            if file.is_file():
                z.write(file, arcname=str(file.relative_to(base)))
print(f'Released zip: {out}')
PY
