from pytrends.request import TrendReq
from tinydb import TinyDB

class PyTrendApiServiceWorker(object):
    kw_list = []

    kw_list_dictionary = {
        'bodystyles': ['coupe', 'pickup'],
        'makes': ["honda", "chevy", "ford", "subaru"],
        'models': ['honda civic', 'ford f-150', 'ford fusion', 'toyota sienna']
    }

    trend_db = TinyDB("./db/tinytrenddb.json")
    
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
    
    def GetTheKeyWords(self):
        return

    def SetKwArray(self, kwList):
        self.kw_list = []
        self.kw_list = kwList
        return
    
    def GetKwTrendData(self):
        print(self.kw_list)
        df = self.pytrends.get_historical_interest(
            self.kw_list,
            year_start=2018,
            month_start=1, 
            day_start=1, 
            hour_start=0, 
            year_end=2018, 
            month_end=3, 
            day_end=1, 
            hour_end=0, 
            cat=0, 
            geo='', 
            gprop='', 
            sleep=0)
        df.to_csv("bodystyle_trends.txt")
        self.trend_db.insert({'makes_trend_data_2018': df.to_json()})
        
pt = PyTrendApiServiceWorker()
pt.SetKwArray(pt.kw_list_dictionary['bodystyles'])
print("running...")
pt.GetKwTrendData()