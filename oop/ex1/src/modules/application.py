from modules.number import Number
from modules.operation import Operation
from modules.answer import Answer
from modules.choice import Choice

class Application():
    def __init__(self):
        print('Enter number 1, number 2 and operation:')
        # Инициализация классов
        self.num1 = Number(float(input()))
        self.num2 = Number(float(input()))
        self.oper = Operation(str(input()))
        self.answer = Answer()
        self.answer.calculation(self.num1.getNum(), self.num2.getNum(), self.oper.getOper())
        self.choice = Choice(self.num1, self.num2, self.oper, self.answer)

    def run(self):
        while True:
            self.answer.showAnswer()
            print('Enter 1 for continue calculations, 2 for new calculations and 3 for exit:')
            self.choice = Choice(self.num1, self.num2, self.oper, self.answer).newChoice(int(input()))