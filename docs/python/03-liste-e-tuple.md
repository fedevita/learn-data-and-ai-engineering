# 03 · Liste e tuple

## Liste

Una lista è una sequenza ordinata e modificabile. Può contenere di tutto, ma in pratica contiene
elementi dello stesso tipo: una lista di stringhe, una lista di dizionari (una tabella).

```python
>>> xs = [30, 10, 20]
>>> len(xs), xs[0], xs[-1], xs[1:]
(3, 30, 20, [10, 20])
>>> 10 in xs
True
```

### Modificare (sul posto: cambiano `xs` e restituiscono `None`)

| Metodo | Effetto |
|---|---|
| `xs.append(x)` | aggiunge in coda |
| `xs.extend(altra)` | aggiunge tutti gli elementi di un'altra lista |
| `xs.insert(i, x)` | inserisce in posizione `i` |
| `xs.pop()` / `xs.pop(i)` | toglie e restituisce l'ultimo / quello in posizione `i` |
| `xs.remove(x)` | toglie la prima occorrenza di `x` (`ValueError` se non c'è) |
| `xs.sort()` | ordina sul posto |
| `xs.reverse()` | inverte sul posto |
| `xs.clear()` | svuota |
| `xs[i] = x` / `del xs[i]` | sostituisce / cancella per posizione |

### Interrogare (restituiscono un valore, `xs` non cambia)

`xs.index(x)`, `xs.count(x)`, `sorted(xs)`, `reversed(xs)`, `len(xs)`, `sum(xs)`, `min(xs)`,
`max(xs)`, `any(xs)`, `all(xs)`.

`sort` e `sorted` accettano `key=` ("ordina secondo cosa") e `reverse=True`:

```python
>>> rows = [{"name": "b", "amount": 5}, {"name": "a", "amount": 9}]
>>> sorted(rows, key=lambda r: r["amount"], reverse=True)
[{'name': 'a', 'amount': 9}, {'name': 'b', 'amount': 5}]
```

`lambda r: r["amount"]` è una funzione anonima di una riga: prende `r`, restituisce `r["amount"]`.

### Scorrere

```python
for x in xs:                    # gli elementi
for i, x in enumerate(xs):      # posizione e elemento
for a, b in zip(xs, ys):        # due liste in parallelo
for i in range(len(xs)):        # solo gli indici (raramente serve davvero)
```

### List comprehension: costruire una lista in una riga

```python
>>> [x * 2 for x in xs]
[60, 20, 40]
>>> [x for x in xs if x > 15]
[30, 20]
>>> [row["amount"] for row in rows]
[5, 9]
```

Equivale a un `for` con `append`, ma dichiara l'intento in modo più chiaro. Se diventa lunga o
annidata, torna al `for`.

### Trappole

- `xs = xs.sort()` → `xs` diventa `None`. O `xs.sort()` da solo, o `ys = sorted(xs)`.
- `ys = xs` non copia: sono due nomi per la stessa lista. Modifichi `ys`, cambia anche `xs`.
  Copia con `ys = xs.copy()` o `ys = list(xs)`.
- Non aggiungere o togliere elementi a una lista mentre la scorri con `for`. Costruiscine una
  nuova.
- `xs[3]` su una lista di 3 elementi → `IndexError`. Gli indici partono da 0.

## Tuple

Una tupla è una lista immutabile: `(1, 2)`, `("Anna", 1234.5)`. Si usa per record fissi e per
restituire più valori da una funzione:

```python
def min_max(xs: list[float]) -> tuple[float, float]:
    return min(xs), max(xs)      # restituisce una tupla

lo, hi = min_max([3, 1, 2])      # "unpacking": lo=1, hi=3
```

L'unpacking funziona ovunque ci sia una sequenza: `for k, v in d.items()`, `a, b = b, a` per
scambiare due valori.

## Prova tu

1. Parti da `xs = [3, 1, 2]`. Fai `ys = xs`, poi `ys.append(9)` e stampa `xs`. Poi rifallo con
   `ys = xs.copy()`.
2. Data `rows = [{"c": "Bar", "a": -1.2}, {"c": "Casa", "a": -750}, {"c": "Bar", "a": -1.2}]`,
   ottieni in una riga la lista delle sole categorie, e in un'altra le righe ordinate per
   importo.
3. `sorted(["31/12/2024", "01/01/2025"])` e poi `sorted(["2024-12-31", "2025-01-01"])`. Guarda
   l'ordine e ripensa alla domanda di es01.
