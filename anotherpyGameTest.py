import sys, pygame as pg
pg.init()

screen = width, height = 400, 400
white = [255, 255, 255]
mario = 'C:\\Users\\zaffar\\.vscode\\Pygame\\Mario sprites\\tile007.png' 
mariorunright = 'C:\\Users\\zaffar\\.vscode\\Pygame\\Mario sprites\\tile009.png'

class Mario(object):
    def __init__(self):
        self.image = pg.image.load(mario)
        self.position = [200, 200]
    
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
            self.clock.tick(60)
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    sys.exit()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.player.position[1] -= 10
                        
            if keys[pg.K_RIGHT]:
                self.player.position[0] += 10
                self.player.image = pg.image.load(mariorunright)
            if keys[pg.K_LEFT]:
                self.player.position[0] -= 10

            if self.player.position[1] < 200:
                pg.time.wait(500)
                self.player.position[1] += 5

            self.screen.fill(white)
            self.player.draw(self.screen)
            pg.display.flip()

g = Run()
g.run()