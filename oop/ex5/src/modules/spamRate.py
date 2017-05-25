class SpamRate:  # Сортировка по количеству спама
    def __init__(self):
        self.rateOfSpam = {}
        self.sortRat = []
        self.i = 0
        self.l = lambda x: x[1]

    def addInRateOfSpam(self, name, rate):
        if name in self.rateOfSpam:
            # Ищем среднее между имеющимся и новым
            self.rateOfSpam[name] = (float(self.rateOfSpam[name]) + rate) / 2
        else:
            self.rateOfSpam[name] = rate

    def sortSpamRate(self):
        self.sortRat = sorted(self.rateOfSpam.items(), key=self.l, reverse=True)
        self.showSpamRate()

    def showSpamRate(self):
        print('Top-5 spammers:')
        for elem in self.sortRat:
            if self.i < 5:  # Первые пять спаммеров
                print('{}. {} with rating of spam: {}'.format(self.i + 1, elem[0], elem[1]))
                self.i += 1
            else:
                break