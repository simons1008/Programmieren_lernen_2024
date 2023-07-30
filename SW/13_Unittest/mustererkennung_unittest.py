# Modul für den Unittest importieren 
import unittest

# Modul mit Zugriff auf die Variable sys.path importieren
# import sys

# Pfad der zu testenden Funktionen anhängen
# sys.path.append("mein Pfad")

# zu testende Funktion importieren
import mustererkennung as muster

# Testfunktionen definieren
class Mein_test(unittest.TestCase):

    def test_erkannte_zahlen(self):
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 0), "Erkannte zahl(en): 1 2 3")
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 1), "Erkannte zahl(en): 2 3")
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 2), "Erkannte zahl(en): 2 3")
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 3), "Erkannte zahl(en): 2 3")
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 4), "Erkannte zahl(en): 2 3")
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 5), "Erkannte zahl(en): 2")
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 6), "Erkannte zahl(en): 2")
        self.assertEqual(muster.erkannte_zahlen(muster.muster, 7), "Erkannte zahl(en): keine")

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
