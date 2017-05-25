import datetime

class Timer:
    def __init__(self, myDS, myMessage, api):
        # Инициализация необходимых данных
        self.checkDict = {}
        self.textMes = []

        self.nowTime = datetime.datetime.now()  # Проверка времени сейчас
        myDS.myOutput()
        self.checkDict = myDS.__dictFromF__  # Загрузка словаря из файла
        self.dateOfEvent(myDS, myMessage, api)

    def dateOfEvent(self, myDS, myMessage, api):
        for elem in self.checkDict:
            if type(self.checkDict[elem]) is list:  # Если список событий
                for mes in self.checkDict[elem]:
                    self.checkTime(mes, elem, myDS, myMessage, api)
            else:  # Если только 1 событие
                self.checkTime(self.checkDict[elem], elem, myDS, myMessage, api)

    def checkTime(self, mes, id, myDS, myMessage, api):
        textMes = str(mes).split(' :: ')
        forDate = str(textMes[0]).split('.')
        userTime = datetime.datetime(int(forDate[0]),  # Установка времени из сообщения
                                     int(forDate[1]),
                                     int(forDate[2]),
                                     int(forDate[3]),
                                     int(forDate[4]))
        if self.nowTime >= userTime:  # Если время уже пришло
            myMessage.sendAnswer('Right now: {}'.format(str(textMes[1])), api, id)  # Отправить сообщение
            print('An event message has been sent.')
            myDS.delEvent(str(mes), id)  # Удалить событие