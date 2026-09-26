# Roadmap

Ritmo previsto: meno di 3 ore a settimana, quindi 2-3 sessioni da 45-60 minuti.
Le stime sono indicative: l'obiettivo è capire, non correre.

Legenda: `[ ]` da fare · `[~]` in corso · `[x]` fatto

## Fase 1 — Fondamenta (circa 3 mesi)

### M00 · Ambiente di lavoro (1 sessione)
- [x] es00 · uv, pytest, ruff e il primo commit (2026-09-26)

### M01 · Python per i dati (6-8 sessioni)
- [x] es01 · Stringhe, funzioni, eccezioni: parsing di importi e date italiane (2026-09-26)
- [ ] es02 · Liste e dizionari: leggere un CSV e sommare per categoria
- [ ] es03 · Gestione errori e logging: righe malformate
- [ ] es04 · Dataclass: una `Transaction` con validazione
- [ ] es05 · Scrivere output: report mensile in JSON e CSV, CLI con argparse
- [ ] es06 · Mini progetto: due estratti conto in formati diversi → uno schema comune

### M02 · SQL con DuckDB (6-8 sessioni)
- [ ] SELECT, WHERE, ORDER BY sulle transazioni
- [ ] GROUP BY e funzioni di aggregazione
- [ ] JOIN tra transazioni, conti e categorie
- [ ] Window functions: saldo progressivo, confronto mese su mese
- [ ] Viste e CTE
- [ ] Mini progetto: il report mensile di M01 riscritto in SQL

## Fase 2 — Pipeline (circa 3-4 mesi)

### M03 · La prima pipeline ETL (5 sessioni)
- [ ] Estrarre da CSV e da un'API pubblica (tassi di cambio)
- [ ] Trasformare con Polars, salvare in Parquet
- [ ] Idempotenza e riesecuzioni sicure

### M03-bis · Assaggio di AI (2 sessioni)
- [ ] Un modello locale (Ollama) categorizza le transazioni senza categoria

### M04 · Postgres in Docker e modellazione (6 sessioni)
- [ ] docker compose, tabelle, chiavi, indici
- [ ] Star schema: fatti e dimensioni
- [ ] Carichi incrementali

### M05 · Orchestrazione (5 sessioni)
- [ ] Scheduling, retry, backfill con un orchestratore (Dagster o Airflow)

### M06 · Qualità dei dati (4 sessioni)
- [ ] Test sui dati, contratti, riconciliazione dei saldi

## Fase 3 — AI engineering (circa 3 mesi)

### M07 · LLM API (5 sessioni)
- [ ] Prompt, structured output, token e costi (Claude API e Ollama)

### M08 · Embeddings e RAG (5 sessioni)
- [ ] Ricerca semantica con pgvector sui dati del progetto

### M09 · Agenti (6 sessioni)
- [ ] Tool use, text-to-SQL sul warehouse, un MCP server, valutazioni

## Fase 4 — Avanzato (opzionale)
- [ ] Streaming con Redpanda (Kafka)
- [ ] Lakehouse con MinIO e Iceberg
- [ ] Serving con FastAPI e monitoring
