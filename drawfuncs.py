
from tidal import *
from math import radians, floor

MAX_HEIGHT = 240
MAX_WIDTH = 135


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

def get_colour(i, set):
    colour_list = COLOUR_SETS[set][0]
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


def make_pretty(angle_sweep = 50, jump = 2, set = 0):
    
    steps = floor(MAX_WIDTH/(2*jump))
    h_step = (MAX_HEIGHT/2)/steps
    
    display.fill(get_colour(0, set))
    for i in range(0,steps):
        angle = get_angle(i, steps, angle_sweep)
        #x_offset = i*jump
        #y_offset = round(i*h_step)
        #display.draw_rect(x_offset, y_offset, MAX_WIDTH-2*x_offset, MAX_HEIGHT - 2*y_offset, get_colour(i))
        draw_square(i*jump, round(i*h_step), get_colour(i, set), angle)

