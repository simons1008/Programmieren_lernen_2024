# Programm prüft, ob ein Schlüssel im Dictionary bereits vorhanden ist

# Dictionary englisch_deutsch
englisch_deutsch = {'cat': 'Katze', 'dog': 'Hund', 'cow': 'Kuh', 'bird': 'Vogel'}

# Schlüssel erfragen
key = input("Gib ein englisches Wort an: ")

# Prüfen, ob Schlüssel vorhanden
if key in englisch_deutsch:
    print("Der Schlüssel ist nicht frei")
else:
    print("Der Schlüssel ist frei")
