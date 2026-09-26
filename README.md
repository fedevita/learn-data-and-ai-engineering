# learn-data-and-ai-engineering

Percorso pratico, un passo alla volta, per diventare data & AI engineer partendo dalle basi.

## Come funziona

- **Un unico progetto filo rosso.** Costruiamo una piccola piattaforma dati per le finanze
  personali (transazioni bancarie sintetiche). Cresce modulo dopo modulo: prima Python e SQL,
  poi pipeline, orchestrazione e qualità dei dati, infine LLM, RAG e agenti sopra gli stessi dati.
- **Un modulo = una cartella** in `modules/NN-nome/`, con un `README.md` (teoria essenziale, il
  perché, i link) e uno o più esercizi. Ogni esercizio è un file con funzioni da completare e un
  file di test che all'inizio è rosso. Il tuo obiettivo è farlo diventare verde.
- **Il ciclo di lavoro:** leggi il README → lanci i test (rossi) → implementi → test verdi →
  `ruff` pulito → commit → chiedi la review a Claude (`review m01/es01`).
- **Niente soluzioni nel repo.** Se ti blocchi chiedi un indizio a Claude: prima un
  suggerimento, poi uno più esplicito, la soluzione solo se serve davvero.

## Comandi

```bash
uv sync                                  # crea l'ambiente e installa le dipendenze
uv run pytest                            # lancia tutti i test
uv run pytest modules/01-python-basics   # solo un modulo
uv run pytest -k es01                    # solo un esercizio
uv run ruff check .                      # controllo qualità del codice
uv run ruff format .                     # formattazione automatica
```

## Convenzioni

- Prosa (README, spiegazioni) in italiano. Codice (nomi di file, funzioni, variabili) in inglese,
  come nel mondo del lavoro.
- Un commit per esercizio, con messaggio tipo `m01/es02: leggo il CSV con DictReader`.
- Ogni esercizio è pensato per 30-60 minuti. Se ne serve di più, va bene: chiedi un indizio.

Il percorso completo e lo stato di avanzamento sono in [ROADMAP.md](ROADMAP.md).
