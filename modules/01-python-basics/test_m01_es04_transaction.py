import dataclasses
import logging
from pathlib import Path

import pytest
from es03_cleaning import UNCATEGORIZED
from es04_transaction import Transaction, load_transactions

SAMPLES = Path(__file__).resolve().parents[2] / "data" / "samples"

RAW = {
    "date": "02/01/2025",
    "description": "  Spesa Esselunga  ",
    "amount": "-64,30",
    "category": " Spesa ",
}


def test_from_row_converts_and_strips():
    t = Transaction.from_row(RAW)
    assert t.date == "2025-01-02"
    assert t.description == "Spesa Esselunga"
    assert t.amount == pytest.approx(-64.3)
    assert isinstance(t.amount, float)
    assert t.category == "Spesa"


def test_from_row_fills_missing_category():
    t = Transaction.from_row({**RAW, "category": ""})
    assert t.category == UNCATEGORIZED


@pytest.mark.parametrize(
    ("date", "amount"),
    [
        ("31/02/2025", "-1,00"),  # data inesistente
        ("02/01/2025", "abc"),  # importo non numerico
    ],
)
def test_from_row_rejects_invalid_rows(date, amount):
    with pytest.raises(ValueError):
        Transaction.from_row({**RAW, "date": date, "amount": amount})


def test_category_defaults_to_uncategorized():
    t = Transaction(date="2025-01-02", description="Caffè al bar", amount=-1.2)
    assert t.category == UNCATEGORIZED


@pytest.mark.parametrize("field", ["description", "category"])
@pytest.mark.parametrize("value", ["", "   "])
def test_rejects_blank_text_fields(field, value):
    kwargs = {
        "date": "2025-01-02",
        "description": "Caffè al bar",
        "amount": -1.2,
        "category": "Bar",
    }
    kwargs[field] = value
    with pytest.raises(ValueError):
        Transaction(**kwargs)


def test_equal_fields_mean_equal_transactions():
    a = Transaction.from_row(RAW)
    b = Transaction.from_row(dict(RAW))
    assert a == b
    assert a is not b


def test_transaction_is_frozen():
    t = Transaction.from_row(RAW)
    with pytest.raises(dataclasses.FrozenInstanceError):
        t.amount = 0.0


def test_month():
    assert Transaction.from_row(RAW).month == "2025-01"


def test_load_transactions_reads_a_clean_file_without_warnings(caplog):
    with caplog.at_level(logging.WARNING):
        transactions = load_transactions(SAMPLES / "transactions_simple.csv")
    assert len(transactions) == 20
    assert all(isinstance(t, Transaction) for t in transactions)
    assert caplog.records == []


def test_load_transactions_skips_invalid_rows_with_a_warning(caplog):
    with caplog.at_level(logging.WARNING):
        transactions = load_transactions(SAMPLES / "transactions_messy.csv")
    assert [t.description for t in transactions] == [
        "Stipendio gennaio",
        "Spesa Esselunga",
        "Caffè al bar",
        "Cena pizzeria",
        "Netflix",
        "Caffè al bar",
        "Affitto",
        "Farmacia",
    ]
    assert transactions[0].amount == pytest.approx(2100.0)
    assert transactions[0].month == "2025-01"
    assert transactions[2].category == UNCATEGORIZED
    messages = [r.getMessage() for r in caplog.records if r.levelno == logging.WARNING]
    assert len(messages) == 4
    for line_no in (5, 6, 8, 9):
        assert any(f"riga {line_no}" in m for m in messages), (
            f"nessun warning per la riga {line_no}"
        )
