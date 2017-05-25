import math

class Formula:   # Поиск ответа
    def __init__(self):
        self.lastAnswer = 3

    def calculation(self, num):
        # Пока ответ не будет приближенно точен
        while abs(self.lastAnswer - self.getAns()) > 0.00001:
            self.lastAnswer = self.getAns()
            self.setAns(num)

    def setAns(self, num):
        self.__ans__ = (self.lastAnswer + (num / self.lastAnswer)) / 2

    def getAns(self):
        return self.__ans__

    def showAns(self, num):
        print('Answer is {}'.format(self.getAns()))
        print('Correct answer is {}'.format(math.sqrt(num)))