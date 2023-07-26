# Programm druckt die erkannten Zahlen als String und als Integer

# Import der zu testenden Funktionen
import mustererkennung

# Funktion aufrufen
antwort = mustererkennung.erkannte_zahlen(mustererkennung.muster, 5)
print(antwort)

# Antwort aufspalten
bestandteile = antwort.split()
print(bestandteile)

# Erkannte Zahlen als Integer drucken
i = 2
if bestandteile[i] != "keine":
    while i < len(bestandteile):
        print("zahl =", int(bestandteile[i]))
        i += 1

