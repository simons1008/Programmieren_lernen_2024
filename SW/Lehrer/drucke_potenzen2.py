# Potenzen berechnen: 2. Potenz und 3. Potenz des Eingabewerts

# 2. Potenz berechnen
# Funktion mit Datentyp
def quadratzahl(zahl: float) -> float:
    quadratzahl = zahl * zahl
    return quadratzahl

# 3. Potenz berechnen
# Funktion  mit Datentyp
def kubikzahl(zahl: float) -> float:
    kubikzahl = zahl * zahl * zahl
    return kubikzahl

# Ergebnisse drucken
print("Zahl  Quadratzahl  Kubikzahl")
for zahl in range(4):
    print("{:4.2f} {:12.2f} {:10.2f}".format(zahl, quadratzahl(zahl), kubikzahl(zahl)))


    
