import pandas as pd


class TrendLoader(object):

    def __init__(self):
        df = pd.read_csv("keyword_trendz.txt")
        print(df.head())



tl = TrendLoader()