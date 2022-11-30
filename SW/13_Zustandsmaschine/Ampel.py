# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden

# Zustandsautomat zur Steuerung einer Ampel
# Taste1 schaltet GRUEN - GELB - ROT - ROT/GELB - GRUEN
# Taste2 schaltet die Ampel dunkel
# Einsatz der Bibliothek statemachine
# Für die Aktionen der Tasten: Zeilen 101 bis 104 auskommentieren

# Bibliothek für den Zustandsautomaten
from statemachine import *
# Bibliothek für die Timer
from neotimer_win import *
# Bibliothek für Windows-Funktionen
import msvcrt

# Begrüßung
print("Zustandsautomat mit zwei Zuständen. Zustandswechsel mit den Tasten 1 und 2")
print("Abbruch mit der Taste q")
print()

# Erzeuge das Objekt state_machine
state_machine = StateMachine()

# Vorbelegung des Zeichens von der Tastatur
key_in = ' '

# Timer 500 ms, 1000 ms, 2000 ms, 5000 ms für periodische Ausführung
mytimer_500 = Neotimer(500)
myTimer_1000 = Neotimer(1000)
myTimer_2000 = Neotimer(2000)
myTimer_5000 = Neotimer(5000)

# Funktionen in den Zuständen
# Bis zum Zustandswechsel wird die Funktion wiederholt aufgerufen
# Einmaliger Aufruf durch Abfrage von state_machine.execute_once
# Die Ampel ist grün
# Ampel ist dunkel
def keine():
    if state_machine.execute_once:
        print("Die Ampel ist dunkel")

# Die Ampel ist rot
def rot():
    if state_machine.execute_once:
        print("Die Ampel ist rot")

# Die Ampel ist rot/gelb
def rot_gelb():
    if state_machine.execute_once:
        print("Die Ampel ist rot/gelb")

def gruen():
    if state_machine.execute_once:
        print("Die Ampel ist grün")
    if mytimer_500.repeat_execution():
        print("gruen() aufgerufen")

# Die Ampel ist gelb
def gelb():
    if state_machine.execute_once:
        print("Die Ampel ist gelb")

# Tasten einlesen
def taste_gedrueckt(zeichen):
    global key_in
    # Taste gedrückt?
    if msvcrt.kbhit():
        # Ja: Zeichen einlesen
        key_in = msvcrt.getwch()
    # Taste für den Zustandsübergang?
    if key_in == zeichen:
        # globale Variable zurücksetzen
        key_in = ' '
        return True
    else:
        return False

def taste1_gedrueckt():
    return taste_gedrueckt('1')

def taste2_gedrueckt():
    return taste_gedrueckt('2')
    
# Zustände definieren
# Initial ist der erste Zustand
KEINE = state_machine.add_state(keine)
ROT = state_machine.add_state(rot)
ROT_GELB = state_machine.add_state(rot_gelb)
GRUEN = state_machine.add_state(gruen)
GELB = state_machine.add_state(gelb)

# Zustandsübergänge hinzufügen
# Normale Übergänge
ROT.attach_transition(taste1_gedrueckt, ROT_GELB)
ROT_GELB.attach_transition(taste1_gedrueckt, GRUEN)
GRUEN.attach_transition(taste1_gedrueckt, GELB)
GELB.attach_transition(taste1_gedrueckt, ROT)

# Übergänge durch Timer
##ROT.attach_transition(myTimer_5000.repeat_execution, ROT_GELB)
##ROT_GELB.attach_transition(myTimer_1000.repeat_execution, GRUEN)
##GRUEN.attach_transition(myTimer_2000.repeat_execution, GELB) 
##GELB.attach_transition(myTimer_1000.repeat_execution, ROT)

# Übergänge nach KEINE
ROT.attach_transition(taste2_gedrueckt, KEINE)
ROT_GELB.attach_transition(taste2_gedrueckt, KEINE)
GRUEN.attach_transition(taste2_gedrueckt, KEINE)
GELB.attach_transition(taste2_gedrueckt, KEINE)

# Übergang von KEINE
KEINE.attach_transition(taste1_gedrueckt, ROT)

# Loop
while True:
    state_machine.run()
    # Abbruch mit der Taste q
    if key_in == 'q':
        break   
