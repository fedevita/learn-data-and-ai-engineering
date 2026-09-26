# 06 · Errori ed eccezioni

## Leggere un traceback

```
Traceback (most recent call last):
  File "modules/01-python-basics/es02_csv.py", line 24, in total_by_category
    totals[cat] = totals[cat] + amount
KeyError: 'Bar'
```

Dal basso: **cosa** (`KeyError: 'Bar'`, la chiave "Bar" non c'è ancora), poi **dove** (file,
riga, funzione, e la riga di codice). Nei traceback lunghi cerca l'ultima riga che riguarda un
file tuo.

## I tipi di errore che vedrai

| Errore | Significa | Causa tipica |
|---|---|---|
| `SyntaxError` | Python non riesce nemmeno a leggere il file | parentesi o virgolette non chiuse, `:` mancante |
| `IndentationError` | indentazione incoerente | mix di spazi, blocco non indentato |
| `NameError` | nome mai definito | typo, variabile usata prima di crearla, import mancante |
| `AttributeError` | l'oggetto non ha quel metodo | è di un tipo diverso da quello che pensi: `type(x)` |
| `TypeError` | operazione tra tipi incompatibili | `"1" + 1`, argomenti sbagliati a una funzione |
| `ValueError` | tipo giusto, valore inaccettabile | `float("abc")`, `strptime` con data inesistente |
| `KeyError` | chiave assente nel dizionario | nome colonna sbagliato, manca `.get` |
| `IndexError` | posizione fuori dalla lista | `xs[len(xs)]`, lista vuota |
| `FileNotFoundError` | percorso sbagliato | lanci il comando da una cartella diversa da quella che pensi |
| `UnicodeDecodeError` | encoding sbagliato | manca `encoding="utf-8"` |
| `ModuleNotFoundError` | modulo non trovato | pacchetto non installato (`uv add`), nome errato |
| `NotImplementedError` | funzione ancora da scrivere | è il tuo esercizio |

## Gestire: `try` / `except`

```python
try:
    amount = parse_amount(row["amount"])
except ValueError:
    logger.warning("importo non valido: %r", row["amount"])
    continue
```

- Cattura sempre un tipo specifico. `except:` nudo (o `except Exception:`) nasconde anche i bug
  veri.
- `except ValueError as e:` ti dà l'oggetto errore; `str(e)` è il messaggio.
- `else:` gira solo se non ci sono stati errori, `finally:` sempre. Con `with` per i file di
  solito non servono.

## Sollevare: `raise`

```python
if not text.strip():
    raise ValueError(f"importo mancante: {text!r}")
```

Solleva quando la funzione non può fare il suo lavoro. Sempre con un messaggio che dica **cosa**
e **con quale valore** (`!r` mostra la stringa tra virgolette, così vedi anche gli spazi).

## Chiedere perdono, non permesso

```python
# "permesso" (LBYL, look before you leap): controlli prima
if text.replace(",", "").replace("-", "").isdigit():
    ...

# "perdono" (EAFP, easier to ask forgiveness than permission): provi e gestisci l'errore
try:
    return float(text)
except ValueError:
    ...
```

In Python il secondo stile è idiomatico: più corto, e non duplica regole che `float` conosce già
meglio di te. È quello che hai fatto in es01 lasciando che fosse `float` a validare.

## Nei test

```python
with pytest.raises(ValueError):
    parse_amount("abc")
```

Il test è verde solo se dentro il blocco viene sollevato proprio `ValueError`.

## Prova tu

1. Nel REPL provoca di proposito un `NameError`, un `TypeError`, un `KeyError` e un
   `IndexError`. Leggi ogni messaggio.
2. Scrivi `def safe_float(text: str) -> float | None` che restituisce `None` invece di sollevare.
3. Chiama `parse_date("31/02/2024")` e leggi il messaggio che `strptime` ha scritto per te.
