# Funktionen Input und Output

# Funktion baut die Antwort
def gib_antwort(name):
    antwort = "Hallo " + name
    return antwort

# Input von der Tastatur
mein_name = input("Wie heißt du? ")

# Aufruf der Funktion
meine_antwort = gib_antwort(mein_name)

# Output zum Bildschirm
print(meine_antwort)
