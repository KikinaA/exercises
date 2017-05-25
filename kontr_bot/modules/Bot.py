import time
import os
from modules.User import User
from modules.Message import Message
from modules.DataStore import DataStore
from modules.Timer import Timer

class Bot:
    def run(self):
        # Инициализируем классы
        user = User()
        api = user.getApi()
        myMessage = Message()
        myDS = DataStore()

        while True:  # Проверка сообщений на наличие новых
            message = api.messages.get(time_offset=0)
            if len(message) != 1 and message[1]['read_state'] == 0:
                api.messages.markAsRead(peer_id=message[1]['uid'])
                myMessage.setCommand(message)  # Обработка сообщения
                myMessage.checkCommand(myDS, api)  # Проверка команды

            if os.path.isfile('test.json'):  # Если файл уже существует
                myTimer = Timer(myDS, myMessage, api)  # Включение таймера
            time.sleep(10)  # Приостановка работы программы на 10 секунд