class Number:   # Класс, в котором хранятся данные о числе
    def __init__(self, num):
        self.__num__ = num

    def getNum(self):
        return self.__num__

    def setNum(self, num):
        self.__num__ = num