# Kosten für Volumentarif berechen
# Die Kosten werden durch das Datenvolumen im Monat bestimmt

# Funktion mit Datentyp
def volumentarif(verbrauch: list[float]) -> float:
    kosten = 0
    for i in range(len(verbrauch)):
        kosten += verbrauch[i] * 6.5
    return kosten
