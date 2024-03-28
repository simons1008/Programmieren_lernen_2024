# KI Einführung - Beziehung zwischen zwei Zahlenfolgen finden
#                 Modell exportieren
#                 Vergleich mit der exakten analytischen Lösung
# Quellen: https://www.youtube.com/@BreakingLab/playlists 
#          KI programmieren lernen - Künstliche Intelligenz Tutorials
#          https://dev.mrdbourke.com/tensorflow-deep-learning/
#          01_neural_network_regression_in_tensorflow/
#          https://docs.scipy.org/doc/scipy/reference/generated/
#          scipy.stats.linregress.html

# Bibliotheken importieren
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datensatz erzeugen und plotten
# Erzeuge Features
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Erzeuge Labels
y = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27])

# Visualisierung
plt.scatter(X, y);
plt.show()

# Modell erstellen
model = tf.keras.Sequential([tf.keras.layers.Dense(1)])

# Modell kompilieren
model.compile(loss=tf.keras.losses.mse, # mse - mean square error
              optimizer=tf.keras.optimizers.SGD()) # SGD - stochastic gradient descent

# Modell fitten (fit - dazupassen)
model.fit(tf.expand_dims(X, axis=-1), y, epochs=200) # Dimension der Input-Form expandieren

# Modell mit X-Wert testen
X_neu = np.array([11])
y_neu = model.predict(X_neu)
print(f"X_neu = {X_neu}, y_neu = {y_neu}")

# analytische Berechnung der Ausgleichsgeraden
res = stats.linregress(X, y)
print("\nanalytische Berechnung der Ausgleichsgeraden")
print(f"Steigung         = {res.slope}")
print(f"Achsenabschnitt  = {res.intercept}")
print(f"Bestimmtheitsmaß = {res.rvalue*res.rvalue}")

# Visualisierung
# Zahlenfolge mit dem neuen X-Wert
plt.scatter(X, y, c="b");
plt.scatter(X_neu, y_neu, c="r")
# exakte Ausgleichsgerade
x_Koordinaten = np.array([1, 11])
y_Koordinaten = res.intercept + res.slope*x_Koordinaten
plt.plot(x_Koordinaten, y_Koordinaten, "c")
plt.show()

# Modell für eine spätere Benutzung exportieren
model.save("my_model.keras")

# Weiter?
input("Modell exportiert. Weiter?")
