# Das Programm lädt die numpy Array aus 75 Dateien und erstellt
# daraus ein großes numpy Array, das gespeichert wird

# Bibliotheken importieren
import numpy as np
import pprint

# Buchstaben
buchstabe = ["H_0", "S_0", "U_0"]

# Ansichten
ansicht = ["", "_lilinks", "_links", "_rechts", "_rerechts"]

# Positionen
position = ["", "_hoch", "_runter", "_nali", "_nare"]

# Dateiname
dateiname = []

# Labels
labels = []

# Schleife über 3 Buchstaben
for i in range(3):
    fp_buchstabe = "{:}".format(buchstabe[i])
    # Schleife über 5 Ansichten
    for j in range(5):
        fp_ansicht = fp_buchstabe + "{:}".format(ansicht[j])
        # Schleife über 5 Positionen
        for k in range(5):
            fp_position = fp_ansicht + "{:}.npy".format(position[k])
            # Dateiname speichern
            dateiname.append(fp_position)
            # Labels speichern (der Index i ist das Label)
            labels.append(i)       

# print
pprint.pprint(dateiname)

# Datensatz mit dem Inhalt der ersten Datei initialisieren
datensatz = np.load(dateiname[0])

# Zeilenvektor bilden
datensatz = datensatz.reshape((1,256))
print(datensatz)
print(datensatz.shape)

# Schleife über alle Dateien
for i in range (1, len(dateiname)):
    # Dateiinhalt laden
    inhalt = np.load(dateiname[i])

    # Zeilenvektor bilden
    inhalt = inhalt.reshape((1,256))

    # Dateiinhalt anhängen
    datensatz = np.append(datensatz, inhalt, 0)
    print(datensatz.shape)

# Typ des Datensatzes angeben
print(type(datensatz))

# Datensatz speichern
np.save("HSU_data.npy", datensatz)

# labels in numpy array konvertieren
labels = np.array(labels)
print(labels.shape)

# labels speichern
np.save("HSU_labels.npy", labels)
