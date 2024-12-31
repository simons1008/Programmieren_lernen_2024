# Modul für den Unittest importieren 
import unittest

# Modul mit Zugriff auf die Variable sys.path importieren
import sys

# Pfad der zu testenden Funktionen anhängen
sys.path.append("../10_Aufgaben_mit_Funktionen_loesen")

# zu testende Funktion importieren
import watt_fuer_wenig

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_watt_fuer_wenig(self):
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(0), 13.5)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(10), 21.0)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(20), 28.5)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(50), 51.0)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(100), 88.5)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(140), 118.5)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
