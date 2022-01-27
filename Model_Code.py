import requests
import json

class DataModel:

    def __init__(self,url,params):
        
        self.url_obj = self.get_Url_Information()
        self.access = self.url_obj['API_KEY']
        self.finance_url = url
        self.params = params

    def get_Url_Information(self):

        load_JSON_files = open('Url_Information.JSON')
        get_JSON_obj = json.load(load_JSON_files)

        return get_JSON_obj


    def get_Finance_Data(self):
        
        query_string = self.params

        headers = {
            'x-api-key': self.access
        }

        url = self.finance_url


        api_result = requests.get(url, headers = headers, params = query_string)

        api_response = api_result.json()

        return api_response