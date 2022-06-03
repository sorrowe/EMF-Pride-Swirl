from tidal import *
from app import App
from .drawfuncs import make_pretty

class MakePretty(App):

    def __init__(self):
        super().__init__()
        self.angle = 50
        self.jump = 2

    def on_activate(self):
        super().on_activate() # This will clear the screen by calling TextWindow.redraw()
        self.do_display()

        self.buttons.on_press(JOY_CENTRE, self.do_display)
        self.buttons.on_press(JOY_LEFT, lambda: self.angle_change(-10))
        self.buttons.on_press(JOY_RIGHT, lambda: self.angle_change(10))
        self.buttons.on_press(JOY_UP, lambda: self.jump_change(1))
        self.buttons.on_press(JOY_DOWN, lambda: self.jump_change(-1))

        #self.buttons.on_press(BUTTON_A, self.change_colour_set)
        
    def angle_change(self, change):
        self.angle = (self.angle + change) % 360

    def jump_change(self, change):
        self.jump = max(1, self.jump + change)

    def do_display(self):
        make_pretty(self.angle, self.jump)

    #def change_colour_set(self):



main = MakePretty