"""Sandbox: scrivi qui quello che vuoi provare e lancialo con il bottone ▶ (o F5).

Non ha test e non fa parte dei moduli: è il tuo quaderno degli esperimenti.
Metti un breakpoint su una riga qualsiasi e avvia con F5 per vedere le variabili.
"""

s = "  Caffè al bar  "
print(type(s))
print([m for m in dir(s) if not m.startswith("_")])
print(s.strip().upper())

xs = [3, 1, 2]
xs.sort()
print(xs)

row = {"category": "Bar", "amount": "-1,20"}
print(row.get("note", "nessuna nota"))
