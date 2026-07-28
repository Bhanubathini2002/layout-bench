#!/usr/bin/env bash
# Create the four virtualenvs layout-bench needs (macOS / Linux).
#   ./setup.sh                 # all of them
#   ./setup.sh base onnx       # just these
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
venvs="$repo/.venvs"
mkdir -p "$venvs"

envs=("$@")
[ ${#envs[@]} -eq 0 ] && envs=(base onnx torch unstructured)

for name in "${envs[@]}"; do
  req="$repo/requirements/$name.txt"
  if [ ! -f "$req" ]; then
    echo "no requirements/$name.txt - skipping" >&2
    continue
  fi

  dir="$venvs/$name"
  echo "=== $name -> $dir ==="
  [ -d "$dir" ] || python3 -m venv "$dir"

  "$dir/bin/python" -m pip install --upgrade pip --quiet
  "$dir/bin/python" -m pip install -r "$req"
done

echo
echo "Done. Run the benchmark with:  python3 bench.py --all"
