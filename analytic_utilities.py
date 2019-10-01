import pandas as pd
import numpy as np
from sklearn import linear_model
from tinydb import TinyDB
import matplotlib.pyplot as plt


class AnalyticsUtility(object):
    model_dict = {}

    trend_db = TinyDB("./db/tinytrenddb.json")

    def __init__(self, file_path):
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
            new_df_dictionary[i] = []
        col_len = len(cols)
        df_len = len(df)
        # this is our while loop endcase for 24 hr aggs, cause zero index
        indexer = interval_size-1
        while indexer <= (df_len -interval_size-1):
            for i in cols:




tp = AnalyticsUtility('./bodystyle_trends.txt')
