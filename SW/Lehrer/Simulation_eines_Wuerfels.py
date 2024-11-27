# Simulation eines Würfels

# Bibliothek importieren
import random

# Ergebnismenge definieren
ergebnismenge = ["1", "2", "3", "4", "5", "6"]

# Ergebniszähler
anzahl = 0

# Würfeln
for i in range(6000):
    ergebnis = random.choice(ergebnismenge)
    # print(ergebnis)
    if ergebnis == "3":
        anzahl += 1

# Anzahl der Ergebnisses ausgeben
print("Anzahl =", anzahl)
