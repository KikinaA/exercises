from modules.mbox import Mbox
from modules.dspam import Dspam
from modules.allMails import AllMails
from modules.spamRate import SpamRate
from modules.barChart import BarChart

class App:
    def __init__(self):
        self.name = ''

        self.mbox = Mbox()
        self.dspam = Dspam()
        self.allMails = AllMails()
        self.spamRate = SpamRate()
        self.barChart = BarChart()

    def run(self):
        self.readData()
        self.dspam.showAverValue(len(self.allMails.getListMail()))  # Среднее значение спама
        self.allMails.addInDictMail()
        self.allMails.showDict()
        self.spamRate.sortSpamRate()  # Сортировка по количеству спама
        self.barChart.showBarChart(self.allMails.getDictMail())

    def readData(self):
        mboxData = self.mbox.getMboxData()
        for line in mboxData:
            l = line.split(' ')
            if l[0] == 'From':  # Считывание отправителя
                self.allMails.addMailName(l[1])
                self.name = l[1]
            if l[0] == 'X-DSPAM-Confidence:':  # Считывание значение спама
                self.dspam.setDspam(float(l[1]))
                self.spamRate.addInRateOfSpam(self.name, float(l[1]))