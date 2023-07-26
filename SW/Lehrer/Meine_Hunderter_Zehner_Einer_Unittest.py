# Modul für den Unittest importieren 
import unittest

# zu testende Funktion einfügen
def hunderter_zehner_einer(ganzzahl: int) -> list[int]:
    anzahl_h = ganzzahl // 100
    rest_h = ganzzahl % 100

    anzahl_z = rest_h // 10
    rest_z = rest_h % 10

    anzahl_e = rest_z
    anzahl_liste = [anzahl_h, anzahl_z, anzahl_e]
    return anzahl_liste

# Testfunktionen definieren
class Hunderter_zehner_einer_test(unittest.TestCase):

    def test_hunderter_zehner_einer(self):
        self.assertEqual(hunderter_zehner_einer(0), [0, 0, 0])
        self.assertEqual(hunderter_zehner_einer(10), [0, 1, 0])
        self.assertEqual(hunderter_zehner_einer(100), [1, 0, 0])
        self.assertEqual(hunderter_zehner_einer(109), [1, 0, 9])
        self.assertEqual(hunderter_zehner_einer(200), [2, 0, 0])
        self.assertEqual(hunderter_zehner_einer(290), [2, 9, 0])
        self.assertEqual(hunderter_zehner_einer(900), [9, 0, 0])
        self.assertEqual(hunderter_zehner_einer(999), [9, 9, 9])

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
