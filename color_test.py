"""This tests the Color class."""

from game.shared.color import Color
import pytest

Color._red = 5
Color._green = 5
Color._blue = 5 
Color._alpha = 255


def test_to_tuple():
    """This tests the to tuple method."""
    assert Color._red == 5
    assert Color._green == 5
    assert Color._blue == 5
    assert Color._alpha == 255

    tuple = (Color._red, Color._green, Color._blue, Color._alpha)
    assert tuple == (5, 5, 5, 255)


pytest.main(["-v", "--tb=line", "-rN", __file__])
