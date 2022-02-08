# Potenzen berechnen: 2. Potenz und 3. Potenz des Eingabewerts

# Funktion mit Datentyp
def potenzen(zahl: float) -> list[float]:
    quadratzahl = zahl * zahl
    kubikzahl = quadratzahl * zahl
    return [quadratzahl, kubikzahl]
