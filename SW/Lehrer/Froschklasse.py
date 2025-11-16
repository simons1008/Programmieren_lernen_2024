# Objektorientierte Programmierung

# Klassendefinition
class BauplanFroschKlasse():
    """ Hilfetext für die BauplanFroschKlasse """
    
    # Methoden der Klasse
    def __init__(self, rufname, farbe, laenge, gewicht):
        self.rufname = rufname 
        self.farbe = farbe
        self.laenge = laenge
        self.gewicht = gewicht

    def tut_quaken(self, anzahl = 1):
        print(anzahl * "quak ")

    def tut_springen(self, weite = 30):
        print(self.rufname, "springt", weite, "Zentimeter")

# Instanz erstellen
frosch_fritz = BauplanFroschKlasse("Fritz", "grün", "4.5 Zentimeter", "6 Gramm")

# Eigenschaften drucken
print(frosch_fritz.rufname)
print(frosch_fritz.farbe)
print(frosch_fritz.laenge)
print(frosch_fritz.gewicht)

# Methoden aufrufen
frosch_fritz.tut_quaken(3)
frosch_fritz.tut_springen()
