"""This tests the Shape class."""

from game.shared.color import Color
from game.casting.shape import Shape
from game.shared.point import Point
import pytest

Shape._color = Color(5, 5, 5, 255)
Shape._text = "0"
Shape._font_size = 15
Shape._position = Point(0, 0)
Shape._velocity = Point(1, 1)
max_x = 50
max_y = 50

def test_get_color():
    """This tests the get color method."""
    assert Shape._color._red == 5
    assert Shape._color._green == 5
    assert Shape._color._blue == 5
    assert Shape._color._alpha == 255


def test_get_text():
    """This tests the get text method"""
    assert Shape._text == "0"


def test_get_font_size():
    """This tests the get font size method."""
    assert Shape._font_size == 15


def test_get_position():
    """This tests the get position method."""
    assert Shape._position._x == 0
    assert Shape._position._y == 0


def test_get_velocity():
    """This tests the get velocity method."""
    assert Shape._velocity._x == 1
    assert Shape._velocity._y == 1

def test_set_color():
    """This tests the set color method."""
    assert Shape._color._red == 5
    assert Shape._color._green == 5
    assert Shape._color._blue == 5
    assert Shape._color._alpha == 255


def test_set_position():
    """This tests the set position method."""
    assert Shape._position._x == 0
    assert Shape._position._y == 0


def test_set_text():
    """This tests the set text method."""
    assert Shape._text == "0"


def test_set_font_size():
    """This tests the set font size method."""
    assert Shape._font_size == 15


def test_set_velocity():
    """This tests the set velocity method."""
    assert Shape._velocity._x == 1
    assert Shape._velocity._y == 1


pytest.main(["-v", "--tb=line", "-rN", __file__])
