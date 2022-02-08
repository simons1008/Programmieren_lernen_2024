# Computer errät die Zahl - GUI Version
# Der Benutzer hilft: Benutzer-Zahl ist größer, kleiner, richtig

# Modul für die GUI-Erstellung importieren
import tkinter as tk

def rate_zahl():
    global obere, untere
    # Steuer-Variable setzen
    x.set((obere + untere)//2)

def zeige_kommentar():
    # Kommentar erzeugen und im Gitter platzieren
    label4 = tk.Label(root,
                      text ="Zahl erraten!          Versuche = " + str(versuche),
                      fg="magenta",
                      font = ("arial", 25))
    label4.grid(row=3, column=0)

def onKeyPress(event):
    global versuche, obere, untere
    # Tasten auswerten
    if event.keysym == "Down":
        versuche += 1
        obere = max(untere, x.get() - 1)
        rate_zahl()
    elif event.keysym == "Up":
        versuche += 1
        untere = min(obere, x.get() + 1)
        rate_zahl()
    elif event.keysym == "equal":
        zeige_kommentar()
    elif event.keysym == "q":
        root.destroy()
    else:
        return

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# untere und obere Grenze der Zahl
untere = 1
obere = 100

# Anzahl der Versuche
versuche = 0

# Bedienungsanleitung-1 erzeugen und im Gitter platzieren
label1 = tk.Label(root,
                       text = "↑ für \"größer\"               ↓ für \"kleiner\"",
                       font = ("arial", 25))
label1.grid(row=0, column=0)

# Steuer-Variable für die geratene Zahl erzeugen
x = tk.IntVar()

# Steuer-Variable initialisieren
rate_zahl()

# Ausgabe der Zahl erzeugen und im Gitter platzieren
label2 = tk.Label(root,
                       textvariable = x,
                       fg="red",
                       font = ("arial", 100))
label2.grid(row=1, column=0)

# Bedienungsanleitung-2 erzeugen und im Gitter platzieren
label3 = tk.Label(root,
                       text ="= bei richtiger Zahl    q zum Beenden",
                       font = ("arial", 25))
label3.grid(row=2, column=0)

# Auf Tastendruck reagieren, wenn Focus im Fenster ist
root.bind("<KeyPress>", onKeyPress)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
