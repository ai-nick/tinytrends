import pandas as pd
import numpy as np
from sklearn import linear_model
from tinydb import TinyDB
import matplotlib.pyplot as plt


class TrendPredictor(object):
    model_dict = {}

    trend_db = TinyDB("./db/tinytrenddb.json")

    def __init__(self, file_path, no_index = True):
        if(no_index):
            self.full_data = pd.DataFrame().from_csv(file_path, index_col=None)
        else:
            self.full_data = pd.DataFrame().from_csv(file_path)
        return

    def print_out_db(self):
        print(self.trend_db.all())

    def predict_column(self, col_name):
        self.full_data[col_name] = self.full_data[col_name].shift(1)
        self.full_data.dropna(inplace=True)
        test_split_index = (int(len(self.full_data) * .3))
        train_split_index = len(self.full_data) - (int(len(self.full_data) * .3))
        print(self.full_data.head())
        y_train = self.full_data[col_name].head(train_split_index)
        y_test = self.full_data[col_name].tail(test_split_index)
        self.full_data = self.full_data.drop(columns=[col_name, "date", "isPartial"])
        X_Train = self.full_data.head(train_split_index)
        X_Test = self.full_data.tail(test_split_index)
        model = linear_model.TheilSenRegressor()
        print(X_Test.head(), X_Train.tail())
        model.fit(X_Train, y_train)
        print(model.score(X_Test, y_test))

    def split_and_predict(self, df, y_col, train_percent):
        test_split_index = (int(len(df) * (1.0-train_percent)))
        train_split_index = (int(len(df) * train_percent))
        y_train = df[y_col].head(train_split_index)
        y_test = df[y_col].tail(test_split_index)
        # any columns beside the label column should (by convention) be dropped 
        # prior to passing df to this method
        df = df.drop(columns=[y_col])
        X_Train = df.head(train_split_index)
        X_Test = df.tail(test_split_index)
        model = linear_model.TheilSenRegressor()
        model.fit(X_Train, y_train)
        print(model.score(X_Test, y_test))
        plt.plot(model.predict(X_Test))
        plt.plot(list(y_test))
        plt.gca().legend(('predicted','actual'))
        plt.show()

    def get_feature_correlation_cartesian(self, drop_cols=False):
        df = self.full_data
        if(drop_cols != False):
            df = self.full_data.drop(columns=['isPartial', 'date'])
        columns = df.columns.values
        for i in range(len(columns)):
            if(i+1 != len(columns)):
                for i2 in range(i+1, len(columns)):
                    print(columns[i] + " corr with " + columns[i2])
                    print(df[columns[i]].corr(df[columns[i2]]))
            

    def predict_column_better_features(self, col_name, train_percent):
        working_df = pd.DataFrame(self.full_data[col_name])
        working_df[col_name+"_rolling_55"] = working_df.rolling(window=55)[col_name].mean()
        working_df[col_name+"_rolling_34"] = working_df.rolling(window=34)[col_name].mean()
        working_df[col_name+"_rolling_13"] = working_df.rolling(window=13)[col_name].mean()
        working_df[col_name+"_rolling_5"] = working_df.rolling(window=5)[col_name].mean()
        working_df[col_name+"_34_roc"] = working_df[col_name].pct_change(34)
        working_df[col_name+"_21_roc"] = working_df[col_name].pct_change(21)
        working_df[col_name+"_3_roc"] = working_df[col_name].pct_change(3)
        working_df[col_name] = working_df[col_name].shift(1)
        working_df.dropna(inplace=True)
        print(working_df.head())
        self.split_and_predict(working_df, col_name, train_percent)





tp = TrendPredictor('./bodystyle_trends24.txt')
tp.predict_column_better_features('coupe', .89)
#tp.get_feature_correlation_cartesian()