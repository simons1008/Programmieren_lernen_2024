# Vergleich Perzeptron (selbst erstellt) und Perzeptron mit SkLearn
# Quelle:  https://www.youtube.com/@STARTUPTEENS/playlists 
#          Programmiere mit Python - Baue deine eigene KI! #21

# Bibliothek importieren
from sklearn.linear_model import Perceptron
import numpy as np
import time

# eigenen Code importieren
from mein_perzeptron_als_klasse import Perzeptron

# Daten in numpy-Array speichern
# [groesse, laenge]
feature = np.array([[37.92655435, 23.90101111],
                    [35.88942857, 22.73639281],
                    [29.49674574, 21.42168559],
                    [32.48016326, 21.7340484 ],
                    [38.00676226, 24.37202837],
                    [30.73073988, 22.69832608],
                    [35.93672343, 21.07445241],
                    [38.65212459, 20.57099727],
                    [35.52041768, 21.74519457],
                    [37.69535497, 20.33073640],
                    [33.00699292, 22.57063861],
                    [33.73140934, 23.81730782],
                    [43.85053380, 20.05153803],
                    [32.95555986, 24.12153986],
                    [36.38192916, 19.20280266],
                    [36.54270168, 20.45388966],
                    [33.08246118, 22.20524015],
                    [31.76866280, 21.01201139],
                    [42.24260825, 20.44394610],
                    [29.04450264, 22.46633771],
                    [30.04284328, 21.54561621],
                    [18.95626707, 19.66737753],
                    [18.60176718, 17.74023009],
                    [12.85314993, 18.42746953],
                    [28.62450072, 17.94781944],
                    [21.00655655, 19.33438286],
                    [17.33580556, 18.81696459],
                    [31.17129195, 17.23625014],
                    [19.36176482, 20.67772798],
                    [27.26581705, 16.71312863],
                    [21.19107828, 19.00673617],
                    [19.08131597, 15.24401994],
                    [26.69761925, 17.05937466],
                    [4.44136559 , 3.52432493 ],
                    [10.26395607, 1.07729281 ],
                    [7.39058439 , 3.44234423 ],
                    [4.23565118 , 4.28840232 ],
                    [3.87875761 , 5.12407692 ],
                    [15.12959925, 6.26045879 ],
                    [5.93041263 , 1.70841905 ],
                    [4.25054779 , 5.01371294 ],
                    [2.15139117 , 4.16668657 ],
                    [2.38283228 , 3.83347914 ]])

# Array-Dimensionen ausgeben
print("Array-Dimensionen")
print(feature.shape)

# Einen Vektor mit Einsen anhängen
# Dadurch wird der Bias w[2] addiert
feature = np.concatenate((feature, np.ones(43).reshape(43,1)), axis=1)
print("Array-Dimensionen mit dem Vektor von Einsen")
print(feature.shape)

# Label speichern. Vereinfachung:
# - die ersten  21 sind features von Hunden
# - die letzten 22 sind features von Nicht-Hunden
labels = np.concatenate((np.ones(21), np.zeros(22)))

# Funktion nimmt einen Zeitstempel
def ticks_us():
    return int(time.perf_counter_ns()/1000.0)

# Funktion berechnet die Differenz zwischen zwei Zeitstempeln    
def ticks_diff(ticks1, ticks2):
    return ticks2 - ticks1

# Instanzen erstellen
sk_perzeptron = Perceptron()
perzeptron = Perzeptron(100)

# Lernschritt aufrufen, Zeit messen
ticks1 = ticks_us()
perzeptron.lernschritt(feature, labels)
ticks2 = ticks_us()
print("Dauer von perzeptron.lernschritt:", ticks_diff(ticks1, ticks2), "Mikrosekunden")
print("Gewichte")
print(perzeptron.w)
print("Anzahl der Epochen")
print(perzeptron.cnt)


# Fit aufrufen, Zeit messen
# Die feature wurden durch den Aufruf perzeptron.lernschritt normalisiert
ticks1 = ticks_us()
sk_perzeptron.fit(feature, labels)
ticks2 = ticks_us()
print("Dauer von sk_perzeptron.fit:", ticks_diff(ticks1, ticks2), "Mikrosekunden")
print("Weights assigned to the features")
print(sk_perzeptron.coef_)
print("The actual number of iterations to reach the stopping criterion")
print(sk_perzeptron.n_iter_)

# Weiter?
input("Weiter? ")

