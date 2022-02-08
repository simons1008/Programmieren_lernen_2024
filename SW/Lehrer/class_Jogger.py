class Jogger():
    """ sportliche Klasse für das Verwalten von gelaufenen Zeiten """

    def __init__(self, altersklasse, zeit=[]):
        self.altersklasse = altersklasse
        self.gelaufene_zeiten  = zeit

    def zeiterfassen(self, zeiten):
        self.gelaufene_zeiten += zeiten

Laeufer_Hans = Jogger("M40")
print(Laeufer_Hans.altersklasse)
Laeufer_Hans.zeiterfassen(["2:30"])
print(Laeufer_Hans.gelaufene_zeiten)
Laeufer_Hans.zeiterfassen(["2:40", "3:10"])
print(Laeufer_Hans.gelaufene_zeiten)

