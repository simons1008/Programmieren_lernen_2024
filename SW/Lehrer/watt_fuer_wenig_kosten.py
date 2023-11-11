# monatliche Kosten für Tarif Watt für wenig berechnen (Schritt 1)

# Datenanalyse (Schritt  2)
# Input der Funktion ist der monatliche Verbrauch in kWh
# Output der Funktion sind die dadurch verursachten Kosten in EUR
# Grundpreis      13.50 EUR
# Verbrauchspreis  0.75 EUR/kWh

# Funktion mit Datentyp (Schritt 3 und Schritt 5)
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 13.5 + verbrauch * 0.75
    return kosten

# Ergebnisse berechnen, Liste initialisieren (Ab hier: Schritt 6)
verbrauch = range(0, 150, 10)
kosten1 = []

# Listen mit den Kosten des Tarifs erstellen
for x in verbrauch:
    kosten1.append(watt_fuer_wenig(x))

# Ergebnisse drucken
print("Verbrauch Kosten")
for i in range(len(verbrauch)):
    print(verbrauch[i], "\t", kosten1[i])    
