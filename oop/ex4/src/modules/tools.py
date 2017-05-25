from matplotlib import pyplot as plt

class Tools:
        def graf(self, origData, procData, size):
            fig, ax = plt.subplots()
            ax.plot([i for i in range(30)], origData)
            ax.plot([i for i in range(size, 30)], procData)
            plt.show()