# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden.

# Bibliothek für den Zustandsautomaten
from statemachine import *
# Bibliothek für den Timer
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

# Timer initialisieren
mytimer = Neotimer(500)

# Funktionen in den Zuständen
def state1_logic():
    if state_machine.execute_once:
        print("Automat im Zustand 1")
    if mytimer.repeat_execution():
        print("bei der Arbeit")

def state2_logic():
    if state_machine.execute_once:
        print("Automat im Zustand 2")

# Zustände definieren
state1 = state_machine.add_state(state1_logic)
state2 = state_machine.add_state(state2_logic)

# Funktionen für Zustandsübergänge
def taste_gedrueckt(zeichen):
    global key_in
    # Taste gedrückt?
    if msvcrt.kbhit():
        # Ja: Zeichen einlesen
        key_in = msvcrt.getwch()
    # Taste für den Zustandsübergang?
    if key_in == zeichen:
        return True
    else:
        return False

def taste1_gedrueckt():
    return taste_gedrueckt('1')

def taste2_gedrueckt():
    return taste_gedrueckt('2')
    
# Zustandsübergänge definieren
state1.attach_transition(taste2_gedrueckt, state2)
state2.attach_transition(taste1_gedrueckt, state1)

# Main loop
while True:
    state_machine.run()
    # Abbruch mit der Taste q
    if key_in == 'q':
        break



   
