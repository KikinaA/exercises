from src.ex4 import sma
import statistics

def test_sma_1_5():
    global win
    win = [1, 2, 3, 4, 5]
    assert sma(1, 5) ==  statistics.mean(win)

def test_sma_10_3():
    global win
    win = [1, 2, 3]
    assert sma(10, 3) ==  statistics.mean(win)

def test_sma_7_5():
    global win
    win = [1, 2, 3, 4]
    assert sma(7, 5) ==  None