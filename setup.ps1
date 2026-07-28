# Create the four virtualenvs layout-bench needs (Windows).
#   powershell -ExecutionPolicy Bypass -File setup.ps1            # all of them
#   powershell -ExecutionPolicy Bypass -File setup.ps1 base,onnx  # just these
param([string[]]$Envs = @("base", "onnx", "torch", "unstructured"))

$ErrorActionPreference = "Stop"
$repo = $PSScriptRoot
$venvs = Join-Path $repo ".venvs"
New-Item -ItemType Directory -Force -Path $venvs | Out-Null

foreach ($name in $Envs) {
  $req = Join-Path $repo "requirements\$name.txt"
  if (-not (Test-Path $req)) { Write-Warning "no requirements/$name.txt - skipping"; continue }

  $dir = Join-Path $venvs $name
  Write-Host "=== $name -> $dir ===" -ForegroundColor Cyan
  if (-not (Test-Path $dir)) { python -m venv $dir }

  $py = Join-Path $dir "Scripts\python.exe"
  & $py -m pip install --upgrade pip --quiet
  & $py -m pip install -r $req
}

Write-Host "`nDone. Run the benchmark with:  python bench.py --all" -ForegroundColor Green
