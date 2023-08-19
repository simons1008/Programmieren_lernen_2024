# Perzeptron als Klasse
# Quelle:  https://www.youtube.com/@STARTUPTEENS/playlists 
#          Programmiere mit Python - Baue deine eigene KI! #20

# Bibliotheken importieren
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

# Array-Dimensionen ausgeben
##print("Array-Dimensionen")
##print(feature.shape)

# Einen Vektor mit Einsen anhängen
# Dadurch wird der Bias w[2] addiert
feature = np.concatenate((feature, np.ones(43).reshape(43,1)), axis=1)
##print("Array-Dimensionen mit dem Vektor von Einsen")
##print(feature.shape)

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
        self.cnt = 0

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
        # +/- groesse zu w[0]
        # +/- breite  zu w[1]
        # +/- 1       zum Bias w[2]
        cnt = 0
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
                self.cnt = cnt
                break
            cnt += 1
        else:
            print("Es wurde keine Lösung gefunden.")
        
        
    def visualize(self, feature, labels):
        plt.title('Trainingsdaten')
        plt.xlabel("Größe auf "  + "{:4.2f}".format(perzeptron.skalierungsfaktor[0]) + " cm normiert")
        plt.ylabel("Breite auf " + "{:4.2f}".format(perzeptron.skalierungsfaktor[1]) + " cm normiert")
        plt.scatter(feature[:,0], feature[:,1], c=labels)
        x0 = np.array([0.5, 1])
        w = self.w
        if w[1] != 0:
            x1 = -(w[0] * x0 + w[2]) / w[1]
            plt.plot(x0, x1)
        plt.show()

    def falsche_klassifikationen(self):
        plt.plot(range(self.max_epochs), self.fehler)
        plt.xlabel('Epoche')
        plt.ylabel('Falsche Klassifikationen')
        plt.show()

# nur ausführen, wenn das Programm direkt aufgerufen wird
if __name__ == "__main__":

    # Instanz erstellen
    perzeptron = Perzeptron(100)

    # Lernschritt aufrufen
    perzeptron.lernschritt(feature, labels)

    # Daten und Linie darstellen
    perzeptron.visualize(feature, labels)

    # falsche Klassifikationen darstellen
    perzeptron.falsche_klassifikationen()

    # gelernte Gewichte ausgeben
    print("gelernte Gewichte")
    print(perzeptron.w)

    # Anzahl der Epochen ausgeben
    print("Anzahl der Epochen")
    print(perzeptron.cnt)

    # neues feature angeben
    # das neue feature wird vom Perzeptron skaliert
    x_neu = [40.0, 20.0, 1]

    # gelernte Gewichte auf das neue feature anwenden und Voraussage machen
    if perzeptron.perzeptron(x_neu):
        print("Das ist ein Hund!")
    else:
        print("Das ist kein Hund...")

    # Ende
    input("Fertig? ")
