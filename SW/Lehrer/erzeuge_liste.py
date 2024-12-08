# Erzeuge eine Liste mit dem Vielfachen einer Zahl

# Funktion mit Datentyp
def erzeuge_liste(zahl: int) -> list[int]:
    meine_liste = []
    for i in range(1, 11):
        meine_liste.append(i * zahl)
    return meine_liste
