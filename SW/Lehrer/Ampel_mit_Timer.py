# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden

# Zustandsautomat zur Steuerung einer Ampel
# Timer schaltet ein Mal GELB_BLINKEN - ROT
# Danach - ROT_GELB - GRUEN - GELB - ROT - ROT_GELB - GRUEN usw. 
# Einsatz der Bibliothek statemachine

# Bibliothek für den Zustandsautomaten
from statemachine import *
# Bibliothek für die Timer
from neotimer_win import *

# Begrüßung
print("Zustandsautomat zur Steuerung einer Ampel. Zustandswechsel über Timer")
print("Ende nach 50 Sekunden")
print()

# Erzeuge das Objekt state_machine
state_machine = StateMachine()

# Timer 500 ms für die wiederholte print-Ausgabe
myTimer_500 = Neotimer(500)

# Timer 1000 ms, 2000 ms, 5000 ms, 10000 ms für periodische Ausführung
myTimer_1000 = Neotimer(1000)
myTimer_2000 = Neotimer(2000)
myTimer_5000 = Neotimer(5000)
myTimer_10000 = Neotimer(10000)

# Timer 50000 ms zum Beenden des Programms
myTimer_50000 = Neotimer(50000)
myTimer_50000.start()


# Funktionen in den Zuständen
# Bis zum Zustandswechsel wird die Funktion wiederholt aufgerufen
# Einmaliger Aufruf durch Abfrage von state_machine.execute_once
# Ampel blinkt gelb
def gelb_blinken():
    if state_machine.execute_once:
        print("Die Ampel blinkt gelb")
    if myTimer_500.repeat_execution():
        print("gelb_blinken() aufgerufen")

# Die Ampel ist rot
def rot():
    if state_machine.execute_once:
        print("Die Ampel ist rot")

# Die Ampel ist rot/gelb
def rot_gelb():
    if state_machine.execute_once:
        print("Die Ampel ist rot/gelb")

# Die Ampel ist grün
def gruen():
    if state_machine.execute_once:
        print("Die Ampel ist grün")

# Die Ampel ist gelb
def gelb():
    global ende
    if state_machine.execute_once:
        print("Die Ampel ist gelb")
        ende = True
   
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

# Loop
while True:
    state_machine.run()
    if myTimer_50000.finished():
        input("Program ausgeführt. Weiter?")
        break
    
