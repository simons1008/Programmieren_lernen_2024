# Meine Lösung der Aufgabe am Ende von startupteens Python Tutorial #20
# Perzeptron als Klasse - Code erweitert um die Anzahl der Beine
# Antworten auf die Fragen:
# - Durch das zusätzliche Datum "Beine" wird die Anzahl der Epochen kleiner. 
# Für die Gerade im 2D-Plot muss w[0] * x0 berücksichtigt werden!
# Quelle:  https://www.youtube.com/@STARTUPTEENS/playlists 
#          Programmiere mit Python - Baue deine eigene KI! #20

# Bibliotheken importieren
import numpy as np
import matplotlib.pyplot as plt

# Daten in numpy-Array speichern
# [beine, groesse, breite]
feature = np.array([[4.0, 37.92655435, 23.90101111],
                    [4.0, 35.88942857, 22.73639281],
                    [4.0, 29.49674574, 21.42168559],
                    [4.0, 32.48016326, 21.7340484 ],
                    [4.0, 38.00676226, 24.37202837],
                    [4.0, 30.73073988, 22.69832608],
                    [4.0, 35.93672343, 21.07445241],
                    [4.0, 38.65212459, 20.57099727],
                    [4.0, 35.52041768, 21.74519457],
                    [4.0, 37.69535497, 20.33073640],
                    [4.0, 33.00699292, 22.57063861],
                    [4.0, 33.73140934, 23.81730782],
                    [4.0, 43.85053380, 20.05153803],
                    [4.0, 32.95555986, 24.12153986],
                    [4.0, 36.38192916, 19.20280266],
                    [4.0, 36.54270168, 20.45388966],
                    [4.0, 33.08246118, 22.20524015],
                    [4.0, 31.76866280, 21.01201139],
                    [4.0, 42.24260825, 20.44394610],
                    [4.0, 29.04450264, 22.46633771],
                    [4.0, 30.04284328, 21.54561621],
                    [4.0, 18.95626707, 19.66737753],
                    [4.0, 18.60176718, 17.74023009],
                    [4.0, 12.85314993, 18.42746953],
                    [4.0, 28.62450072, 17.94781944],
                    [4.0, 21.00655655, 19.33438286],
                    [4.0, 17.33580556, 18.81696459],
                    [4.0, 31.17129195, 17.23625014],
                    [4.0, 19.36176482, 20.67772798],
                    [4.0, 27.26581705, 16.71312863],
                    [4.0, 21.19107828, 19.00673617],
                    [4.0, 19.08131597, 15.24401994],
                    [4.0, 26.69761925, 17.05937466],
                    [2.0, 4.44136559 , 3.52432493 ],
                    [2.0, 10.26395607, 1.07729281 ],
                    [2.0, 7.39058439 , 3.44234423 ],
                    [2.0, 4.23565118 , 4.28840232 ],
                    [2.0, 3.87875761 , 5.12407692 ],
                    [2.0, 15.12959925, 6.26045879 ],
                    [0.0, 5.93041263 , 1.70841905 ],
                    [0.0, 4.25054779 , 5.01371294 ],
                    [0.0, 2.15139117 , 4.16668657 ],
                    [0.0, 2.38283228 , 3.83347914 ]])
# Array-Dimensionen ausgeben
print("Array-Dimensionen")
print(feature.shape)

# Einen Vektor mit Einsen anhängen
# Dadurch wird der Bias w[3] addiert
feature = np.concatenate((feature, np.ones(43).reshape(43,1)), axis=1)
print("Array-Dimensionen mit dem Vektor von Einsen")
print(feature.shape)

# Label speichern. Vereinfachung:
# - die ersten  21 sind features von Hunden
# - die letzten 22 sind features von Nicht-Hunden
labels = np.concatenate((np.ones(21), np.zeros(22)))

# Klasse erstellen
class Perzeptron:
    def __init__(self, max_epochs):
        self.w = None # Dimension von w hängt von den Trainingsdaten ab
        self.skalierungsfaktor = None
        self.trainiert = False
        self.max_epochs = max_epochs
        self.fehler = np.zeros(max_epochs)

    def perzeptron(self, x):
        if self.trainiert:
            x /= self.skalierungsfaktor # neue Daten skalieren
        if np.dot(self.w, x) > 0:
            return 1 
        else:
            return 0
        
    def lernschritt(self, feature, labels):
        self.skalierungsfaktor = np.max(feature, 0)
        feature /= self.skalierungsfaktor
        np.random.seed(5) # damit die 'zufälligen' Zahlen immer gleich sind
        self.w = np.random.rand(feature.shape[1])
        # Perzeptron Lernregel
        # +/- beine   zu w[0]
        # +/- groesse zu w[1]
        # +/- breite  zu w[2]
        # +/- 1       zum Bias w[3]
        cnt = 0
        self.fehler = np.zeros(self.max_epochs)
        while cnt < self.max_epochs:
            for index in range(len(feature)):
                x = feature[index]
                label = labels[index]
                delta = label - self.perzeptron(x)
                if delta != 0: # falsch klassifiziert
                    self.fehler[cnt] += 1
                    self.w += delta * x
            # wenn trainiert
            if self.fehler[cnt] == 0:
                self.trainiert = True
                break
            cnt += 1
        else:
            print("Es wurde keine Lösung gefunden.")
        

    def visualize(self, feature, labels):
        plt.title('Trainingsdaten')
        plt.xlabel("Größe auf "  + "{:4.2f}".format(perzeptron.skalierungsfaktor[1]) + " cm normiert")
        plt.ylabel("Breite auf " + "{:4.2f}".format(perzeptron.skalierungsfaktor[2]) + " cm normiert")
        plt.scatter(feature[:,1], feature[:,2], c=labels)
        x1 = np.array([0.5, 1])
        w = self.w
        if w[2] != 0:
            # Skalarprodukt nach x2 aufgelöst
            # w[0] wird mit der Anzahl der Beine in der Hunde-Ebene multipliziert
            # Mit Normalisierung:   w[0] wird mit x0 = 1 multipliziert
            # (Ohne Normalisierung: w[0] wird mit x0 = 4 multipliziert)
            x2 = -(w[0] + w[1] * x1 + w[3]) / w[2]
            plt.plot(x1, x2)
        plt.show()

    def falsche_klassifikationen(self):
        plt.plot(range(self.max_epochs), self.fehler)
        plt.xlabel('Epoche')
        plt.ylabel('Falsche Klassifikationen')
        plt.show()


# Instanz erstellen
perzeptron = Perzeptron(100)

# Lernschritt aufrufen
perzeptron.lernschritt(feature, labels)

# Daten 3D darstellen
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(feature[:,1], feature[:,0], feature[:,2], c=labels)
ax.set_title('Trainingsdaten 3-dimensional')
ax.set_xlabel("Breite auf "  + "{:4.2f}".format(perzeptron.skalierungsfaktor[2]) + " cm normiert")
ax.set_ylabel("Beine auf "  + "{:}".format(perzeptron.skalierungsfaktor[0]) + " normiert")
ax.set_zlabel("Größe auf " + "{:4.2f}".format(perzeptron.skalierungsfaktor[1]) + " cm normiert")
plt.show()

# Daten und Linie darstellen
perzeptron.visualize(feature, labels)

# falsche Klassifikationen darstellen
perzeptron.falsche_klassifikationen()

# gelernte Gewichte ausgeben
print("gelernte Gewichte")
print(perzeptron.w)

# neues feature angeben
# das neue feature wird vom Perzeptron skaliert
x_neu = [4, 40.0, 20.0, 1]

# gelernte Gewichte auf das neue feature anwenden und Voraussage machen
if perzeptron.perzeptron(x_neu):
    print("Das ist ein Hund!")
else:
    print("Das ist kein Hund...")

# Ende
input("Fertig? ")
