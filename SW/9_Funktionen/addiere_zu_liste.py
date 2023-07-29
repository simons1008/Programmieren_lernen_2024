# Addiere eine Zahl zu einer Liste 

# Funktion mit Datentyp
def addiere_zu_liste(meine_liste: list[int], zahl: int) -> list[int]:
    for i in range(len(meine_liste)):
        meine_liste[i] += zahl
    return meine_liste
