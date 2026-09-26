import logging
from pathlib import Path

import pytest
from es02_csv import read_transactions
from es03_cleaning import UNCATEGORIZED, clean_transaction, clean_transactions

MESSY = Path(__file__).resolve().parents[2] / "data" / "samples" / "transactions_messy.csv"


def test_clean_transaction_converts_types_and_strips():
    row = {
        "date": "02/01/2025",
        "description": "  Spesa Esselunga  ",
        "amount": "-64,30",
        "category": " Spesa ",
    }
    cleaned = clean_transaction(row)
    assert cleaned["date"] == "2025-01-02"
    assert cleaned["description"] == "Spesa Esselunga"
    assert cleaned["amount"] == pytest.approx(-64.3)
    assert isinstance(cleaned["amount"], float)
    assert cleaned["category"] == "Spesa"


def test_clean_transaction_fills_missing_category():
    row = {"date": "04/01/2025", "description": "Caffè al bar", "amount": "-1,20", "category": ""}
    assert clean_transaction(row)["category"] == UNCATEGORIZED


@pytest.mark.parametrize(
    ("date", "amount"),
    [
        ("31/02/2025", "-58,40"),  # data inesistente
        ("2025-01-12", "-58,40"),  # formato sbagliato
        ("07/01/2025", ""),  # importo vuoto
        ("15/01/2025", "abc"),  # importo non numerico
    ],
)
def test_clean_transaction_rejects_invalid_rows(date, amount):
    row = {"date": date, "description": "x", "amount": amount, "category": "Casa"}
    with pytest.raises(ValueError):
        clean_transaction(row)


def test_clean_transactions_keeps_only_valid_rows_in_order(caplog):
    rows = read_transactions(MESSY)
    assert len(rows) == 12
    with caplog.at_level(logging.WARNING):
        cleaned = clean_transactions(rows)
    assert [c["description"] for c in cleaned] == [
        "Stipendio gennaio",
        "Spesa Esselunga",
        "Caffè al bar",
        "Cena pizzeria",
        "Netflix",
        "Caffè al bar",
        "Affitto",
        "Farmacia",
    ]
    assert cleaned[2]["category"] == UNCATEGORIZED
    assert cleaned[0]["amount"] == pytest.approx(2100.0)


def test_clean_transactions_logs_one_warning_per_invalid_row(caplog):
    with caplog.at_level(logging.WARNING):
        clean_transactions(read_transactions(MESSY))
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert len(warnings) == 4
    messages = [r.getMessage() for r in warnings]
    for line_no in (5, 6, 8, 9):
        assert any(f"riga {line_no}" in m for m in messages), (
            f"nessun warning per la riga {line_no}"
        )


def test_clean_transactions_with_valid_rows_logs_nothing(caplog):
    rows = [{"date": "02/01/2025", "description": "x", "amount": "1,00", "category": "A"}]
    with caplog.at_level(logging.WARNING):
        cleaned = clean_transactions(rows)
    assert len(cleaned) == 1
    assert caplog.records == []


def test_clean_transactions_with_no_rows():
    assert clean_transactions([]) == []
