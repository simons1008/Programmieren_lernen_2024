# Modul für den Unittest importieren 
import unittest

# Modul mit Zugriff auf die Variable sys.path importieren
import sys

# Pfad der zu testenden Funktionen anhängen
sys.path.append("../10_Aufgaben_mit_Funktionen_loesen")

# zu testende Funktionen importieren
import watt_fuer_wenig
import billig_strom

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_watt_fuer_wenig(self):
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(0), 15.6)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(10), 18.8)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(50), 31.6)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(100), 47.6)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(150), 63.6)

    def test_billig_strom(self):
        self.assertAlmostEqual(billig_strom.billig_strom(0), 12.8)
        self.assertAlmostEqual(billig_strom.billig_strom(10), 16.4)
        self.assertAlmostEqual(billig_strom.billig_strom(50), 30.8)
        self.assertAlmostEqual(billig_strom.billig_strom(100), 48.8)
        self.assertAlmostEqual(billig_strom.billig_strom(150), 66.8)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
