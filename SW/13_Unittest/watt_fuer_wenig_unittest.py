# Modul für den Unittest importieren 
import unittest

# monatliche Kosten für Tarif Watt für wenig berechnen
# Funktion mit Datentyp
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 15.6 + verbrauch * 0.32
    return kosten

# Testfunktionen definieren
class Stromtarif_test(unittest.TestCase):

    def test_watt_fuer_wenig(self):
        self.assertAlmostEqual(watt_fuer_wenig(0), 15.6)
        self.assertAlmostEqual(watt_fuer_wenig(10), 18.8)
        self.assertAlmostEqual(watt_fuer_wenig(50), 31.6)
        self.assertAlmostEqual(watt_fuer_wenig(100), 47.6)
        self.assertAlmostEqual(watt_fuer_wenig(150), 63.6)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
