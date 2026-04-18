import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.arithmetic
def test_add_positive():
    assert add(2, 3) == 5

@pytest.mark.arithmetic
def test_add_negative():
    assert add(-1, -1) == -2

@pytest.mark.edge_case
def test_add_zero():
    assert add(5, 0) == 5

def test_add_mixed():
    assert add(-5, 5) == 0

@pytest.mark.arithmetic
def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-1, -1) == 0

@pytest.mark.edge_case
def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_mixed():
    assert subtract(0, 5) == -5

@pytest.mark.arithmetic
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-2, 3) == -6

@pytest.mark.edge_case
def test_multiply_zero():
    assert multiply(5, 0) == 0