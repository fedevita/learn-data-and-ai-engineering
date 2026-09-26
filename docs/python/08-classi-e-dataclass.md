# 08 · Classi e dataclass

Fin qui una transazione è un dizionario: `row["amount"]`. Funziona, ma niente ti garantisce che
la chiave esista, che sia scritta giusta (`"amont"`?) o che il valore sia un float e non una
stringa. Una **classe** definisce una volta per tutte com'è fatto un oggetto; una **dataclass** è
una classe fatta apposta per contenere dati, e Python scrive per te il codice ripetitivo.

## Come lo scopro da solo

```python
>>> from dataclasses import dataclass, fields, asdict
>>> help(dataclass)                 # i parametri: frozen, order, ...
>>> t = Transaction(date="2025-01-02", description="Caffè", amount=-1.2)   # quella di es04
>>> t                               # la stampa leggibile la genera @dataclass
Transaction(date='2025-01-02', description='Caffè', amount=-1.2, category='Senza categoria')
>>> [f.name for f in fields(t)]     # i campi, con nome, tipo e default
>>> asdict(t)                       # torna un dizionario
>>> dir(t)                          # attributi e metodi, tuoi e generati
```

In VS Code, passa il mouse su `Transaction(` e vedi la firma del costruttore generato.
Riferimento: https://docs.python.org/it/3/library/dataclasses.html

## Una classe a mano, per capire cosa genera @dataclass

```python
class Point:
    def __init__(self, x: float, y: float):   # gira quando scrivi Point(3, 4)
        self.x = x                             # self è l'oggetto che si sta costruendo
        self.y = y

    def distance_from_origin(self) -> float:   # un metodo: funzione che riceve l'oggetto
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3, 4)
p.x                        # 3
p.distance_from_origin()   # 5.0
```

`self` è il primo parametro di ogni metodo: Python ci mette l'oggetto su cui hai chiamato il
metodo. `p.distance_from_origin()` è la stessa cosa di `Point.distance_from_origin(p)`.

## @dataclass

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    label: str = ""      # i campi con default vanno dopo quelli senza

p = Point(3, 4)          # __init__ generato: Point(x, y, label="")
q = Point(x=3, y=4)
p == q                   # True: __eq__ confronta campo per campo (classe a mano: False)
p                        # Point(x=3, y=4, label=''): __repr__ generato
```

I campi sono le righe `nome: tipo`. Il tipo non viene controllato a runtime (`Point("a", "b")`
passa), ma documenta e fa lavorare Pylance. Per un default mutabile (una lista) non scrivere
`items: list = []`: usa `field(default_factory=list)`, altrimenti la lista è condivisa tra tutti
gli oggetti.

## Validare: `__post_init__`

```python
@dataclass
class Point:
    x: float
    y: float

    def __post_init__(self) -> None:
        if self.x < 0 or self.y < 0:
            raise ValueError(f"coordinate negative: {self.x}, {self.y}")
```

Gira da solo alla fine dell'`__init__` generato. Se solleva, l'oggetto non viene creato: chi lo
riceve sa che è valido. È la stessa idea di `parse_amount`: controllare sulla soglia, una volta,
invece che ovunque.

## `frozen=True`: oggetti immutabili

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3, 4)
p.x = 5                  # dataclasses.FrozenInstanceError
```

Nessuna funzione può modificarti l'oggetto sotto i piedi (la lezione della review di es03), e gli
oggetti diventano usabili come chiavi di dizionario o elementi di un set. Per "modificarne" uno si
crea una copia: `dataclasses.replace(p, x=5)`.

## Metodi, `@property`, `@classmethod`

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float

    @property
    def norm(self) -> float:        # attributo calcolato: p.norm, senza parentesi
        return (self.x**2 + self.y**2) ** 0.5

    @classmethod
    def from_dict(cls, d: dict[str, float]) -> "Point":
        return cls(**d)             # cls è la classe stessa; ** spacchetta il dizionario

Point.from_dict({"x": 3, "y": 4}).norm    # 5.0
```

- `@property`: per valori derivati dai campi, che non vale la pena memorizzare.
- `@classmethod`: riceve la classe (`cls`) invece dell'oggetto. È il modo standard per i
  costruttori alternativi: `Point.from_dict(...)`, `date.fromisoformat(...)`, `Path.home()`.
- `Point(**d)` equivale a `Point(x=d["x"], y=d["y"])`: le chiavi del dizionario diventano nomi
  di argomento. Se manca una chiave o ce n'è una in più: `TypeError`.
- `"Point"` tra virgolette nell'annotazione perché a quella riga la classe non è ancora finita
  di definire.

## Dizionario o dataclass?

Dizionario quando le chiavi le decidono i dati (le colonne di un CSV qualsiasi, un JSON di cui
non conosci la forma). Dataclass quando le chiavi le decidi tu e sono sempre quelle: la riga
pulita di una pipeline, una configurazione, il risultato di una funzione con più valori. Più
avanti vedrai `pydantic`, una dataclass che controlla anche i tipi.

## Prova tu

1. Nel REPL definisci `Point` con `@dataclass`, crea `Point(1, 2)` e prova `==`, `print`,
   `asdict`. Poi rifallo con `frozen=True` e prova ad assegnare `p.x = 9`.
2. Aggiungi un `__post_init__` che rifiuta `x < 0`: `Point(-1, 2)` deve sollevare `ValueError`.
   Guarda il traceback: da quale riga parte?
3. `help(dataclasses.replace)`, poi usa `replace` per ottenere un `Point` con `x` diverso.
