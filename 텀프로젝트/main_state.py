from pico2d import*
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
    enemy.enemys.append(enemy.Sold(150,380))
    enemy.enemys.append(enemy.Reinhard(800,350))
    enemy.enemys.append(enemy.Para(1000,500))
    back = background.Background()


def exit():
    del(hero)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            hero.handle_events(event)


def update(frame_time):

    hero.update(frame_time)
    genji.bullet_update(frame_time)
    enemy.enemys_update(frame_time)

    clear_canvas()
    delay(0.020)
    
def draw(frame_time):
    clear_canvas()
    back.draw()

    enemy.enemys_draw(frame_time)
    if menu.Menu_OnOff == True:
        menu.draw()
    hero.draw()
    genji.bullet_draw(frame_time)
    update_canvas()



