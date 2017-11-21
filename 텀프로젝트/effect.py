from pico2d import *

damage_effect=[]

class Effect_Balck_IO:
    image = None
    def __init__(self):
        if Effect_Balck_IO.image == None:
            Effect_Balck_IO.image = load_image('테스트검정.png')

        self.Black_in = True
        self.Alpha_num = 0.0
        self.i =0
    def update(self,frame_time):
        if self.i%20 ==0:
            if self.Black_in == True:
                self.Alpha_num += 0.05
                if self.Alpha_num >= 1.0:
                    self.Black_in = False

            else:
                self.Alpha_num-=0.05
                if self.Alpha_num <= 0.0:
                    self.Black_in = True
            Effect_Balck_IO.image.opacify(self.Alpha_num)
        self.i += 1
    def draw(self):

        Effect_Balck_IO.image.draw(600,300)

class Effect_damage:
    image = None
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.up_num=0
        self.alpha_num = 1.0
        self.delete = False
        if Effect_damage.image == None :
            Effect_damage.image = load_image('데미지.png')

    def update(self, frame_time):
        self.up_num +=2
        self.alpha_num-=0.05
        Effect_damage.image.opacify(self.alpha_num)
        if self.alpha_num <= 0:
            self.delete = True
    def draw(self, frame_time):
        Effect_damage.image.draw(self.x, self.y+ self.up_num)

def damage_update(frame_times):
    for da in damage_effect:
        da.update(frame_times)
        if da.delete == True:
            damage_effect.remove(da)

def damage_draw(frame_times):
    for da in damage_effect:
        da.draw(frame_times)
