# Modul für den Unittest importieren 
import unittest

# zu testende Funktion importieren (oder einfügen)
def quersumme(ganzzahl: int) -> int:
    anzahl_h = ganzzahl // 100
    rest_h = ganzzahl % 100

    anzahl_z = rest_h // 10
    rest_z = rest_h % 10

    anzahl_e = rest_z
    quersumme = anzahl_h + anzahl_z + anzahl_e
    return quersumme

# Testfunktionen definieren
class quersumme_test(unittest.TestCase):

    def test_quersumme(self):
        self.assertEqual(quersumme(0), 0)
        self.assertEqual(quersumme(10), 1)
        self.assertEqual(quersumme(100), 1)
        self.assertEqual(quersumme(109), 10)
        self.assertEqual(quersumme(200), 2)
        self.assertEqual(quersumme(290), 11)
        self.assertEqual(quersumme(900), 9)
        self.assertEqual(quersumme(999), 27)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
