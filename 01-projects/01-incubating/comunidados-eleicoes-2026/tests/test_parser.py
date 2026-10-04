import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from collector import canonical_hash
from parser import parse_ea20


def test_hash_independent_of_key_order():
    assert canonical_hash({"a": 1, "b": 2}) == canonical_hash({"b": 2, "a": 1})


def test_parse_minimal_ea20():
    payload = {"dt": "04/10/2026", "pst": "10,00", "cand": [{"n": "10", "nm": "Exemplo", "cc": "ABC", "vap": "100", "pvap": "50,00"}]}
    rows = parse_ea20(payload, "2026-10-04T18:00:00-03:00")
    assert rows[0]["candidate_name"] == "Exemplo"
    assert rows[0]["processed_share"] == "10,00"
