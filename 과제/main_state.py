from pico2d import*
import random
import game_framework
import start_state
import main_state
import title_state

BOY_SPEED = 20.0  #보이의 속도 조절
MAX_ANIMATION_TIME = 0.1 #0.1초마다 애니메이션프레임을 증가시킨다. 애니메이션 프레임속도 조절

Animation_time =0
current_time = get_time()

class Grass:
 def __init__(self):
  self.image = load_image('grass.png')
 def draw(self):
  self.image.draw(400, 30)

class Boy:
    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH = BOY_SPEED
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0,1,2,3
    stand_frames, run_frames =0,0
    def __init__(self):
      self.x, self.y = random.randint(100, 700), random.randint(50,550)
      self.frame = random.randint(0,7)
      self.dir =-1
      self.state = 0
      self.total_frames =0
      if Boy.image == None :
          Boy.image = load_image('인디아나존스실사그자체.png')





    def update(self):
      global current_time, Animation_time
      frame_time = get_time() - current_time
      frame_rate = 1.0 / frame_time
      Animation_time += frame_time
      print("Frame Rate: %f fps, Frame Time : %f sec, Animation_Time : %f " % (frame_rate, frame_time, Animation_time))

      distance = Boy.RUN_SPEED_PPS* frame_time
      self.total_frames += 1.0
      if Animation_time> MAX_ANIMATION_TIME:
        self.frame = (self.frame +1)%7 #현재는 프레임마다 애니메이션이 바뀐다. => 이를 일정시간지나면 바뀌게 해야함.
        Animation_time = 0
      self.x += (self.dir*distance)

      if self.x>800:
          self.dir = -1
          self.x =800
          self.state = self.LEFT_RUN
          print("Change Time: %f, Total Frames : %d" %(get_time(), self.total_frames))
      if self.x < 0:
          self.dir = 1
          self.x = 0
          self.state = self.RIGHT_RUN
          print("Change Time: %f, Total Frames : %d" %(get_time(), self.total_frames))
      current_time += frame_time


    
    def draw(self):
      self.image.clip_draw(self.frame*30,0, 30, 48, self.x, self.y)

    
            
def enter():
    global boy, grass, team
    grass = Grass()
    boy = Boy()




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


def update():
    boy.update()
   # delay(0.01)




def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()



