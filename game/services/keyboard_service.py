"""This module takes care of all the input from
the keyboard."""

import pyray
import raylib
from game.shared.point import Point
from game.casting.score import Score


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size
        self._total_score = 0

    def get_mouse_input(self, score):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """

        while raylib.IsMouseButtonPressed(raylib.MOUSE_BUTTON_LEFT):
            if raylib.MOUSE_BUTTON_LEFT.equals(coin.get_position()):
                coin.remove_shape("coins", coin.get_position())
                self.total_score = score.add_points()
                return self.total_score 