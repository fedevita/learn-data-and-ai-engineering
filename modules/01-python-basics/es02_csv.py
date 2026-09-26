"""es02 · Leggere un CSV e sommare per categoria.

Lancia i test con: uv run pytest modules/01-python-basics -k es02
Suggerimento: ti servono il modulo `csv` e `parse_amount` da es01_parsing.
"""

import csv
from pathlib import Path

from es01_parsing import parse_amount


def read_transactions(path: str | Path) -> list[dict[str, str]]:
    """Legge un CSV di transazioni e restituisce una lista di dizionari, uno per riga.

    Le chiavi sono le intestazioni del file (date, description, amount, category).
    I valori restano stringhe: nessuna conversione qui.
    """
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return rows


def total_by_category(transactions: list[dict[str, str]]) -> dict[str, float]:
    """Somma gli importi per categoria.

    Esempio: [{"category": "Bar", "amount": "-1,20"}, {"category": "Bar", "amount": "-1,20"}]
             -> {"Bar": -2.4}
    Con una lista vuota restituisce un dizionario vuoto.
    """
    totals = {}
    for t in transactions:
        cat = t["category"]
        totals[cat] = totals.get(cat, 0.0) + parse_amount(t["amount"])
    return totals
