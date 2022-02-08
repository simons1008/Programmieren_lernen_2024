# Modul für den Unittest importieren 
import unittest

# zu testende Funktion importieren
import watt_fuer_wenig

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_watt_fuer_wenig(self):
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(0),    8.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(50),  16.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(100), 24.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(150), 32.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(200), 40.2)
        self.assertAlmostEqual(watt_fuer_wenig.watt_fuer_wenig(250), 48.2)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
