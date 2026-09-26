# 02 · Numeri, stringhe, booleani, None

## Numeri: `int` e `float`

```python
>>> 7 / 2          # divisione: sempre float
3.5
>>> 7 // 2         # divisione intera
3
>>> 7 % 2          # resto
1
>>> 2 ** 10        # potenza
1024
>>> round(3.14159, 2)
3.14
>>> abs(-5), max(3, 9), min([4, 1, 8]), sum([1, 2, 3])
(5, 9, 1, 6)
```

Conversioni: `int("12")`, `float("1.5")`, `str(12)`. Se la stringa non è convertibile:
`ValueError`. Un importo come `"1.234,56"` va preparato prima (es01).

I float non sono esatti: `0.1 + 0.2` dà `0.30000000000000004`. Nei test si confronta con
`pytest.approx`; per i soldi "veri" si usa `decimal.Decimal` oppure i centesimi come interi.
Ci torneremo in M04.

## Stringhe: `str`

Una stringa è una sequenza **immutabile** di caratteri: i metodi non la modificano, restituiscono
una stringa nuova. Se scrivi `s.strip()` senza usare il risultato, non è cambiato niente.

```python
>>> s = "Caffè al bar"
>>> len(s), s[0], s[-1], s[0:5]
(12, 'C', 'r', 'Caffè')
>>> "bar" in s
True
```

I metodi che userai di più:

| Metodo | Esempio | Risultato |
|---|---|---|
| `strip()` | `"  x  ".strip()` | `'x'` |
| `lower()` / `upper()` | `"Bar".lower()` | `'bar'` |
| `replace(a, b)` | `"1.234".replace(".", "")` | `'1234'` |
| `split(sep)` | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `sep.join(lista)` | `"-".join(["2024", "12"])` | `'2024-12'` |
| `startswith(x)` / `endswith(x)` | `"file.csv".endswith(".csv")` | `True` |
| `isdigit()` | `"123".isdigit()` | `True` |
| `zfill(n)` | `"5".zfill(2)` | `'05'` |
| `count(x)` | `"a,b,c".count(",")` | `2` |
| `find(x)` | `"abc".find("c")` | `2` (`-1` se assente) |

**f-string**: il modo per costruire testo con dentro dei valori.

```python
>>> nome, importo = "Anna", 1234.5
>>> f"{nome} ha speso {importo:.2f} euro"
'Anna ha speso 1234.50 euro'
```

`:.2f` = due decimali. Altri utili: `:,` separatore delle migliaia, `:>10` allinea a destra in
10 caratteri, `!r` mostra il valore "come lo scriveresti in Python" (utile per vedere gli spazi:
`f"{text!r}"` → `'  7,10  '`).

Virgolette: `"..."` e `'...'` sono equivalenti. `"""..."""` per testi su più righe e per le
docstring.

## Booleani e "verità"

`True` e `False` nascono dai confronti: `==`, `!=`, `<`, `<=`, `>`, `>=`, `in`, `is`. Si
combinano con `and`, `or`, `not`.

Ogni valore ha una verità implicita: sono falsi `0`, `0.0`, `""`, `None`, `[]`, `{}`, `set()`;
tutto il resto è vero. Da qui l'idioma:

```python
if not rows:        # la lista è vuota
    return {}
```

`==` confronta i valori, `is` l'identità. Usa `is` solo con `None`: `if x is None:`.

## `None`

Rappresenta "nessun valore". Una funzione senza `return` restituisce `None`: è la causa del bug
classico `xs = xs.sort()`, perché `sort` modifica sul posto e restituisce `None`.

## Prova tu

1. `"1.234,56".replace(".", "").replace(",", ".")` e poi `float(...)` del risultato. Poi inverti
   l'ordine dei due `replace`: cosa succede e perché?
2. `f"{3.14159:.1f}"`, `f"{1234567:,}"`, `f"{'x':>5}"`, `f"{'  ciao ':!r}"`... l'ultimo dà errore:
   la forma giusta è `f"{'  ciao '!r}"`. Leggi il messaggio d'errore, poi correggi.
3. `bool("")`, `bool("0")`, `bool(0)`, `bool([])`, `bool([0])`. Spiega a voce ogni risultato.
