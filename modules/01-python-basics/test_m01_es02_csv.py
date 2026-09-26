from pathlib import Path

import pytest
from es02_csv import read_transactions, total_by_category

SAMPLE = Path(__file__).resolve().parents[2] / "data" / "samples" / "transactions_simple.csv"


def test_read_transactions_returns_one_dict_per_row():
    rows = read_transactions(SAMPLE)
    assert len(rows) == 20
    assert rows[0] == {
        "date": "02/01/2025",
        "description": "Stipendio gennaio",
        "amount": "2.100,00",
        "category": "Stipendio",
    }


def test_read_transactions_keeps_values_as_strings():
    for row in read_transactions(SAMPLE):
        assert all(isinstance(value, str) for value in row.values())


def test_read_transactions_handles_accents():
    descriptions = {row["description"] for row in read_transactions(SAMPLE)}
    assert "Caffè al bar" in descriptions


def test_total_by_category_sums_amounts():
    totals = total_by_category(read_transactions(SAMPLE))
    assert set(totals) == {
        "Stipendio",
        "Spesa",
        "Bar",
        "Trasporti",
        "Ristoranti",
        "Casa",
        "Abbonamenti",
        "Salute",
        "Regali",
    }
    assert totals["Stipendio"] == pytest.approx(4200.0)
    assert totals["Casa"] == pytest.approx(-1651.60)
    assert totals["Bar"] == pytest.approx(-3.60)
    assert totals["Spesa"] == pytest.approx(-177.50)


def test_total_by_category_with_no_transactions():
    assert total_by_category([]) == {}
