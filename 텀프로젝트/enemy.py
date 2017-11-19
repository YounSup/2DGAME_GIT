from pico2d import *
from genji import *

enemys= []
LEFT, RIGHT = 0 ,1
class Robot:
    image = [None, None]
    def __init__(c, x, y, z=0, dir = 1):
        c.x, c.y, c.z = x, y, z
        c.damage, c.speed = 0,0
        c.state= 0
        c.dir = dir
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
            Robot.image[c.dir].clip_draw(c.frame * 90,0,90,86,c.x,c.y)

class Reinhard:
    image = None
    def __init__(c, x, y, z=0, dir = 1):
        c.x,c.y,c.z = x, y, z
        c.damage, c.speed = 0,0
        c.state= 0
        c.dir = dir
        c.frame =0
        c.count =0
        if Reinhard.image == None:
            Reinhard.image = load_image('라인하르트.png')
    def idle(c):
        if c.dir == RIGHT :
            c.x += 5
            c.count +=1
            if c.count == 50:
                c.count =0
                c.dir =LEFT
        elif c.dir == LEFT:
            c.x -= 5
            c.count +=1
            if c.count == 50:
                c.count =0
                c.dir =RIGHT
    def update(c):
        c.frame = (c.frame+1)%2
        c.idle()
        
    def draw(c):
        if c.dir == LEFT:
            Reinhard.image.clip_draw(c.frame * 199, 177 ,199,177,c.x,c.y)
        else:
            Reinhard.image.clip_draw(c.frame * 199, 0 ,199,177,c.x,c.y)

class Sold:
    image = None
    def __init__(c, x, y, z=0, dir = 1):
        c.x,c.y,c.z = x, y, z
        c.damage, c.speed = 0,0
        c.state= 0
        c.dir = dir
        c.frame =0
        c.count =0
        if Sold.image == None:
            Sold.image = load_image('sold.png')
    def idle(c):
        if c.dir == RIGHT :
            c.x += 5
            c.count +=1
            if c.count == 60:
                c.count =0
                c.dir =LEFT
        elif c.dir == LEFT:
            c.x -= 5
            c.count +=1
            if c.count == 60:
                c.count =0
                c.dir =RIGHT
                
    def update(c):
        c.frame = (c.frame+1)%9
        c.idle()

        
    def draw(c):
        if c.dir == LEFT:
            Sold.image.clip_draw(c.frame * 300, 300 ,300,300,c.x,c.y)
        else:
            Sold.image.clip_draw(c.frame * 300, 0 ,300,300,c.x,c.y)
    
    def attack(c):
        if c.dir == Right:
            throw_knife.append(bullet(c.x+30, c.y+15, c.z, Left,1))
        else:
            throw_knife.append(bullet(c.x-30, c.y+15, c.z, Right,1))


class Para:
    image = None
    image_boost = None
    def __init__(c, x, y, z=0, dir = 1):
        c.x, c.y, c.z = x,y, z
        c.damage, c.speed = 0, 0
        c.state = 0
        c.dir = dir
        c.frame = 0
        c.count = 0
        if Para.image == None:
            Para.image = load_image('파라.png')
            Para.image_boost = load_image('파라부스터W200.png')

    def idle(c):
        if c.dir == RIGHT:
            c.x += 5
            c.y += 1
            c.count += 1
            if c.count == 30:
                c.count = 0
                c.dir = LEFT
        elif c.dir == LEFT:
            c.x -= 5
            c.y -=1
            c.count += 1
            if c.count == 30:
                c.count = 0
                c.dir = RIGHT

    def update(c):
        c.frame = (c.frame+1)%3
        c.idle()

    def draw(c):
        if c.dir == LEFT:
            Para.image_boost.clip_draw(c.frame * 200, 150, 200, 150, c.x + 50, c.y + 20, 100, 75)
            Para.image.clip_draw( 0, 0, 300, 275, c.x, c.y,150,137)

        else:
            Para.image_boost.clip_draw(c.frame * 200, 0, 200, 150, c.x - 50, c.y + 20, 100, 75)
            Para.image.clip_draw(300, 0, 300, 275, c.x, c.y,150,137)


    def attack(c):
        if c.dir == Right:
            throw_knife.append(bullet(c.x -75, c.y - 45, c.z, Left, 2))
        else:
            throw_knife.append(bullet(c.x +75, c.y - 45, c.z, Right, 2))



def enemys_update():
    for enemy in enemys:
        enemy.update()
def enemys_draw():
    for enemy in enemys:
        enemy.draw()

