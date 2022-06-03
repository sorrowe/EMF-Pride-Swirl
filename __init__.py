
from tidal import *
from app import MenuApp
from .drawfuncs import draw_pretty_thing
from .flag_colours import FLAGS, CUSTOM_FLAG_SETTINGS_KEY, get_flag_name, get_custom_flag_default
import settings
from buttons import Buttons
from textwindow import TextWindow

import vga2_8x8 as default_font

DEFAULT_FLAG_SETTINGS_KEY = "EMFPride_default_colour_set"
DEFAULT_JUMP_SETTINGS_KEY = "EMFPride_default_jump"
DEFAULT_ANGLE_SETTINGS_KEY = "EMFPride_default_angle"

class EMFPrideSwirl(MenuApp):
    TITLE = "EMF PRIDE SWIRL"

    def __init__(self):
        super().__init__()
        self.draw_window = None
        self.help_window = None
        choices = (
            ("DRAW", self.do_draw),
            ("CUSTOM", self.do_settings),
            ("HELP", self.do_help),
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

        custom_colours = settings.get(CUSTOM_FLAG_SETTINGS_KEY)
        if not custom_colours:
            custom_colours = get_custom_flag_default()
        
        new_colours = self.keyboard_prompt("hex list:", custom_colours)
        if new_colours != custom_colours:
            settings.set(CUSTOM_FLAG_SETTINGS_KEY, new_colours)
            settings.save()

    def do_help(self):
        if not self.help_window:
            new_buttons = Buttons()
            new_buttons.on_press(BUTTON_B, self.pop_window)
            self.help_window = TextWindow(title="Help", buttons=new_buttons)

        self.push_window(self.help_window, activate=True)
        self.window.cls()
        self.window.println("Draw Mode")
        self.window.println(" B: Back")
        self.window.println(" A: Change flag")
        self.window.println(" U/D: step size")
        self.window.println(" L/R: angle")
        self.window.println(" PRESS: redraw")
        self.window.println("")
        
        self.window.println("Custom")
        self.window.println(" Enter comma")
        self.window.println(" seperated list")
        self.window.println(" of hex values")
        self.window.println("")
        
        self.window.println("Help")
        self.window.println(" B: Back")
        self.window.println("")
        self.window.println(" Hi, code here:")

        lines = self.window.flow_lines("https://github.com/sorrowe/EMF-Pride-Swirl")
        for line in lines:
            self.window.println(line)


class ColoursWindow(TextWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.angle = settings.get(DEFAULT_ANGLE_SETTINGS_KEY, 50)
        self.jump = settings.get(DEFAULT_JUMP_SETTINGS_KEY, 2)
        self.colour_set = settings.get(DEFAULT_FLAG_SETTINGS_KEY, 1)
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
        settings.set(DEFAULT_ANGLE_SETTINGS_KEY, self.angle)
        settings.save()

    def jump_change(self, change):
        self.jump = max(1, self.jump + change)
        settings.set(DEFAULT_JUMP_SETTINGS_KEY, self.jump)
        settings.save()

    def do_display(self):
        draw_pretty_thing(self.angle, self.jump, self.colour_set)

    def change_colour_set(self):
        self.colour_set = (self.colour_set + 1) % len(FLAGS)
        display.fill_rect(0, 230, 135, 10, BLACK)
        display.text(default_font, "{}:{}".format(self.colour_set, get_flag_name(self.colour_set)), 1, 231, WHITE)
        settings.set(DEFAULT_FLAG_SETTINGS_KEY, self.colour_set)
        settings.save()


main = EMFPrideSwirl