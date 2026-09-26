# M01 · Python per i dati

**Obiettivo:** le basi di Python che un data engineer usa ogni giorno, imparate sui dati del
nostro progetto: transazioni bancarie in formato italiano.
**Tempo:** 6-8 sessioni, un esercizio per sessione.

## Prima di iniziare

Le basi del linguaggio sono nelle schede in [docs/python](../../docs/python/README.md): brevi,
in italiano, con esempi da provare nel REPL o in `playground/prove.py`.

- Prima di es02: schede 01 (come esplorare un oggetto), 02 (tipi base), 03 (liste),
  04 (dizionari).
- Prima di es03: schede 06 (errori) e 07 (moduli e file).
- Prima di es04: scheda 08 (classi e dataclass).
- Scheda 05 (funzioni) quando vuoi capire meglio quello che stai già scrivendo.

Il tutorial ufficiale in italiano (https://docs.python.org/it/3/tutorial/) resta il riferimento
completo se una scheda non basta.

## Come lavorare

```bash
uv run pytest modules/01-python-basics -k es01   # test di un esercizio
uv run ruff check .                              # prima del commit
uv run ruff format .
```

Per il commit vale la stessa sequenza del modulo 00 (in PowerShell 5.1 senza `&&`, vedi il
README principale).

Ogni esercizio ha un file `esNN_nome.py` con le funzioni da completare (sono lì, sollevano
`NotImplementedError`) e un file `test_m01_esNN_nome.py` che descrive il comportamento atteso.
**Leggi sempre il test prima di scrivere codice:** è la specifica.

---

## es01 · Parsing di importi e date italiane (30-45 min)

I dati "veri" arrivano quasi sempre come testo, e quasi sempre nel formato sbagliato. Un
estratto conto italiano scrive gli importi come `"1.234,56"` e le date come `31/12/2024`.
Python, e qualsiasi database, vogliono `1234.56` e `2024-12-31`. Convertire è il primo lavoro di
ogni pipeline.

Da completare in `es01_parsing.py`:

- `parse_amount(text: str) -> float` · `"1.234,56"` → `1234.56`, `"-12,50"` → `-12.5`.
  Se il testo non è un importo valido, solleva `ValueError`.
- `parse_date(text: str) -> str` · `"31/12/2024"` → `"2024-12-31"`. Se il formato è sbagliato
  o la data non esiste (31 febbraio), solleva `ValueError`.

Concetti che servono:

- **Metodi delle stringhe:** `.strip()` toglie gli spazi ai bordi, `.replace(vecchio, nuovo)`
  sostituisce. Le stringhe sono immutabili: i metodi restituiscono una stringa nuova.
- **Conversione:** `float("1234.56")` funziona, `float("1234,56")` solleva `ValueError` da
  sola. Spesso la mossa migliore è preparare la stringa e lasciare che sia `float` a lamentarsi.
- **Type hints:** `def parse_amount(text: str) -> float` documenta cosa entra e cosa esce. Python
  non li controlla a runtime, ma le persone e gli strumenti sì. Li useremo sempre.
- **Eccezioni:** `raise ValueError("messaggio")` interrompe la funzione segnalando un errore.
  Chi chiama può gestirlo con `try/except`. Nei test, `pytest.raises(ValueError)` verifica che
  venga sollevata davvero.
- **Date:** `datetime.strptime(text, "%d/%m/%Y")` (dal modulo `datetime`) converte testo in
  data seguendo un formato, e solleva `ValueError` se la data non esiste. Poi
  `.strftime("%Y-%m-%d")` o `.date().isoformat()` la riscrive nel formato ISO. Riferimento
  ai codici di formato: https://docs.python.org/it/3/library/datetime.html#strftime-and-strptime-format-codes

Domanda su cui riflettere (ne parliamo in review): perché scegliamo `2024-12-31` e non
`31/12/2024` come formato "interno"? Suggerimento: prova a ordinare alfabeticamente
`["31/12/2024", "01/01/2025"]`.

## es02 · Leggere un CSV e sommare per categoria (45-60 min)

Il file `data/samples/transactions_simple.csv` contiene 20 transazioni con colonne `date`,
`description`, `amount`, `category`. Aprilo con un editor di testo e guarda come è fatto: gli
importi sono tra virgolette perché contengono una virgola, che è anche il separatore del CSV.
Questo è il motivo per cui non si fa mai `riga.split(",")` a mano: si usa il modulo `csv`.

Da completare in `es02_csv.py`:

- `read_transactions(path) -> list[dict[str, str]]` · legge il file e restituisce una lista con
  un dizionario per riga, chiavi = intestazioni, valori ancora stringhe (nessuna conversione).
- `total_by_category(transactions) -> dict[str, float]` · somma gli importi per categoria.
  Riusa `parse_amount` di es01: `from es01_parsing import parse_amount`.

Concetti che servono:

- **Aprire file:** `with open(path, encoding="utf-8", newline="") as f:`. Il `with` chiude il
  file da solo anche se qualcosa va storto. `encoding="utf-8"` è obbligatorio su Windows,
  altrimenti "Caffè" diventa spazzatura. `newline=""` è richiesto dal modulo `csv`.
- **`csv.DictReader(f)`:** itera sulle righe restituendo un dizionario per riga, usando la
  prima riga come chiavi. Gestisce da solo virgolette e separatori.
- **Costruire una lista:** `rows = []` poi `rows.append(...)` dentro un `for`, oppure
  direttamente `list(reader)`.
- **Accumulare in un dizionario:** `totals[cat] = totals.get(cat, 0.0) + amount`. Il `.get`
  con default evita il `KeyError` la prima volta che incontri una categoria.
- **`Path`:** il test passa il percorso come `pathlib.Path`; `open` lo accetta direttamente.

Per provare a mano, aggiungi in fondo al file una zona prove (gira solo se lanci il file con ▶,
non nei test):

```python
if __name__ == "__main__":
    rows = read_transactions("data/samples/transactions_simple.csv")
    for category, total in total_by_category(rows).items():
        print(f"{category:<12} {total:>10.2f}")
```

Attenzione ai float: `0.1 + 0.2` non fa esattamente `0.3`. Per questo i test confrontano con
`pytest.approx`. In M04 vedremo perché i database usano `DECIMAL` per i soldi.

## es03 · Righe malformate: errori e logging (45-60 min)

Il file `data/samples/transactions_messy.csv` è come arrivano i dati veri. Aprilo e trova a occhio
i problemi prima di scrivere codice: date impossibili, importi vuoti o non numerici, una data nel
formato sbagliato, spazi, una categoria mancante. Una pipeline non deve esplodere alla prima riga
sbagliata, ma neanche ignorarla in silenzio: la salta e lo dice.

Da completare in `es03_cleaning.py`:

- `clean_transaction(row)` · converte una riga (data ISO, importo float, spazi via, categoria
  vuota → `UNCATEGORIZED`). Se non può, solleva `ValueError`. Non gestisce l'errore: lo segnala.
- `clean_transactions(rows)` · scorre le righe, chiama la prima dentro un `try/except`, salta le
  righe non valide con un `logger.warning(...)` e restituisce solo quelle valide.

Perché due funzioni: chi converte non sa cosa vorrebbe fare chi la chiama con una riga sbagliata
(saltarla, fermarsi, metterla da parte). Sollevare l'eccezione lascia la decisione a chi orchestra.
È lo schema di ogni pipeline: funzioni "pure" che sollevano, e un livello sopra che decide.

Concetti che servono (schede 06 e 07):

- **`try/except` nel ciclo:** cattura solo `ValueError`, con `as e` per avere il motivo. Cosa
  succederebbe catturando `Exception`? Prova: scrivi `row["amont"]` per sbaglio e guarda come
  falliscono i test. È il motivo per cui non si cattura mai tutto.
- **`enumerate(rows, start=2)`** per avere il numero di riga come lo vede l'editor (la riga 1 è
  l'intestazione). Chi legge il log deve poter aprire il file e andare dritto alla riga.
- **Logging:** `logger = logging.getLogger(__name__)` in cima al file, poi
  `logger.warning("riga %d scartata: %s", line_no, e)`. Il logging formatta con `%d`/`%s` solo se
  il messaggio viene davvero emesso; una f-string funziona lo stesso, ma questa è la convenzione.
  Livelli: `debug` < `info` < `warning` < `error`. Senza configurazione i warning finiscono
  comunque sullo schermo; `logging.basicConfig(...)` nella zona prove decide formato e livello.
  Riferimento: https://docs.python.org/it/3/howto/logging.html
- **Nei test, la fixture `caplog`** di pytest cattura i messaggi di log: leggi come il test li
  controlla (`caplog.records`, `getMessage()`).
- **Il tipo `dict[str, str | float]`** è scomodo: `row["amount"]` è float o stringa? Dipende da
  quale funzione l'ha prodotta. È il problema che risolve la dataclass di es04.

## es04 · Una `Transaction` tipizzata: dataclass e validazione (45-60 min)

Finora una transazione è un dizionario, e ogni funzione deve fidarsi che dentro ci siano le
chiavi giuste con i tipi giusti: `row["amount"]` è una stringa o un float? Dipende da chi l'ha
prodotto. Una **dataclass** è un dizionario con le chiavi decise una volta per tutte, tipizzate e
validate alla creazione: da qui in poi il resto del codice riceve `Transaction`, non "un dict e
speriamo bene". È lo schema dei dati, scritto in Python.

Da completare in `es04_transaction.py`:

- I quattro **campi** di `Transaction`: `date`, `description`, `amount`, `category` (con default
  `UNCATEGORIZED`). Sono righe della classe, con il tipo: guarda la scheda 08.
- `__post_init__` · valida: `description` e `category` non possono essere vuote o di soli spazi,
  altrimenti `ValueError`.
- `month` · una `@property`: `"2025-01-02"` → `"2025-01"`. Servirà per il report mensile di es05.
- `Transaction.from_row(row)` · un `@classmethod` che costruisce una `Transaction` da una riga
  grezza del CSV, riusando `clean_transaction` di es03.
- `load_transactions(path)` · legge il CSV (es02), costruisce le `Transaction` e salta le righe
  non valide con un warning, come in es03.

Concetti che servono (scheda 08):

- **`@dataclass`** genera per te `__init__`, `__repr__` (la stampa leggibile) e `__eq__` (il
  confronto campo per campo) a partire dai campi dichiarati. `frozen=True` rende l'oggetto
  immutabile: modificare un campo solleva `FrozenInstanceError`. Ti ricorda la review di es03?
- **`__post_init__`** gira da solo alla fine della costruzione: è il posto per i controlli.
- **`@property`** trasforma un metodo in un attributo calcolato: `t.month`, senza parentesi.
- **`@classmethod`** riceve la classe (`cls`) invece dell'oggetto: è il modo standard per avere
  costruttori alternativi (`Transaction.from_row(...)`). Dentro, `cls(...)` crea l'oggetto.
- **Spacchettare con `**`:** `Transaction(**d)` equivale a
  `Transaction(date=d["date"], description=d["description"], ...)`. Guarda come lo usano i test.

Domanda su cui riflettere (ne parliamo in review): `date` è ancora una stringa. Cosa
guadagneresti con `datetime.date`? Prova nel REPL: `from datetime import date`,
`d = date.fromisoformat("2025-01-02")`, poi `d.month`, `d.weekday()`, `d < date(2025, 2, 1)`.

## In arrivo

- es05 · Scrivere output: report mensile in JSON e CSV, CLI con argparse
- es06 · Mini progetto: due estratti conto in formati diversi → uno schema comune
