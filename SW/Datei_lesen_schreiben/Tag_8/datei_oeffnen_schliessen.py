# Datei (ANSI Codierung) lesen und ausgeben

# Modul mit Betriebssystem-Funktion importieren
import os

# Den aktuellen Arbeitsordner ausgeben
print("Der Arbeitsordner ist:", os.getcwd())

# Version mit open() und close()
# Datei öffnen
datei = open("textdatei.txt")
# Datei lesen
mein_text = datei.read()
# Nicht vergessen: Datei schließen!
datei.close()

# Inhalt der Datei ausgeben
print(mein_text)

# Version mit dem Befehl with. Dadurch wird die Datei automatisch geschlossen. 
# Datei öffnen, lesen und schließen
with open("textdatei.txt") as datei:
    mein_text = datei.read()

# Inhalt der Datei ausgeben
print(mein_text)
