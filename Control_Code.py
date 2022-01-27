
import Model_Code
import pandas as pd
from datetime import datetime


class Control:

    def __init__(self):
        pass

    
    def parse_Data(self,oData):
        return pd.DataFrame(oData)
        


    def get_Close_Price_Data(self):
        
        url = 'https://yfapi.net/v8/finance/spark'

        query_string = {
            'symbols': 'AAPL,MSFT',
            'interval': '1d',
            'range': '1y'
        }


        modleObj = Model_Code.DataModel(url, query_string)
    
        stockData = modleObj.get_Finance_Data()

        return self.parse_Data(stockData)


    def get_ROE_Data(self):

        url = 'https://yfapi.net/v11/finance/quoteSummary/AAPL'

        query_string = {
            'symbols': 'AAPL',
            'modules': 'financialData'
        }

        modleObj = Model_Code.DataModel(url, query_string)
    
        stockData = modleObj.get_Finance_Data()

        return self.parse_Data(stockData['quoteSummary']['result'][0]['financialData'])


    

controlObj = Control()
stockData = controlObj.get_ROE_Data()

print(stockData['returnOnEquity'])
# print(datetime.fromtimestamp(stockData['AAPL']['timestamp'][0]))