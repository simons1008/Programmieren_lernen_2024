# Summe ausgeben, bis Ende

# Funktionen definieren
def summe(z1, z2):
    print("Die Summe der beiden Zahlen ist ", zahl1 + zahl2)

def produkt(z1, z2):
    print("Das Produkt der beiden Zahlen ist ", zahl1 * zahl2)

def quotient(z1, z2):
    print("Der Quotient der beiden Zahlen ist", zahl1/ zahl2)

def rechne(z1, z2, op):
    if op == "Summe":
        ergebnis = zahl1 + zahl2
    elif op == "Produkt":
        ergebnis = zahl1 * zahl2
    elif op == "Quotient":
        ergebnis = zahl1 / zahl2
    else:
        ergebnis = "unbekannte operation"
    print(op, "ist", ergebnis)

# Schleife
while True:
    # Benutzereingaben anfordern
    zahl1 = input("zahl1 eingeben ")
    zahl2 = input("zahl2 eingeben ")

    # Strings in Dezimalzahlen umwandeln
    zahl1 = float(zahl1)
    zahl2 = float(zahl2)

    # Funktionen aufrufen
    summe(zahl1, zahl2)
    produkt(zahl1, zahl2)
    quotient(zahl1, zahl2)
    rechne(zahl1, zahl2, "Summe")

    # Benutzer fragen
    antwort = input("Fertig? ")
    if antwort == "j" or antwort == "J":
        # Fertig!
        break
        
# Verabschiedung
print("OK - bis zum nächsten Mal!")
