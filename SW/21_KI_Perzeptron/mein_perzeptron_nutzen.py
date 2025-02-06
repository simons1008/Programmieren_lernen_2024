# Perzeptron nutzen
# - skalierungsfaktor einlesen
# - gelernte Gewichte einlesen
# - neues feature und neues label definieren
# - gelernte Gewichte auf das neue feature anwenden und Voraussage machen

# Bibliothek importieren
import numpy as np

# Perzeptron-Funktion
def perzeptron(w, x):
    if np.dot(w, x) > 0:
        return 1
    else:
        return 0

# Skalierungsfaktor aus Datei lesen
skalierungsfaktor = np.load("skalierungsfaktor.npy")
print("skalierungsfaktor")
print(skalierungsfaktor)

# gelernte Gewichte aus Datei lesen
w = np.load("gewichte.npy")
print("gelernte Gewichte")
print(w)

# neues feature angeben und skalieren
x_neu = [40.0, 20.0, 1]
x_neu /= skalierungsfaktor

# gelernte Gewichte auf das neue feature anwenden und Voraussage machen
print("normalisierte Testdaten")
print(x_neu)
if perzeptron(w, x_neu):
    print("Das ist ein Hund!")
else:
    print("Das ist kein Hund...")

# Ende
input("Voraussage gemacht. Weiter? ") 
