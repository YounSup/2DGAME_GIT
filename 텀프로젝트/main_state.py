from pico2d import*
import effect
import game_framework
import title_state
import start_state
import genji
import enemy
import background


class Menu:
    def __init__(self):
        self.image = load_image('인게임메뉴.png')
        self.Menu_OnOff = False;
    def draw(self):
        self.image.draw(600,300)

def enter():
    global hero, stage, menu, back
    menu = Menu()
    hero = genji.Genji()
    enemy.enemys.append(enemy.Robot(500,200))
    enemy.enemys.append(enemy.Sold(150,250))
    enemy.enemys.append(enemy.Reinhard(800,350))
    enemy.enemys.append(enemy.Para(1000,500,200))
    back = background.Background()


def exit():
    del(hero)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            hero.handle_events(event,frame_time)


def update(frame_time):

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

        elif bullet.index >= 1:  #적총알과 겐지 충돌중
            if collision(bullet, hero) and  hero.protect_onoff == False:
                bullet.delete = True
                effect.damage_effect.append(effect.Effect_damage(hero.x, hero.y+100))
                hero.hp -= 10
            elif collision(bullet, hero) and  hero.protect_onoff == True:
                bullet.out = True
                if bullet.state == 0:
                    bullet.state = 1
                else :
                    bullet.state = 0


    clear_canvas()
    delay(0.020)

def draw(frame_time):
    back.draw()

    enemy.enemys_draw(frame_time)
    if menu.Menu_OnOff == True:
        menu.draw()
    hero.draw()
    genji.bullet_draw(frame_time)
    effect.damage_draw(frame_time)
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
