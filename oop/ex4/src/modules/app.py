from modules.sma import SMA
from modules.tools import Tools

class App:
    def __init__(self):
        self.sma = SMA()
        self.tools = Tools()

    def run(self):
        self.size = int(input('Enter size of window: '))
        self.sma.process(self.size)
        self.tools.graf(self.sma.getOrigData(), self.sma.getProcData(), self.size)