import pandas as pd
import numpy as np
from sklearn import linear_model


class TrendPredictor(object):
    model_dict = {}

    def __init__(self):
        self.full_data = pd.DataFrame().from_csv('./bodystyle_trends.txt', index_col=None)
        return

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
        df = df.drop(columns=[col_name])
        X_Train = df.head(train_split_index)
        X_Test = df.tail(test_split_index)
        model = linear_model.TheilSenRegressor()
        model.fit(X_Train, y_train)
        print(model.score(X_Test, y_test))


    def predict_column_better_features(self, col_name):
        working_df = pd.DataFrame(self.full_data[col_name])
        working_df[col_name+"_rolling_55"] = working_df.rolling(window=55)[col_name].mean()
        working_df[col_name+"_rolling_34"] = working_df.rolling(window=34)[col_name].mean()
        working_df[col_name+"_rolling_13"] = working_df.rolling(window=13)[col_name].mean()
        working_df[col_name+"_rolling_5"] = working_df.rolling(window=5)[col_name].mean()
        working_df[col_name] = working_df[col_name].shift(1)
        working_df.dropna(inplace=True)
        test_split 





tp = TrendPredictor()
tp.predict_column('pickup')
