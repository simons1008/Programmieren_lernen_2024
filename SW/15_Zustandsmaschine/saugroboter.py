# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden

# Zustandsautomat zur Steuerung eines Saugroboters
# Taste a bedeutet an_aus
# Taste k bedeutet kollision_erkannt
# Taste g bedeutet genug_gedreht
# Einsatz der Bibliothek statemachine

# Bibliothek für den Zustandsautomaten
from statemachine import *
# Bibliothek für die Timer
from neotimer_win import *
# Bibliothek für Windows-Funktionen
import msvcrt

# Begrüßung
print("Zustandsautomat zur Steuerung eines Saugroboters. Zustandswechsel mit den Tasten a, k und g")
print("Abbruch mit der Taste q")
print()

# Erzeuge das Objekt state_machine
state_machine = StateMachine()

# Vorbelegung des Zeichens von der Tastatur
key_in = ' '

# Timer 500 ms für periodische Ausführung
mytimer_500 = Neotimer(500)

# Funktionen in den Zuständen
# Bis zum Zustandswechsel wird die Funktion wiederholt aufgerufen
# Einmaliger Aufruf durch Abfrage von state_machine.execute_once
# Der Saugroboter ist im Standby
def standby():
    if state_machine.execute_once:
        print("Der Saugroboter ist im Standby")

# Der Saugroboter fährt geradeaus
def geradeaus_fahren():
    if state_machine.execute_once:
        print("Der Saugroboter fährt geradeaus")
    if mytimer_500.repeat_execution():
        print("geradeaus_fahren aufgerufen")

# Der Saugroboter dreht
def drehen():
    if state_machine.execute_once:
        print("Der Saugroboter dreht")

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

def an_aus():
    return taste_gedrueckt('a')

def kollision_erkannt():
    return taste_gedrueckt('k')

def genug_gedreht():
    return taste_gedrueckt('g')

# Zustände definieren
# Initial ist der erste Zustand
STANDBY = state_machine.add_state(standby)
GERADEAUS_FAHREN = state_machine.add_state(geradeaus_fahren)
DREHEN = state_machine.add_state(drehen)

# Zustandsübergänge hinzufügen
STANDBY.attach_transition(an_aus, GERADEAUS_FAHREN)
GERADEAUS_FAHREN.attach_transition(kollision_erkannt, DREHEN)
DREHEN.attach_transition(genug_gedreht, GERADEAUS_FAHREN)
DREHEN.attach_transition(an_aus, STANDBY)
GERADEAUS_FAHREN.attach_transition(an_aus, STANDBY)

# Loop
while True:
    state_machine.run()
    # key_in wird in der Funktion taste_gedrueckt() gesetzt 
    # Abbruch mit der Taste q
    if key_in == 'q':
        break   

