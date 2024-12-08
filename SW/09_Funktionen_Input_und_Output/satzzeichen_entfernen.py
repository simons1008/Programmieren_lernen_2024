# Das Programm soll aus Sätzen die Satzzeichen entfernen

# Originalsätze
original1 = "Wie wird das Wetter?"
original2 = "Wie Programmieren geht, weiß ich."
original3 = "Heute gab es etwas Gutes zu essen!"

# Input der Funktion ist ein Satz
# Output der Funktion ist ein Satz ohne die Satzzeichen ? ! . ,

# Funktion mit Datentyp
def entferne_satzzeichen(original: str) -> str:
    schritt1 = original.replace("?", "")
    schritt2 = schritt1.replace("!", "")
    schritt3 = schritt2.replace(".", "")
    schritt4 = schritt3.replace(",", "")
    return schritt4

# Liste mit den Originalsätzen
originale = [original1, original2, original3]

# Ergebnisse prüfen
for x in originale:
    print(x)
    ohne_satzzeichen = entferne_satzzeichen(x)
    print(ohne_satzzeichen)
