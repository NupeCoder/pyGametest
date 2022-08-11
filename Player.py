import pygame  as pg

mario = 'Pygame\\Mario sprites\\tile007.png' 
right1 = 'Pygame\\Mario sprites\\tile008.png'
right2 = 'Pygame\\Mario Sprites\\tile009.png'
left1 = 'Pygame\\Mario sprites\\tile004.png'
left2 = 'Pygame\\Mario sprites\\tile003.png'
left3 = 'Pygame\\Mario sprites\\tile002.png'


class Mario(object):
    def __init__(self):
        self.position = [200, 200]
        self.current = 0
        self.right = []
        self.left = []
        self.right.append(pg.image.load(mario))
        self.right.append(pg.image.load(right1))
        self.right.append(pg.image.load(right2))
        self.left.append(pg.image.load(left1))
        self.left.append(pg.image.load(left2))
        self.left.append(pg.image.load(left3))
        self.image = pg.image.load(mario)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200


    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    
    def leftmove(self):
        self.move(-10, 0)
        self.image = self.left[self.current]
        for i in range(len(self.left)-1):
            self.current += 1

        if self.current >= (len(self.left)):
            self.current = 0


    def rightmove(self):
        self.move(10, 0)
        self.image = self.right[self.current]
        for i in range(len(self.right)-1):
            self.current += 1

        if self.current >= (len(self.right)):
            self.current = 0
        

    def draw(self, surface):
        surface.blit(self.image, self.rect)
