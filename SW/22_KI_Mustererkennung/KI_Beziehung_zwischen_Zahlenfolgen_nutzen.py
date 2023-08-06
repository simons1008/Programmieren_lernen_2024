# KI Einführung - Beziehung zwischen zwei Zahlenfolgen nutzen
# Quelle: Walter Stein https://steinphysik.de/download/272/

# Library importieren
from tensorflow import keras

# Modell laden
reconstructed_model = keras.models.load_model("my_model.keras")

# Wert voraussagen
print(reconstructed_model.predict([11]))

# Weiter?
input("Rekonstruiertes Modell ausgeführt. Weiter?")
