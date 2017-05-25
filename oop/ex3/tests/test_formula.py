from src.modules.formula import Formula

def test_formula_0():
    assert Formula.calculation(0) == ZeroDivisionError

def test_formula_2():
    assert Formula.calculation(2) == 1 / (2 * 3)