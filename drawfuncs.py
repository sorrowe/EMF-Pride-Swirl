
from tidal import display
from math import radians, floor
from .flag_colours import get_colour, get_flag_colours
import settings

MAX_HEIGHT = 240
MAX_WIDTH = 135

def get_angle(i, steps, sweep):
    return radians((i/steps) * sweep);


def draw_square(w_off, h_off, colour, rotation=0):
    poly = [
        (w_off, h_off),
        (MAX_WIDTH - w_off, h_off),
        (MAX_WIDTH - w_off, MAX_HEIGHT - h_off),
        (w_off, MAX_HEIGHT - h_off),
        (w_off, h_off),
    ] 

    display.fill_polygon(poly, 0, 0, colour, rotation, floor(MAX_WIDTH/2), floor(MAX_HEIGHT/2))


def draw_pretty_thing(angle_sweep = 50, jump = 2, colour_set = 0):
    
    steps = floor(MAX_WIDTH/(2*jump))
    h_step = (MAX_HEIGHT/2)/steps
    
    colour_list = get_flag_colours(colour_set)
    display.fill(get_colour(0, colour_list))
    for i in range(0,steps):
        angle = get_angle(i, steps, angle_sweep)
        draw_square(i*jump, round(i*h_step), get_colour(i, colour_list), angle)
