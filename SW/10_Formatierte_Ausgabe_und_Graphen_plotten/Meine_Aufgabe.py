# Aufgabe der Funktion ...

# Input der Funktion ...
# Output der Funktion ...

# Funktion mit Datentyp
def meine_funktion(mein_input: datentyp) -> datentyp:
    mein_output = ...
    return mein_output

# Input und Output initialisieren
meine_input_liste = ...
meine_output_liste = []

# Output erstellen
for x in meine_input_liste: 
    meine_output_liste.append(meine_funktion(x))

# Ergebnisse drucken
print("Meine Überschrift") 
for i in range(len(meine_input_liste)):
    print("Mein Format String".format(meine_input_liste[i], meine_output_liste[i]))
