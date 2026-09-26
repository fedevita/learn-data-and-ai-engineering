# 01 · Come scoprire cosa sa fare un oggetto

In Python tutto è un oggetto: una stringa, una lista, un file aperto, una funzione. Ogni oggetto
ha un tipo, e il tipo decide quali **metodi** (funzioni "attaccate" all'oggetto) puoi chiamare
con `oggetto.metodo(...)`. Non devi ricordarli a memoria: devi saperli trovare. Cinque strumenti.

## 1. Il REPL: prova prima di scrivere

```bash
uv run python
```

Si apre un prompt `>>>` dove ogni riga viene eseguita subito. È il posto dove provare un metodo
prima di usarlo nel codice. Si esce con `exit()`.

```python
>>> s = "  Ciao, Anna  "
>>> s.strip()
'Ciao, Anna'
>>> s.strip().lower().split(",")
['ciao', ' anna']
```

Nel REPL il risultato di un'espressione viene stampato da solo; in uno script serve `print()`.

## 2. `type`, `dir`, `help`

```python
>>> type(s)
<class 'str'>
>>> [m for m in dir(s) if not m.startswith("_")]
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', ...]
>>> help(s.split)
```

- `type(x)` dice che cos'è. Se un metodo "non esiste", nove volte su dieci è perché `x` non è del
  tipo che pensavi.
- `dir(x)` elenca attributi e metodi. Quelli che iniziano con `__` sono interni: ignorali.
- `help(x)` o `help(x.metodo)` mostra la documentazione. Frecce per scorrere, `q` per uscire.
  Funziona anche sui tipi: `help(str)`, `help(dict.get)`.

## 3. VS Code fa lo stesso lavoro senza uscire dall'editor

- Scrivi `s.` e aspetta (o `Ctrl+Spazio`): appare l'elenco dei metodi con la descrizione.
- Passa il mouse sopra un nome: tipo, firma e documentazione.
- `F12` su un nome ti porta alla definizione. Sulla libreria standard apre il file che descrive
  firme e tipi.
- Il debugger ([docs/vscode.md](../vscode.md)) mostra valore e tipo di ogni variabile mentre il
  programma è fermo su un breakpoint. È `type()` e `print()` senza sporcare il codice.

## 4. La documentazione ufficiale

- Tipi built-in (`str`, `list`, `dict`, `set`, `int`, `float`) con tutti i metodi:
  https://docs.python.org/it/3/library/stdtypes.html. Da tenere nei preferiti.
- Indice della libreria standard: https://docs.python.org/it/3/library/index.html

Come si legge una firma: `str.replace(old, new, count=-1)` significa due parametri obbligatori
(`old`, `new`) e uno opzionale (`count`) con il suo valore predefinito. Nelle pagine più vecchie
gli opzionali sono tra parentesi quadre: `str.split([sep])`.

## 5. Quando qualcosa esplode: leggere il traceback

```
Traceback (most recent call last):
  File "modules/01-python-basics/es01_parsing.py", line 20, in parse_amount
    return text.append("!")
AttributeError: 'str' object has no attribute 'append'
```

Leggilo dal basso. L'ultima riga è il **tipo** di errore e il **messaggio** ("una stringa non ha
`append`"). Le righe sopra dicono **dove**: file, riga, funzione, e la riga di codice. Se il
traceback è lungo, cerca l'ultima riga che riguarda un file tuo e non della libreria. I tipi di
errore più comuni sono nella [scheda 06](06-errori-ed-eccezioni.md).

## Prova tu

1. Nel REPL: `xs = [3, 1, 2]`, poi `dir(xs)`. Scegli tre metodi che non conosci, leggi
   `help(xs.<metodo>)` e provali.
2. `help(dict.get)`: a cosa serve il secondo parametro? Ti serve in es02.
3. In VS Code apri `playground/prove.py`, scrivi `s = "ciao"` e poi `s.` e guarda l'elenco.
   Passa il mouse su `strip`.
