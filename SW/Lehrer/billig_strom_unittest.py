# Modul für den Unittest importieren 
import unittest

# Modul mit Zugriff auf die Variable sys.path importieren
import sys

# Pfad der zu testenden Funktionen anhängen
sys.path.append("../10_Funktionen_konstruieren")

# zu testende Funktion importieren
import billig_strom

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_billig_strom(self):
        self.assertAlmostEqual(billig_strom.billig_strom(0), 9.2)
        self.assertAlmostEqual(billig_strom.billig_strom(10), 17.3)
        self.assertAlmostEqual(billig_strom.billig_strom(20), 25.4)
        self.assertAlmostEqual(billig_strom.billig_strom(50), 49.7)
        self.assertAlmostEqual(billig_strom.billig_strom(100), 90.2)
        self.assertAlmostEqual(billig_strom.billig_strom(140), 122.6)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
