# Potenzen berechnen: 2. Potenz und 3. Potenz des Eingabewerts

# 2. und 3. Potenz berechnen
# Funktion mit Datentyp
def potenzen(zahl: float) -> list[float]:
    quadratzahl = zahl * zahl
    kubikzahl = quadratzahl * zahl
    return [quadratzahl, kubikzahl]

# Ergebnisse drucken
print("Zahl  Quadratzahl  Kubikzahl")
for zahl in range(4):
    ergebnis = potenzen(zahl)
    print("{:4.2f} {:12.2f} {:10.2f}".format(zahl, ergebnis[0], ergebnis[1]))

    
