from pico2d import*
import random
import game_framework
import title_state


Right, Left = 0,1

global genji_bullet_num
genji_bullet_num = 0

class Map:
    def __init__(self):
        self.image = load_image('testmap.png')
    def draw(self):
        self.image.draw(600,300)
class Menu:
    def __init__(self):
        self.image = load_image('인게임메뉴.png')
        self.Menu_OnOff = False;
    def draw(self):
        self.image.draw(600,300)


class Grass:
 def __init__(self):
  self.image = load_image('grass.png')
 def draw(self):
  self.image.draw(400, 30)

class bullet:
    global genji_bullet_num
    image = None
    genji_bullet_num +=1
    def __init__(self):
        self.Draw_value = False
        self.x, self.y, self.z =0,0,0
        self.speed, self.damage= 20,10
        self.Rotateangle =0
        self.state = Right
        if bullet.image == None:
            self.image_tn = load_image('겐지표창.png')

    def update(self):
        global genji_bullet_num
        if self.state == Right:
            self.x += self.speed
        elif self.state == Left:
            self.x -= self.speed

        self.Rotateangle +=60
        if self.x >=1200 or self.x <=0:
            self.Draw_value = False

    def draw(self):
        if self.Draw_value == True:
            if self.state == Right:
              #  self.image_tn.draw(self.x,self.y,47,48)
                self.image_tn.rotate_draw(self.Rotateangle,self.x,self.y,47,48)
            elif self.state == Left:
                self.image_tn.rotate_draw(self.Rotateangle, self.x, self.y, 47, 48)

class Genji:
    def __init__(self):
        self.image = load_image('겐지스프라이트.png')
        self.imageleft = load_image('겐지스프라이트왼쪽.png')
        self.image_Rightjump = load_image('겐지점프.png')
        self.image_Leftjump = load_image('겐지점프왼쪽.png')
        self.image_Skill=[load_image('질풍참1.png'),load_image('질풍참2.png'),
                          load_image('질풍참3.png'),load_image('질풍참4.png'),
                          load_image('질풍참5.png'),load_image('질풍참6.png')]

        self.x, self.y, self.z = 100, 50 , 0
        self.Skill_1_OnOff = True; # True가 스킬 on임
        self.bodyframe = 0
        self.attackstate = 0 #공격상태
        self.attackframe = 0 #공격모션프레임
        self.jumpcount, self.jump_num, self.jumpstate, self.savey = 0, 0, False,0
        self.jumpframe = 1
        self.genjistate = 0 #겐지상태 좌,우 이동 멈춤
        self.drawnum =0 #스프라이트 아닌 애니메이션 변수

        self.KEYCHECK_LEFT, self.KEYCHECK_RIGHT = 0, 0  # 키눌림용 변수
        self.KEYCHECK_UP, self.KEYCHECK_DOWN = 0, 0

    def update(self):
        self.bodyframe = (self.bodyframe + 1) % 13
        if self.jumpstate == True:
            if self.jumpframe ==7:
                self.jumpstate = False;
                self.jumpframe = 1
            self.jumpframe +=1

        if self.attackframe >= 13:
            self.attackframe = 0
            self.attackstate = 0

        if self.attackstate == 1:
            self.attackframe = self.attackframe + 1

        if self.KEYCHECK_LEFT == 1:
            self.x -= 4
        if self.KEYCHECK_RIGHT == 1:
            self.x += 4
        if self.KEYCHECK_DOWN == 1:
            self.y -=2
        if self.KEYCHECK_UP == 1:
            self.y +=2

        if self.jumpcount > 0:
            self.jump_num -= 2
            self.y += self.jump_num
            if self.y < self.savey:
                self.y = self.savey
                self.jumpcount = 0



    def draw(self): #출력부분


            if self.genjistate == Right:  # 겐지가 오른쪽볼때
                if self.jumpcount == 0:
                    self.image.clip_draw(self.bodyframe * 300, 600, 300, 300, self.x, self.y)
                elif self.jumpcount >=1:
                    if self.jumpstate == False:
                       self.image_Rightjump.clip_draw(0, 0, 300, 300, self.x, self.y)
                    else:
                       self.image_Rightjump.clip_draw(300*self.jumpframe, 0, 300, 300, self.x, self.y)

                if self.attackstate == 0 and self.jumpstate == False: #팔 출력부분
                    self.image.clip_draw(self.bodyframe * 300, 300, 300, 300, self.x, self.y)
                elif self.attackstate == 1 and self.jumpstate == False:
                    self.image.clip_draw(self.attackframe * 300, 0, 300, 300, self.x, self.y)


            elif self.genjistate == Left:  # 겐지가 왼쪽볼때
                if self.jumpcount == 0:
                    self.imageleft.clip_draw(self.bodyframe * 300, 600, 300, 300, self.x, self.y)
                elif self.jumpcount >=1:
                    if self.jumpstate == False:
                       self.image_Leftjump.clip_draw(0, 0, 300, 300, self.x, self.y)
                    else:
                       self.image_Leftjump.clip_draw(300*self.jumpframe, 0, 300, 300, self.x, self.y)

                if self.attackstate == 0 and self.jumpstate == False: #팔 출력부분
                    self.imageleft.clip_draw(self.bodyframe * 300, 300, 300, 300, self.x, self.y)
                elif self.attackstate == 1 and self.jumpstate == False:
                    self.imageleft.clip_draw(self.attackframe * 300, 0, 300, 300, self.x, self.y)

            # 이펙트는 앞에
            if self.Skill_1_OnOff == False:
                if self.genjistate == 0:
                    self.image_Skill[self.drawnum].draw(self.x - 150, self.y + 20, 750, 192)
                if self.genjistate == 1:
                    self.image_Skill[self.drawnum].draw(self.x + 150, self.y + 20, 750, 192)
                self.drawnum += 1
                if self.drawnum == 6:
                     self.Skill_1_OnOff = True;

         
def enter():
    global genji, throw_knife, stage, menu
    menu = Menu()
    genji = Genji()
    stage = Map()
    throw_knife = [bullet() for i in range(30)]
    genji.genjistate = 0

def exit():
    global genji, throw_knife, menu
    del(genji)
    del(throw_knife)
    del(stage)

def handle_events():
    global select_num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #game_framework.change_state(title_state)
            menu.Menu_OnOff = True;
            print('sdf')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            genji.genjistate = 1
            genji.KEYCHECK_LEFT = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            genji.KEYCHECK_LEFT = 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            genji.genjistate = 0
            genji.KEYCHECK_RIGHT = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            genji.KEYCHECK_RIGHT = 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            genji.KEYCHECK_UP = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            genji.KEYCHECK_UP = 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            genji.KEYCHECK_DOWN = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            genji.KEYCHECK_DOWN = 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
            genji.attackstate = 1
            for bullet in throw_knife:
                if bullet.Draw_value ==False:
                    bullet.Draw_value = True;
                    if genji.genjistate == Right:
                        bullet.state = Right
                        bullet.x = genji.x + 80
                        bullet.y = genji.y + 60
                    else:
                        bullet.state = Left
                        bullet.x = genji.x - 80
                        bullet.y = genji.y + 60
                    break

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LALT:
            if genji.jumpcount <2:
                if genji.jumpcount ==0:
                    genji.savey = genji.y
                genji.jumpcount += 1
                genji.jump_num = 25
                if genji.jumpcount ==2:
                    genji.jumpstate = True;

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT and genji.Skill_1_OnOff == True:
            if genji.genjistate == 0:
                genji.x += 350
            elif genji.genjistate == 1:
                genji.x -= 350
            genji.drawnum =0
            genji.Skill_1_OnOff = False;

def update():
    genji.update()
    for bullet in throw_knife:
        if bullet.Draw_value == True:
            bullet.update()
    clear_canvas()
    delay(0.020)
def draw():
    stage.draw()
    genji.draw()
    for bullet in throw_knife:
        if bullet.Draw_value == True:
            bullet.draw()
    if menu.Menu_OnOff == True:
        menu.draw()
    update_canvas()



