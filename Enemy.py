import pygame as pg
import random

bullet1 = pg.image.load('Pygame\\Torpedo Ted\\tile000.png')
bullet2 = pg.image.load('Pygame\\Torpedo Ted\\tile001.png')
bullet3 = pg.image.load('Pygame\\Torpedo Ted\\tile002.png')
bullet4 = pg.image.load('Pygame\\Torpedo Ted\\tile003.png')

randomLocation  =  [ [400,200], [379, 2], [33, 6], [18, 88] ]

class Bullet(object):
    def __init__(self):
        self.position = position = random.choice(randomLocation)
        self.animation = []
        self.current = 0
        self.animation.append((bullet1))
        self.animation.append((bullet2))
        self.animation.append((bullet3))
        self.animation.append((bullet4))
        self.image = self.animation[self.current]
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position [1]
        

    def animate(self):
        self.rect.x -= 5
        if self.current >= len(self.animation) - 1:
            self.current = 0
            self.image = self.animation[self.current]
        else:
            self.current += 1
            self.image = self.animation[self.current]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.animate()