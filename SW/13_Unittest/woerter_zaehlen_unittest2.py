# Unittest für: 
# - Das Programm soll die Wörter in einem Satz zählen
# - Version 2 des Programms entfernt alle Satzzeichen vor dem Zählen


# Modul für den Unittest importieren
import unittest

# Modul´"Regular expression operations" importieren
import re

# Originalsätze
original1 = "Wie wird das Wetter?"
original2 = "Wie Programmieren geht, weiß ich."
original3 = "Heute gab es etwas Gutes zu essen!"
original4 = "Wie wird das Wetter ?"
original5 = "Wie Programmieren geht , weiß ich ."
original6 = "Heute gab es etwas Gutes zu essen !"

# Input der Funktion ist ein Satz
# Output der Funktion ist die Anzahl der Wörter im Satz
# Funktion mit Datentyp
def zaehle_woerter2(original: str) -> str:
    # Entferne alle Zeichen, die keine Buchstaben (\w) 
    # oder Leerzeichen (\s) sind
    ohne_satzzeichen = re.sub(r'[^\w\s]', '', original)
    liste = ohne_satzzeichen.split()
    anzahl = len(liste)
    return anzahl

# Testfunktionen definieren
class Mein_test(unittest.TestCase):

    def test_zaehle_woerter(self):
        self.assertEqual(zaehle_woerter2(original1), 4)
        self.assertEqual(zaehle_woerter2(original2), 5)
        self.assertEqual(zaehle_woerter2(original3), 7)
        self.assertEqual(zaehle_woerter2(original4), 4)
        self.assertEqual(zaehle_woerter2(original5), 5)
        self.assertEqual(zaehle_woerter2(original6), 7)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
