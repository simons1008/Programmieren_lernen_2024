# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden

# Zustandsautomat zur Steuerung einer Ampel
# Taste1 schaltet GELB_BLINKEN - ROT - ROT_GELB - GRUEN - GELB - ROT
# Taste2 schaltet die Ampel auf GELB_BLINKEN

# Time-Bibliothek
import time

# Bibliothek für Windows-Funktionen
import msvcrt

# Begrüßung
print("Zustandsautomat zur Steuerung einer Ampel. Zustandswechsel mit den Tasten 1 und 2")
print("Abbruch mit der Taste q")
print()

# Vorbelegung des Zeichens von der Tastatur
key_in = ' '

# Funktionen in den Zuständen
# Bis zum Zustandswechsel wird die Funktion 1x aufgerufen
# Ampel blinkt gelb
def gelb_blinken():
    if wechsel:
        print("Die Ampel blinkt gelb")
    print("gelb_blinken() aufgerufen")
    time.sleep(0.5)

# Die Ampel ist rot
def rot():
    if wechsel:
        print("Die Ampel ist rot")

# Die Ampel ist rot/gelb
def rot_gelb():
    if wechsel: 
        print("Die Ampel ist rot/gelb")

# Die Ampel ist grün
def gruen():
    if wechsel: 
        print("Die Ampel ist grün")

# Die Ampel ist gelb
def gelb():
    if wechsel:
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
   
# Initialisierung
zustand = 'GELB_BLINKEN'
wechsel = True

# Loop
while True:
    if zustand == 'GELB_BLINKEN':
        gelb_blinken()
        wechsel = False
        if taste_gedrueckt('1'):
            zustand = 'ROT'
            wechsel = True
    elif zustand == 'ROT':
        rot()
        wechsel = False
        if taste_gedrueckt('1'):
            zustand = 'ROT_GELB'
            wechsel = True
    elif zustand == 'ROT_GELB':
        rot_gelb()
        wechsel = False
        if taste_gedrueckt('1'):
            zustand = 'GRUEN'
            wechsel = True
    elif zustand == 'GRUEN':
        gruen()
        wechsel = False
        if taste_gedrueckt('1'):        
            zustand = 'GELB'
            wechsel = True
    elif zustand == 'GELB':
        gelb()
        wechsel = False
        if taste_gedrueckt('1'):        
            zustand = 'ROT'
            wechsel = True
    else:
        print("Fehler im Programm")
    if taste_gedrueckt('2'):
        zustand = 'GELB_BLINKEN'
        wechsel = True
    if taste_gedrueckt('q'):
        break
