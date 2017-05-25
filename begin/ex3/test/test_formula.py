from src import ex3

def test_formula_1():
    assert ex3.formula(1) ==  1 / 3

def test_formula_0():
    assert ex3.formula(0) == None

def test_formula_minus1():
    assert ex3.formula(-1) == 1/(-3)