import statistics
from src.modules.sma import SMA
from src.modules.window import Window

def test_sma_5():
    Window.__win__ = [1, 2, 3]
    SMA.win = [1, 2, 3]
    assert SMA.calc(2, 5) == None

def test_sma_3():
    Window.__win__ = [1, 2, 3]
    SMA.win = [1, 2, 3]
    assert SMA.calc(2, 3) == statistics.mean([1, 2, 3])