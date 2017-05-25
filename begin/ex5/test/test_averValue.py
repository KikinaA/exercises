from src.ex5 import *

def test_averValue_22_2():
    assert averValue(22, 2) == 11

def test_averValue_4_0():
    assert averValue(4, 0) == ZeroDivisionError