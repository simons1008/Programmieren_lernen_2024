# QR Code dekodieren mit opencv-python
# Quelle: How To Decode A QR Code In Python
# https://www.youtube.com/watch?v=2w7jUVv6A74 

# opencv-python muss installiert sein: pip install opencv-python
# cv Bibliothek importieren
import cv2

# Objekt erstellen
detector =cv2.QRCodeDetector()

# Bild importieren
img = cv2.imread("Willkommen_bei_Wikipedia.png")

# Bild anzeigen
cv2.imshow("QR Code", img)
# auf einen Tastendruck warten, damit die GUI ihre Aufgaben erledigen kann
cv2.waitKey(0)
# Fenster schließen
cv2.destroyAllWindows()

# QRCodeDetector hat Methoden geerbt von GraphicalCodeDetector 
# https://docs.opencv.org/4.9.0/d7/d90/classcv_1_1GraphicalCodeDetector.html
# mit der Methode detectAndDecode den QR Code dekodieren
qr_text, points, straight_code = detector.detectAndDecode(img)
print("QR Text:")
print("========")
print(qr_text)

# Abfrage
input("\nFertig?")
 
