from pico2d import *
import game_framework
import title_state

name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    open_canvas(1200,600,sync=True)
    image=load_image('kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()

def update(frame_time):
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state) 
    delay(0.01)
    logo_time += 0.01
    
def draw(frame_time):
    global image
    clear_canvas()
    image.draw(600, 300)
    update_canvas()

def handle_events(frame_time):
    global a

def pause():
    a =10
def resume():
    a=10
    
