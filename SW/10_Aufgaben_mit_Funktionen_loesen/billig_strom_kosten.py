# monatliche Kosten für Tarif Billig Strom berechnen 

# Datenanalyse 
# Input der Funktion ist der monatliche Verbrauch in kWh
# Output der Funktion sind die dadurch verursachten Kosten in EUR
# Grundpreis       9.20 EUR
# Verbrauchspreis  0.81 EUR/kWh

# Funktion mit Datentyp 
def billig_strom(verbrauch: float) -> float:
    kosten = 9.2 + verbrauch * 0.81
    return kosten

# Ergebnisse berechnen, Liste initialisieren 
verbrauch = range(0, 150, 10)
kosten1 = []

# Listen mit den Kosten des Tarifs erstellen
for x in verbrauch:
    kosten1.append(billig_strom(x))

# Ergebnisse drucken
print(" Verbrauch Kosten")
for i in range(len(verbrauch)):
    print(verbrauch[i], "\t", kosten1[i])    
