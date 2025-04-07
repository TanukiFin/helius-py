import requests
import json
import pandas as pd
import numpy as np
import time
import datetime
import random
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', 30) #None

from config import MAINNET_API_URL, MAINNET_RPC_URL
from utility import _make_get_request


class enhancedAPI:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_API_URL
        self.api_key = api_key

    def get_balances(self, address: str):
        path = f"/v0/addresses/{address}/balances"
        url = self.base_url + path + self.api_key_query
        return _make_get_request(url)

    def fetch_transactions_by_address(self, address, params={}, attempts=10): # max: 100 txs
        for i in range(attempts):
            try:
                url = f"{self.base_url}/v0/addresses/{address}/transactions?api-key={self.api_key}"
                response = requests.get(url, params=params )
                data = response.json()
                return  data   
            except:
                print("error fetch_transactions_by_address: wait for 10 sec...")
                time.sleep(10)
        
    def fetch_transactions_by_signatures(self, sig_list):
        url = f"{self.base_url}/v0/transactions/?api-key={self.api_key}"
        headers = {
                'Content-Type': 'application/json',
        }
        param = {
            "transactions": sig_list
                #["593wEz7afr4bH8puUEeqVeDsFAcWSnwydmU4NkHDFX19Hdvf2i5tJF6WheU6RRd6F7jHgUh6kEvujiUPCo36x8Do",
                #"4DCrERdsW3q6QZtaswEw4Ut9qDWLFKixUxmZUvLvSYC3mxVk4eSBk2RLHXcTC6TkFb93eycvPiTeWC71kFFQiyj9"]
        }

        response = requests.post(url, headers=headers, data=json.dumps(param))
        data = response.json()
        
        return  data   