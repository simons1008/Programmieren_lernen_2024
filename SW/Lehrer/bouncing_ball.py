# Einführung in pygame
# Quelle: https://www.pygame.org/docs/tut/PygameIntro.html
# Geändert: "Frames per second" begrenzt
#           ballrect.move() ersetzt durch ballrect.move_ip() 
#           pygame.display.flip() ersetzt durch pygame.display.update()
#           Programm kommentiert

# Bibliotheken importieren
import sys, pygame
# alle Module initialisieren
pygame.init()

# Frames per second festlegen
FPS = 60
# Clock objekt erzeugen
FramesPerSec = pygame.time.Clock()

# Breite und Höhe des Fensters festlegen
width, height = 640, 480
size = width, height
# Geschwindigkeit nach rechts und nach unten festlegen
speed = [2, 2]
# Farbe definieren
BLACK = 0, 0, 0

# Grafik-Fenster erzeugen
screen = pygame.display.set_mode(size)

# Bild laden
ball = pygame.image.load("intro_ball.gif")
# Rechteck in der Größe des Bildes erzeugen
ballrect = ball.get_rect()

# Game Loop
while True:
    # Ereignisse prüfen    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame Fenster schließen
            pygame.quit()
            # Python Skript beenden
            sys.exit()

    # ballrect Variable mit speed bewegen
    ballrect.move_ip(speed)
    # wenn ballrect links oder rechts aus dem Fenster läuft
    if ballrect.left < 0 or ballrect.right > width:
        # speed in die Gegenrichtung
        speed[0] = -speed[0]
    # wenn ballrect links oder rechts aus dem Fenster läuft
    if ballrect.top < 0 or ballrect.bottom > height:
        # speed in die Gegenrichtung       
        speed[1] = -speed[1]

    # Grafik-Fenster auswischen
    screen.fill(BLACK)
    # Blocktransfer source = ball, destination = ballrect
    screen.blit(ball, ballrect)
    # Grafik-Fenster aktualisieren
    pygame.display.update()
    # Frames per second begrenzen
    FramesPerSec.tick(FPS)

