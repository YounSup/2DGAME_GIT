from pico2d import *

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
