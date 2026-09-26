# M00 · Ambiente di lavoro

**Obiettivo:** avere un ambiente Python riproducibile e imparare il ciclo di lavoro che useremo
in tutti i moduli: test rosso → implemento → test verde → commit.
**Tempo:** 1 sessione.

## Gli strumenti

- **uv** gestisce la versione di Python, l'ambiente virtuale e le dipendenze con un solo comando.
  Il file `pyproject.toml` dichiara cosa serve, `uv.lock` blocca le versioni esatte così il
  progetto si comporta uguale su ogni macchina. È l'equivalente moderno di `pip` + `venv`.
- **pytest** esegue i test. Un test è una funzione che inizia con `test_` e usa `assert` per
  dire cosa si aspetta. Se l'`assert` fallisce, il test è rosso.
- **ruff** controlla lo stile e gli errori comuni (`ruff check`) e formatta il codice
  (`ruff format`). Nel mondo del lavoro il codice passa sempre da uno strumento così prima di
  entrare in un repository.

## Passi

1. Nella cartella del progetto lancia `uv sync`. Crea `.venv/` (ignorata da git) e `uv.lock`.
2. Lancia `uv run pytest`. Vedrai test rossi: è normale, sono gli esercizi da fare.
   `uv run` esegue un comando dentro l'ambiente del progetto, senza doverlo "attivare".
3. Lancia `uv run pytest modules/00-setup`. Leggi l'output: pytest ti dice quale test fallisce,
   in quale riga, e perché (`NotImplementedError`). Impara a leggere questo output, lo vedrai
   centinaia di volte.

## es00 · Il primo test verde

Apri `hello.py`. C'è una funzione `greet` che deve restituire il saluto `"Ciao, <nome>!"`.
Il test in `test_m00_hello.py` dice esattamente cosa si aspetta: leggilo prima di scrivere codice.

Quando il test è verde:

```bash
uv run ruff check .
uv run ruff format .
git add -A
git commit -m "m00/es00: primo test verde"
```

Poi apri Claude e scrivi `review m00/es00`.

## Per approfondire

- Tutorial ufficiale di Python in italiano: https://docs.python.org/it/3/tutorial/
- Documentazione di uv: https://docs.astral.sh/uv/
- Come è fatto un test pytest: https://docs.pytest.org/en/stable/getting-started.html
