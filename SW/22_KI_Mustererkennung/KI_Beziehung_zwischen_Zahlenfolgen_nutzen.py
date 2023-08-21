# KI Einführung - Modell laden
#               - Modell nutzen, d. h. Voraussage machen
# Quellen: Walter Stein https://steinphysik.de/download/272/
#          https://www.tensorflow.org/guide/keras/serialization_and_saving

# Library importieren
from tensorflow import keras

# Modell laden
reconstructed_model = keras.models.load_model("my_model.keras")

# Wert voraussagen
print(reconstructed_model.predict([11]))

# Weiter?
input("Rekonstruiertes Modell ausgeführt. Weiter?")
