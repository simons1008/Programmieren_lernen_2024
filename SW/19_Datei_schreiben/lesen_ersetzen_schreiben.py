# Datei lesen - einen Text ersetzen - Datei schreiben
# Der Kommandozeilen-Parameter wählt die Textcodierung

# Modul mit Zugriff auf den Interpreter importieren
import sys

# Kommandozeilen-Parameter lesen
def parameter_lesen() -> str:
    if len(sys.argv) != 2:
        return("Fehler")
    else:
        return(sys.argv[1])

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
    with open("bericht1.txt", mode="r", encoding=parameter) as datei:
        der_ganze_text = datei.read()

# Inhalt der Datei ausgeben
if ok:
    print(der_ganze_text)

# Text ersetzen
if ok:
    der_ganze_text = der_ganze_text.replace("Luftschiffe", "Zeppeline")

# Inhalt der Datei ausgeben
if ok:
    print(der_ganze_text)

# Datei öffnen, schreiben und schließen
if ok:
    with open("bericht2.txt", mode="w", encoding=parameter) as datei:
        datei.write(der_ganze_text)

