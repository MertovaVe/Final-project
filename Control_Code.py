
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
            'symbols': 'AAPL,MSFT,TSLA',
            'interval': '1d',
            'range': '1y'
        }


        modleObj = Model_Code.DataModel(url, query_string)
    
        stockData = modleObj.get_Finance_Data()

        stockDF = self.parse_Data(stockData)


        for x in range(len(stockDF.loc['timestamp'])):
            for y in range(len(stockDF.loc['timestamp'][x])):
                stockDF.loc['timestamp'][x][y] = datetime.fromtimestamp(stockDF.loc['timestamp'][x][y])
            

        #print(datetime.fromtimestamp(stockDF.loc['timestamp'][0][5]))
        #print(stockDF.loc['timestamp'])

        return stockDF

    # you have to input the company code, such as AAPL,MSFT,TSLA
    def get_Finance_Indicators_Data(self, company_symbols):

        url = 'https://yfapi.net/v11/finance/quoteSummary/'+company_symbols

        query_string = {
            'symbols': company_symbols,
            'modules': 'financialData'
        }

        modleObj = Model_Code.DataModel(url, query_string)
    
        stockData = modleObj.get_Finance_Data()

        stockDF = self.parse_Data(stockData['quoteSummary']['result'][0]['financialData'])

        finance_Indicator = [{
            'Name':'return On Equity',
            'Value':stockDF['returnOnEquity']['fmt']
        },{
            'Name':'return On Assets',
            'Value':stockDF['returnOnAssets']['fmt']
        },{
            'Name':'debt To Equity',
            'Value':stockDF['debtToEquity']['fmt']
        }]

        return finance_Indicator


    def get_Gernal_Market_Indexes(self):
        url = 'https://yfapi.net/v6/finance/quote/marketSummary'

        query_string = {
            'lang': 'en',
            'region': 'US'
        }

        modleObj = Model_Code.DataModel(url, query_string)
    
        stockData = modleObj.get_Finance_Data()

        stockDF = self.parse_Data(stockData['marketSummaryResponse']['result'])

        Market_Index = [{
            'Name':'S&P 500',
            'Index': stockDF[stockDF['fullExchangeName']=='SNP']['regularMarketPrice'][0]['fmt']
        },{
            'Name':'Nasdaq Composite',
            'Index': stockDF[stockDF['fullExchangeName']=='Nasdaq GIDS']['regularMarketPrice'][2]['fmt']
        }]

        return Market_Index

        

controlObj = Control()
stockData = controlObj.get_Close_Price_Data()

print(stockData)
#stockData = controlObj.get_Finance_Indicators_Data('TSLA')


#print(stockData)

# print(stockData['returnOnEquity'])

# print(datetime.fromtimestamp(stockData['AAPL']['timestamp'][0]))