import sys, pygame as pg
from Player import Mario
from Enemy import Bullet
import random

time = pg.time.get_ticks()
pg.init()
pg.font.init()


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
        self.font = pg.font.SysFont('comicsansms', 20)
        pg.display.update()
        self.score = 0

    def finish(self):
        finish = True

        while finish == True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            self.screen.fill(white)
            self.screen.blit(pg.font.Font.render(self.font, 'GAME OVER', True, (0,0,0)), [200,100])
            pg.display.flip()
            


    def run(self):
        run = True

        jump = False
        fall = False
        flipup = False
        flipdown = False
        flip = False
        boost = 10 
        randomLocation  =  [ [200, 400], [400,200], [0, 200], [200, 0] ]
        
        while run == True:
            
            positions = random.choice(randomLocation)
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
            
            if flipup == True:
                self.enemy.image = pg.transform.rotate(self.enemy.image, -90)
                self.enemy.rect.width = 20
                self.enemy.rect.height = 40
                self.enemy.movey()

            if flipdown == True:
                self.enemy.image = pg.transform.rotate(self.enemy.image, 90)
                self.enemy.rect.width = 20
                self.enemy.rect.height = 40
                self.enemy.moveydown()

            if flip == True:
                self.enemy.image = pg.transform.flip(self.enemy.image, True, False)
                self.enemy.movexright()

            self.screen.fill(white)
            #  if int(pg.time.get_ticks()/1000) % 5 == 0:  code to do something every 5 seconds
            
            pg.draw.line(self.screen, [0,0,0], [0,228], [400,228], 3)
            self.screen.blit(pg.font.Font.render(self.font, str(self.score), True, (0,0,0)), [200,100])
            if self.enemy.rect.x  in [0,400] or self.enemy.rect.y in [0,400]:
                self.score += 1
                self.enemy.rect.x, self.enemy.rect.y = positions[0], positions[1]
                
                flipup = False
                flipdown = False
                flip = False
                self.enemy.reset()
                if positions[0] < 200:
                    flip = True
                if positions[1] < 200:
                    flipdown = True
                if positions[1] > 200:
                    flipup = True

            self.enemy.draw(self.screen)
            self.player.draw(self.screen)
            if self.player.rect.colliderect(self.enemy.rect):
                pg.draw.rect(self.screen, [255, 0, 0], self.player.rect, 4)
                pg.draw.rect(self.screen, [255, 0, 0], self.enemy.rect, 4)
                #self.finish()
                #run = False
                
            pg.display.flip()

g = Run()
g.run()