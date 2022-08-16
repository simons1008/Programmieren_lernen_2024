# WICHTIG: In IDLE gibt es einen Konflikt zwischen .mainloop() und .kbhit().
# Deshalb muss das Programm von der Eingabeaufforderung aus gestartet werden.

# Diese Bibliothek gibt Zugriff auf nützliche Funktionen auf Windows-Plattformen
import msvcrt

# Begrüßung
print("Drücke eine Taste, Ende mit der Taste q")

# Zeichen initialisieren
key_in = '.'

# Loop
while True:
   # Taste gedrückt?
   if msvcrt.kbhit():
      # Ja: Zeichen lesen und drucken
      key_in = msvcrt.getwch()
      print("kbhit! " + key_in)
   # Ende mit der Taste q
   if key_in == 'q':
      break; 
