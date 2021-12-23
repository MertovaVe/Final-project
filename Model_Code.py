import requests

class DataModel:

    def __init__(self):
        pass

    def get_finance_data(self):

        querystring = {
            'symbols': 'AAPL,MSFT',
            'interval': '1d',
            'range': '1y'
        }

        headers = {
            'x-api-key': '5aOPNl1LsP64L4C704qT8azZcshNA5Av7rezlD5a'
        }

        url = 'https://yfapi.net/v8/finance/spark'


        api_result = requests.get(url, headers = headers, params = querystring)

        api_response = api_result.json()

        return api_response


