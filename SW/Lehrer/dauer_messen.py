# Programm misst, wie lange der Druck eines langen Texts dauert

import time

# Funktion nimmt einen Zeitstempel
def ticks_us():
    return int(time.perf_counter_ns()/1000.0)

# Funktion berechnet die Differenz zwischen zwei Zeitstempeln    
def ticks_diff(ticks1, ticks2):
    return ticks2 - ticks1

# Zeit nehmen
ticks1 = ticks_us()

# einen langen Text drucken
print(1000 * "*")

# Zeit nehmen
ticks2 = ticks_us()

# Dauer anzeigen
print("Der Druck dauerte", ticks_diff(ticks1, ticks2), "Mikrosekunden")
