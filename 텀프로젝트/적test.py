from pico2d import *

open_canvas(1200,600)



class Robot:
    image = [None, None]
    def __init__(c):
        c.x, c.y, c.z = 300,60,0
        c.damage, c.speed = 0,0
        c.state= 1 #idle
        c.frame =0
        if Robot.image[0] == None or Robot.image[1] == None :
          Robot.image[0] = load_image('쫄따구.png')
          Robot.image[1] = load_image('쫄따구오른쪽.png')

    def update(c):
        c.frame = (c.frame+1)%4
        c.x +=2
        if c.x >= 500:
            c.x = 0
            c.state = 0
    def draw(c):
            c.image[c.state].clip_draw(c.frame * 90,0,90,86,c.x,c.y)

e= Robot()
a = True;
while a:
    clear_canvas()
    e.update()
    e.draw()
    update_canvas()
    delay(0.01)
