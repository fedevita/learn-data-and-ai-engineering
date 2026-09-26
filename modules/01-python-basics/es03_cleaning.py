"""es03 · Righe malformate: gestione errori e logging.

Lancia i test con: uv run pytest modules/01-python-basics -k es03
Ti servono: `from es01_parsing import parse_amount, parse_date`, try/except, logging.
"""

import logging

from es01_parsing import parse_amount, parse_date
from es02_csv import read_transactions

logger = logging.getLogger(__name__)

UNCATEGORIZED = "Senza categoria"


def clean_transaction(row: dict[str, str]) -> dict[str, str | float]:
    """Converte una riga grezza (tutte stringhe) in una riga pulita.

    - "date": da "gg/mm/aaaa" a ISO "aaaa-mm-gg" (parse_date)
    - "description": senza spazi ai bordi
    - "amount": float (parse_amount)
    - "category": senza spazi ai bordi; se vuota, UNCATEGORIZED

    Solleva ValueError se la data o l'importo non sono validi. Non gestisce
    l'errore: lo segnala a chi chiama.
    """
    result = {}
    result["date"] = parse_date(row["date"])
    result["description"] = row["description"].strip()
    result["amount"] = parse_amount(row["amount"])
    result["category"] = row["category"].strip() or UNCATEGORIZED
    return result


def clean_transactions(rows: list[dict[str, str]]) -> list[dict[str, str | float]]:
    """Pulisce tutte le righe, saltando quelle non valide.

    Per ogni riga che clean_transaction rifiuta (ValueError) scrive un
    logger.warning che contiene "riga N" e il motivo, dove N è il numero di
    riga come lo vede l'editor: l'intestazione è la riga 1, quindi la prima
    transazione è la riga 2.

    Restituisce solo le righe valide, nell'ordine originale.
    """
    rows_cleaned = []
    for line_no, row in enumerate(rows, start=2):
        try:
            rows_cleaned.append(clean_transaction(row))
        except ValueError as e:
            logger.warning("riga %d scartata: %s", line_no, e)
    return rows_cleaned


if __name__ == "__main__":
    # Zona prove: lancia questo file con ▶ per vedere i warning sul file "sporco".
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    cleaned = clean_transactions(read_transactions("data/samples/transactions_messy.csv"))
    print(f"{len(cleaned)} righe valide")
