import sys, pygame as pg
pg.init()

screen = width, height = 400, 400
white = [255, 255, 255]
mario = 'Mario sprites\\tile007.png' 
right1 = 'Mario sprites\\tile008.png'
right2 = 'Mario Sprites\\tile009.png'
rightjump = 'Mario sprites\\tile010.png'
left1 = 'Mario sprites\\tile004.png'
left2 = 'Mario sprites\\tile003.png'
left3 = 'Mario sprites\\tile002.png'
leftjump = 'Mario sprites\\tile001.png'

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



    def move(self, x, y):
        self.position[0] += x
        self.position[1] += y
        

    def draw(self, surface):
        surface.blit(self.image, self.position)

class Run(object):
    def __init__(self):
        self.screen = pg.display.set_mode(screen)
        self.player = Mario()
        self.clock = pg.time.Clock()


    def run(self):
        run = True
        while run:
            self.clock.tick(10)
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    sys.exit()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.player.move(0, -50)
                        
            if keys[pg.K_RIGHT]:
                self.player.move(10, 0)
                self.player.image = self.player.right[self.player.current]
                for i in range(len(self.player.right)-1):
                    self.player.current += 1
                
                    
                if self.player.current >= (len(self.player.right)):
                    self.player.current = 0
                    

            if keys[pg.K_LEFT]:
                self.player.move(-10, 0)
                self.player.image = self.player.left[self.player.current]
                for i in range(len(self.player.left)-1):
                    self.player.current += 1

                    
                if self.player.current >= (len(self.player.left)):
                    self.player.current = 0


            if self.player.position[1] < 200:
                pg.time.wait(50)
                if self.player.image in self.player.right:
                    self.player.image = pg.image.load(rightjump)
                if self.player.image in self.player.left:
                    self.player.image = pg.image.load(leftjump)
                self.player.position[1] += 10

            self.screen.fill(white)
            self.player.draw(self.screen)
            pg.display.flip()

g = Run()
g.run()