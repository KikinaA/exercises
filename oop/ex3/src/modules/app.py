from modules.formula import Formula
from modules.comLine import ComLine

class App:
    def __init__(self):
        self.comLine = ComLine()
        self.formula = Formula()

    def run(self):
        self.formula.calc(self.comLine.getElem())
        self.comLine.showComStr()
        self.formula.showAnswer()