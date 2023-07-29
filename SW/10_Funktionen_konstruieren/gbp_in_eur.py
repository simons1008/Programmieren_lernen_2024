# Kurzbeschreibung: Britische Pfund in Euro umrechnen (1 GBP = 1,21 EUR)

# Datenanalyse: GBP und EUR werden als Dezimalzahlen angegeben

# Funktion definieren: Name - Eingabewert - Rückgabewert
def GBP_in_EUR(gbp: float) -> float:
    # Rumpf
    eur = gbp * 1.21
    return eur

# Ergebnisse prüfen
# Überschrift der Tabelle drucken
print(" GBP   EUR")

# Schleife über GBP
gbp = 0.0
while gbp <= 10.0:
#    print(gbp, GBP_in_EUR(gbp))
    print("{:5.2f} {:5.2f}".format(gbp, GBP_in_EUR(gbp)))
    gbp += 0.5
