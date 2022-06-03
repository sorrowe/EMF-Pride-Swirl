
from tidal import *
from math import radians, floor
import settings
import vga2_8x8 as default_font

MAX_HEIGHT = 240
MAX_WIDTH = 135

COLOUR_SET_SETTINGS_KEY = "EMFPride_custom_pride_flag"


COLOUR_SETS = (
    (
        (
            (255, 0, 24),
            (255, 165, 44),
            (255, 255, 65),
            (0, 128, 24),
            (0, 0, 249),
            (134, 0, 125),
        ),
        "Custom"
    ),
    (
        (
            (255, 0, 24),
            (255, 165, 44),
            (255, 255, 65),
            (0, 128, 24),
            (0, 0, 249),
            (134, 0, 125),
        ),
        "Classic"
    ),
    (
        (
            (255, 0, 24),
            (255, 165, 44),
            (255, 255, 65),
            (0, 128, 24),
            (0, 0, 249),
            (134, 0, 125),
            (255, 255, 255),
            (245, 169, 184),
            (91, 206, 250),
            (97, 54, 2),
            (0, 0, 0),
        ),
        "Progress"
    ),
    (
        (
            (91, 206, 250),
            (245, 169, 184),
            (255, 255, 255),
            (245, 169, 184),
            (91, 206, 250),
        ),
        "Trans"
    ),
    (
        (
            (255, 244, 48),
            (255, 255, 255),
            (156, 89, 209),
            (0, 0, 0),
        ),
        "NB"
    ),
    (
        (
            (255, 27, 141),
            (255, 218, 0),
            (27, 179, 255),
        ),
        "Pan"
    ),
    (
        (
            (208, 0, 112),
            (140, 71, 153),
            (0, 50, 160),
        ),
        "Bi"
    ),
    (
        (
            (0, 0, 0),
            (164, 164, 164),
            (255, 255, 255),
            (129, 0, 129),
        ),
        "Asexual"
    ),
)

def get_angle(i, steps, sweep):
    return radians((i/steps) * sweep);

def get_colour_list(i):
    colour_list = COLOUR_SETS[i][0]
    if i == 0:
        custom_colours = settings.get(COLOUR_SET_SETTINGS_KEY)
        if custom_colours:
            new_list = string_to_colour_list(custom_colours)
            if len(new_list) > 0:
                colour_list = new_list
    return colour_list

def get_colour(i, colour_list):
    return color565(*colour_list[i % len(colour_list)])

def draw_square(w_off, h_off, colour, rotation=0):
    poly = [
        (w_off, h_off),
        (MAX_WIDTH - w_off, h_off),
        (MAX_WIDTH - w_off, MAX_HEIGHT - h_off),
        (w_off, MAX_HEIGHT - h_off),
        (w_off, h_off),
    ] 

    display.fill_polygon(poly, 0, 0, colour, rotation, floor(MAX_WIDTH/2), floor(MAX_HEIGHT/2))


def make_pretty(angle_sweep = 50, jump = 2, colour_set = 0):
    
    steps = floor(MAX_WIDTH/(2*jump))
    h_step = (MAX_HEIGHT/2)/steps
    
    colour_list = get_colour_list(colour_set)
    display.fill(get_colour(0, colour_list))
    for i in range(0,steps):
        angle = get_angle(i, steps, angle_sweep)
        draw_square(i*jump, round(i*h_step), get_colour(i, colour_list), angle)


def colour_list_to_string(colour_list):
    string_list = ['#%02x%02x%02x' % x for x in colour_list]
    return ", ".join(string_list)

def string_to_colour_list(colour_string):
    colour_list = []
    hex_list = colour_string.split(",")
    for hex_string in hex_list:
        rgb = read_hex_string(hex_string)
        if rgb:
            colour_list.append(rgb)
    
    return colour_list

def read_hex_string(hex_str):
    hex_str = hex_str.strip()
    if len(hex_str) == 7 and hex_str[0] == "#":
        hex_str = hex_str[1:]
    if len(hex_str) == 6:
        try:
            rgb = (int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6],16))
        except:
            return None
        
        return rgb
    return None