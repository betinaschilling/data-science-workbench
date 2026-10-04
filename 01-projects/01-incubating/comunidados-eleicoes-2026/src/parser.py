from __future__ import annotations

from typing import Any


def _first(obj: dict[str, Any], *keys: str, default=None):
    for key in keys:
        if key in obj and obj[key] not in (None, ""):
            return obj[key]
    return default


def parse_ea20(payload: dict[str, Any], collected_at: str) -> list[dict[str, Any]]:
    """Normaliza campos candidatos conhecidos, falhando explicitamente se o contrato não for reconhecido."""
    candidates = payload.get("cand") or payload.get("candidatos")
    if not isinstance(candidates, list):
        raise ValueError("Contrato EA20 não reconhecido: lista de candidatos ausente.")

    rows = []
    for c in candidates:
        rows.append({
            "collected_at": collected_at,
            "candidate_number": _first(c, "n", "numero"),
            "candidate_name": _first(c, "nm", "nome"),
            "party": _first(c, "cc", "partido", "sg"),
            "votes": _first(c, "vap", "votos"),
            "vote_share": _first(c, "pvap", "percentual"),
            "source_update": _first(payload, "dt", "dataAtualizacao"),
            "processed_share": _first(payload, "pst", "percentualSecoesTotalizadas"),
        })
    return rows
