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

DRAGON = []
scores = []
ss= []
k= 0
fileName = "genji_score.pickle"
show_rank = False
rank_image = None
mainbgm = None

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



def SaveScores():
    global scores
    f = open(fileName, "wb")
    pickle.dump(scores, f)
    f.close()


def enter():
    global hero, menu, back, st_num ,finish, mt, current_time, time_score, rank_image , show_rank , scores, ss,MAX_STAGE, dragon_time,DRAGON, mainbgm
    dragon_time =0
    DRAGON = []
    current_time = get_time()
    show_rank = False
    time_score = 0.0
    st_num = 1
    MAX_STAGE =6
    finish = False
    mt =0
    menu = Menu()
    hero = genji.Genji()
    scores = []
    ss = []
    loadScores()


    enemy.enemys.append(enemy.Robot(500, 250))
    enemy.enemys.append(enemy.Robot(800, 350))
    enemy.enemys.append(enemy.Robot(950, 200))
    back = background.Background()
    if rank_image == None:
        rank_image = load_image('랭킹.png')
        mainbgm = load_music('Hanamura.mp3')
        mainbgm.set_volume(128)
    mainbgm.repeat_play()


def exit():
    global hero, menu, back
    del(hero)
    del(menu)
    del(back)
    enemy.enemys=[]

def handle_events(frame_time):
    global  show_rank
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type , event.key) == (SDL_KEYDOWN, SDLK_SPACE) and show_rank:
            game_framework.change_state(title_state)
        else:
            hero.handle_events(event,frame_time)


def update(frame_time):
    global  mt,finish, st_num, current_time, time_score, show_rank, MAX_STAGE, dragon_time, DRAGON
    if show_rank == False:
        time_score = get_time() - current_time

    hero.update(frame_time)
    genji.bullet_update(frame_time)
    enemy.enemys_update(frame_time)
    effect.damage_update(frame_time)

    if st_num ==6:
        dragon_time+=1
        if dragon_time >750:
            DRAGON.append(enemy.Dragon(1400, hero.y + 200))
            DRAGON.append(enemy.Dragon(1400, hero.y + 100))
            DRAGON.append(enemy.Dragon(1400, hero.y ))
            dragon_time =0

    for i in DRAGON:
        i.update(frame_time)

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
                hero.hp = max(hero.hp-8,0)
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
            hero.hp = max(hero.hp - enemys.damage, 0)
            effect.damage_effect.append(effect.Effect_damage(hero.x, hero.y + 100))

    for i in DRAGON:
        if collision(hero, i) and hero.vlrur == False: # 겐지와 적 몸박
            hero.vlrur = True
            hero.hp = max(hero.hp - i.damage, 0)
            effect.damage_effect.append(effect.Effect_damage(hero.x, hero.y + 100))

    if hero.alive == False and show_rank == False:
        entry = Entry(max((int)((st_num)*1000+(st_num)*200 - time_score*25),0), time_score, st_num)
        add(entry)
        score_sort()
        show_rank = True
    if enemy.enemys == [] and finish == False and show_rank == False and hero.alive:#몬스터를 다 잡았을때
        if st_num ==MAX_STAGE: #클리어하고 기록해야함
            st_num+=1
            entry = Entry(max((int)((st_num)*1000+(st_num)*200 - time_score*25),0), time_score, st_num)
            add(entry)
            score_sort()
            show_rank = True
        if show_rank == False:
            effect.damage_effect.append(effect.Effect_Balck_IO())
            finish = True
            st_num +=1
    if finish and show_rank == False:
        mt += 1
        if mt>=60:
            if st_num ==2:
                enemy.enemys.append(enemy.Sold(500, 350))
                enemy.enemys.append(enemy.Sold(800, 200))
            elif st_num == 3:
                enemy.enemys.append(enemy.Reinhard(550, 200))
                enemy.enemys.append(enemy.Reinhard(550, 350))
                enemy.enemys.append(enemy.Reinhard(750, 275))
            elif st_num == 4:
                enemy.enemys.append(enemy.Sold(700, 350))
                enemy.enemys.append(enemy.Sold(400, 200))
                enemy.enemys.append(enemy.Robot(350, 400))
                enemy.enemys.append(enemy.Robot(540, 350))
                enemy.enemys.append(enemy.Robot(950, 200))
            elif st_num == 5:
                enemy.enemys.append(enemy.Sold(800, 250))
                enemy.enemys.append(enemy.Sold(100, 400))
                enemy.enemys.append(enemy.Sold(400, 200))
                enemy.enemys.append(enemy.Robot(350, 400))
                enemy.enemys.append(enemy.Robot(540, 350))
                enemy.enemys.append(enemy.Robot(950, 200))
                enemy.enemys.append(enemy.Reinhard(650, 200))
                enemy.enemys.append(enemy.Reinhard(650, 350))
                enemy.enemys.append(enemy.Reinhard(850, 275))
                enemy.enemys.append(enemy.Reinhard(1050, 350))
            elif st_num == 6:
                enemy.enemys.append(enemy.Hanjo(700, 300))
            else: pass
            hero.x, hero.y, hero.z = 100, 250, 0
            mt=0
            finish = False




    clear_canvas()


def draw(frame_time):
    global time_score,st_num, rank_image, DRAGON
    back.draw()
    rank_image.draw(565, 570, rank_image.w // 2, rank_image.h // 8)
    hero.font.draw(400, 570, 'Stage:%d' % st_num, (250, 250, 250))
    hero.font.draw(550, 570, 'Time:%f' % time_score, (250, 250, 250))

    enemy.enemys_draw(frame_time)
    if menu.Menu_OnOff == True:
        menu.draw()
    hero.draw()
    genji.bullet_draw(frame_time)
    effect.damage_draw(frame_time)
    k = 0
    for i in DRAGON:
        i.draw()

    if show_rank:
        rank_image.draw(600, 300)
        hero.font.draw(350, 530 , '순위   스테이지     최종점수        Time', (200, 200, 200))
        for i in ss:
            if k <=9:
                hero.font.draw(360, 440 - 40 * k, '%d' % (k+1), (200, 200, 200))
                hero.font.draw(460, 440 - 40 * k, '%d' % i.stage, (200, 200, 200))
                hero.font.draw(590, 440 - 40 * k, '%d' % i.score, (200, 200, 200))
                hero.font.draw(720, 440 - 40 * k, '%f' % i.time, (200, 200, 200))
            k += 1
        hero.font.draw(330, 480 , 'Now', (200, 0, 0))
        hero.font.draw(460, 480 , '%d' % st_num, (200, 0, 0))
        hero.font.draw(590, 480 , '%d' % max((int)(st_num * 1000+st_num*200 - time_score * 25), 0), (200, 0, 0))
        hero.font.draw(720, 480 , '%f' % time_score, (200, 0, 0))



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


def score_sort():
    global ss
    tempar= scores
    for j in range(len(tempar)):
        temp = 0
        savei= 0
        for i in range(len(tempar)):
            if tempar[i].score > temp:
                temp = tempar[i].score
                savei =i
        ss.append(Entry(tempar[savei].score,tempar[savei].time,tempar[savei].stage))
        for i in tempar:
            if i.score == temp:
                tempar.remove(i)
                break
