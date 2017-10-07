from pico2d import *
open_canvas(1200,600)



image2 = load_image('stage1-1.jpg')
image2.draw(600,300)
update_canvas()

class Genji:
    def __init__(self):
        self.x, self.y =100,50
        self.bodyframe = 0
        self.attackstate=0
        self.attackframe=0
        self.image = load_image('겐지스프라이트.png')
        self.imageleft= load_image('겐지스프라이트왼쪽.png')
        self.genjistate=0
        self.KEYCHECK_LEFT,self.KEYCHECK_RIGHT = 0, 0 #키눌림용 변수
    def update(self):
        self.bodyframe = (self.bodyframe +1) %13

        if self.attackframe >= 13:
            self.attackframe =0
            self.attackstate =0
        
        if self.attackstate ==1:
            self.attackframe = self.attackframe +1


        if self.KEYCHECK_LEFT == 1:
            self.x -= 2
            
        if self.KEYCHECK_RIGHT == 1:
            self.x += 2
            
        if self.x>800:
            self.x=0
        elif self.x<0:
            self.x=750
    def draw(self):
        if self.genjistate == 0: #겐지가 오른쪽볼때
            self.image.clip_draw(self.bodyframe*300,600,300,300,self.x,self.y)
            if self.attackstate == 0:
                self.image.clip_draw(self.bodyframe*300,300,300,300,self.x,self.y)
            elif self.attackstate == 1:
                self.image.clip_draw(self.attackframe*300,0,300,300,self.x,self.y)
         
                
        elif self.genjistate ==1: #겐지가 왼쪽볼때
            self.imageleft.clip_draw(self.bodyframe*300,600,300,300,self.x,self.y)
            if self.attackstate  == 0:
                self.imageleft.clip_draw(self.bodyframe*300,300,300,300,self.x,self.y)
            elif self.attackstate == 1:
                self.imageleft.clip_draw(self.attackframe*300,0,300,300,self.x,self.y)


genji=Genji()
genji.genjistate =0
running = True;

def handle_events():
 global running
 events = get_events()
 for event in events:
  if event.type == SDL_QUIT:
   close_canvas()
  elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
   close_canvas()

   
  elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
   genji.genjistate =1
   genji.KEYCHECK_LEFT=1
  elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
   genji.KEYCHECK_LEFT=0
   
  elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
   genji.genjistate =0
   genji.KEYCHECK_RIGHT=1
  elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
   genji.KEYCHECK_RIGHT=0

   
  elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
   genji.attackstate = 1
   


while running:
   handle_events()
   genji.update()
   clear_canvas()
   image2.draw(600,300)
   genji.draw()
   update_canvas()
   delay(0.02)
