"""This module takes care of the score"""

class Score:
    """THis class responsibility is to keep count of the score,
       for each coin the mouse gets its 10 points
       
       Atributes:
            points(int): points you get went taking a coin.
    """
    def __init__(self):
        """Constructs a new score instance to hold the points
           goten by taking coins.

           Arg:
           points(int): points you get went taking a coin.
        """
        self._score = 0
    
    def get_points(self):
        """Gets the poitns as a string.
           
           Returns: 
              the textualized points.
        """
        return self._score
    
    def add_points(self):
        """Adds 10 points for each coin taken.
        
           Returns:
              New textualized points.
        """
        self._score = self._score + 10
        return self._score
    
    def set_points(self, score):
        """Uppdates the poitns to the new points.
           
           Returns: 
              points(int): points you get went taking a coin.
        """
        self._score = score