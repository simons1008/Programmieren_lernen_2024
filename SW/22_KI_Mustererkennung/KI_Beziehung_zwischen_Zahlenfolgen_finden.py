# KI Einführung - Beziehung zwischen zwei Zahlenfolgen finden
# Quelle: Walter Stein https://steinphysik.de/download/272/

# Library importieren
from tensorflow import keras

# Neuronales Netz definieren
model = keras.Sequential()
model.add(keras.layers.Dense(units=1, input_shape=[1]))

# Modell kompilieren
model.compile(optimizer='sgd', loss='mean_squared_error')

# Zahlenreihen
inputs=[1, 2, 3, 4, 5, 6, 7, 8, 9]
expected_outputs=[3, 6, 9, 12, 15, 18, 21, 24, 27]

# Modell fitten
model.fit(inputs, expected_outputs, epochs=200)

# Wert voraussagen
print(model.predict([11]))

# Modell für eine spätere Benutzung exportieren
model.save("my_model.keras")

# Weiter?
input("Modell exportiert. Weiter?")
