from pico2d import *

open_canvas(1200,600)


LEFT, RIGHT = 0 ,1

class Robot:
    image = [None, None]
    def __init__(c):
        c.x, c.y, c.z = 300,60,0
        c.damage, c.speed = 0,0
        c.state= 0
        c.dir = 1
        c.frame =0
        c.count =0
        if Robot.image[0] == None or Robot.image[1] == None :
          Robot.image[0] = load_image('쫄따구.png')
          Robot.image[1] = load_image('쫄따구오른쪽.png')
          
    def idle(c):
        if c.dir == RIGHT :# 오른쪽
            c.x += 5
            c.count +=1
            if c.count == 10:
                c.count =0
                c.dir =LEFT
        elif c.dir == LEFT:
            c.x -= 5
            c.count +=1
            if c.count == 10:
                c.count =0
                c.dir =RIGHT
                
    def update(c):
        c.frame = (c.frame+1)%4
        c.idle()
        
    def draw(c):
            c.image[c.dir].clip_draw(c.frame * 90,0,90,86,c.x,c.y)

class Reinhard:
    image = None
    def __init__(c):
        c.x,c.y,c.z = 500, 250, 0
        c.damage, c.speed = 0,0
        c.state= 0
        c.dir = 1
        c.frame =0
        c.count =0
        if Reinhard.image == None:
            Reinhard.image = load_image('라인하르트.png')
    def idle(c):
        if c.dir == RIGHT :
            c.x += 5
            c.count +=1
            if c.count == 10:
                c.count =0
                c.dir =LEFT
        elif c.dir == LEFT:
            c.x -= 5
            c.count +=1
            if c.count == 10:
                c.count =0
                c.dir =RIGHT
    def update(c):
        c.frame = (c.frame+1)%2
        c.idle()
        
    def draw(c):
        if c.dir == LEFT:
            c.image.clip_draw(c.frame * 199, 177 ,199,177,c.x,c.y)
        else:
            c.image.clip_draw(c.frame * 199, 0 ,199,177,c.x,c.y)
    

e= Robot()
f= Reinhard()

a = True;

while a:
    clear_canvas()
    e.update()
    f.update()
    e.draw()
    f.draw()
    update_canvas()
    delay(0.05)
