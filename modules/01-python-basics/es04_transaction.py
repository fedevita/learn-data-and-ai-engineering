"""es04 · Dataclass: una Transaction tipizzata con validazione.

Lancia i test con: uv run pytest modules/01-python-basics -k es04
Ti servono (scheda 08): `@dataclass`, campi con tipo, `__post_init__`, `@property`,
`@classmethod`, e `**` per spacchettare un dizionario negli argomenti di una chiamata.
Da importare: `from es02_csv import read_transactions` e
`from es03_cleaning import UNCATEGORIZED, clean_transaction`.
"""

import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from es02_csv import read_transactions
from es03_cleaning import UNCATEGORIZED, clean_transaction, clean_transactions

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Transaction:
    """Una transazione già pulita: campi convertiti e validati.

    - date: str, ISO "aaaa-mm-gg"
    - description: str, senza spazi ai bordi, mai vuota
    - amount: float, negativo per le uscite
    - category: str, mai vuota; se manca vale UNCATEGORIZED (è il default)

    frozen=True: una volta creata non si può modificare (ricordi la review di es03?).
    """

    date: str
    description: str
    amount: float
    category: str = UNCATEGORIZED

    def __post_init__(self) -> None:
        """Gira da solo subito dopo la creazione: qui si valida.

        Solleva ValueError se description o category sono vuote o di soli spazi.
        """
        if self.description.strip() == "" or self.category.strip() == "":
            raise ValueError("The description or category is empty or consists only of spaces.")

    @property
    def month(self) -> str:
        """Il mese della transazione come "aaaa-mm": "2025-01-02" -> "2025-01"."""
        parsed = datetime.strptime(self.date, "%Y-%m-%d")
        parsed_iso = parsed.strftime("%Y-%m")
        return parsed_iso

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "Transaction":
        """Costruisce una Transaction da una riga grezza del CSV (tutte stringhe).

        Riusa clean_transaction di es03, che fa già conversioni e pulizia: qui basta
        trasformare il dizionario pulito in una Transaction. Se la riga non è valida
        clean_transaction solleva ValueError da sola: non serve gestirlo qui.
        """
        return cls(**clean_transaction(row))


def load_transactions(path: str | Path) -> list[Transaction]:
    """Legge il CSV e restituisce le Transaction valide, nell'ordine del file.

    Le righe non valide vengono saltate con un logger.warning che contiene "riga N" e il
    motivo, con la stessa convenzione di es03 (intestazione = riga 1).
    """
    transactions = []
    rows = read_transactions("data/samples/transactions_messy.csv")
    for row in rows:
        transactions.append(Transaction.from_row(row))
    return transactions


if __name__ == "__main__":
    # Zona prove: lancia questo file con ▶ e guarda come si stampa una dataclass.
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    for transaction in load_transactions("data/samples/transactions_messy.csv"):
        print(transaction)
