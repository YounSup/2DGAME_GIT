from pico2d import*
Right, Left = 0,1
throw_knife=[]
i =0
class bullet:
    image = None
    image_bullet = None
    image_Para_bullet = None
    def __init__(self ,X, Y,Z, STATE, INDEX):
        self.index = INDEX
        self.x, self.y, self.z =X,Y,Z
        self.speed, self.damage= 20,10
        self.Rotateangle =0
        self.state = STATE
        self.delete = False

        if bullet.image == None:
            bullet.image = load_image('겐지표창.png')
            bullet.image_bullet = load_image('총알.png')
            bullet.image_Para_bullet=load_image('파라총알.png')

    def update(self,frame):
        if self.index <2:
            if self.state == Right:
                self.x += self.speed
            elif self.state == Left:
                self.x -= self.speed
        elif self.index ==2:
            if self.state == Right:
                self.x += self.speed
                self.y -= self.speed-10
            elif self.state == Left:
                self.x -= self.speed
                self.y -= self.speed-10
        self.Rotateangle +=60
        if self.x >=1200 or self.x <=0:
            self.delete = True

    def get_bb(self):
        return self.x - 10, self.y - 120 , self.x + 10, self.y - 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        if self.state == Right:
            if self.index == 0:
                bullet.image.rotate_draw(self.Rotateangle,self.x,self.y,47,48)
            elif self.index == 1:
                bullet.image_bullet.clip_draw(30, 0 ,30,11,self.x,self.y)
            elif self.index == 2:
                bullet.image_Para_bullet.clip_draw(0, 0 ,52,49,self.x,self.y)

        elif self.state == Left:
            if self.index ==0:
               bullet.image.rotate_draw(self.Rotateangle, self.x, self.y, 47, 48)
            elif self.index == 1:
               bullet.image_bullet.clip_draw(0, 0 ,30,11,self.x,self.y)
            elif self.index == 2:
               bullet.image_Para_bullet.clip_draw(0, 0 ,52,49,self.x,self.y)
        self.draw_bb()



class Genji:
    def __init__(self):
        self.image = load_image('겐지스프라이트.png')
        self.imageleft = load_image('겐지스프라이트왼쪽.png')
        self.image_Rightjump = load_image('겐지점프.png')
        self.image_Leftjump = load_image('겐지점프왼쪽.png')
        self.image_Skill=[load_image('질풍참1.png'),load_image('질풍참2.png'),
                          load_image('질풍참3.png'),load_image('질풍참4.png'),
                          load_image('질풍참5.png'),load_image('질풍참6.png')]
        self.image_Right_Ult = load_image('용검RIGHT.png')
        self.image_LEFT_Ult = load_image('용검LEFT.png')
        self.image_ult_attack_right =[load_image('용검Right공격1.png'), load_image('용검Right공격2.png')]
        self.image_ult_attack_left = [load_image('용검Left공격1.png'), load_image('용검Left공격2.png')]
        self.image_skill_cooltime_n = load_image('겐지스킬.png')
        self.image_shadow = load_image('그림자.png')
        self.image_skill_cooltime_u = load_image('겐지스킬아이콘.png')

        
        self.x, self.y, self.z = 100, 250 , 0
        self.Skill_1_OnOff = True; # True가 스킬 on임
        self.bodyframe = 0
        self.attackstate = 0 #공격상태
        self.attackframe = 0 #공격모션프레임
        self.jumpcount, self.jump_num, self.jumpstate, self.savey = 0, 0, False,0
        self.jumpframe = 1
        self.genjistate = 0 #겐지상태 좌,우 이동 멈춤
        self.drawnum =0 #스프라이트 아닌 애니메이션 변수
        self.ult_OnOFF = False # 궁극기 온오프
        self.ult_attacknum = 0 #궁극기 공격시 모션
        self.ult_flag = 0 #궁극기 모션 플레그
        self.KEYCHECK_LEFT, self.KEYCHECK_RIGHT = 0, 0  # 키눌림용 변수
        self.KEYCHECK_UP, self.KEYCHECK_DOWN = 0, 0
        self.NUM_SKILL_ON = self.image_skill_cooltime_u.h
        self.cool_shift = 0
        self.cool_protect =0
        self.cool_ult =self.NUM_SKILL_ON




    def update(self, frame):
        global i
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
            self.x = max(20, self.x-4)
        if self.KEYCHECK_RIGHT == 1:
            self.x = min(1180,self.x+4)
        if self.KEYCHECK_DOWN == 1:
            self.y = max(120, self.y-3)
        if self.KEYCHECK_UP == 1:
            if self.jumpcount == 0:
                self.y = min(380, self.y+3)


        if self.jumpcount > 0:
            self.jump_num -= 2
            self.y += self.jump_num
            self.z += self.jump_num
            if self.y < self.savey:
                self.y = self.savey
                self.jumpcount = 0
                self.z =0



        if self.cool_shift >0:
            self.cool_shift -=1
        if self.cool_protect>0:
            self.cool_protect -=1

        if self.cool_ult>0 and i%10 ==0:
            self.cool_ult-=1

        i+=1
    def get_bb(self):
        return self.x-30, self.y-60, self.x+30, self.y-30
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self): #출력부분
            if self.jumpcount>0:
                self.image_shadow.draw(self.x, self.savey - 65, self.image_shadow.w // 2, self.image_shadow.h)
            else:
                self.image_shadow.draw(self.x, self.y - 65, self.image_shadow.w // 2, self.image_shadow.h)
            if self.genjistate == Right:  # 겐지가 오른쪽볼때
                if self.ult_OnOFF == True:
                    if self.ult_flag == 0: #공격키를 안눌르면 플레그 =0
                        self.image_Right_Ult.clip_draw(self.bodyframe * 300, 300, 300, 300, self.x+40, self.y+40)
                    elif self.ult_flag >0:
                        if self.ult_attacknum%2 == 0:
                            self.image_ult_attack_right[0].draw(self.x+40, self.y+40,300,300)
                        else:
                            self.image_ult_attack_right[1].draw(self.x + 80, self.y + 40, 300, 300)
                        self.ult_flag +=1
                        if self.ult_flag == 5:
                            self.ult_flag =0
                    self.image_Right_Ult.clip_draw(self.bodyframe * 300, 0, 300, 300, self.x+40, self.y+40)
                else: #궁극기 아닐때
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

                if self.ult_OnOFF == True:
                    if self. ult_flag ==0:
                        self.image_LEFT_Ult.clip_draw(self.bodyframe * 300, 300, 300, 300, self.x-40, self.y+40)
                    elif self.ult_flag > 0:
                        if self.ult_attacknum % 2 == 0:
                            self.image_ult_attack_left[0].draw(self.x - 40, self.y + 40, 300, 300)
                        else:
                            self.image_ult_attack_left[1].draw(self.x - 80, self.y + 40, 300, 300)
                        self.ult_flag += 1
                        if self.ult_flag == 5:
                            self.ult_flag = 0
                    self.image_LEFT_Ult.clip_draw(self.bodyframe * 300, 0, 300, 300, self.x+-40, self.y+40)
                else: #궁극기 아닐때
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
            self.draw_bb()
            nw = self.image_skill_cooltime_n.w//2
            nh = self.image_skill_cooltime_n.h//2
            uw = self.image_skill_cooltime_u.w//2
            uh = self.image_skill_cooltime_u.h

            self.image_skill_cooltime_n.clip_draw(0,0,nw,nh,700,50)# 질풍참 쿨
            self.image_skill_cooltime_n.clip_draw(0, nh, nw, nh -self.cool_shift, 700, 50 -self.cool_shift/2)  # 질풍참 온

            self.image_skill_cooltime_n.clip_draw(nw +1 ,0,nw, nh, 700+ nw, 50)#튕기기 쿨

            self.image_skill_cooltime_u.clip_draw(uw, 0, uw, uw, 500, 50)  # 궁극기 클
            self.image_skill_cooltime_u.clip_draw(0,0,uw,uw- self.cool_ult, 500,50- self.cool_ult/2) #궁극기 온
            debug_print('x=%d, y=%d z=%d' % (self.x, self.y, self.z))


    def handle_events(self,event):
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.genjistate = 1
                    self.KEYCHECK_LEFT = 1

                elif event.key == SDLK_RIGHT:
                    self.genjistate = 0
                    self.KEYCHECK_RIGHT = 1

                elif event.key == SDLK_UP:
                    self.KEYCHECK_UP = 1

                elif event.key == SDLK_DOWN:
                    self.KEYCHECK_DOWN = 1

                elif event.key == SDLK_LCTRL:
                    if self.ult_OnOFF == False:
                        self.attackstate = 1

                        if self.genjistate == Right:
                            throw_knife.append(bullet(self.x + 80, self.y + 60, self.z, Right,0))
                        else:
                            throw_knife.append(bullet(self.x - 80, self.y + 60, self.z, Left,0))
                    else:
                        self.ult_attacknum += 1
                        self.ult_flag = 1

                elif event.key == SDLK_LALT:
                        if self.jumpcount < 2:
                            if self.jumpcount == 0:
                                self.savey = self.y
                            self.jumpcount += 1
                            self.jump_num = 25
                            if self.jumpcount == 2:
                                self.jumpstate = True;

                elif event.key == SDLK_LSHIFT and self.Skill_1_OnOff == True:
                        if self.cool_shift ==0 :
                            if self.genjistate == 0:
                                self.x = min(1180, self.x + 350)
                            elif self.genjistate == 1:
                                self.x = max(20, self.x - 350)
                            self.drawnum = 0
                            self.Skill_1_OnOff = False;
                            self.cool_shift= self.NUM_SKILL_ON
                        else :
                            print("쿨타임 질풍참")

                elif event.key == SDLK_q:
                        if self.cool_ult <=0:
                            self.ult_OnOFF = True
                            self.cool_ult = self.NUM_SKILL_ON


            if event.type == SDL_KEYUP:

                if event.key == SDLK_LEFT:
                    self.KEYCHECK_LEFT = 0


                elif event.key == SDLK_RIGHT:
                    self.KEYCHECK_RIGHT = 0


                elif event.key == SDLK_UP:
                    self.KEYCHECK_UP = 0


                elif event.key == SDLK_DOWN:
                    self.KEYCHECK_DOWN = 0


def bullet_update(frame_time):
    for bullet in throw_knife:
        bullet.update(frame_time)
        if bullet.delete == True:
            throw_knife.remove(bullet)
def bullet_draw(frame_time):
    for bullet in throw_knife:
        bullet.draw()
