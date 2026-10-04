from __future__ import annotations

import html
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REPORTS = BASE / "reports"


def build_placeholder() -> Path:
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / "index.html"
    body = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ComuniDados | Eleições 2026</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#111;color:#f4f1e8}.wrap{max-width:1100px;margin:auto;padding:40px 24px}
.brand{letter-spacing:.08em}.card{margin-top:32px;padding:28px;border:1px solid #383838;border-radius:18px;background:#181818}
.muted{color:#aaa}h1{font-size:clamp(2rem,6vw,4rem);margin:.2em 0}
</style></head><body><main class="wrap"><div class="brand">COMUNIDADOS · ML & DATA PRODUCTS</div>
<h1>Eleições 2026</h1><p>Presidência da República · Brasil</p>
<section class="card"><h2>V0 em incubação</h2><p>O painel será preenchido após a primeira coleta oficial validada.</p>
<p class="muted">Fonte: Tribunal Superior Eleitoral (TSE). Painel independente e não oficial.</p></section>
</main></body></html>"""
    out.write_text(body, encoding="utf-8")
    return out


if __name__ == "__main__":
    print(build_placeholder())
