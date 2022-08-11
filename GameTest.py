import sys, pygame as pg
from Player import Mario
from Enemy import Bullet

time = pg.time.get_ticks()
pg.init()


screen = width, height = 400, 400
white = [255, 255, 255]
leftjump = 'Pygame\\Mario sprites\\tile001.png'
rightjump = 'Pygame\\Mario sprites\\tile010.png'
    

class Run(object):
    def __init__(self):
        self.screen = pg.display.set_mode(screen)
        self.player = Mario()
        self.enemy = Bullet()
        self.clock = pg.time.Clock()
        self.firsttime = pg.time.get_ticks()
        self.newbullet = False


    def bulletspawner(self):
        if self.newbullet == True:
            b = Bullet()
            b.draw(self.screen)


    def run(self):
        run = True
        jump = False
        fall = False
        boost = 10
        while run:
            
            self.clock.tick(10)
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    sys.exit()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        if self.player.rect.y == 200:
                            jump = True


            if keys[pg.K_RIGHT]:
                self.player.rightmove()
                    

            if keys[pg.K_LEFT]:
                self.player.leftmove()


            if jump == True:
                if self.player.image in self.player.right:
                        self.player.image = pg.image.load(rightjump)
                if self.player.image in self.player.left:
                        self.player.image = pg.image.load(leftjump)
                self.player.rect.y -= boost
                boost -= 1
                if boost == 0:
                    jump = False
                    fall = True
                    boost = 10
                    
            if fall == True:
                self.player.rect.y += boost
                boost -= 1
                if boost == 0:
                    fall = False
                    boost = 10

            self.screen.fill(white)
            #  if int(pg.time.get_ticks()/1000) % 5 == 0:  code to do something every 5 seconds
            self.enemy.draw(self.screen)
            pg.draw.line(self.screen, [0,0,0], [0,228], [400,228], 3)
            if self.enemy.rect.x <= 0:
                self.enemy.rect.x, self.enemy.rect.y = 400, 200
                self.newbullet = True
            self.player.draw(self.screen)
            if self.player.rect.colliderect(self.enemy.rect):
                pg.draw.rect(self.screen, [255, 0, 0], self.player.rect, 4)
                

            
            pg.display.flip()

g = Run()
g.run()