"""This module holds a dict of minerals to be used
in the 'Greed' game as falling objects. It also has
methods to access the objects in the dict."""

class Cast:
    """A collection of shapes.

    The responsibility of a cast is to keep track of a collection of shapes. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _shapes (dict): A dictionary of shapes { key: group_name, value: a list of shapes }
    """

    def __init__(self):
        """Constructs a new Shape."""
        self._shapes = {}
        
    def add_shape(self, group, shape):
        """Adds an shape to the given group.
        
        Args:
            group (string): The name of the group.
            shape (Shape): The shape to add.
        """
        if not group in self._shapes.keys():
            self._shapes[group] = []
            
        if not shape in self._shapes[group]:
            self._shapes[group].append(shape)

    def get_shapes(self, group):
        """Gets the shapes in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The shapes in the group.
        """
        results = []
        if group in self._shapes.keys():
            results = self._shapes[group].copy()
        return results
    
    def get_all_shapes(self):
        """Gets all of the shapes in the cast.
        
        Returns:
            List: All of the shapes in the cast.
        """
        results = []
        for group in self._shapes:
            results.extend(self._shapes[group])
        return results

    def get_first_shape(self, group):
        """Gets the first shape in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first shape in the group.
        """
        result = None
        if group in self._shapes.keys():
            result = self._shapes[group][0]
        return result

    def remove_shape(self, group, shape):
        """Removes an shape from the given group.
        
        Args:
            group (string): The name of the group.
            shape (Shape): The shape to remove.
        """
        if group in self._shapes:
            self._shapes[group].remove(shape)
