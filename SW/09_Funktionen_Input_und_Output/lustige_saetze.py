# Lustige Sätze

import random

# Beispielsätze
subjekt = ["Der Hund", "Die Journalistin", "Der Maler"]
prädikat = ["vergräbt", "interviewt", "malt"]
objekt = ["den Knochen", "den Bürgermeister", "ein Bild"]

# Funktion definieren
def zufall(subjekt, prädikat, objekt) -> str:
    mein_subjekt = random.choice(subjekt)
    mein_prädikat = random.choice(prädikat)
    mein_objekt = random.choice(objekt)
    mein_satz = mein_subjekt + " " + mein_prädikat + " " + mein_objekt
    return mein_satz

# mein_subjekt = random.choice(subjekt)
# mein_prädikat = random.choice(prädikat)
# mein_objekt = random.choice(objekt)
# mein_satz = mein_subjekt + " "  mein_prädikat + " " + mein_objekt

# Funktion baut den Satz
mein_satz = zufall(subjekt, prädikat, objekt)

# Ausgabe
print(mein_satz)
