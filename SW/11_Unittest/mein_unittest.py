# Modul für den Unittest importieren 
import unittest

# zu testende Funktionen definieren
def dezimalzahl1():
    return 0.6999999

def dezimalzahl2():
    return 0.69999999

# Testfunktion definieren
class mein_test(unittest.TestCase):

    def test_dezimalzahl1(self):
        self.assertAlmostEqual(dezimalzahl1(), 0.7)

    def test_dezimalzahl2(self):
        self.assertAlmostEqual(dezimalzahl2(), 0.7)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
