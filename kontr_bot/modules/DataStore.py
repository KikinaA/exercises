import json
import os

class DataStore():
    def __init__(self):
        self.__dictFromF__ = {}

    def getDict(self):
        return self.__dictFromF__

    def myInput(self, name, text):
        if os.path.isfile('test.json'):  # Если файл уже существует
            self.myOutput()

        if name in self.__dictFromF__:  # Если данный пользователь уже отправлял сообщение
            if type(self.__dictFromF__[name]) is list:  # Если было уже несколько сообщений
                self.__dictFromF__[name].append(text)
            else:  # Если только одно сообщение
                self.__dictFromF__[name] = [self.__dictFromF__[name], text]  # Создаем список сообщений
        else:
            self.__dictFromF__[name] = text
        json.dump(self.__dictFromF__, open('test.json', 'w'))  # Сохраняем данные
        print('Message saved.')

    def myOutput(self):  # Выгружаем словарь из файла
        try: self.__dictFromF__ = json.load(open('test.json', 'r'))
        except: self.__dictFromF__ = {}

    def delEvent(self, event, myID):
        self.myOutput()  # Выгружаем данные из файла
        newList = []
        if self.__dictFromF__[myID] == event:  # Если сообщение только одно
            del self.__dictFromF__[myID]  # Удаляем сообщение и id
        else:  # Если сообщений несколько
            for l in self.__dictFromF__[myID]:  # Открываем список сообщений
                if l != event:  # Если сообщение не удаляется
                    newList.append(l)  # Добавляем его в список
        self.__dictFromF__[myID] = newList
        json.dump(self.__dictFromF__, open('test.json', 'w'))  # Сохраняем данные
        print('Message deleted.')