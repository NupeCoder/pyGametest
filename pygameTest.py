import sys, pygame as pg
pg.init()

size = width, length = 400, 400

ball = pg.image.load('intro_ball.gif')
ballrect = ball.get_rect()


white = [255, 255, 255]

position = [200, 200]

while 1:
    display = pg.display.set_mode(size)

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()


        if event.type == pg.KEYDOWN:
            if event.key == (pg.K_RIGHT):
                position[0] += 10
                print('right')
            if event.key == (pg.K_LEFT):
                position[0] -= 10
                print('left')
            if event.key == (pg.K_UP):
                position[1] -= 20
                print('up')
    
    if position[1] < 200:
        pg.time.wait(500)
        position[1] += 5

    display.blit(ball, position)
    pg.display.flip()