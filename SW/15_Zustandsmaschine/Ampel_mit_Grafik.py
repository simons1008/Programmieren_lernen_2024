# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden

# Zustandsautomat zur Steuerung einer Ampel
# Taste1 schaltet GELB_BLINKEN - ROT - ROT_GELB - GRUEN - GELB - ROT
# Taste2 schaltet die Ampel auf GELB_BLINKEN
# Einsatz der Bibliothek statemachine
# Für die periodische Ausführung: Zeilen 32 bis 34 und 104 bis 108 aktivieren

# Bibliothek für den Zustandsautomaten
from statemachine import *
# Bibliothek für die Timer
from neotimer_win import *
# Bibliothek für Windows-Funktionen
import msvcrt

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()
root.geometry("120x240")

# Bildausgabe erzeugen
bild_schwarz = tk.PhotoImage(file="schwarz.png")
label_schwarz_oben = tk.Label(root, image = bild_schwarz)
label_schwarz_mitte = tk.Label(root, image = bild_schwarz)
label_schwarz_unten = tk.Label(root, image = bild_schwarz)
bild_gelb = tk.PhotoImage(file="gelb.png")
label_gelb = tk.Label(root, image = bild_gelb)
bild_rot = tk.PhotoImage(file="rot.png")
label_rot = tk.Label(root, image = bild_rot)
bild_gruen = tk.PhotoImage(file="gruen.png")
label_gruen = tk.Label(root, image = bild_gruen)

# Alle Label in GUI Elemente einbetten
label_schwarz_oben.grid(row=0, column=0, padx=20) # padx zur Zentrierung 
label_schwarz_mitte.grid(row=1, column=0, padx=20)
label_schwarz_unten.grid(row=2, column=0, padx=20)
label_rot.grid(row=0, column=0, padx=20) 
label_gelb.grid(row=1, column=0, padx=20)
label_gruen.grid(row=2, column=0, padx=20)

# Funktion macht alle Label unsichtbar 
# Die Label erinnern sich an ihre Position im Fenster 
def label_unsichtbar_machen():
    label_schwarz_oben.grid_remove() 
    label_schwarz_mitte.grid_remove()
    label_schwarz_unten.grid_remove()
    label_rot.grid_remove()
    label_gelb.grid_remove()
    label_gruen.grid_remove()

# Erzeuge das Objekt state_machine
state_machine = StateMachine()

# Timer 500 ms zum Blinkek
myTimer_500 = Neotimer(500)

# Timer 1000 ms, 2000 ms, 5000 ms, 10000 ms für periodische Ausführung
myTimer_1000 = Neotimer(1000)
myTimer_2000 = Neotimer(2000)
myTimer_5000 = Neotimer(5000)
myTimer_10000 = Neotimer(10000)

# globale Variable
eingeschaltet = False

# Funktion aufrufen
label_unsichtbar_machen()

# Funktionen in den Zuständen
# Bis zum Zustandswechsel wird die Funktion wiederholt aufgerufen
# Einmaliger Aufruf durch Abfrage von state_machine.execute_once
# Ampel blinkt gelb
def gelb_blinken():
    global eingeschaltet
    if state_machine.execute_once:
        print("Die Ampel blinkt gelb")
    if myTimer_500.repeat_execution():
        label_unsichtbar_machen()
        if eingeschaltet == False:
            label_schwarz_oben.grid()
            label_gelb.grid()
            label_schwarz_unten.grid()
        else:
            label_schwarz_oben.grid()
            label_schwarz_mitte.grid()
            label_schwarz_unten.grid()
        eingeschaltet = not eingeschaltet

# Die Ampel ist rot
def rot():
    if state_machine.execute_once:
        print("Die Ampel ist rot")
        label_unsichtbar_machen()
        label_rot.grid()
        label_schwarz_mitte.grid()
        label_schwarz_unten.grid()

# Die Ampel ist rot/gelb
def rot_gelb():
    if state_machine.execute_once:
        print("Die Ampel ist rot/gelb")
        label_unsichtbar_machen()
        label_rot.grid()
        label_gelb.grid()
        label_schwarz_unten.grid()

# Die Ampel ist grün
def gruen():
    if state_machine.execute_once:
        print("Die Ampel ist grün")
        label_unsichtbar_machen()
        label_schwarz_oben.grid()
        label_schwarz_mitte.grid()
        label_gruen.grid()

# Die Ampel ist gelb
def gelb():
    if state_machine.execute_once:
        print("Die Ampel ist gelb")
        label_unsichtbar_machen()
        label_schwarz_oben.grid()
        label_gelb.grid()
        label_schwarz_unten.grid()

# Funktion ruft state_machine.run() alle 100 ms auf
def state_machine_loop():
    state_machine.run()
    root.after(100, state_machine_loop)

# Zustände definieren
# Initial ist der erste Zustand
GELB_BLINKEN = state_machine.add_state(gelb_blinken)
ROT = state_machine.add_state(rot)
ROT_GELB = state_machine.add_state(rot_gelb)
GRUEN = state_machine.add_state(gruen)
GELB = state_machine.add_state(gelb)

# Zustandsübergänge hinzufügen
# Übergänge durch Timer
GELB_BLINKEN.attach_transition(myTimer_10000.repeat_execution, ROT)
ROT.attach_transition(myTimer_5000.repeat_execution, ROT_GELB)
ROT_GELB.attach_transition(myTimer_1000.repeat_execution, GRUEN)
GRUEN.attach_transition(myTimer_2000.repeat_execution, GELB) 
GELB.attach_transition(myTimer_1000.repeat_execution, ROT)

# state_machine_loop zum ersten Mal aufrufen
state_machine_loop()

# Hauptschleife, zur GUI Anzeige und Event-Verarbeitung 
root.mainloop()

