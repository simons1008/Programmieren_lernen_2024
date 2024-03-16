# KI Einführung - Beziehung zwischen zwei Zahlenfolgen finden - Zahl/Quadratzahl
#                 Modell exportieren
# Quellen: Walter Stein https://steinphysik.de/download/272/
#          https://www.tensorflow.org/guide/keras/serialization_and_saving

# Library importieren
from tensorflow import keras

# Neuronales Netz definieren
model = keras.Sequential()
model.add(keras.layers.Dense(units=1, input_shape=[1]))

# Modell kompilieren
model.compile(optimizer='sgd', loss='mean_squared_error')

# Zahlenreihen
inputs=[1, 2, 3, 4, 5, 6, 7, 8, 9]
expected_outputs=[1, 4, 9, 16, 25, 36, 49, 64, 81]

# Modell fitten
model.fit(inputs, expected_outputs, epochs=200)

# Wert voraussagen
print(model.predict([11]))

# Modell für eine spätere Benutzung exportieren
model.save("my_model.keras")

# Weiter?
input("Modell exportiert. Weiter?")
