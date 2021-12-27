import os
import requests
from dotenv import load_dotenv
from requests.api import head

class FlightSearch:
    
    def __init__(self):
        load_dotenv()
        self.city = ""
        self.iata = ""
        self.url = "https://tequila-api.kiwi.com/locations/query"
        self.headers = {
            "apikey" : os.getenv("TEQUILA_TOKEN")
        }
    
    def get_iata_code(self,city):
        print(city)
        request_string = {
            "term":city
        }
        
        if city != "":
            try:
                response = requests.get(url=self.url, headers=self.headers, json = request_string)
                response.raise_for_status()
            except:
                print("Tequila was weak :(")
                print(response.text)
            else:
                print(response.json())
                self.iata = "TESTING"
                return self.iata
        else:
            return self.iata