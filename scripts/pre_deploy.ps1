# FinAuto docs v1 publish gate — run from finauto-docs/
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..

function Run-Step($label, $command) {
    Write-Host "=== $label ==="
    Invoke-Expression $command
    if ($LASTEXITCODE -ne 0) { throw "$label failed with exit $LASTEXITCODE" }
}

Run-Step "VG-D01 mkdocs build" "python -m mkdocs build --strict"
Run-Step "VG-D04 help map" "python scripts/validate_help_urls.py --strict"
Run-Step "VG-D06 legacy styles" "python scripts/check_legacy_styles.py --docs-dir docs"
Run-Step "VG-D07 orphan assets" "python scripts/check_orphan_assets.py --docs-dir docs"
Run-Step "VG-D08 corpus" "python scripts/validate_corpus.py --corpus site/ai/corpus.jsonl"
Run-Step "RAG smoke" "python scripts/rag_smoke.py --corpus site/ai/corpus.jsonl"
Run-Step "Help matrix" "python scripts/smoke_help_matrix.py --site-dir site"

Write-Host "=== ALL GATES PASSED ==="
