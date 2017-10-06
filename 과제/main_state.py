from pico2d import*
import random
import game_framework
import start_state
import main_state
import title_state

open_canvas()

class Grass:
 def __init__(self):
  self.image = load_image('grass.png')
 def draw(self):
  self.image.draw(400, 30)

class Boy:
 def __init__(self):
  self.x, self.y = random.randint(100, 700), random.randint(100,400)
  self.frame = random.randint(0,7)
  self.image = load_image('run_animation.png')
  self.select = False;
 def update(self):
  self.frame = (self.frame + 1) % 8
  self.x += 2
  if self.x > 800:
   self.x=0
 def draw(self):
  self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

def enter():
    global boy, grass
    grass = Grass()
    boy = Boy()


def exit():
    global boy, grass
    del(boy)
    del(grass)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


def update():
    boy.update()
def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


