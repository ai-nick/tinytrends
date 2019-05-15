from pytrends.request import TrendReq

class PyTrendApiServiceWorker(object):
    kw_list = []
    
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
            month_end=2, 
            day_end=1, 
            hour_end=0, 
            cat=0, 
            geo='', 
            gprop='', 
            sleep=0)
        print(len(df))
        df["acura_avg"] = df["acura"].rolling(window=5).mean()
        print(df["acura_avg"])
        
pt = PyTrendApiServiceWorker()
pt.SetKwArray(["acura", "italian food", "patagonia"])
print("running...")
pt.GetKwTrendData()