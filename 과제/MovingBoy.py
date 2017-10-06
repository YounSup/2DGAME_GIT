from pico2d import*
import random

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

def handle_events():
 global running
 events = get_events()
 for event in events:
  if event.type == SDL_QUIT:
   close_canvas()
  elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
   close_canvas()
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
   for boy in team:
    boy.select = False;
   team[0].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F2:
   for boy in team:
    boy.select = False;
   team[1].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F3:
   for boy in team:
    boy.select = False;
   team[2].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F4:
   for boy in team:
    boy.select = False;
   team[3].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F5:
   for boy in team:
    boy.select = False;
   team[4].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F6:
   for boy in team:
    boy.select = False;
   team[5].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F7:
   for boy in team:
    boy.select = False;
   team[6].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F8:
   for boy in team:
    boy.select = False;
   team[7].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F9:
   for boy in team:
    boy.select = False;
   team[8].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F10:
   for boy in team:
    boy.select = False;
   team[9].select = True
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F11:
   for boy in team:
    boy.select = False;
   team[10].select = True
  elif event.type == SDL_MOUSEMOTION:
   for boy in team:
    if boy.select == True:
     boy.x, boy.y = event.x, 600- event.y

team = [Boy() for i in range(11)]
running = True;
grass = Grass()

while running:
 handle_events()
 for boy in team:
  boy.update()
 clear_canvas()
 grass.draw()
 for boy in team:
  boy.draw()
 update_canvas()
  
 delay(0.05)
