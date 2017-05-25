class Message:
    def __init__(self):
        self.__myDict__ = {}

    def getCommand(self):
        return self.__myDict__

    def setCommand(self, message_list):  # Обработка полученных сообщений
        for message in message_list:
            if type(message) is int:
                continue

            if message['read_state'] == 0:
                if 'chat_id' not in message:
                    self.__myDict__[str(message['uid'])] = str(message['body'])
                    self.newID = str(message['uid'])

    def checkCommand(self, myDS, api):
        myDict = self.__myDict__
        for elem in myDict:
            line = str(myDict[elem])
            l = line.split('/')

            if l[0] == 'del':
                myDS.delEvent(str(l[1]), elem)  # Отправляем команду в DataStore
            if l[0] == 'all':
                myDS.myOutput()
                text = myDS.getDict()
                self.answerAll(text, self.newID, api)  # Отправляем словарь данных из json
            if l[0] == 'save':
                myDS.myInput(elem, str(l[1]))  # Отправляем строку в DataStore

    def answerAll(self, myAnswer, myID, api):  # Ответ на команду "показать все"
        newStr = ''
        for name in myAnswer:
            if name == myID:  # Если имя совпадает с номером id
                if type(myAnswer[name]) is list:  # Если сообщений несколько
                    for myStr in myAnswer[name]:
                        newStr += str(myStr) + '\n'  # Создаем строки с символом перехода на новую строку
                    self.sendAnswer(newStr, api, myID)
                else:  # Если сообщение одно
                    self.sendAnswer(str(myAnswer[name]), api, myID)

    def sendAnswer(self, myAnswer, api, id):  # Отправка ответов пользователю
        api.messages.send(user_id=id, message=myAnswer)
        print('Message sent.')