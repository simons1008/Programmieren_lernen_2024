# Dateipfad angeben, Datei lesen und ausgeben
# Der Kommandozeilen-Parameter wählt die Textcodierung

# Modul mit Betriebssystem-Funktion importieren
import os
# Modul mit Zugriff auf den Interpreter importieren
import sys

# Kommandozeilen-Parameter lesen
def parameter_lesen() -> str:
    if len(sys.argv) != 2:
        return("Fehler")
    else:
        return(sys.argv[1])

# Den aktuellen Arbeitsordner ausgeben
print("Der Arbeitsordner ist:", os.getcwd())

# Kommandozeilen-Parameter lesen
parameter = parameter_lesen()

# Textcodierung wählen
if parameter == "ansi":
    ok = True
elif (parameter == "utf-8") or (parameter == "utf_8"):
    ok = True
elif parameter == "Fehler":
    print("Parameter fehlt!")
    ok = False
else:
    print("Parameter unbekannt")
    ok = False

# Datei öffnen, lesen und schließen
if ok:
    with open("../../info.txt", encoding=parameter) as datei:
        mein_text = datei.read()

# Inhalt der Datei ausgeben
if ok:
    print(mein_text)
