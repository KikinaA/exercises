import sys

class Mbox:
    def __init__(self):
        try:
            f = open('mbox.txt', 'r')  # Взятие данных из файла
            self.__mboxData__ = f.readlines()
            f.close()
        except:  # Если файла нет
            print('File not found.')
            sys.exit()

    def getMboxData(self):
        return self.__mboxData__