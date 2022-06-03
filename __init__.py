
from tidal import *
from app import TextApp
from .drawfuncs import make_pretty, COLOUR_SETS
import settings

import vga2_8x8 as default_font

DEFAULT_CUSTOM = COLOUR_SETS[0]

class MakePretty(TextApp):

    def __init__(self):
        super().__init__()
        self.angle = 50
        self.jump = 2
        self.colour_set = 0

    def on_activate(self):
        super().on_activate() # This will clear the screen by calling TextWindow.redraw()
        self.do_display()

    def on_start(self):
        super().on_start()
        self.buttons.on_press(JOY_CENTRE, self.do_display)
        self.buttons.on_press(JOY_LEFT, lambda: self.angle_change(-10))
        self.buttons.on_press(JOY_RIGHT, lambda: self.angle_change(10))
        self.buttons.on_press(JOY_UP, lambda: self.jump_change(1))
        self.buttons.on_press(JOY_DOWN, lambda: self.jump_change(-1))

        self.buttons.on_press(BUTTON_A, self.change_colour_set)
        #self.buttons.on_press(BUTTON_B, self.set_custom)
        
    def angle_change(self, change):
        self.angle = (self.angle + change) % 360

    def jump_change(self, change):
        self.jump = max(1, self.jump + change)

    def do_display(self):
        make_pretty(self.angle, self.jump, self.colour_set)

    def change_colour_set(self):
        self.colour_set = (self.colour_set + 1) % len(COLOUR_SETS)
        display.fill_rect(0, 230, 135, 10, BLACK)
        display.text(default_font, "{}:{}".format(self.colour_set, self.get_colour_name()), 1, 231, WHITE)

    def get_colour_name(self):
        return COLOUR_SETS[self.colour_set][1]

    def set_to_string(self, colour_set):
        colours = colour_set[0]
        string_list = ['#%02x%02x%02x' % x for x in colours]
        return ", ".join(string_list)

    def set_custom(self):
        current_colours = self.set_to_string(0)
        new_colours = self.keyboard_prompt("hex, comma seperated:", current_colours, multiline_allowed=True)
        if new_colours != current_colours:
            settings.set("custom_flag", new_colours)
            settings.save()


main = MakePretty