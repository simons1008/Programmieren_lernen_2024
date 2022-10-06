# monatliche Kosten für Tarif Billig-Strom berechnen
# Funktion mit Datentyp
def billig_strom(verbrauch: float) -> float:
    kosten = 9.2 + verbrauch * 0.81
    return kosten
