from pico2d import *

open_canvas(1200, 600)

image2 = load_image('stage1-1.jpg')

image2.draw(600, 300)

update_canvas()


class Genji:
    def __init__(self):
        self.image = load_image('겐지스프라이트.png')
        self.imageleft = load_image('겐지스프라이트왼쪽.png')
        self.image_Rightjump = load_image('겐지점프.png')
        self.image_Leftjump = load_image('겐지점프왼쪽.png')
        self.x, self.y, self.z = 100, 50 , 0
        self.bodyframe = 0
        self.attackstate = 0 #공격상태
        self.attackframe = 0 #공격모션프레임
        self.jumpcount, self.jump_num, self.jumpstate, self.savey = 0, 0, False,0
        self.jumpframe = 1
        self.genjistate = 0 #겐지상태 좌,우 이동 멈춤

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

            if self.genjistate == 0:  # 겐지가 오른쪽볼때
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


            elif self.genjistate == 1:  # 겐지가 왼쪽볼때
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








genji = Genji()
genji.genjistate = 0
running = True;


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LALT:
            if genji.jumpcount <2:
                if genji.jumpcount ==0:
                    genji.savey = genji.y
                genji.jumpcount += 1
                genji.jump_num = 25
                if genji.jumpcount ==2:
                    genji.jumpstate = True;



while running:
    handle_events()
    genji.update()
    clear_canvas()
    image2.draw(600, 300)
    genji.draw()
    update_canvas()
    delay(0.02)