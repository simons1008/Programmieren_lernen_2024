# Unittest für: 
# - Das Programm soll die Wörter in einem Satz zählen

# Modul für den Unittest importieren
import unittest

# Originalsätze
original1 = "Wie wird das Wetter?"
original2 = "Wie Programmieren geht, weiß ich."
original3 = "Heute gab es etwas Gutes zu essen!"

# Input der Funktion ist ein Satz
# Output der Funktion ist die Anzahl der Wörter im Satz
# Funktion mit Datentyp
def zaehle_woerter(original: str) -> str:
    liste = original.split()
    anzahl = len(liste)
    return anzahl

# Testfunktionen definieren
class Mein_test(unittest.TestCase):

    def test_zaehle_woerter(self):
        self.assertEqual(zaehle_woerter(original1), 4)
        self.assertEqual(zaehle_woerter(original2), 5)
        self.assertEqual(zaehle_woerter(original3), 7)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
