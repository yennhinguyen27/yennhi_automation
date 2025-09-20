import requests

class APIHelper:
    def __init__(self, base_url=""):
        self.base_url = base_url

    def get_request(self, endpoint, headers=None, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, headers=headers, params=params)
        return response

    #def post_request(self, endpoint, headers=None, data=None, json=None):
        #url = self.base_url + endpoint
        #print("🔎 Gọi POST tới:", url)
        #response = requests.post(url, headers=headers, data=data, json=json)
        #return response