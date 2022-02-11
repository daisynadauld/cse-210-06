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
        self._score = 1
        
    def calc_score(self, total_score):
        """Calculates the new total score.
        
        Returns:
            int: The total score.
        """
        _total_score = total_score

        if self._text == '*':
            _total_score += self._score
        elif self._text == '0':
            _total_score -= self._score
        return _total_score
