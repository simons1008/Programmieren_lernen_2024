# Programm soll den Benutzer nach seinem Namen fragen
# und eine Begrüßung ausgeben (Schritt 1)

# Input der Funktion ist ein Name
# Output der Funktion ist eine Begrüßung (Schritt 2)

# Funktion definieren (Schritt 3 und Schritt 5)
def begruessung(name: str) -> str:
    antwort = "Hallo " + name
    return antwort

# Ergebnis prüfen (Schritt 6)
name = input("Wie heißt du? ")
antwort = begruessung(name)
print(antwort)
