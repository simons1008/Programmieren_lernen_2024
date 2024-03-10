# Supervised learning: Erkenne Hund - nicht Hund
# - Perzeptron-Funktion definieren
# - Perzeptron-Lernregel anwenden
# - gelernte Gewichte ausgeben
# - neues feature und neues label definieren
# - gelernte Gewichte auf das neue feature anwenden und Voraussage machen
# Quelle:  https://www.youtube.com/@STARTUPTEENS/playlists 
#          Programmiere mit Python - Baue deine eigene KI! #19

# Bibliothek importieren
import numpy as np
import matplotlib.pyplot as plt

# Daten in numpy-Array speichern
# [groesse, breite]
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

# feature in eine zufällige Reihenfolge bringen
# erstelle einen neuen Zufallsgenerator mit seed, 
# damit die 'zufällige' Reihenfolge immer gleich ist
rng = np.random.default_rng(12345)
rng.shuffle(feature)

# Array-Dimensionen ausgeben
print("Array-Dimensionen")
print(feature.shape)

# Einen Vektor mit Einsen anhängen
# Dadurch wird der Bias w[2] addiert
feature = np.concatenate((feature, np.ones(43).reshape(43,1)), axis=1)
print("Array-Dimensionen mit dem Vektor von Einsen")
print(feature.shape)

# feature skalieren
maximum = np.max(feature, 0)
print("Maximalwert in jeder Spalte")
print(maximum)
skalierungsfaktor = np.max(feature, 0)
feature /= skalierungsfaktor
print(feature)

# Label speichern. Vereinfachung:
# - die ersten  21 sind features von Hunden
# - die letzten 22 sind features von Nicht-Hunden
labels = np.concatenate((np.ones(21), np.zeros(22)))

# labels in die DIESELBE zufällige Reihenfolge WIE feature bringen
# erstelle einen neuen Zufallsgenerator mit seed, 
# damit die 'zufällige' Reihenfolge immer gleich ist
rng = np.random.default_rng(12345)
rng.shuffle(labels)

# Funktion visualisiert
# Diese Funktion ist eine Vereinfachung des Originals
def visualize(feature, labels, w): 
    plt.title('Trainingsdaten')
    plt.xlabel("Größe auf "  + "{:4.2f}".format(skalierungsfaktor[0]) + " cm normiert")
    plt.ylabel("Breite auf " + "{:4.2f}".format(skalierungsfaktor[1]) + " cm normiert")
    plt.scatter(feature[:,0], feature[:,1], c=labels)

    # Linie erstellen
    # x0 vorgeben
    x0 = np.array([0.5, 1])
    # x1 mit Hilfe der gelernten Gewichte berechnen
    # Division durch Null ist verboten
    if w[1] != 0: 
        x1 = -(w[0] * x0 + w[2]) / w[1]
        plt.plot(x0, x1)
    plt.show()
    
# zufällige Gewichte erstellen
# w[0], w[1], [w[2]
np.random.seed(5) # damit die 'zufälligen' Zahlen immer gleich sind
w = np.random.rand(feature.shape[1])
print("zufällige Gewichte")
print(w)

# Perzeptron-Funktion
def perzeptron(w, x):
    if np.dot(w, x) > 0:
        return 1
    else:
        return 0

# Perzeptron Lernregel
# +/- groesse zu w[0]
# +/- breite  zu w[1]
# +/- 1       zum Bias w[2]
cnt = 0
max_epochs = 100
fehler = np.zeros(max_epochs)
while cnt < max_epochs:
    for index in range(len(feature)):
        x = feature[index]
        label = labels[index]
        delta = label - perzeptron(w, x)
        if delta != 0: # falsch klassifiziert
            fehler[cnt] += 1
            w += delta * x
    # wenn trainiert
    if fehler[cnt] == 0:
        # Visualisieren        
        visualize(feature, labels, w)
        break
    cnt += 1
else:
    print("Es wurde keine Lösung gefunden.")

# Fehler in den Epochen zeigen
plt.plot(range(max_epochs), fehler)
plt.xlabel('Epochen')
plt.ylabel('Falsche Klassifikationen')
plt.show()

# gelernte Gewichte ausgeben
print("gelernte Gewichte")
print(w)

# neues feature angeben und skalieren
x_neu = [40.0, 20.0, 1]
x_neu /= skalierungsfaktor

# neues feature an die Trainingsdaten anhängen 
feature = np.concatenate((feature, np.atleast_2d(x_neu)))
# neues label für das neue feature anhängen
labels = np.concatenate((labels, np.atleast_1d(0.5)))
# visualisieren
visualize(feature, labels, w)

# gelernte Gewichte auf das neue feature anwenden und Voraussage machen
print("\nnormalisierte Testdaten")
print(x_neu)
if perzeptron(w, x_neu):
    print("Das ist ein Hund!")
else:
    print("Das ist kein Hund...")

# Ende
input("Fertig? ")
 
