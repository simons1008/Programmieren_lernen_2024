# State Vector Machine arbeitet mit nicht-linearem Datensatz
# Quelle:  https://www.youtube.com/@STARTUPTEENS/playlists 
#          Programmiere mit Python - Baue deine eigene KI! #21

# Bibliotheken importieren
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# Nicht-linearen Datensatz erstellen
sigma = 5
hunde = 26
sonst = 53

X1 = sigma * np.random.randn(hunde, 2) + (30, 22)
X2 = sigma * np.random.randn(sonst, 2) + (20, 15)
feature = np.concatenate((X1, X2))
label = np.concatenate((np.ones(hunde), np.zeros(sonst)))

# Funktion plottet das Ergebnis
def plot_svm(clf, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)

    plt.xlabel('Grösse [cm]')
    plt.ylabel('Breite [cm]')
    plt.title('Trainingsdaten')
    plt.show()


# Instanz erstellen
svm = SVC()

# Training
svm.fit(feature, label)

# Ergebnis plotten
plot_svm(svm, feature, label)
