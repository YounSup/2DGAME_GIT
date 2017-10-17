from pico2d import*
import random
import game_framework
import start_state
import main_state
import title_state
import json

BOYNUM = 5


LKC=0
RKC=0

class Grass:
 def __init__(self):
  self.image = load_image('grass.png')
 def draw(self):
  self.image.draw(400, 30)

class Boy:
    image = None
  
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0,1,2,3
    stand_frames, run_frames =0,0
    def __init__(self):
      self.x, self.y = random.randint(100, 700), random.randint(50,550)
      self.frame = random.randint(0,7)
      self.dir =1
      self.state = 3
      if Boy.image == None :
          Boy.image = load_image('animation_sheet.png')
      self.select = False;

    def handle_left_run(self):
        self.x -=5
        self.run_frames +=1
        if self.x<0:
            self.state = self.RIGHT_RUN
            self.x=0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0
            
    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0
            
    def handle_right_run(self):
        self.x +=5
        self.run_frames += 1
        if self.x>800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0
            
    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames =0



    handle_state = {
    LEFT_RUN: handle_left_run,
    RIGHT_RUN: handle_right_run,
    LEFT_STAND: handle_left_stand,
    RIGHT_STAND: handle_right_stand
    }
    


    def update(self):
      self.frame = (self.frame +1)%8
     # self.handle_state[self.state](self)

      if self.state == self.RIGHT_RUN:
          self.x = min (800, self.x +5)
      elif self.state == self.LEFT_RUN:
          self.x = max(0, self.x - 5)
    
    def draw(self):
      self.image.clip_draw(self.frame*100,self.state*100, 100, 100, self.x, self.y)
     
    
            
def enter():
    global boy, grass, team, select_num,data
    grass = Grass()
    boy = Boy()
    #team = [Boy() for i in range(BOYNUM)]
    select_num = 0
    print('Select Num : {}'.format(select_num))

    data_file = open('team_data.json','r')
    data=json.load(data_file)
    data_file.close()

    plyer_state_table = {
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN" : Boy.RIGHT_RUN,
        "LEFT_STAND": Boy.LEFT_STAND,
        "RIGHT_STAND": Boy.RIGHT_STAND,
    }

    team = []
    for name in data:
        player = Boy()
        player.name = name
        player.x = data[name]['x']
        player.y = data[name]['y']
        player.state = plyer_state_table[data[name]['StartState']]
        team.append(player)

    return team
    team[select_num].select = True;

def exit():
    global boy, grass
    del(boy)
    del(grass)

def handle_events():
    global select_num, RKC, LKC
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if team[select_num].state in (team[select_num].RIGHT_STAND, team[select_num].LEFT_STAND):
                team[select_num].state = team[select_num].LEFT_RUN


        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if team[select_num].state in (team[select_num].RIGHT_STAND, team[select_num].LEFT_STAND):
                team[select_num].state = team[select_num].RIGHT_RUN

        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            if team[select_num].state in (team[select_num].RIGHT_RUN,team[select_num].LEFT_RUN):
                team[select_num].state = team[select_num].RIGHT_STAND


        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            if team[select_num].state in (team[select_num].LEFT_RUN,team[select_num].RIGHT_RUN):
                team[select_num].state = team[select_num].LEFT_STAND


        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if select_num < BOYNUM-1:
                select_num +=1
                print('Select Num : {}'.format(select_num))
                for boy in team:
                    boy.select = False;
                    team[select_num].select = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if select_num > 0:
                select_num -=1
                print('Select Num : {}'.format(select_num))
                for boy in team:
                    boy.select = False;
                    team[select_num].select = True

      #  elif event.type == SDL_MOUSEMOTION:
      #     for boy in team:
      #      if boy.select == True:
      #       boy.x, boy.y = event.x, 600- event.y

def update():
    for boy in team:
        boy.update()
    delay(0.05)
def draw():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    
    update_canvas()
    


