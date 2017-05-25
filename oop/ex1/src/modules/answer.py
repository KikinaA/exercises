class Answer:   # Класс, отвечающий за поиск ответа
    def calculation(self, num1, num2, oper):
        if oper == '+':
            self.__answer__ = self.summ(num1, num2)
        elif oper == '-':
            self.__answer__ = self.min(num1, num2)
        elif oper == '*':
            self.__answer__ = self.mult(num1, num2)
        elif oper == '/':
            self.__answer__ = self.divis(num1, num2)
        else:
            print('Error! Enter operation like +, -, * or /.')
            self.__answer__ = None
        self.getAnswer()

    def summ(self, num1, num2):
        return num1 + num2

    def min(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2

    def divis(self, num1, num2):
        return num1 / num2

    def getAnswer(self):
        return self.__answer__

    def showAnswer(self):
        print('Answer: {}'.format(self.getAnswer()))