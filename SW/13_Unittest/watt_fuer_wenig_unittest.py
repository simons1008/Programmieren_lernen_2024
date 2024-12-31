# Modul für den Unittest importieren 
import unittest

# monatliche Kosten für Tarif Watt für wenig berechnen
# Funktion mit Datentyp
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 13.5 + verbrauch * 0.75
    return kosten

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_watt_fuer_wenig(self):
        self.assertAlmostEqual(watt_fuer_wenig(0), 13.5)
        self.assertAlmostEqual(watt_fuer_wenig(10), 21.0)
        self.assertAlmostEqual(watt_fuer_wenig(20), 28.5)
        self.assertAlmostEqual(watt_fuer_wenig(50), 51.0)
        self.assertAlmostEqual(watt_fuer_wenig(100), 88.5)
        self.assertAlmostEqual(watt_fuer_wenig(140), 118.5)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
