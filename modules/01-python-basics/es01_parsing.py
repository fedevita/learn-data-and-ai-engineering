"""es01 · Parsing di importi e date italiane.

Lancia i test con: uv run pytest modules/01-python-basics -k es01
"""


def parse_amount(text: str) -> float:
    """Converte un importo in formato italiano in float.

    Esempi:
        "1.234,56" -> 1234.56
        "-12,50"   -> -12.5
        "  7,10  " -> 7.1
        "100"      -> 100.0

    Solleva ValueError se il testo non è un importo valido (es. "abc", "").
    """
    raise NotImplementedError("TODO es01: implementa parse_amount")


def parse_date(text: str) -> str:
    """Converte una data "gg/mm/aaaa" nel formato ISO "aaaa-mm-gg".

    Esempi:
        "31/12/2024" -> "2024-12-31"
        "5/3/2025"   -> "2025-03-05"

    Solleva ValueError se il formato è sbagliato o la data non esiste.
    """
    raise NotImplementedError("TODO es01: implementa parse_date")
