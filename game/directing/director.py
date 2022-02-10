"""The Director module keeps track of the cycle of the game. 
It loops through the input, updates, and output phases until 
the game ends."""

from game.shared.point import Point
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._total_score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_shape("robots")
        velocity = self._keyboard_service.get_direction()

        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of shapes.
        """
        banner = cast.get_first_shape("banners")
        robot = cast.get_first_shape("robots")
        minerals = cast.get_shapes("minerals")

        banner.set_text("Score: {}".format(self._total_score))
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for mineral in minerals:
            
            mineral.move_next(max_x, max_y)
            
            if robot.get_position().equals(mineral.get_position()):
                self._total_score = mineral.calc_score(self._total_score)
                banner.set_text("Score: {}".format(self._total_score))
                mineral._position = Point(random.randint(1, max_x), 0)
                

    def _do_outputs(self, cast):
        """Draws the shapes on the screen.
        
        Args:
            cast (Cast): The cast of shapes.
        """
        self._video_service.clear_buffer()
        shapes = cast.get_all_shapes()
        self._video_service.draw_shapes(shapes)
        self._video_service.flush_buffer() 
