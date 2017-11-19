from pico2d import*
import game_framework
import title_state
import start_state
import genji
import enemy

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

def enter():
    global hero, stage, menu
    menu = Menu()
    hero = genji.Genji()
    enemy.enemys.append(enemy.Robot(500,200))
    stage = Map()

def exit():
    del(hero)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            hero.handle_events(event)

def update():
    hero.update()
    genji.bullet_update()
    enemy.enemys_update()
    clear_canvas()
    delay(0.020)
def draw():
    stage.draw()
    hero.draw()
    genji.bullet_draw()
    enemy.enemys_draw()
    if menu.Menu_OnOff == True:
        menu.draw()
    update_canvas()



