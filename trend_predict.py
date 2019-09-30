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




tp = TrendPredictor()
tp.predict_column('pickup')
