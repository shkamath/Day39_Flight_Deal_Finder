from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

dm = DataManager()
fs = FlightSearch()

flight_data = dm.get_data()

for city in flight_data:
    if city['iataCode'] == "":
        iata_code = fs.get_iata_code(city['city'])
        id = city['id']
        if iata_code != "":
            new_data = {
                'price':{
                    'iataCode':iata_code
                }
            }
            #dm.put_data(new_data,id)
