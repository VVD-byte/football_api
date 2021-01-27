import requests
import json

#from .models import Game, Sorev, Comands
from datetime import datetime, timedelta


class parser:
    def __init__(self):
        self.url = 'https://www.championat.com/stat/football/%s.json'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        }
        self.data = '2001-04-01'

    def start_pars_all(self):
        while self.data != datetime.strftime(datetime.now(), "%Y-%m-%d"):
            print(requests.get(self.url %self.data, headers = self.headers).text)

    def get_data(self):
        datetime.strftime(datetime.strptime(self.data, "%Y-%m-%d") + timedelta(days=1), "%Y-%m-%d")

if __name__ == '__main__':
    parser().start_pars_all()
