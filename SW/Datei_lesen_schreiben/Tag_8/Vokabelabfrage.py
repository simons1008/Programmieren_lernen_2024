# Vokabelabfrage:
# - Der Computer liest die Vokabelliste von einer Datei im CSV UTF-8 Format
#   (Diese Datei kann mit EXCEL erstellt werden)      
# - Die Vokabelliste wird in eine zufällige Reihenfolge gebracht
# - Danach gibt der Computer die erste deutsche Bedeutung aus
#   (Ausgabe in einem Fenster)
# - Danach wird das Programm über Schaltflächen im Fenster gesteuert
#       Schaltfläche "Lösung":
#           Der Computer gibt die englische Bedeutung aus
#       Schaltfläche "Weiter": 
#           Der Computer gibt die nächste deutsche Bedeutung aus
#           Der Computer löscht die englische Bedeutung

# Modul für die CSV-Datei importieren
import csv
# Modul für den schönen Ausdruck importieren
import pprint
# Modul für das GUI importieren
import tkinter as tk
# Modul für den Zufall importieren
import random

# Funktion für Schaltfläche "Lösung"
def aktionLoesung():
    # englische Bedeutung ausgeben
    englisch.set(meine_liste[zaehler][0])

# Funktion für Schaltfläche "Weiter"
def aktionWeiter():
    global zaehler
    # die nächste deutsche Bedeutung ausgeben
    zaehler +=1
    if zaehler >= len(meine_liste):
        zaehler = 0
    deutsch.set(meine_liste[zaehler][1])
    # die englische Bedeutung löschen
    englisch.set("")

# Vokabelliste initialisieren
meine_liste = []

# CSV-Datei öffnen, lesen, schließen
with open("idioms.csv", encoding="utf-8") as csvdatei:
    csv_reader_object = csv.reader(csvdatei, delimiter=";")
    # Jede Zeile in die Liste schreiben
    for row in csv_reader_object:
        meine_liste.append(row)

# Ausgabe (zur Kontrolle)
pprint.pprint(meine_liste)
# Zufällige Reihenfolge der Zeilen
random.shuffle(meine_liste)
# Ausgabe (zur Kontrolle)
pprint.pprint(meine_liste)

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Fenstertitel und Fenstergröße setzen
root.title("Vokabelabfrage")
root.geometry("600x250")

# Zähler für die Zeilen der Liste
zaehler = 0

# Steuervariable erzeugen
deutsch = tk.StringVar()
# die erste deutsche Bedeutung setzen
deutsch.set(meine_liste[zaehler][1])
# Steuervariable erzeugen
englisch = tk.StringVar()
# die englische Bedeutung löschen
englisch.set("")                    

# Textausgabe erzeugen und in GUI einbetten
label1 = tk.Label(root, textvariable=deutsch, fg="blue", font=("arial", 25))
label1.pack()
# Textausgabe erzeugen und in GUI einbetten
label2 = tk.Label(root, textvariable=englisch, fg="green", font=("arial", 25))
label2.pack()

# Schaltfläche erzeugen und in GUI einbetten
loesung = tk.Button(root, text="Lösung", bg="lightgreen", font=("arial", 25), command=aktionLoesung)
loesung.pack()
# Schaltfläche erzeugen und in GUI einbetten
weiter = tk.Button(root, text="Weiter", bg="lightblue", font=("arial", 25), command=aktionWeiter)
weiter.pack()

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
