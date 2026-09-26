# 05 · Controllo di flusso e funzioni

## `if`, `for`, `while`

```python
if amount < 0:
    kind = "uscita"
elif amount > 0:
    kind = "entrata"
else:
    kind = "zero"

kept = []
for row in rows:
    if row["amount"] == "":
        continue              # salta questa riga, passa alla prossima
    if len(kept) == 10:
        break                 # esce dal ciclo
    kept.append(row)

while not done:
    ...
```

L'indentazione (4 spazi) non è estetica: definisce cosa sta dentro un blocco. `ruff format` la
sistema per te.

`range(5)` → 0, 1, 2, 3, 4 · `range(2, 5)` → 2, 3, 4 · `range(0, 10, 2)` → 0, 2, 4, 6, 8.

## Funzioni

```python
def parse_amount(text: str) -> float:
    """Una riga che dice cosa fa. Poi, se serve, i dettagli."""
    cleaned = text.strip().replace(".", "").replace(",", ".")
    return float(cleaned)
```

- `def nome(parametri) -> tipo_del_risultato:`. Nomi in `snake_case`, e sono verbi: `parse_`,
  `read_`, `total_`.
- `return` termina la funzione. Senza `return`, restituisce `None`.
- Le variabili create dentro (`cleaned`) esistono solo lì. È una cosa buona: la funzione dipende
  solo dai suoi parametri, e la puoi capire e testare da sola.

### Chiamare

```python
parse_amount("12,50")                        # per posizione
read_transactions(path="data/x.csv")         # per nome
open(path, encoding="utf-8", newline="")     # misto: i nomi rendono chiaro cosa è cosa
```

### Valori predefiniti

```python
def read_csv(path: str, sep: str = ",") -> list[dict[str, str]]:
```

`sep` è opzionale. Trappola classica: mai un valore predefinito modificabile (`def f(xs=[])`),
perché quella lista viene condivisa tra tutte le chiamate. Usa `xs=None` e crea la lista dentro.

### Type hints

Documentano il contratto; VS Code li usa per l'autocompletamento e per segnalarti errori prima
di eseguire. Quelli che userai: `int`, `float`, `str`, `bool`, `list[str]`, `dict[str, float]`,
`list[dict[str, str]]`, `str | None` (può essere `None`), `Path`.

### Le funzioni sono valori

Puoi passarle ad altre funzioni: `sorted(rows, key=row_date)`. `lambda` crea una funzione
usa-e-getta: `key=lambda r: r["date"]`.

## Stile che conta davvero

- Una funzione fa una cosa e sta in una schermata. Se fa due cose, sono due funzioni.
- "Guard clause": prima i casi anomali con un `return` o un `raise`, poi il caso normale, senza
  `else` annidati.

  ```python
  if not rows:
      return {}
  ...  # caso normale, non indentato
  ```

- Un nome buono vale più di un commento. `t` no, `transactions` sì. `data` quasi mai.

## Prova tu

1. Scrivi `def kind(amount: float) -> str` che restituisce `"entrata"`, `"uscita"` o `"zero"`.
   Provala nel REPL con tre valori.
2. Scrivi `def is_expense(row: dict[str, str]) -> bool` e usala in una list comprehension per
   filtrare `rows`.
3. Scrivi una funzione con un parametro predefinito e chiamala nei due modi.
