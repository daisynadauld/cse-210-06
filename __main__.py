"""The main module starts the 'Greed' game that
allows you to catch gems or rocks that fall from
the top of the screen. Main creates a list of gems
and rocks for the game to manipulate."""

import os
import random

from game.casting.shape import Shape
from game.casting.mineral import Mineral
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
ROBOT_FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed"
YELLOW = Color(255,233,0)
DEFAULT_MINERAL = 40


def main():
    """Creates the characters of the game and starts
    the game."""
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner =Shape()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(YELLOW)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_shape("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)

    robot =Shape()
    robot.set_text("#")
    robot.set_font_size(ROBOT_FONT_SIZE)
    robot.set_color(YELLOW)
    robot.set_position(position)
    cast.add_shape("robots", robot)
    
    # create the minerals
    for n in range(DEFAULT_MINERAL):
        character = random.randint(1, 2)
        name = ""
        if character == 1:
            name = "0" #rock
        else:
            name = "*" #gem

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        
        velocity = Point(0, random.randint(3, 5))

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        mineral = Mineral()
        mineral.set_text(name)
        mineral.set_font_size(FONT_SIZE)
        mineral.set_color(color)
        mineral.set_position(position)
        mineral.set_velocity(velocity)

        cast.add_shape("minerals", mineral) 
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
