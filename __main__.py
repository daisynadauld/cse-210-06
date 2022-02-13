"""The main module starts the 'Treasure Hunt' game that
allows you to catch coins that fall from
the top of the screen. Main creates a list of coins for the game to manipulate."""

import os
import random


from game.casting.shape import Shape
from game.casting.coin import Coin
from game.casting.cast import Cast
from game.casting.score import Score
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
    
    # create the minerals
    character = ""
    x = random.randint(1, COLS - 1)
    y = random.randint(1, ROWS - 1)
    position = Point(x, y)
    position = position.scale(CELL_SIZE)   
    velocity = Point(0, random.randint(3, 5))
    color = YELLOW
    
    coins = Coin()
    coins.set_text(character)
    coins.set_font_size(FONT_SIZE)
    coins.set_color(color)
    coins.set_position(position)
    coins.set_velocity(velocity)

    cast.add_shape("coins", coins) 
    # creats score
    score = Score()

   
    
    # start the game
    keyboard_services = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_services, video_service)
    director.start_game(cast, keyboard_services, score)


if __name__ == "__main__":
    main()
