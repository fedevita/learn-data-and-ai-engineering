"""es00 · Il primo test verde.

Completa la funzione `greet` e lancia: uv run pytest modules/00-setup
"""


def greet(name: str) -> str:
    """Restituisce il saluto nel formato "Ciao, <name>!".

    Esempio: greet("Anna") -> "Ciao, Anna!"
    """
    return f"Ciao, {name}!"
