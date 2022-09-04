# Modul für den Unittest importieren 
import unittest

# Modul mit Zugriff auf die Variable sys.path importieren
import sys

# Pfad der zu testenden Funktionen anhängen
sys.path.append("../10_Formatierte_Ausgabe_und_Graphen_plotten")

# zu testende Funktionen importieren
import flatrate as flat
import volumentarif as vol

# Testfunktionen definieren
class Internet_tarif_test(unittest.TestCase):

    def test_flatrate(self):
        self.assertAlmostEqual(flat.flatrate(0),  0.00)
        self.assertAlmostEqual(flat.flatrate(1),  8.99)
        self.assertAlmostEqual(flat.flatrate(2), 17.98)
        self.assertAlmostEqual(flat.flatrate(3), 26.97)

    def test_volumentarif(self):
        self.assertAlmostEqual(vol.volumentarif([0]),        0.0)
        self.assertAlmostEqual(vol.volumentarif([1]),        6.5)
        self.assertAlmostEqual(vol.volumentarif([1, 2]),    19.5)
        self.assertAlmostEqual(vol.volumentarif([1, 2, 3]), 39.0)
        
# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
