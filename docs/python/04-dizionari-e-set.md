# 04 · Dizionari e set

## Dizionari

Un dizionario associa chiavi a valori. È la struttura più usata nel lavoro sui dati: una riga di
CSV letta con `DictReader` è un dizionario, un record JSON è un dizionario.

```python
>>> row = {"date": "02/01/2025", "amount": "2.100,00", "category": "Stipendio"}
>>> row["category"]
'Stipendio'
>>> row["note"]
KeyError: 'note'
>>> row.get("note")              # None se la chiave manca
>>> row.get("note", "")          # valore predefinito se manca
''
>>> "amount" in row              # cerca tra le chiavi
True
```

### Scrivere

```python
row["note"] = "spesa"            # aggiunge o sovrascrive
del row["note"]                  # cancella (KeyError se manca)
row.pop("note", None)            # cancella e restituisce, senza errore se manca
row.update({"a": 1, "b": 2})     # aggiunge o sovrascrive più chiavi insieme
```

### Scorrere

```python
for key in row:                      # le chiavi
for key, value in row.items():       # le coppie
for value in row.values():           # i valori
```

`row.keys()`, `row.values()`, `row.items()` non sono liste ma "viste": se ti serve una lista,
`list(row.keys())`. I dizionari mantengono l'ordine di inserimento.

### L'idioma dell'accumulo (ti serve in es02)

Sommare per categoria vuol dire: per ogni riga, prendi il totale corrente della sua categoria
(0 se è la prima volta che la incontri) e aggiungi l'importo.

```python
totals = {}
for row in rows:
    cat = row["category"]
    totals[cat] = totals.get(cat, 0.0) + parse_amount(row["amount"])
```

Versione "pro" con lo stesso risultato: `collections.defaultdict(float)` crea da solo lo `0.0`
alla prima chiave; `collections.Counter` conta le occorrenze. Scheda 07.

### Dict comprehension

```python
>>> {row["category"]: row["amount"] for row in rows}
```

Le chiavi duplicate si sovrascrivono: resta l'ultima.

### Strutture annidate

Una tabella è una lista di dizionari: `rows[0]["amount"]`. Un JSON può avere dizionari dentro
dizionari: `data["account"]["iban"]`. Quando non sai com'è fatto un oggetto, `print(type(x))` e
`print(x.keys())` a ogni livello, oppure il debugger.

### Trappole

- `KeyError` = quella chiave non c'è. Controlla il nome esatto (maiuscole, spazi) con
  `print(row.keys())`.
- Le chiavi devono essere immutabili: stringhe, numeri, tuple sì; liste no.
- `d = {}` è un dizionario vuoto, non un set. Il set vuoto è `set()`.

## Set

Un set è una collezione senza duplicati e senza ordine. Serve per "quali categorie esistono?" e
per le operazioni tra insiemi.

```python
>>> cats = {row["category"] for row in rows}      # set comprehension
>>> set(["Bar", "Casa", "Bar"])
{'Bar', 'Casa'}
>>> "Bar" in cats
True
>>> cats.add("Salute"); cats.discard("Casa")
>>> {1, 2, 3} & {2, 3, 4}, {1, 2, 3} | {4}, {1, 2, 3} - {2}
({2, 3}, {1, 2, 3, 4}, {1, 3})
```

`len(set(xs)) == len(xs)` è il modo rapido per chiedere "ci sono duplicati?".

## Prova tu

1. Ricostruisci a mano l'accumulo per categoria con
   `rows = [{"c": "Bar", "a": 1}, {"c": "Casa", "a": 2}, {"c": "Bar", "a": 3}]`.
   Risultato atteso: `{"Bar": 4, "Casa": 2}`.
2. `help(dict.setdefault)`: riscrivi l'accumulo usandolo.
3. Dato `xs = ["a", "b", "a", "c", "b"]`, trova gli elementi che compaiono più di una volta
   (suggerimento: un dizionario che conta, poi un filtro).
