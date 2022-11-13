# Modul für den Unittest importieren 
import unittest

# zu testende Funktion einfügen
def meine_funktion:
    ...

# Testfunktionen definieren
class Mein_test(unittest.TestCase):

    def test_meine_funktion(self):
        self.assertEqual(meine_funktion(mein_input1), mein_output1)
        self.assertEqual(meine_funktion(mein_input2), mein_output2)
        self.assertEqual(meine_funktion(mein_input3), mein_output3)
        self.assertEqual(meine_funktion(mein_input4), mein_output4)

# Unittest ausführen, wenn die Datei direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
