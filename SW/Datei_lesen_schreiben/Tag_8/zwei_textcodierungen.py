# Datei lesen und ausgeben
# Der Kommandozeilen-Parameter wählt Textcodierung und Dateiname

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

# Textcodierung und Dateiname wählen
if parameter == "ansi":
    name = "textdatei.txt"
    ok = True
elif (parameter == "utf-8") or (parameter == "utf_8"):
    name = "textdatei_utf_8.txt"
    ok = True
elif parameter == "Fehler":
    print("Parameter fehlt!")
    ok = False
else:
    print("Parameter unbekannt")
    ok = False

# Datei öffnen, lesen und schließen
if ok:
    print(name)
    with open(name, encoding=sys.argv[1]) as datei:
        mein_text = datei.read()

# Inhalt der Datei ausgeben
if ok:
    print(mein_text)
