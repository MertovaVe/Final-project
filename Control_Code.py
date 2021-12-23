
import Model_Code
import pandas as pd 

class Control:

    def __init__(self):
        pass

    
    def parseData(self,oData):
        return pd.DataFrame(oData)
        


    def getStockData(self):


        modleObj = Model_Code.DataModel()
    
        stockData = modleObj.get_finance_data()

        return self.parseData(stockData)


controlObj = Control()
stockData = controlObj.getStockData()

print(stockData['AAPL']['close'])