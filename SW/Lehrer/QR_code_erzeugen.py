# QR Code erzeugen mit der Bibliothek qrcode
# Quelle: How To Generate A QR Code In Python
# https://www.youtube.com/watch?v=AR5aBAOB4QI

# qrcode muss installiert sein: pip install qrcode
# qrcode importieren
import qrcode

# Textzeile definieren
sprichwort = "Übung macht den Meister!"

# Dateiname definieren
dateiname = "mein_QR_code.png"

# Bild mit dem QR code erzeugen
img = qrcode.make(sprichwort)

# Bild in einer Datei speichern
img.save(dateiname)

# Abfrage
print(f"\nDas Bild wurde in der Datei {dateiname} gespeichert")
input("\nFertig?")
