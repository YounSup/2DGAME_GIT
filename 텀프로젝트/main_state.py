from pico2d import*
import effect
import game_framework
import title_state
import start_state
import genji
import enemy
import background
import pickle
import time


scores = []
ss= []
k= 0
fileName = "genji_score.pickle"
show_rank = False

class Entry:
    def __init__(self, score, time,stage):
        self.score = score
        self.time = time
        self.stage =stage

class Menu:
    def __init__(self):
        self.image = load_image('인게임메뉴.png')
        self.Menu_OnOff = False;
    def draw(self):
        self.image.draw(600,300)


def add(score):
    global scores
    scores.append(score)
    SaveScores()


def loadScores():
    global scores
    scores = []
    f = open(fileName, "rb")
    scores = pickle.load(f)
    f.close()
    for i in scores:
        ss.append(i.score)


def SaveScores():
    global scores
    f = open(fileName, "wb")
    pickle.dump(scores, f)
    f.close()


def enter():
    global hero, stage, menu, back, st_num ,finish, mt, current_time, time_score
    current_time = get_time()
    time_score = 0.0
    st_num = 1
    finish = False
    mt =0
    menu = Menu()
    hero = genji.Genji()


    #enemy.enemys.append(enemy.Hanjo(500,200))
    #enemy.enemys.append(enemy.Dragon(1200,300))
    #enemy.enemys.append(enemy.Dragon(1200, 350))
    #enemy.enemys.append(enemy.Dragon(1200, 400))
    #enemy.enemys.append(enemy.Reinhard(800,350))
    #enemy.enemys.append(enemy.Para(1000,500,200))
    enemy.enemys.append(enemy.Robot(500, 250))
    enemy.enemys.append(enemy.Robot(800, 350))
    enemy.enemys.append(enemy.Robot(950, 200))
    enemy.enemys.append(enemy.Robot(250, 350))
    enemy.enemys.append(enemy.Robot(450, 150))
    back = background.Background()



def exit():
    global hero, stage, menu, back, black
    del(hero)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            hero.handle_events(event,frame_time)


def update(frame_time):
    global  mt,finish, st_num, current_time, time_score, show_rank
    if show_rank == False:
        time_score = get_time() - current_time

    hero.update(frame_time)
    genji.bullet_update(frame_time)
    enemy.enemys_update(frame_time)
    effect.damage_update(frame_time)



    for bullet in  genji.throw_knife:
        if bullet.index == 0:
            for enemys in enemy.enemys: #겐치 표창과 적이 충돌중
                if collision(bullet, enemys):
                    bullet.delete= True
                    effect.damage_effect.append(effect.Effect_damage(bullet.x, bullet.y))
                    effect.damage_effect.append(effect.Effect_genji_bullet(enemys.x, enemys.y))
                    enemys.hp -= bullet.damage
                   
        elif bullet.index >= 1:  #적총알과 겐지 충돌중
            if collision(bullet, hero) and  hero.protect_onoff == False:
                bullet.delete = True
                hero.hp -= 10
                effect.damage_effect.append(effect.Effect_damage(hero.x, hero.y + 100))

            elif collision(bullet, hero) and  hero.protect_onoff == True:
                bullet.out = True
                if bullet.state == 0:
                    bullet.state = 1
                else :
                    bullet.state = 0

    for enemys in enemy.enemys:
        if collision2(hero, enemys): # 몬스터 ai 범위에 들어온다면
            enemys.state =1
        if collision(hero, enemys) and hero.vlrur == False: # 겐지와 적 몸박
            hero.vlrur = True
            hero.hp-= enemys.damage
            effect.damage_effect.append(effect.Effect_damage(hero.x, hero.y + 100))


    if enemy.enemys == [] and finish == False and show_rank == False:#몬스터를 다 잡았을때
        if st_num ==3: #클리어하고 기록해야함
            entry = Entry(max((int)(st_num*1000 - time_score*50),0), time_score)
            add(entry)
            show_rank = True
        if show_rank == False:
            effect.damage_effect.append(effect.Effect_Balck_IO())
            finish = True
            st_num +=1

    if finish and show_rank == False:
        mt += 1
        if mt>=60:
            if st_num ==2:
                enemy.enemys.append(enemy.Sold(500, 250))
                enemy.enemys.append(enemy.Robot(800, 350))
                enemy.enemys.append(enemy.Sold(800, 200))
                enemy.enemys.append(enemy.Robot(250, 350))
                enemy.enemys.append(enemy.Robot(450, 150))
            elif st_num == 3:
                enemy.enemys.append(enemy.Robot(250, 350))
            else: pass

            hero.x, hero.y, hero.z = 100, 250, 0
            mt=0
            finish = False

    clear_canvas()


def draw(frame_time):
    global time_score,st_num
    back.draw()
    hero.font.draw(400, 570, 'Stage:%d' % st_num, (255, 00, 00))
    hero.font.draw(550, 570, 'Time:%f' % time_score, (255, 00, 00))
    enemy.enemys_draw(frame_time)
    if menu.Menu_OnOff == True:
        menu.draw()
    hero.draw()
    genji.bullet_draw(frame_time)
    effect.damage_draw(frame_time)
    k = 0
    if show_rank:
        loadScores()
        for i in scores:
            hero.font.draw(200, 300 + 50 * k, '스테이지: %d' % i.stage, (200, 200, 200))
            hero.font.draw(300, 300 + 50 * k, '최종점수: %d' % i.score, (200, 200, 200))
            hero.font.draw(500, 300 + 50 * k, 'Time: %f' % i.time, (200, 200, 200))
            k += 1
    #for i in ss:
        #print(i)
    #k=0
    #for i in ss:
    #    hero.font.draw(300, 300 +50*k, '%d' %i, (200, 200, 200))
     #   k+=1

    update_canvas()


def collision(a,b):
    la,ba,ra,ta = a.get_bb()
    lb,bb,rb,tb = b.get_bb()
    az ,bz = a.z, b.z

    if la>rb: return False
    if ra<lb: return False
    if ta<bb: return False
    if ba>tb: return False
    if az-bz >0 :return False
    return True


def collision2(a,b):
    la,ba,ra,ta = a.get_bb()
    lb,bb,rb,tb = b.get_bb2()
    az ,bz = a.z, b.z

    if la>rb: return False
    if ra<lb: return False
    if ta<bb: return False
    if ba>tb: return False
    if az-bz >0 :return False
    return True
