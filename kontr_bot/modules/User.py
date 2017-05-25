import vk

class User:  # Вход в вк
    def __init__(self):
        session = vk.AuthSession(app_id='*********',
                                 user_login='**************',
                                 user_password='*************',
                                 scope='offline, messages, wall, friends, photos, status')
        self.__api__ = vk.API(session)

    def getApi(self):
        return self.__api__