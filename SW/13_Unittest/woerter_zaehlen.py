# Das Programm soll die Wörter in einem Satz zählen

# Originalsätze
original1 = "Wie wird das Wetter?"
original2 = "Wie Programmieren geht, weiß ich."
original3 = "Heute gab es etwas Gutes zu essen!"

# Input der Funktion ist ein Satz
# Output der Funktion ist die Anzahl der Wörter im Satz
# Funktion mit Datentyp
def zaehle_woerter(original: str) -> str:
    liste = original.split()
    anzahl = len(liste)
    return anzahl

# Liste mit den Originalsätzen
originale = [original1, original2, original3]

# Ergebnisse prüfen
for x in originale:
    print(x)
    anzahl = zaehle_woerter(x)
    print(anzahl, "Wörter")
