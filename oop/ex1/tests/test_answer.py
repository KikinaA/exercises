from src.modules.answer import Answer

def test_calculation_summ():
    assert Answer.calculation(1, 1, '+') == 2

def test_calculation_min():
    assert Answer.calculation(3, 2, '-') == 1

def test_calculation_mult():
    assert Answer.calculation(2, 2, '*') == 4

def test_calculation_divis():
    assert Answer.calculation(9, 3, '/') == 3