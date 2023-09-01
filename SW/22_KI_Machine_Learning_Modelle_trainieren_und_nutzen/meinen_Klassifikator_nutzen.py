# Klassifikator für H S U Grauwert-Bilder nutzen
# Quelle: https://scikit-learn.org/stable/model_persistence.html#model-persistence

# Bibliotheken importieren
import numpy as np
from joblib import dump, load

# Testdaten laden
X_test = np.load("HSU_test_data.npy")

# Testlabels laden
y_test = np.load("HSU_test_labels.npy")

# Klassifikator laden
clf2 = load("mein_Klassifikator.joblib")

# Geladenes Modell mit den Testdaten testen
print("Vorhersage des geladenen Modells")
predicted = clf2.predict(X_test)

# Vorhersage ausgeben
print(predicted)

# Sollwerte ausgeben
print(y_test)

# Fehler ausgeben
print(predicted - y_test)

# Genauigkeit für die gegebenen Testdaten und Testlabels ausgeben
print("Score: {:5.2f}".format(clf2.score(X_test, y_test)))

# Ende
input("Fertig?")
