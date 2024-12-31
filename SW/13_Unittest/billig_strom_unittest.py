# Modul für den Unittest importieren 
import unittest

# monatliche Kosten für Tarif Billig-Strom berechnen
# Funktion mit Datentyp
def billig_strom(verbrauch: float) -> float:
    kosten = 9.2 + verbrauch * 0.81
    return kosten

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_billig_strom(self):
        self.assertAlmostEqual(billig_strom(0), 9.2)
        self.assertAlmostEqual(billig_strom(10), 17.3)
        self.assertAlmostEqual(billig_strom(20), 25.4)
        self.assertAlmostEqual(billig_strom(50), 49.7)
        self.assertAlmostEqual(billig_strom(100), 90.2)
        self.assertAlmostEqual(billig_strom(140), 122.6)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
