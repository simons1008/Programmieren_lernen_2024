# monatliche Kosten für Tarif Billig-Strom berechnen
# Funktion mit Datentyp
def billig_strom(verbrauch: float) -> float:
    kosten = 4.9 + verbrauch * 0.19
    return kosten
