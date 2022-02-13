"""The Director module keeps track of the cycle of the game. 
It loops through the input, updates, and output phases until 
the game ends."""

from game.shared.point import Point
from game.services.keyboard_service import KeyboardService
from game.casting.score import Score
import random
import raylib

class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast, keyboard_service, score):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(keyboard_service)
            self._do_updates(cast, score)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, keyboard_service):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._keyboard_service = keyboard_service.get_mouse_input()

    def _do_updates(self, cast, score):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of shapes.
        """
        banner = cast.get_first_shape("banners")
        coins = cast.get_shapes("coins")
        banner.set_text(f"Score: {self._score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        direction = self._keyboard_service
        
        
        
        for coin in coins:
            coin.move_next(max_x, max_y)
            if direction.__eq__(coin.get_position()):
                if raylib.IsMouseButtonPressed(raylib.MOUSE_BUTTON_LEFT):
                    cast.remove_shape("coins", coin)
                    self._score = score.add_points()
                    banner.set_text(f"Score: {self._score}")
                    cast.add_shape("coin", coin)
                    coin._position = Point(random.randint(1, max_x))
                    coin._velocity = Point(0, random.randint(3, 5))


    def _do_outputs(self, cast):
        """Draws the shapes on the screen.
        
        Args:
            cast (Cast): The cast of shapes.
        """
        self._video_service.clear_buffer()
        shapes = cast.get_all_shapes()
        self._video_service.draw_shapes(shapes)
        self._video_service.flush_buffer() 
