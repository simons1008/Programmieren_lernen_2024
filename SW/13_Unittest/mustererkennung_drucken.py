# Programm druckt die erkannten Zahlen als String und als Integer

# Import der zu testenden Funktionen
import mustererkennung as mu_er

# Funktion aufrufen
antwort = mu_er.erkannte_zahlen(mu_er.muster, 5)
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

