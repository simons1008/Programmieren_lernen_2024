# move_player - Bewege den Spieler
# Auszug aus pygame.examples.moveit

# Bibliotheken importieren
import os
import pygame as pg

# Aktuellen Ordner bestimmen
main_dir = os.path.split(os.path.abspath(__file__))[0]

# Höhe und Breite des Fensters
WIDTH = 640
HEIGHT = 480
# Höhe und Breite der animierten Figur (sprite)
SPRITE_WIDTH = 80
SPRITE_HEIGHT = 60

# Klasse für den Spieler 
class GameObject:
    # Initialisierung
    def __init__(self, image, height, speed):
        # Geschwindigkeit der Bewegung
        self.speed = speed                     
        # Bild des Objekts
        self.image = image
        # zu Beginn steht das Objekt hier
        self.pos = image.get_rect().move(0, height)

    # bewege das Objekt 
    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed

        # steuert das Objekt so, dass es das Fenster nicht verlassen kann
        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.top > HEIGHT - SPRITE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < SPRITE_WIDTH:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.top = HEIGHT - SPRITE_HEIGHT

# Funktion zum Laden des Bildes
def load_image(name):
    # Datei-Pfad erstellen
    path = os.path.join(main_dir, "data", name)
    # Bild laden und Pixel Format ändern
    return pg.image.load(path).convert_alpha()

# Hauptprogramm
def main():
    # initialisiere das Programm
    pg.init()
    # Objekt zur Zeiterfassung 
    clock = pg.time.Clock()
    # erstelle das Fenster
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    # lade das Spieler-Bild
    player = load_image("player1.gif")
    # lade das Hintergrund-Bild
    background = load_image("liquid.bmp")

    # vergrößere das Hintergrund-Bild, damit es das Fenster füllt (4x)
    background = pg.transform.scale2x(background)
    background = pg.transform.scale2x(background)

    # Hintergrund ins Fenster schreiben (blit - Block Transfer)
    screen.blit(background, (0, 0))

    # Instanz für den Spieler erstellen
    p = GameObject(player, 10, 3)

    # Fenstertitel setzen
    pg.display.set_caption("Bewege den Spieler")

    # hier werden die Benutzer-Ereignisse erfasst und verarbeitet
    while True:
        # erfasse alle gedrückten Tasten
        # bewege den Player 
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            p.move(up=True)
        if keys[pg.K_DOWN]:
            p.move(down=True)
        if keys[pg.K_LEFT]:
            p.move(left=True)
        if keys[pg.K_RIGHT]:
            p.move(right=True)

        # Hintergrund ins Fenster schreiben (blit - Block Transfer)
        screen.blit(background, (0, 0))

        # erfasse Benutzer-Ereignisse 
        for e in pg.event.get():
            # Programm beenden, wenn das Fenster geschlossen wird
            if e.type == pg.QUIT:
                return

        # Spieler ins Fenster schreiben (blit - Block Transfer)
        screen.blit(p.image, p.pos)
        # Tempo des Spiels: 60 Frames per Second
        clock.tick(60)
        # Fenster aktualisieren
        pg.display.update()
        # Warten [Millisekunden]
        pg.time.delay(20)


if __name__ == "__main__":
    # Hauptprogramm aufrufen
    main()
    # alle pygame module zurücksetzen
    pg.quit()
