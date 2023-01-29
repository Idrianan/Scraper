import requests
import time
class Scrapper:
    def __init__(self):
        pass

    def define(self,region:str) ->str:
        regions = ["Санкт-Петербург", "Москва"]
        if not(region in regions):
            raise ValueError
        elif region == "Санкт-Петербург":
            return 'spb'
        elif region == "Москва":
            return 'msk'

    def set_URI(self,town:str) -> None:
        town = self.define(town)
        self.URI = "https://gogov.ru/covid-19/"+town+ "#data"
        self.headers = {
            'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
            }
    
    def create_response(self,town:str) -> requests.Response:
        self.set_URI(town)
        while True:
            try:
                return requests.get(self.URI,headers=self.headers)
            except:
                print("Error, trying another time")
                time.sleep(5)
