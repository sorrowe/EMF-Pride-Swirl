
from tidal import *
from app import TextApp, MenuApp
from .drawfuncs import make_pretty, COLOUR_SETS, colour_list_to_string, COLOUR_SET_SETTINGS_KEY
import settings
from buttons import Buttons
from textwindow import TextWindow

import vga2_8x8 as default_font

DEFAULT_CUSTOM = COLOUR_SETS[0]

DEFAULT_COLOUR_SET = "EMFPride_default_colour_set"
DEFAULT_JUMP = "EMFPride_default_jump"
DEFAULT_ANGLE = "EMFPride_default_angle"

class EMFPrideSwirl(MenuApp):
    TITLE = "EMF PRIDE SWIRL"

    def __init__(self):
        super().__init__()
        self.draw_window = None
        self.setting_window = None
        choices = (
            ("DRAW", self.do_draw),
            ("CUSTOM", self.do_settings),
            ("HELP", lambda: print("Selected HELP!")),
        )

        self.window.set_choices(choices)

    def do_draw(self):
        if not self.draw_window:
            new_buttons = Buttons()
            new_buttons.on_press(BUTTON_B, self.pop_window)
            self.draw_window = ColoursWindow(buttons=new_buttons)

        self.push_window(self.draw_window, activate=True)
        self.window.do_display()
    
    def do_settings(self):

        custom_colours = settings.get(COLOUR_SET_SETTINGS_KEY)
        if not custom_colours:
            custom_colours = colour_list_to_string(COLOUR_SETS[0][0])
        
        new_colours = self.keyboard_prompt("hex list:", custom_colours)
        if new_colours != custom_colours:
            settings.set(COLOUR_SET_SETTINGS_KEY, new_colours)
            settings.save()


class ColoursWindow(TextWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.angle = settings.get(DEFAULT_ANGLE, 50)
        self.jump = settings.get(DEFAULT_JUMP, 2)
        self.colour_set = settings.get(DEFAULT_COLOUR_SET, 1)
        if self.buttons:
            buttons = self.buttons
            buttons.on_press(JOY_CENTRE, self.do_display)
            buttons.on_press(JOY_LEFT, lambda: self.angle_change(-10))
            buttons.on_press(JOY_RIGHT, lambda: self.angle_change(10))
            buttons.on_press(JOY_UP, lambda: self.jump_change(1))
            buttons.on_press(JOY_DOWN, lambda: self.jump_change(-1))

            buttons.on_press(BUTTON_A, self.change_colour_set)

        
    def angle_change(self, change):
        self.angle = (self.angle + change) % 360
        settings.set(DEFAULT_ANGLE, self.angle)
        settings.save()

    def jump_change(self, change):
        self.jump = max(1, self.jump + change)
        settings.set(DEFAULT_JUMP, self.jump)
        settings.save()

    def do_display(self):
        make_pretty(self.angle, self.jump, self.colour_set)

    def change_colour_set(self):
        self.colour_set = (self.colour_set + 1) % len(COLOUR_SETS)
        display.fill_rect(0, 230, 135, 10, BLACK)
        display.text(default_font, "{}:{}".format(self.colour_set, self.get_colour_name()), 1, 231, WHITE)
        settings.set(DEFAULT_COLOUR_SET, self.colour_set)
        settings.save()

    def get_colour_name(self):
        return COLOUR_SETS[self.colour_set][1]


main = EMFPrideSwirl