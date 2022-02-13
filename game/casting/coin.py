"""This module takes care of the score of the game
by adding or subtracting points depending on whether
you catch a gem or a rock."""

from game.casting.shape import Shape

class Coin(Shape):
    """
    An item that changes your score if you catch it. 
    
    The responsibility of Mineral is to give a point when a gem is caught
    and take away a point if a rock is caught.

    Attributes:
        _score (int): The amount you gain or lose when you catch a gem or rock.
    """
    def __init__(self):
        """Constructs a new Mineral."""
        super().__init__()
        self._coin = "$"
        
    def get_coin(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._coin
    
    def set_coin(self, coin):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._coin = coin
