import pandas as pd
import numpy as np
from sklearn import linear_model
from tinydb import TinyDB
import matplotlib.pyplot as plt


class AnalyticsUtility(object):
    model_dict = {}

    trend_db = TinyDB("./db/tinytrenddb.json")

    def __init__(self, file_path):
        self.filename = file_path.split('.')[0]
        print(self.filename)
        self.full_data = pd.DataFrame().from_csv(file_path, index_col=None)
        return

    def print_out_db(self):
        print(self.trend_db.all())

    def get_feature_correlation_cartesian(self):
        print(self.full_data.head())
        df = self.full_data.drop(columns=['isPartial', 'date'])
        #df.fillna(0.0, inplace=True)
        columns = df.columns.values
        for i in range(len(columns)):
            if(i+1 != len(columns)):
                for i2 in range(i+1, len(columns)):
                    print(columns[i] + " corr with " + columns[i2])
                    print(df[columns[i]].corr(df[columns[i2]]))

    def aggregate_and_save(self, interval_size):
        df = self.full_data
        print(df['date'][23+24])
        df = self.full_data.drop(columns=['date', 'isPartial'])
        new_df_dictionary = {}
        cols = df.columns.values
        for i in cols:
            colSeries = pd.Series(df[i])
            new_df_dictionary[i] = colSeries.groupby(colSeries.index // interval_size).sum()
        new_df = pd.DataFrame().from_dict(new_df_dictionary)
        new_df.to_csv(self.filename + str(interval_size)+".txt")



tp = AnalyticsUtility('bodystyle_trends.txt')
tp.aggregate_and_save(24)