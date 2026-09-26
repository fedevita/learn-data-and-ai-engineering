"""es02 · Leggere un CSV e sommare per categoria.

Lancia i test con: uv run pytest modules/01-python-basics -k es02
Suggerimento: ti servono il modulo `csv` e `parse_amount` da es01_parsing.
"""

from pathlib import Path


def read_transactions(path: str | Path) -> list[dict[str, str]]:
    """Legge un CSV di transazioni e restituisce una lista di dizionari, uno per riga.

    Le chiavi sono le intestazioni del file (date, description, amount, category).
    I valori restano stringhe: nessuna conversione qui.
    """
    raise NotImplementedError("TODO es02: implementa read_transactions")


def total_by_category(transactions: list[dict[str, str]]) -> dict[str, float]:
    """Somma gli importi per categoria.

    Esempio: [{"category": "Bar", "amount": "-1,20"}, {"category": "Bar", "amount": "-1,20"}]
             -> {"Bar": -2.4}
    Con una lista vuota restituisce un dizionario vuoto.
    """
    raise NotImplementedError("TODO es02: implementa total_by_category")
