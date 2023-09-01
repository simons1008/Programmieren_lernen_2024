# Klassifikator für H S U Grauwert-Bilder trainieren und testen
# Quellen: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
#          https://scikit-learn.org/stable/model_persistence.html#model-persistence

# Bibliotheken importieren
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from joblib import dump, load

# Daten laden
data = np.load("HSU_data.npy")

# Labels laden
labels = np.load("HSU_labels.npy")

# Daten in Trainingsdaten und Testdaten aufspalten
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.3, random_state = 1, shuffle=True)

# Klassifikator erstellen
clf = RandomForestClassifier()

# Mit den Trainingsdaten trainieren (fit - dazupassen)
clf.fit(X_train, y_train)

# Modell mit den Testdaten testen
print("Vorhersage des trainierten Modells")
predicted = clf.predict(X_test)

# Vorhersage ausgeben
print(predicted)

# Sollwerte ausgeben
print(y_test)

# Fehler ausgeben
print(predicted - y_test)

# Erkennungsleistung für die gegebenen Testdaten und Testlabels ausgeben
print("Score: {:5.2f}".format(clf.score(X_test, y_test)))

# Metrics Classification Report ausgeben
print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

# Einzelnes Sample vorhersagen - erfordert reshape
predicted = clf.predict(X_test[4].reshape(1, -1))

# Vorhersage und Sollwert
print("Vorhersage eines einzelnen Samples")
print("Istwert: {:} Sollwert: {:}".format(predicted, y_test[4]))

# Testdaten speichern
np.save("HSU_test_data.npy", X_test)

# Testlabels speichern
np.save("HSU_test_labels.npy", y_test)

# Klassifikator speichern
dump(clf, "mein_Klassifikator.joblib")

# Weiter?
input("Modell exportiert. Weiter?")
