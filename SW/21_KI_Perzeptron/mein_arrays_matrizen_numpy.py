# Supervised learning: Erkenne Hund - nicht Hund
# Daten zum Trainieren des Perzeptrons speichern
# Quelle:  https://www.youtube.com/@STARTUPTEENS/playlists 
#          Programmiere mit Python - Baue deine eigene KI! #10


# Bibliothek importieren
import numpy as np

# Dictionary mit Listen
data = {
'beine': [4, 4, 4, 4, 4],
'groesse': [35.4, 28.6, 32.7, 23.9, 45.6],
'breite': [21.9, 18.7, 16.4, 15.8, 25.6],
}

# Einen Dictionary-Eintrag ausgeben
print("Ein Dictionary-Eintrag")
print(data['groesse'])

# Daten in numpy-Array speichern
# Features als Zeilen gespeichert
feature = np.array([data['beine'], data['groesse'], data['breite']])

# numpy-Array ausgeben
print("numpy-Array")
print(feature)

# Array-Dimensionen ausgeben
print("Dimensionen")
print(feature.shape)

# Ende
input("Fertig? ")
