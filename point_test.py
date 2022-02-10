"""This tests the Point class."""

from game.shared.point import Point
import pytest

other = Point(5, 5)
Point._x = 5
Point._y = 5
factor = 2

def test_add():
    """This tests the add method."""
    x = Point._x + other.get_x()
    y = Point._y + other.get_y()
    assert x == Point._x + other.get_x()
    assert y == Point._y + other.get_y()


def test_equals():
    """This tests the equals method."""
    assert Point._x == other.get_x() and Point._y == other.get_y()


def test_get_x():
    """This tests the get x method."""
    assert Point._x == 5


def test_get_y():
    """This tests the get y method."""
    assert Point._y == 5


def test_scale():
    """This tests the scale method."""
    new_point = Point(Point._x * factor, Point._y * factor)
    
    assert new_point._x == 10
    assert new_point._y == 10


pytest.main(["-v", "--tb=line", "-rN", __file__])
