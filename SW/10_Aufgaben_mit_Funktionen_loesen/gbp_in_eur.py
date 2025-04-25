# Das Programm soll britische Pfund in Euro umrechnen und eine Tabelle ausgeben

# Input der Funktion ist eine Dezimalzahl in der Einheit britische Pfund
# Output der Funktion ist eine Dezimalzahl in der Einheit Euro
# Umrechnungsfaktor 1 gbp = 1.21 eur

# Funktion mit Datentyp
def gbp_in_eur(gbp: float) -> float:
    eur = 1.21 * gbp
    return eur

# Input und Output initialisieren
gbp_liste = []
for i in range(21):
    gbp_liste.append(i * 0.5)
eur_liste = []

# Output erstellen
for x in gbp_liste: 
    eur_liste.append(gbp_in_eur(x))

# Ergebnisse drucken
print("gbp    eur")
for x, y in zip(gbp_liste, eur_liste):
    print("{:5.2f} {:5.2f}".format(x, y))
