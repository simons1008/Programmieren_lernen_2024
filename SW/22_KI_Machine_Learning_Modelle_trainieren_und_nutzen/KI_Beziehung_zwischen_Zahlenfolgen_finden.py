# KI Einführung - Beziehung zwischen zwei Zahlenfolgen finden
#                 Modell exportieren
# Quellen: https://www.youtube.com/@BreakingLab/playlists 
#          KI programmieren lernen - Künstliche Intelligenz Tutorials
#          https://dev.mrdbourke.com/tensorflow-deep-learning/
#          01_neural_network_regression_in_tensorflow/ 

# Bibliotheken importieren
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

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
model.compile(loss=tf.keras.losses.mae, # mae - mean absolute error
              optimizer=tf.keras.optimizers.SGD(), # SGD - stochastic gradient descent
              metrics=["mae"])

# Modell fitten (fit - dazupassen)
model.fit(tf.expand_dims(X, axis=-1), y, epochs=100) # Dimension der Input-Form expandieren

# Zusammenfassung anzeigen
model.summary()

# Modell mit X-Wert testen
X_neu = np.array([11])
y_neu = model.predict(X_neu)
print(f"X_neu = {X_neu}, y_neu = {y_neu}")

# Visualisierung mit dem neuen X-Wert
plt.scatter(X, y, c="b");
plt.scatter(X_neu, y_neu, c="r") 
plt.show()

# Modell für eine spätere Benutzung exportieren
model.save("my_model.keras")

# Weiter?
input("Modell exportiert. Weiter?")
