# Satzzeichen entfernen

# Originalsätze
original1 = "Wie wird das Wetter?"
original2 = "Wie Programmieren geht, weiß ich."
original3 = "Heute gab es etwas Gutes zu essen!"

# Funktion entfernt die Satzzeichen ? ! . ,
def vereinfache(original: str) -> str:
    vereinfachung1 = original.replace("?", "")
    vereinfachung2 = vereinfachung1.replace("!", "")
    vereinfachung3 = vereinfachung2.replace(".", "")
    vereinfachung4 = vereinfachung3.replace(",", "")
    return vereinfachung4

# Liste mit den Originalsätzen
originale = [original1, original2, original3]

# alle Sätze vereinfachen
for x in originale:
    print(x)
    vereinfachung = vereinfache(x)
    print(vereinfachung)
