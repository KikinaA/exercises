import math
from src import ex2

def test_formula_25():
    assert ex2.formula(25, 3) == math.sqrt(25)

def test_formula_4():
    assert ex2.formula(4, 3) == math.sqrt(4)

def test_formula_9():
    assert ex2.formula(9, 3) == math.sqrt(9)