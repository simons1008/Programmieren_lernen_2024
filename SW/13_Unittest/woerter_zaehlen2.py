# Das Programm soll die Wörter in einem Satz zählen
# Version 2 entfernt alle Satzzeichen vor dem Zählen

# Modul´"Regular expression operations" importieren
import re

# Originalsätze
original1 = "Wie wird das Wetter?"
original2 = "Wie Programmieren geht, weiß ich."
original3 = "Heute gab es etwas Gutes zu essen!"
original4 = "Wie wird das Wetter ?"
original5 = "Wie Programmieren geht , weiß ich ."
original6 = "Heute gab es etwas Gutes zu essen !"

# Input der Funktion ist ein Satz
# Output der Funktion ist die Anzahl der Wörter im Satz
# Funktion mit Datentyp
def zaehle_woerter2(original: str) -> str:
    # Entferne alle Zeichen, die keine Buchstaben (\w) 
    # oder Leerzeichen (\s) sind
    ohne_satzzeichen = re.sub(r'[^\w\s]', '', original)
    liste = ohne_satzzeichen.split()
    anzahl = len(liste)
    return anzahl

# Liste mit den Originalsätzen
originale = [original1, original2, original3, 
             original4, original5, original6]

# Ergebnisse prüfen
for x in originale:
    print(x)
    anzahl = zaehle_woerter2(x)
    print(anzahl, "Wörter")
