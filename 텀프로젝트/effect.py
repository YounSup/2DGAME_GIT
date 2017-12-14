from pico2d import*
import main_state
damage_effect=[]


class Effect_Balck_IO:
    image = None
    def __init__(self):
        if Effect_Balck_IO.image == None:
            Effect_Balck_IO.image = load_image('테스트검정.png')
        self.state = 1
        self.Black_in = True
        self.Alpha_num = 0.0
        self.i =0
        self.delete = False
    def update(self,frame_time):
        if self.i%3 ==0:
            if self.Black_in == True:
                self.Alpha_num += 0.05
                if self.Alpha_num >= 1.0:
                    self.Black_in = False

            else:
                self.Alpha_num-=0.05
                if self.Alpha_num <= 0.0:
                    self.delete= True
            Effect_Balck_IO.image.opacify(self.Alpha_num)
        self.i += 1

    def draw(self,frame_time):
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

class Effect_genji_bullet:
    image = None
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.frame = 0;
        self.delete = False
        if Effect_genji_bullet.image == None :
            Effect_genji_bullet.image = load_image('타격이펙트.png')

    def update(self, frame_time):
        self.frame += 1;
        if self.frame ==5:
            self.delete = True
            
    def draw(self, frame_time):
        if self.frame <= 4:
           Effect_genji_bullet.image.clip_draw(181 * self.frame, 0  ,181 ,180 ,   self.x, self.y, 90,90)

class Effect_genji_ult:
    image = None
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.frame = 0;
        self.delete = False
        self.save_frame =0
        if Effect_genji_ult.image == None :
            Effect_genji_ult.image = load_image('용검이펙트.png')

    def update(self, frame_time):
        self.save_frame += frame_time
        self.x = main_state.hero.x
        self.y = main_state.hero.y+30
        if self.save_frame >=0.06:
            self.frame += 1
            self.save_frame = 0
        if self.frame ==18:
            self.delete = True
            
    def draw(self, frame_time):
        if self.frame <= 17:
           Effect_genji_ult.image.clip_draw(348 * self.frame, 0  ,348 ,445 ,   self.x, self.y)




def damage_update(frame_times):
    for da in damage_effect:
        da.update(frame_times)
        if da.delete == True:
            damage_effect.remove(da)

def damage_draw(frame_times):
    for da in damage_effect:
        da.draw(frame_times)


