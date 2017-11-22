from pico2d import *
import genji

enemys= []
LEFT, RIGHT = 0 ,1
i = 0
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
                
    def update(c, frame):
        c.frame = (c.frame+1)%4
        c.idle()

    def get_bb(self):
        return self.x - 25, self.y - 70, self.x + 25, self.y-45

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(c):
            Robot.image[c.dir].clip_draw(c.frame * 90,0,90,86,c.x,c.y)
            c.draw_bb()
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
    def update(c, frame):
        c.frame = (c.frame+1)%2
        c.idle()
    def get_bb(self):
        return self.x - 50, self.y - 75, self.x + 40, self.y-50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(c):
        if c.dir == LEFT:
            Reinhard.image.clip_draw(c.frame * 199, 177 ,199,177,c.x,c.y)
        else:
            Reinhard.image.clip_draw(c.frame * 199, 0 ,199,177,c.x,c.y)
        c.draw_bb()
class Sold:
    image = None
    def __init__(c, x, y, z=0, dir = 1):
        c.x,c.y,c.z = x, y, z
        c.damage, c.speed = 0,0
        c.state= 0
        c.dir = dir
        c.frame =0
        c.count =0
        c.attack_frametime=0
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
    def get_bb(self):
        return self.x - 30, self.y - 60, self.x + 30, self.y  -30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def update(c, frame):
        c.frame = (c.frame+1)%9
        c.idle()
        c.attack_frametime += frame
        if c.attack_frametime >=0.1:
            c.attack()
            c.attack_frametime=0
        print(c.attack_frametime)
    def draw(c):
        if c.dir == LEFT:
            Sold.image.clip_draw(c.frame * 300, 300 ,300,300,c.x,c.y)
        else:
            Sold.image.clip_draw(c.frame * 300, 0 ,300,300,c.x,c.y)
        c.draw_bb()
    def attack(c):
        if c.dir == RIGHT:
            genji.throw_knife.append(genji.bullet(c.x+ 75, c.y+15, c.z, LEFT,1))
        else:
            genji.throw_knife.append(genji.bullet(c.x-75 , c.y+15, c.z, RIGHT,1))


class Para:
    image = None
    image_boost = None
    image_shadow = None
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
            Para.image_shadow = load_image('그림자.png')

    def idle(c):
        if c.dir == RIGHT:
            c.x += 5

            c.count += 1
            if c.count == 30:
                c.count = 0
                c.dir = LEFT
        elif c.dir == LEFT:
            c.x -= 5

            c.count += 1
            if c.count == 30:
                c.count = 0
                c.dir = RIGHT
    def get_bb(self):
        return self.x - 25, self.y - 180, self.x + 25, self.y-50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def update(c,frame):
        c.frame = (c.frame+1)%3
        c.idle()

    def draw(c):
        if c.dir == LEFT:
            Para.image_boost.clip_draw(c.frame * 200, 150, 200, 150, c.x + 50, c.y + 20, 100, 75)
            Para.image.clip_draw( 0, 0, 300, 275, c.x, c.y,150,137)

        else:
            Para.image_boost.clip_draw(c.frame * 200, 0, 200, 150, c.x - 50, c.y + 20, 100, 75)
            Para.image.clip_draw(300, 0, 300, 275, c.x, c.y,150,137)
        c.draw_bb()
        Para.image_shadow.draw(c.x, c.y - 300, Para.image_shadow.w//2, Para.image_shadow.h)
    def attack(c):
        if c.dir == RIGHT:
            genji.throw_knife.append(genji.bullet(c.x -75, c.y - 45, c.z, LEFT, 2))
        else:
            genji.throw_knife.append(genji.bullet(c.x +75, c.y - 45, c.z, RIGHT, 2))



def enemys_update(frame_time):
    global i
    if i %2 == 0:
        for enemy in enemys:
            enemy.update(frame_time)
    i+=1
def enemys_draw(frame_time):
    for enemy in enemys:
        enemy.draw()

