from __future__ import annotations
import argparse, hashlib, json, os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import requests

BASE=Path(__file__).resolve().parents[1]
RAW=BASE/"data"/"raw"; STATE=BASE/"data"/"state"
DEFAULT_URL=os.getenv("TSE_RESULTS_URL","https://resultados.tse.jus.br/oficial/ele2026/6257/dados/br/br-c0001-e006257-u.json")

def canonical_hash(payload:dict)->str:
    return hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def collect_once(url:str)->Path|None:
    r=requests.get(url,timeout=30,headers={"User-Agent":"ComuniDados-Eleicoes/0.1"})
    r.raise_for_status(); payload=r.json()
    if not isinstance(payload,dict) or not (payload.get("cand") or payload.get("candidatos")):
        raise ValueError("Payload recebido não corresponde ao EA20 esperado; nada será persistido.")
    digest=canonical_hash(payload); STATE.mkdir(parents=True,exist_ok=True)
    hf=STATE/"last.sha256"
    if hf.exists() and hf.read_text().strip()==digest: return None
    now=datetime.now(ZoneInfo("America/Sao_Paulo")); target=RAW/now.strftime("%Y-%m-%d")
    target.mkdir(parents=True,exist_ok=True); path=target/f"snapshot_{now:%Y%m%d_%H%M%S}.json"
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8"); hf.write_text(digest,encoding="utf-8")
    return path

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--once",action="store_true"); p.add_argument("--url",default=DEFAULT_URL); a=p.parse_args()
    if not a.once: p.error("Use --once; o agendamento pertence ao GitHub Actions.")
    print(collect_once(a.url) or "sem alteração")
