# Umrechnung von Grad Celsius in Grad Fahrenheit

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()
root.title("Umrechnung Celsius in Fahrenheit")

# Funktion zur Umrechnung von Celsius in Fahrenheit
def celsius_in_fahrenheit(event):
    # Eingabefeld auslesen und in Integer umwandeln
    celsius = int(eingabefeld_wert.get())
    # Umrechnen
    fahrenheit = celsius * 9/5 + 32
    # Steuervariable setzen
    ausgabefeld_wert.set(fahrenheit)

# Steuervariable für das Eingabefeld erzeugen
eingabefeld_wert=tk.StringVar()

# Eingabefeld erzeugen und in GUI Elemente einbetten
eingabefeld = tk.Entry(root, textvariable=eingabefeld_wert, font = ("arial", 25))
eingabefeld.pack()

# Taste "Return" ruft die Funktion celsius_in_fahrenheit auf
eingabefeld.bind('<Key-Return>', celsius_in_fahrenheit)

# Steuervariable für das Ausgabefeld erzeugen und initialisieren
ausgabefeld_wert = tk.StringVar()
ausgabefeld_wert.set("      ")

# Ausgabefeld erzeugen und in GUI Elemente einbetten
ausgabefeld = tk.Label(root, textvariable=ausgabefeld_wert, bg="yellow", font = ("arial", 25))
ausgabefeld.pack()

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
