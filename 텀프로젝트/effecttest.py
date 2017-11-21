from pico2d import *
class Background:
    image =None
    def __init__(self):
        if Background.image == None:
            Background.image = load_image('background.jpg')

    def draw(self):
        Background.image.draw(600,300)
