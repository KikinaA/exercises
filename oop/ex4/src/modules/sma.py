import random
import statistics

from modules.window import Window

class SMA:  # работа с очередью
    def __init__(self):
        self.win = Window()

        self.__procData__ = []
        self.__origData__ = []

    def process(self, size):
        i = 0
        while i < 30:
            self.num = random.randint(1, 100)
            self.__origData__.append(self.num)  # добавляем данные о функции

            self.ans = self.calc(self.num, size)  # ищем значение sma
            if self.ans != None:
                self.__procData__.append(self.ans)  # добавляем ответ, если очередь была заполнена
            i += 1

    def calc(self, num, size):
        if len(self.win.getWin()) < size:  # если размер очереди меньше установленного окна
            self.win.addNumInWin(num)
            return None

        else:  # очередь равна размеру окна
            self.win.sliceWin()
            self.win.addNumInWin(num)
            return statistics.mean(self.win.getWin())

    def getProcData(self):
        return self.__procData__

    def getOrigData(self):
        return self.__origData__