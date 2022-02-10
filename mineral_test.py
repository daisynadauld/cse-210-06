"""This tests the Mineral class."""

from game.casting.shape import Shape
from game.casting.mineral import Mineral
import pytest
       
def test_calc_score():
    """This tests the calc score method"""
    _total_score = 10
    Mineral._score = 1
    Mineral._text = '*'

    assert (Mineral._text == '*' or Mineral._text == '0')

    if Mineral._text == '*':
        _total_score += Mineral._score
    elif Mineral._text == '0':
        _total_score -= Mineral._score

    assert _total_score == 11


pytest.main(["-v", "--tb=line", "-rN", __file__])