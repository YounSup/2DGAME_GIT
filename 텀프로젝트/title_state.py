from pico2d import *
import game_framework
import main_state
import start_state
import effect
import genji
import enemy

name = "TitleState"
image = None
bgm = None
def enter():
    global image, bgm
    image = load_image('게임메뉴화면1.jpg')
    bgm = load_music('characterSelectStage.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
def exit():
    global image, bgm
    del(image)
    del(bgm)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == ( SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw(frame_time):
    clear_canvas()
    image.draw(600,300)
    update_canvas()

def pause():
    pass
def update(frame_time):
    pass
