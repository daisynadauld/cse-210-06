"""This module get´s the information of the proretities 
of Coin that are defined with the methods in the Shape class"""

from game.casting.shape import Shape

class Coin(Shape):
    """
    An item that changes your score if you catch it. 
    
    The responsibility of Coin is to get the coin properities

    Attributes:
        _coin (str): the treusre.
    """
    def __init__(self):
        """Constructs a new Coin."""
        super().__init__()
        self._coin = ""

    def get_coin(self):
        """Gets the Coin information.
        
        Returns:
            string: The message.
        """
        return self._coin
    
    def set_coin(self, coin):
        """Updates the Coin to the given one.
        
        Args:
            Coin (string): a tresure.
        """
        self._coin = coin