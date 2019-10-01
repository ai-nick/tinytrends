import pandas as pd
import matplotlib.pyplot as plt

class TrendAnalyzer(object):

    def __init__(self):
        self.df = pd.read_csv("keyword_trendz_makes_search.txt")

    def plot_trends(self):
        plt.plot(self.df['date'], self.df['ford'])
        plt.plot(self.df['date'], self.df['honda'])
        plt.plot(self.df['date'], self.df['chevy'])
        plt.plot(self.df['date'], self.df['subaru'])
        plt.gca().legend(('ford','honda','chevy', 'subaru'))
        plt.show()

    def plot_bodystyle_trends(self):
        plt.plot(self.df['date'], self.df['pickup'])
        plt.plot(self.df['date'], self.df['coupe'])
        plt.gca().legend(('pickup','coupe'))
        plt.show()





tl = TrendAnalyzer()
tl.plot_trends()