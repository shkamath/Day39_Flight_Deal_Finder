import requests
import os
from dotenv import load_dotenv
from requests.models import Response

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.key = os.getenv("SHEETY_TOKEN")
        self.endpoint = "https://api.sheety.co/50ed93d69e5a5faa1515f418fb4bcb73/flightDeals/prices"
        self.headers = {
            "Authorization" : self.key
        }
    
    def get_data(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()["prices"]

    def put_data(self,row,id):
        new_endpoint = self.endpoint + f"/{id}"
        response = requests.put(url=new_endpoint,json=row,headers=self.headers)
        response.raise_for_status()