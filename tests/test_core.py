# Here we will put the tests
from dynagamma import square, greet

def test_square_int():
    assert square(3) == 9

def test_square_float():
    assert square(2.5) == 6.25

def test_greet():
    assert greet("Patrick") == "Hello, Patrick!"

