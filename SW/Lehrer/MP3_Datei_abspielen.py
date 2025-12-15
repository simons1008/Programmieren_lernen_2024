# MP3 Datei abspielen
# Zuerst pygame installieren
# - Eingabeaufforderung öffnen und dort eingeben:
# - pip install -U pygame

# time Bibliothek importieren
import time
# Mixer Bibliothek importieren
from pygame import mixer

# Mixer verwenden
mixer.init()
mixer.music.load('Buntspecht_Klopfen_NABU_Lars_Lachmann.mp3')
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
