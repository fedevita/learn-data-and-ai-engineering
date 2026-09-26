# VS Code: lanciare, testare, debuggare

Tutto è già configurato nella cartella `.vscode/` del progetto. Questa guida spiega cosa c'è e
come usarlo. In fondo trovi un esercizio da 10 minuti per provare il debugger.

## Estensioni

VS Code è volutamente minimale: un solo profilo e sette estensioni. Python, Pylance, Python
Debugger, Ruff, Rainbow CSV (colora le colonne dei file CSV), Material Icon Theme e Claude Code.
Quando un modulo futuro avrà bisogno di altro (Jupyter, Docker, YAML...), lo dirà il suo README.

## Prima volta

1. Apri la cartella del progetto (`code .`). Se VS Code propone di installare le estensioni
   consigliate (Python, Python Debugger, Pylance, Ruff, Rainbow CSV), accetta.
2. In basso a destra deve comparire l'interprete del progetto, tipo `3.12.6 ('.venv': venv)`.
   Se non c'è: `Ctrl+Shift+P` → "Python: Select Interpreter" → scegli `.venv\Scripts\python.exe`.
3. Da ora, salvando un file `.py`, Ruff lo formatta da solo. Non serve più `ruff format` a mano.
   I problemi segnalati da `ruff check` invece li vedi sottolineati e nel pannello "Problems":
   correggerli è compito tuo, così impari a riconoscerli.

## Test: l'icona a forma di provetta (Test Explorer)

Nella barra a sinistra c'è l'icona "Testing" (una provetta). Mostra i test del progetto ad
albero: cartella → file → test → casi parametrizzati.

- ▶ accanto a un test, a un file o a una cartella lo esegue. Verde o rosso in tempo reale, e nel
  codice compare un'icona accanto a ogni funzione di test, cliccabile.
- Un test rosso mostra l'errore inline e il confronto atteso/ottenuto.
- 🐛 (Debug Test) esegue il test nel debugger: se hai messo un breakpoint dentro la funzione
  che il test chiama, il programma si ferma lì. È il modo più utile per capire "cosa arriva
  davvero" alla tua funzione.

Se l'elenco è vuoto: pulsante "Refresh" in alto, oppure `Ctrl+Shift+P` → "Test: Refresh Tests".

## Eseguire un file

Con un `.py` aperto, in alto a destra c'è il bottone ▶ "Run Python File" (la freccia accanto
apre "Debug Python File"). Esegue il file nel terminale integrato.

Un file esercizio contiene solo funzioni: eseguirlo non stampa niente. Puoi aggiungergli in
fondo una "zona prove", che gira solo quando lanci il file e non quando i test lo importano:

```python
if __name__ == "__main__":
    print(parse_amount("1.234,56"))
```

Per esperimenti sciolti c'è `playground/prove.py`: scrivi, lancia, cancella, ricomincia.

## Debugger: fermare il programma e guardarci dentro

1. Clicca a sinistra del numero di riga (o `F9`): appare un punto rosso, il breakpoint.
2. Avvia: `F5` esegue la configurazione selezionata nel pannello "Run and Debug"
   (`Ctrl+Shift+D`), oppure 🐛 su un test nel Test Explorer.
3. Il programma si ferma sulla riga, prima di eseguirla. A sinistra il pannello **Variables**
   mostra ogni variabile con valore e tipo. Passa il mouse su un nome nel codice per vederne
   il valore.
4. Barra dei comandi: `F10` esegue la riga e passa alla successiva (step over), `F11` entra
   nella funzione chiamata (step into), `Shift+F11` esce dalla funzione, `F5` continua fino al
   prossimo breakpoint, `Shift+F5` ferma tutto.
5. **Debug Console** (pannello in basso): mentre è fermo puoi scrivere espressioni, per esempio
   `text.strip()`, `type(row)`, `dir(row)`. È il REPL con le variabili di quel momento.

Le configurazioni sono in `.vscode/launch.json`: "Python: file corrente", "Pytest: file
corrente", "Pytest: tutto", più quella usata dal Test Explorer.

## Task: i bottoni per i comandi

Menu Terminal → "Run Task…" (o `Ctrl+Shift+P` → "Tasks: Run Task"): `test: tutto`,
`test: file corrente`, `python: file corrente`, `ruff: check + format`. `Ctrl+Shift+B` lancia
direttamente `ruff: check + format`. Sono definiti in `.vscode/tasks.json`.

## Scorciatoie che vale la pena imparare

| Tasti | Cosa fa |
|---|---|
| `Ctrl+Shift+P` | qualsiasi comando, cercandolo per nome |
| `Ctrl+P` | apri un file per nome |
| `Ctrl+J` | mostra/nascondi il pannello in basso (terminale, problemi, debug console) |
| `F12` / `Alt+←` | vai alla definizione / torna indietro |
| `Ctrl+Spazio` | suggerimenti (metodi, nomi) |
| `F2` | rinomina un nome ovunque è usato |
| `Ctrl+7` | commenta / decommenta la riga (tastiera italiana: è la tua scorciatoia personalizzata) |
| `Shift+Alt+F` | formatta il file (Ruff) |

## es00-bis · Prova il debugger (10 min)

1. Metti un breakpoint sulla prima riga di codice dentro `parse_amount`
   in `modules/01-python-basics/es01_parsing.py`.
2. Nel Test Explorer clicca 🐛 su `test_parse_amount_converts_italian_format`. Il programma
   si ferma: guarda `text` nel pannello Variables. `F5` per passare al caso successivo (il test è
   parametrizzato, si fermerà sei volte).
3. Nella Debug Console scrivi `text.strip().replace(".", "")` e leggi il risultato.
4. Togli il breakpoint (click sul punto rosso) e ferma con `Shift+F5`.
