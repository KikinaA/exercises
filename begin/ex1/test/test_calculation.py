from src.ex1 import *

def test_beginning_plus():
    assert calculation(4, 4, '+') == 8

def test_beginning_minus():
    assert calculation(10, 5, '-') == 5

def test_beginning_division():
    assert calculation(9, 3, '/') == 3

def test_beginning_multipl():
    assert calculation(5, 5, '*') == 25

def test_beginning_wrong_input():
    assert calculation(1, 1, 1) == None