# Kurzbeschreibung: Preise der Einkäufe addieren
# Die Summe in Euro umrechnen (1 GBP = 1,21 EUR)

# Datenanalyse: Die Preise werden als Liste von Dezimalzahlen angegeben.
# Die Summe in Euro wird als Dezimalzahl angegeben

# Funktion definieren: Name - Eingabewert - Rückgabewert
def einkauf_in_GB(einkauf: list[float]) -> float:
    # Rumpf
    summe = 0
    # Schleife über die Länge der Liste
    for i in range(len(einkauf)):
        summe += einkauf[i]
    # Summe umrechnen
    eur = summe * 1.21
    return eur

# Ergebnisse prüfen
print("Alle Käufe EUR:","{:5.2f}".format(einkauf_in_GB([9.0, 11.99, 12.99, 24.99])))

# Ohne Weste
print("Ohne Weste EUR:", "{:5.2f}".format(einkauf_in_GB([9.0, 11.99, 12.99])))
