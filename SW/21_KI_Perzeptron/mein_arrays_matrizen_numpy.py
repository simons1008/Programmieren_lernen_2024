# Supervised learning: Erkenne Hund - nicht Hund
# Daten zum Trainieren des Perzeptrons speichern
# Quelle:  https://www.youtube.com/@STARTUPTEENS/playlists 
#          Programmiere mit Python - Baue deine eigene KI! #10

# Bibliothek importieren
import numpy as np

# Daten in numpy-Array speichern
# [beine, groesse, breite]
feature = np.array([[4.0, 43.85053380, 20.05153803],
                    [4.0, 33.08246118, 22.20524015],
                    [4.0, 38.00676226, 24.37202837],
                    [2.0, 4.23565118 , 4.28840232 ],
                    [0.0, 4.25054779 , 5.01371294 ]])

# numpy-Array ausgeben
print("numpy-Array")
print(feature)

# Array-Dimensionen ausgeben
print("Dimensionen")
print(feature.shape)

# Größtes Element in jeder Spalte
print("\nGrößtes Element in jeder Spalte")
maximum = np.max(feature, 0)
print(maximum)

# Normalisierung der Daten
norm_feature = feature/ maximum
print("\nNormalisierung des numpy-Arrays")
print(norm_feature)

# Ende
input("Fertig? ")
