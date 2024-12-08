# monatliche Kosten für Tarif Billig Strom berechnen (Schritt 1)

# Datenanalyse (Schritt  2)
# Input der Funktion ist der monatliche Verbrauch in kWh
# Output der Funktion sind die dadurch verursachten Kosten in EUR
# Grundpreis       9.20 EUR
# Verbrauchspreis  0.81 EUR/kWh

# Funktion mit Datentyp (Schritt 3 und Schritt 5)
def billig_strom(verbrauch: float) -> float:
    kosten = 9.2 + verbrauch * 0.81
    return kosten

# Ergebnisse berechnen, Liste initialisieren (Ab hier: Schritt 6)
verbrauch = range(0, 150, 10)
kosten1 = []

# Listen mit den Kosten des Tarifs erstellen
for x in verbrauch:
    kosten1.append(billig_strom(x))

# Ergebnisse drucken
print(" Verbrauch Kosten")
for i in range(len(verbrauch)):
    print(verbrauch[i], "\t", kosten1[i])    
