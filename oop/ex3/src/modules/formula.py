class Formula:  # Решение формулы
    def __init__(self):
        self.summ = 0

    def calc(self, comLine):
        for elem in comLine:
            self.summ += self.form(elem)

    def form(self, elem):
        if elem == 0:
            return ZeroDivisionError
        return 1 / (elem * 3)

    def showAnswer(self):
        print('Answer is {}'.format(self.summ))