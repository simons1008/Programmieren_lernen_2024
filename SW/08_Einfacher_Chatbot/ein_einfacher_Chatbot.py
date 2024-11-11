# Ein einfacher Chatbot (chatten mit dem Computer)

# Modul für den Zufall importieren
import random

# Eine Zufallsantwort ist eine der folgenden
zufallsantwort = ["Oh, wirklich",
                  "Interessant ...",
                  "Das kann man so sehen",
                  "Ich verstehe ..."]

# Eine Reaktionsantwort ist ein Wert aus einem Wörterbuch
reaktionsantwort = {"hallo": "aber Hallo",
                    "geht": "Was verstehst du darunter?",
                    "essen": "Ich habe leider keinen Geschmackssinn :("}

# Chatbot begrüßt den Benutzer
print("Willkommen beim Chatbot")
print("Worüber würden Sie gerne heute sprechen?")
print("Zum Beenden einfach 'bye' eintippen")
print("")

# Benutzereingabe initialisieren
benutzereingabe = ""

# Solange wiederholen, bis Benutzer bye eingibt
while benutzereingabe != "bye":
    # Benutzereingabe leeren
    benutzereingabe = ""
    # Solange wiederholen, bis Benutzer etwas eingibt
    while benutzereingabe == "":
        benutzereingabe = input("Ihre Frage/Antwort: ")

    # Benutzereingabe in Kleinbuchstaben umwandeln
    benutzereingabe = benutzereingabe.lower()
    # Liste von Benutzerwörtern erstellen
    benutzerwoerter = benutzereingabe.split()
    #print(benutzerwoerter)

    # reaktionsantwort_ausgegeben initialisieren
    reaktionsantwort_ausgegeben = False

    # Solange es ein Element in benutzerwoerter gibt: Durchlaufe die Schleife
    for element in benutzerwoerter:
        # Wenn das Element ein Schlüsselwort ist
        if element in reaktionsantwort:
            # Passende Reaktionsantwort ausgeben
            print(reaktionsantwort[element])
            # Merken, dass Reaktionsantwort ausgegeben wurde
            reaktionsantwort_ausgegeben = True

    # Wenn keine Reaktionsantwort ausgegeben wurde
    if reaktionsantwort_ausgegeben == False:
        # Zufallsantwort ausgeben
        print(random.choice(zufallsantwort))

# Chatbot verabschiedet den Benutzer
print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal") 
