from tidal import *
from math import radians, floor

MAX_HEIGHT = 240
MAX_WIDTH = 135

COLOUR_LIST = [RED, BRAND_ORANGE, BRAND_YELLOW, GREEN, BLUE, MAGENTA, ADDITIONAL_PURPLE]
COLOUR_LIST_2 = [RED, BLUE]

def get_angle(i, steps, sweep):
    return radians((i/steps) * sweep);

def get_colour(i):
    return COLOUR_LIST[i % len(COLOUR_LIST)]

def draw_square(w_off, h_off, colour, rotation=0):
    poly = [
        (w_off, h_off),
        (MAX_WIDTH - w_off, h_off),
        (MAX_WIDTH - w_off, MAX_HEIGHT - h_off),
        (w_off, MAX_HEIGHT - h_off),
        (w_off, h_off),
    ] 

    display.fill_polygon(poly, 0, 0, colour, rotation, floor(MAX_WIDTH/2), floor(MAX_HEIGHT/2))


def make_pretty(angle_sweep = 50, jump = 2):
    
    steps = floor(MAX_WIDTH/(2*jump))
    h_step = (MAX_HEIGHT/2)/steps
    
    display.fill(CYAN)
    for i in range(0,steps):
        angle = get_angle(i, steps, angle_sweep)
        #x_offset = i*jump
        #y_offset = round(i*h_step)
        #display.draw_rect(x_offset, y_offset, MAX_WIDTH-2*x_offset, MAX_HEIGHT - 2*y_offset, get_colour(i))
        draw_square(i*jump, round(i*h_step), get_colour(i), angle)

