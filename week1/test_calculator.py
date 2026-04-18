import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(5, 0) == 5

def test_add_mixed():
    assert add(-5, 5) == 0

def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-1, -1) == 0

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_mixed():
    assert subtract(0, 5) == -5

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_multiply_by_one():
    assert multiply(7, 1) == 7

def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-6, 2) == -3

def test_divide_float():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)