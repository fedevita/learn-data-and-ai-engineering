"""es04 · Dataclass: una Transaction tipizzata con validazione.

Lancia i test con: uv run pytest modules/01-python-basics -k es04
Ti servono (scheda 08): `@dataclass`, campi con tipo, `__post_init__`, `@property`,
`@classmethod`, e `**` per spacchettare un dizionario negli argomenti di una chiamata.
Da importare: `from es02_csv import read_transactions` e
`from es03_cleaning import UNCATEGORIZED, clean_transaction`.
"""

import logging
from dataclasses import dataclass
from pathlib import Path

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

    # TODO es04: dichiara qui i quattro campi con il loro tipo, nell'ordine sopra.
    # category ha un valore di default: i campi con default vanno dopo quelli senza.

    def __post_init__(self) -> None:
        """Gira da solo subito dopo la creazione: qui si valida.

        Solleva ValueError se description o category sono vuote o di soli spazi.
        """
        raise NotImplementedError("TODO es04: implementa __post_init__")

    @property
    def month(self) -> str:
        """Il mese della transazione come "aaaa-mm": "2025-01-02" -> "2025-01"."""
        raise NotImplementedError("TODO es04: implementa month")

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "Transaction":
        """Costruisce una Transaction da una riga grezza del CSV (tutte stringhe).

        Riusa clean_transaction di es03, che fa già conversioni e pulizia: qui basta
        trasformare il dizionario pulito in una Transaction. Se la riga non è valida
        clean_transaction solleva ValueError da sola: non serve gestirlo qui.
        """
        raise NotImplementedError("TODO es04: implementa from_row")


def load_transactions(path: str | Path) -> list[Transaction]:
    """Legge il CSV e restituisce le Transaction valide, nell'ordine del file.

    Le righe non valide vengono saltate con un logger.warning che contiene "riga N" e il
    motivo, con la stessa convenzione di es03 (intestazione = riga 1).
    """
    raise NotImplementedError("TODO es04: implementa load_transactions")


if __name__ == "__main__":
    # Zona prove: lancia questo file con ▶ e guarda come si stampa una dataclass.
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    for transaction in load_transactions("data/samples/transactions_messy.csv"):
        print(transaction)
