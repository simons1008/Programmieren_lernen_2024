# Eine unendliche Schleife abbrechen

# Variable initialisieren
durchgang = 0

# Unendliche Schleife 
while True:
    # Variable ausgeben
    print("durchgang =", durchgang)
    # Variable inkrementieren
    durchgang += 1
    # Benutzereingabe anfordern
    benutzereingabe = input("Bitte Zahl eingeben: ")
    # Abbruch bei einer bestimmten Benutzereingabe
    if benutzereingabe == "ende":
        break

# Diese Anweisung gehört nicht mehr zur Schleife
print("Nach der Schleife")
