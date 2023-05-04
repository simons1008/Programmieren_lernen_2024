# Modul für den Unittest importieren 
import unittest

# zu testende Funktion einfügen
def hunderter(ganzzahl: int) -> int:
    anzahl = ganzzahl // 100
    return anzahl

# Testfunktionen definieren
class Hunderter_test(unittest.TestCase):

    def test_hunderter(self):
        self.assertEqual(hunderter(0), 0)
        self.assertEqual(hunderter(10), 0)
        self.assertEqual(hunderter(100), 1)
        self.assertEqual(hunderter(109), 1)
        self.assertEqual(hunderter(200), 2)
        self.assertEqual(hunderter(290), 2)
        self.assertEqual(hunderter(900), 9)
        self.assertEqual(hunderter(999), 9)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
