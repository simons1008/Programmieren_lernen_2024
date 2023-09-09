# Summe ausgeben, bis Ende

# Schleife
while True:
    # Benutzereingaben anfordern
    zahl1 = input("zahl1 eingeben ")
    zahl2 = input("zahl2 eingeben ")

    # Strings in Dezimalzahlen umwandeln
    zahl1 = float(zahl1)
    zahl2 = float(zahl2)
    
    print("Die Summe der beiden Zahlen ist ", zahl1 + zahl2)
    antwort = input("Fertig? ")
    if antwort == "j" or antwort == "J":
        # Fertig!
        break

# Verabschiedung
print("OK - bis zum nächsten Mal!")
