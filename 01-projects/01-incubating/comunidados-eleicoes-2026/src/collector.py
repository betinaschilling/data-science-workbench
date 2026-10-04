from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "raw"
STATE = BASE / "data" / "state"
DEFAULT_URL = os.getenv("TSE_RESULTS_URL", "")


def canonical_hash(payload: dict) -> str:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def collect_once(url: str) -> Path | None:
    if not url:
        raise RuntimeError("Defina TSE_RESULTS_URL após validar o endpoint oficial.")
    response = requests.get(url, timeout=30, headers={"User-Agent": "ComuniDados-Eleicoes/0.1"})
    response.raise_for_status()
    payload = response.json()
    digest = canonical_hash(payload)

    STATE.mkdir(parents=True, exist_ok=True)
    hash_file = STATE / "last.sha256"
    if hash_file.exists() and hash_file.read_text().strip() == digest:
        return None

    now = datetime.now(ZoneInfo("America/Sao_Paulo"))
    target = RAW / now.strftime("%Y-%m-%d")
    target.mkdir(parents=True, exist_ok=True)
    path = target / f"snapshot_{now:%Y%m%d_%H%M%S}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    hash_file.write_text(digest, encoding="utf-8")
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Executa exatamente uma coleta.")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()
    if not args.once:
        parser.error("A V0 aceita apenas --once; o scheduler será externo.")
    saved = collect_once(args.url)
    print(saved if saved else "sem alteração")
