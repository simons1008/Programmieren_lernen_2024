# KI Einführung - Modell laden
#               - Modell nutzen, d. h. Voraussage machen
# Quelle:  https://dev.mrdbourke.com/tensorflow-deep-learning/
#          01_neural_network_regression_in_tensorflow/ 

# Bibliotheken importieren
import tensorflow as tf
import numpy as np

# Modell laden
reconstructed_model = tf.keras.models.load_model("my_model.keras")

# Modell mit X-Wert testen
X_neu = np.array([11])
y_neu = reconstructed_model.predict(X_neu)
print(f"X_neu = {X_neu}, y_neu = {y_neu}")

# Weiter?
input("Rekonstruiertes Modell ausgeführt. Weiter?")
