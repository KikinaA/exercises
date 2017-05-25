import sys
from modules.formula import Formula

class App:
    def __init__(self):
        # Инициализация классов
        self.formula = Formula()

    def run(self):
        try: self.num = float(input('Enter the number in the square root: '))
        except:
            print('Error! Enter a number, please.')
            sys.exit()

        self.formula.setAns(self.num)

        self.formula.calculation(self.num)
        self.formula.showAns(self.num)