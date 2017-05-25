from src.modules.formula import Formula

def test_formula_4_2():
    Formula.setAns(4, 2)
    assert Formula.getAns() == (4 + (2 / 4)) / 2