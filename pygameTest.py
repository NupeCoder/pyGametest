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
                max = 20
                jump = 0
                while jump < max:
                    position[1] -= jump
                    jump += 4
                print('up')

    display.blit(ball, position)

    pg.display.flip()