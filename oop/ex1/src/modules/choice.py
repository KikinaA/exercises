import sys

class Choice():
    def __init__(self, num1, num2, oper, answer):
        self.__signal__ = 1
        self.num1 = num1
        self.num2 = num2
        self.oper = oper
        self.answer = answer

    def setVar(self):
        self.num2.setNum(float(input()))
        self.oper.setOper(str(input()))

    def newChoice(self, choice):
        if choice == 1 and self.answer.getAnswer() != None:  # Продолжение работы с ответом
            print('Enter number 2 and operation:')
            self.setVar()
            self.answer.calculation(self.answer.getAnswer(), self.num2.getNum(), self.oper.getOper())

        elif choice == 1 and self.answer.getAnswer() == None:
            print('Error in first number! Please, try again.')
            return

        elif choice == 2:  # Новое выражение
            print('Enter number 1, number 2 and operation:')
            self.num1.setNum(float(input()))
            self.setVar()
            self.answer.calculation(self.num1.getNum(), self.num2.getNum(), self.oper.getOper())

        elif choice == 3:  # Выход
            sys.exit()

        else:
            print('Error! Enter 1, 2 or 3')  # Ошибка ввода
