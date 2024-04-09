import requests
import pytest



class Test_api:

    def __init__(self, base_url):
        self.base_url = base_url


    # get method
    def get(self,endpoint,params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response

    # post method
    def post(self,endpoint,data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url,data)
        return response


    # put method
    def put(self,endpoint,data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url,data)
        return response



    # delete a user
    def delete(self,endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        return response






