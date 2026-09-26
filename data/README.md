# Dati

- `samples/` · piccoli file di esempio, versionati, usati dagli esercizi.
  - `transactions_simple.csv` · 20 transazioni pulite, importi in formato italiano
    (`"1.234,56"`) e date `gg/mm/aaaa`. Usato in M01.
  - `transactions_messy.csv` · 12 transazioni di cui 4 non valide (data impossibile, importo
    vuoto, data in formato ISO, importo non numerico), più spazi e una categoria mancante.
    Usato da es03 in poi.
- `raw/` · dati generati o scaricati dalle pipeline. Non versionato (vedi `.gitignore`).
