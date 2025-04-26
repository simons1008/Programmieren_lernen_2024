# Modul für den Unittest importieren 
import unittest

# monatliche Kosten für Tarif Billig-Strom berechnen
# Funktion mit Datentyp
def billig_strom(verbrauch: float) -> float:
    kosten = 12.8 + verbrauch * 0.36
    return kosten

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_billig_strom(self):
        self.assertAlmostEqual(billig_strom(0), 12.8)
        self.assertAlmostEqual(billig_strom(10), 16.4)
        self.assertAlmostEqual(billig_strom(50), 30.8)
        self.assertAlmostEqual(billig_strom(100), 48.8)
        self.assertAlmostEqual(billig_strom(150), 66.8)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
