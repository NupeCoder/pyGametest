import pygame as pg

bullet1 = pg.image.load('Pygame\\Torpedo Ted\\tile000.png')
bullet2 = pg.image.load('Pygame\\Torpedo Ted\\tile001.png')
bullet3 = pg.image.load('Pygame\\Torpedo Ted\\tile002.png')
bullet4 = pg.image.load('Pygame\\Torpedo Ted\\tile003.png')

randomLocation  =  [ [400,200], [379, 2], [33, 6], [18, 88] ]

class Bullet(object):
    def __init__(self):
        self.position = [400, 200]
        self.animation = []
        self.current = 0
        self.xmove = True
        self.ymove = False
        self.animation.append((bullet1))
        self.animation.append((bullet2))
        self.animation.append((bullet3))
        self.animation.append((bullet4))
        self.image = bullet1
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 200
        
    def movex(self):
        self.rect.x -= 10

    def movexright(self):
        self.rect.x += 10


    def movey(self):
        self.rect.y -= 10

    def moveydown(self):
        self.rect.y += 10

    def animate(self):
        if self.xmove == True:
            self.movex()
        if self.ymove == True:
            self.movey()
        if self.current >= len(self.animation) - 1:
            self.current = 0
            self.image = self.animation[self.current]
        else:
            self.current += 1
            self.image = self.animation[self.current]

    def reset(self):
        self.xmove = False
        self.ymove = False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.animate()