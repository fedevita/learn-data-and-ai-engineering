# 07 · Moduli, file e libreria standard

## Import

Un modulo è un file `.py`. La libreria standard è la collezione di moduli che arriva con Python:
niente da installare.

```python
import csv                          # poi: csv.DictReader(...)
from datetime import datetime       # poi: datetime.strptime(...)
from pathlib import Path
import polars as pl                 # alias, tipico dei pacchetti esterni (M03)
```

Gli import stanno in cima al file, in tre gruppi: libreria standard, pacchetti esterni, moduli
tuoi. Ruff li ordina al salvataggio.

`from es01_parsing import parse_amount` funziona perché i due file sono nella stessa cartella e
pytest la mette nel percorso di ricerca. È il nostro caso speciale da esercizi; in M03 vedrai come
si organizza un progetto vero in pacchetti.

### `if __name__ == "__main__":`

Quando esegui un file direttamente (`uv run python file.py`, o il bottone ▶ di VS Code), la
variabile `__name__` vale `"__main__"`. Quando il file viene importato, vale il nome del modulo.
Quindi:

```python
if __name__ == "__main__":
    print(parse_amount("1.234,56"))
```

gira solo se lanci il file, non quando i test lo importano. È la "zona prove" degli esercizi.

## File e percorsi

```python
from pathlib import Path

path = Path("data") / "samples" / "transactions_simple.csv"   # "/" unisce i pezzi
path.exists(), path.name, path.suffix, path.parent
text = path.read_text(encoding="utf-8")
for p in Path("data/raw").glob("*.csv"):
    ...

with open(path, encoding="utf-8", newline="") as f:
    for line in f:
        ...
```

- `with` chiude il file anche se qualcosa va storto. Sempre.
- `encoding="utf-8"`: sempre, esplicito. Su Windows il default non è UTF-8.
- I percorsi relativi partono dalla cartella da cui lanci il comando, non da dove sta il file. Per
  questo lanciamo tutto dalla radice del progetto, e i test costruiscono il percorso a partire da
  `__file__`.

## La libreria standard che serve a un data engineer

| Modulo | Per cosa | Lo usiamo in |
|---|---|---|
| `csv` | leggere e scrivere CSV correttamente | es02 |
| `json` | `json.load(f)`, `json.dumps(obj, indent=2)` | es05 |
| `datetime` | date, ore, differenze, formati | es01 |
| `pathlib` | percorsi | ovunque |
| `logging` | messaggi con livello (info, warning, error) al posto di `print` | es03 |
| `dataclasses` | record tipizzati senza codice ripetitivo | es04 |
| `argparse` | argomenti da linea di comando | es05 |
| `collections` | `Counter`, `defaultdict` | es02, versione pro |
| `decimal` | soldi senza errori di arrotondamento | M04 |
| `sqlite3` | un database SQL in un file, senza server | M02 usa DuckDB, un cugino più adatto all'analisi |
| `itertools`, `statistics`, `re` | combinazioni, statistiche, espressioni regolari | quando servono |

Riferimento: https://docs.python.org/it/3/library/index.html. Quando devi fare qualcosa di
"standard" (leggere un formato, calcolare una data, ordinare in modo strano), la risposta è quasi
sempre lì dentro, prima di scrivere codice tuo.

## Pacchetti esterni

`uv add polars` scarica il pacchetto, lo scrive in `pyproject.toml` e aggiorna `uv.lock`. Da lì,
`import polars as pl`. Lo faremo in M03; per ora basta la libreria standard.

## Prova tu

1. Nel REPL: `from pathlib import Path`, poi `Path(".").resolve()` e
   `list(Path("data").glob("**/*.csv"))`.
2. `import json`, poi `print(json.dumps({"a": 1, "b": [1, 2]}, indent=2))`.
3. `from collections import Counter`, poi `Counter(["a", "b", "a"])` e
   `help(Counter.most_common)`.
