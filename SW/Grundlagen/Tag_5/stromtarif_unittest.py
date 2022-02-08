# Modul für den Unittest importieren 
import unittest

# zu testende Funktionen importieren
import watt_fuer_wenig
import billig_strom

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_watt_fuer_wenig(self):
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(0),    8.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(50),  16.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(100), 24.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(150), 32.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(200), 40.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(250), 48.2)

    def test_billig_strom(self):
        self.assertAlmostEqual(billig_strom.billig_strom(0),    4.9)
        self.assertAlmostEqual(billig_strom.billig_strom(50),  14.4)
        self.assertAlmostEqual(billig_strom.billig_strom(100), 23.9)
        self.assertAlmostEqual(billig_strom.billig_strom(150), 33.4)
        self.assertAlmostEqual(billig_strom.billig_strom(200), 42.9)
        self.assertAlmostEqual(billig_strom.billig_strom(250), 52.4)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
