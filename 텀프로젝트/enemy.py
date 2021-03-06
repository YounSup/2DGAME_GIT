from pico2d import *
import genji
import main_state
import math
import random
enemys= []
LEFT, RIGHT = 0 ,1
i = 0
bgm = None
class Robot:
    image = [None, None]
    def __init__(c, x, y, z=0, dir = 1):
        c.x, c.y, c.z = x, y, z
        c.damage, c.speed = 3,random.randint(3,8)
        c.hp =100
        c.state= 0
        c.dir = dir
        c.frame =0
        c.count =0
        c.mc = random.randint(10,15)
        if Robot.image[0] == None or Robot.image[1] == None :
          Robot.image[0] = load_image('쫄따구.png')
          Robot.image[1] = load_image('쫄따구오른쪽.png')
          
    def idle(c):
        if c.dir == RIGHT :# 오른쪽
            c.x += c.speed
            c.count +=1
            if c.count == c.mc:
                c.count =0
                c.dir =LEFT
        elif c.dir == LEFT:
            c.x -= c.speed
            c.count +=1
            if c.count == c.mc:
                c.count =0
                c.dir =RIGHT
    def Attack(c):
        if main_state.hero.x > c.x:
            c.dir = RIGHT
            c.x += c.speed
        else:
            c.dir = LEFT
            c.x -= c.speed
        if main_state.hero.jumpcount == 0:
            my= (main_state.hero.y - c.y)//20
            c.y += my
                
    def update(c, frame):
        c.frame = (c.frame+1)%4
        if c.hp<100:
            c.state=2
        if c.state == 0:
            c.idle()
        else:
            c.Attack()

        if c.hp <0:
            c.state=3
    def get_bb(self):
        return self.x - 25, self.y - 70, self.x + 25, self.y-45
    def get_bb2(self):
        return self.x - 200, self.y -90, self.x + 200, self.y+60
    
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb2())
    def draw(c):
            Robot.image[c.dir].clip_draw(c.frame * 90,0,90,86,c.x,c.y)

class Reinhard:
    image = None
    def __init__(c, x, y, z=0, dir = 1):
        c.x,c.y,c.z = x, y, z
        c.damage, c.speed = 10,0
        c.state= 0
        c.dir = dir
        c.frame =0
        c.count =0
        c.hp = 500
        c.i=0
        if Reinhard.image == None:
            Reinhard.image = load_image('라인하르트.png')
    def idle(c):
        if main_state.hero.x > c.x:
            c.dir = RIGHT
            c.x +=1
        else:
            c.dir = LEFT
            c.x -=1
    def update(c, frame):
        c.i+=1
        if c.i%5 ==0:
            c.frame = (c.frame+1)%2
        c.idle()
    def get_bb(self):
        return self.x - 50, self.y - 75, self.x + 40, self.y-50

    def get_bb2(self):
        return self.x - 200, self.y - 90, self.x + 200, self.y + 60
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(c):
        if c.dir == LEFT:
            Reinhard.image.clip_draw(c.frame * 199, 177 ,199,177,c.x,c.y)
        else:
            Reinhard.image.clip_draw(c.frame * 199, 0 ,199,177,c.x,c.y)

class Sold:
    image = None
    def __init__(c, x, y, z=0, dir = 1):
        c.x,c.y,c.z = x, y, z
        c.damage, c.speed = 5,0
        c.state= 0
        c.dir = dir
        c.frame =0
        c.count =0
        c.hp = 150
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
    def get_bb2(self):
        return self.x - 200, self.y - 90, self.x + 200, self.y + 60
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def Attack(self):
        if main_state.hero.x > self.x:
            self.dir = RIGHT
        else:
            self.dir = LEFT
        if main_state.hero.jumpcount == 0:
            my = (main_state.hero.y - self.y) // 10
            self.y += my

    def update(c, frame):
        c.frame = (c.frame+1)%9
        if c.hp<150:
            c.state =1
        c.attack_frametime += frame
        if c.attack_frametime >=0.1:
            c.attack()
            c.attack_frametime=0
        if c.state == 1:
            c.Attack()
        else:
            c.idle()
    def draw(c):
        if c.dir == LEFT:
            Sold.image.clip_draw(c.frame * 300, 300 ,300,300,c.x,c.y)
        else:
            Sold.image.clip_draw(c.frame * 300, 0 ,300,300,c.x,c.y)

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
        c. hp = 100
        c. attack_frame =0
        if Para.image == None:
            Para.image = load_image('파라.png')
            Para.image_boost = load_image('파라부스터W200.png')
            Para.image_shadow = load_image('그림자.png')

    def get_bb2(self):
        return self.x - 200, self.y - 90, self.x + 200, self.y + 60
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
    def attack(c):
        if c.dir == RIGHT:
            genji.throw_knife.append(genji.bullet(c.x +75, c.y - 45, c.z, LEFT, 2))
        else:
            genji.throw_knife.append(genji.bullet(c.x -75, c.y - 45, c.z, RIGHT, 2))
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def update(c,frame):
        c.frame = (c.frame+1)%3
        c.idle()


        c.attack_frame += frame
        if c.attack_frame >= 0.1:
            c.attack()
            c.attack_frame = 0
    def draw(c):
        if c.dir == LEFT:
            Para.image_boost.clip_draw(c.frame * 200, 150, 200, 150, c.x + 50, c.y + 20, 100, 75)
            Para.image.clip_draw( 0, 0, 300, 275, c.x, c.y,150,137)

        else:
            Para.image_boost.clip_draw(c.frame * 200, 0, 200, 150, c.x - 50, c.y + 20, 100, 75)
            Para.image.clip_draw(300, 0, 300, 275, c.x, c.y,150,137)

        Para.image_shadow.draw(c.x, c.y - 300, Para.image_shadow.w//2, Para.image_shadow.h)


class Dragon:
    image_head = None
    image_body = None
    image_tail = None
    shadow = None
    sound = None
    def __init__(self, X=1150, Y=300):
        self.x =X
        self.y =Y
        self.z =0
        self.state, self.hp =0 , 1000
        self.damage = 25
        self.i =0
        self.dragon =False
        if Dragon.image_head==None:
            Dragon.image_head = load_image('D1.png')
            Dragon.image_body = load_image('D2.png')
            Dragon.image_tail = load_image('D3.png')
            Dragon.shadow = load_image('그림자.png')
            Dragon.sound = load_wav('hanjo.wav')
        Dragon.sound.play()
    def get_bb(self):
        return self.x-70 , self.y - 160, self.x + 660, self.y-120
    def get_bb2(self):
        return self.x - 70, self.y - 120, self.x + 660, self.y - 160
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        if i%2==0:
            self.x -=5
            if self.x <-800:
                self.state = 3

        self.i+=1
    def draw(self):

        for i in range(15):
            if i ==14:
                Dragon.image_tail.draw(self.x + 41 * (i + 1),self.y + (40 * math.sin(math.radians(self.x + (i + 1) * 20))))
            else:
                Dragon.image_body.draw(self.x + 40 * (i + 1), self.y + (40 * math.sin(math.radians(self.x + (i + 1) * 20))))

        Dragon.image_head.draw(self.x, self.y + (40*math.sin(math.radians(self.x))))
        Dragon.shadow.draw(self.x+300, self.y - 150,750,21)

class Hanjo:
    image = None
    sound = None
    def __init__(c, x, y, z=0, dir = 1):
        c.x,c.y,c.z = x, y, z
        c.damage, c.speed = 15,0
        c.state= 0
        c.dir = dir
        c.frame =0
        c.count =0
        c.hp = 6000
        c.dragon = False
        c.attack_frametime=0
        if Hanjo.image == None:
            Hanjo.image = load_image('한조.png')
            Hanjo.sound = load_wav('한조대기중.wav')
        Hanjo.sound.play()
    def idle(self):
        if main_state.hero.x > self.x:
            self.dir = RIGHT
            if self.count % 100 < 60:
                self.x = max(self.x - 9, 100)
        else:
            self.dir = LEFT
            if self.count % 100 < 60:
                self.x = min(self.x + 9, 1100)

        if main_state.hero.jumpcount == 0:
            my = ((main_state.hero.y + 40) - self.y) // 10
            self.y += my
    def get_bb(self):
        return self.x - 30, self.y - 85, self.x + 30, self.y  -55
    def get_bb2(self):
        return self.x - 200, self.y - 90, self.x + 200, self.y + 60
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def Attack(self):
        pass

    def update(c, frame):
        if c.count%5 ==0:
            c.frame = (c.frame+1)%2
        if c.hp<0:
            c.dragon = True
        c.attack_frametime += frame
        if c.attack_frametime >=0.4:
            c.attack()
            c.attack_frametime=0

        if c.count%120 ==0:
            c.attack2()




        c.idle()
        c.count += 1
    def draw(c):
        if c.dir == LEFT:
            Hanjo.image.clip_draw(c.frame * 300, 250 ,300,250,c.x,c.y,300//1.2, 250//1.2)
        else:
            Hanjo.image.clip_draw(c.frame * 300, 0 ,300,250,c.x,c.y,300//1.2, 250//1.2)

    def attack(c):
        if c.dir == RIGHT:
            genji.throw_knife.append(genji.bullet(c.x+ 110, c.y-6, c.z, LEFT,3))
        else:
            genji.throw_knife.append(genji.bullet(c.x-110 , c.y-6, c.z, RIGHT,3))
    def attack2(c):
        if c.dir == RIGHT:
            genji.throw_knife.append(genji.bullet(c.x+ 110, c.y-6, c.z, LEFT,3))
            genji.throw_knife.append(genji.bullet(c.x + 110, c.y - 6, c.z, LEFT, 4))
            genji.throw_knife.append(genji.bullet(c.x + 110, c.y - 6, c.z, LEFT, 5))
        else:
            genji.throw_knife.append(genji.bullet(c.x-110 , c.y-6, c.z, RIGHT,3))
            genji.throw_knife.append(genji.bullet(c.x - 110, c.y - 6, c.z, RIGHT, 4))
            genji.throw_knife.append(genji.bullet(c.x - 110, c.y - 6, c.z, RIGHT, 5))


def enemys_update(frame_time):
    global i, bgm
    if i %2 == 0:
        for enemy in enemys:
            enemy.update(frame_time)
            if enemy.hp < 0:
                enemy.state = 3
            if enemy.state ==3:
                enemys.remove(enemy)
                if bgm == None:
                    bgm =load_wav('enemykill.wav')
                bgm.play()
    i+=1
def enemys_draw(frame_time):
    for enemy in enemys:
        enemy.draw()

