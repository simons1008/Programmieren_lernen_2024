# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden.

# Bibliothek für den Zustandsautomaten
from statemachine import *
# Bibliothek für den Timer
from neotimer_win import *
# Bibliothek für Windows-Funktionen
import msvcrt

# Begrüßung
print("Zustandsautomat mit drei Zuständen. Zustandswechsel mit den Tasten 1, 2 und 3")
print("Abbruch mit der Taste q")
print()

# Erzeuge das Objekt state_machine
state_machine = StateMachine()

# Vorbelegung des Zeichens von der Tastatur
key_in = ' '

# Timer initialisieren
mytimer1 = Neotimer(500)
mytimer2 = Neotimer(1000)

# Funktionen in den Zuständen
def state1():
    if state_machine.execute_once:
        print("Automat im Zustand 1")
    if mytimer1.repeat_execution():
        print("bei der Arbeit")

def state2():
    if state_machine.execute_once:
        print("Automat im Zustand 2")
    if mytimer2.repeat_execution():
        print("arbeite langsamer")

def state3():
    if state_machine.execute_once:
        print("Automat im Zustand 3")
        print("Automat ruht")   

# Funktionen für Zustandsübergänge
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
    
def taste3_gedrueckt():
    return taste_gedrueckt('3')

# Zustände definieren
STATE1 = state_machine.add_state(state1)
STATE2 = state_machine.add_state(state2)
STATE3 = state_machine.add_state(state3)

# Zustandsübergänge definieren
STATE1.attach_transition(taste2_gedrueckt, STATE2)
STATE2.attach_transition(taste3_gedrueckt, STATE3)
STATE3.attach_transition(taste1_gedrueckt, STATE1)

# Main loop
while True:
    state_machine.run()
    # Abbruch mit der Taste q
    if key_in == 'q':
        break
