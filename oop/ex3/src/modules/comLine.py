import sys

class ComLine:  # Считывание аргумента командной строки
    def __init__(self):
        try:
            self.__comStr__ = sys.argv[1]
            self.__comStr__ = self.__comStr__.split('--poly=')
            self.__comStr__ = self.__comStr__[1].split(',')
            i = 0
            for elem in self.__comStr__:  # Меняем тип полученных данных на десятичный
                self.__comStr__[i] = int(elem)
                i += 1
        except:
            print('Please, enter the command line arguments. '
                  'The pattern is: --poly=1,2,3, where 1,2,3 is your numbers.')
            sys.exit()

    def getElem(self):
        return self.__comStr__

    def showComStr(self):
        print('Input variables: {}'.format(self.__comStr__))