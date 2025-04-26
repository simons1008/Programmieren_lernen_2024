# monatliche Kosten für Tarif Watt für wenig berechnen
# Funktion mit Datentyp
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 15.6 + verbrauch * 0.32
    return kosten
