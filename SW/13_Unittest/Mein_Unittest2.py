# Modul für den Unittest importieren 
import unittest

# Modul mit Zugriff auf die Variable sys.path importieren
import sys

# Pfad der zu testenden Funktionen anhängen
sys.path.append("mein Pfad")

# Modul importieren, das die zu testende Funktion enthält
import mein_modul

# Testfunktionen definieren
class Mein_test(unittest.TestCase):

    def test_meine_funktion(self):
        self.assertEqual(mein_modul.meine_funktion(mein_input1), mein_output1)
        self.assertEqual(mein_modul.meine_funktion(mein_input2), mein_output2)
        self.assertEqual(mein_modul.meine_funktion(mein_input3), mein_output3)
        self.assertEqual(mein_modul.meine_funktion(mein_input4), mein_output4)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
