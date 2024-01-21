# Umrechnung von Grad Celsius in Grad Kelvin

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()
root.title("Umrechnung Celsius in Kelvin")

# Funktion zur Umrechnung von Celsius in Kelvin
def celsius_in_kelvin(event):
    # Eingabefeld auslesen und in Integer umwandeln
    celsius = int(eingabefeld_wert.get())
    # Umrechnen
    kelvin = celsius + 273
    # Steuervariable setzen
    ausgabefeld_wert.set(kelvin)

# Steuervariable für das Eingabefeld erzeugen
eingabefeld_wert=tk.StringVar()

# Eingabefeld erzeugen und in GUI Elemente einbetten
eingabefeld = tk.Entry(root, textvariable=eingabefeld_wert, font = ("arial", 25))
eingabefeld.pack()

# Taste "Return" ruft die Funktion celsius_in_kelvin auf
eingabefeld.bind('<Key-Return>', celsius_in_kelvin)

# Steuervariable für das Ausgabefeld erzeugen und initialisieren
ausgabefeld_wert = tk.StringVar()
ausgabefeld_wert.set("      ")

# Ausgabefeld erzeugen und in GUI Elemente einbetten
ausgabefeld = tk.Label(root, textvariable=ausgabefeld_wert, bg="yellow", font = ("arial", 25))
ausgabefeld.pack()

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
