# Computer errät die Zahl - GUI Version
# Der Benutzer hilft: Benutzer-Zahl ist größer, kleiner, richtig

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Definiere die Klasse GuiStart
class GuiStart:
    # Initialisierung
    def __init__(self):
        # Konstruktor für das Fenster aufrufen
        self.root = tk.Tk()

        # untere und obere Grenze der Zahl
        self.untere = 1
        self.obere = 100

        # Anzahl der Versuche
        self.versuche = 0
        
        # Bedienungsanleitung-1 erzeugen und im Gitter platzieren
        self.label1 = tk.Label(self.root,
                               text = "↑ für \"größer\"               ↓ für \"kleiner\"",
                               font = ("arial", 25))
        self.label1.grid(row=0, column=0)

        # Steuer-Variable für die geratene Zahl erzeugen
        self.x = tk.IntVar()

        # Steuer-Variable initialisieren
        self.rate_zahl()
        
        # Ausgabe der Zahl erzeugen und im Gitter platzieren
        self.label2 = tk.Label(self.root,
                               textvariable = self.x,
                               fg="red",
                               font = ("arial", 100))
        self.label2.grid(row=1, column=0)
        
        # Bedienungsanleitung-2 erzeugen und im Gitter platzieren
        self.label3 = tk.Label(self.root,
                               text ="= bei richtiger Zahl    q zum Beenden",
                               font = ("arial", 25))
        self.label3.grid(row=2, column=0)

        # Auf Tastendruck reagieren, wenn Focus im Fenster ist
        self.root.bind("<KeyPress>", self.onKeyPress)

        # Hauptschleife, damit die GUI angezeigt wird
        self.root.mainloop()

    def rate_zahl(self):
        # Steuer-Variable setzen
        self.x.set((self.obere + self.untere)//2)

    def zeige_kommentar(self):
        # Kommentar erzeugen und im Gitter platzieren
        self.label4 = tk.Label(self.root,
            text ="Zahl erraten!          Versuche = " + str(self.versuche),
            fg="magenta",
            font = ("arial", 25))
        self.label4.grid(row=3, column=0)

    def onKeyPress(self, event):
        # Tasten auswerten
        if event.keysym == "Down":
            self.versuche += 1
            self.obere = max(self.untere, self.x.get() - 1)
            self.rate_zahl()
        elif event.keysym == "Up":
            self.versuche += 1
            self.untere = min(self.obere, self.x.get() + 1)
            self.rate_zahl()
        elif event.keysym == "equal":
            self.zeige_kommentar()
        elif event.keysym == "q":
            self.root.destroy()
        else:
            return

# GuiStart aufrufen
GuiStart()
