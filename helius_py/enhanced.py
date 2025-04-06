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



def fetch_transactions_by_address(address, api_key, params={}): # max: 100 txs
    while True:
        try:
            url = f"https://api.helius.xyz/v0/addresses/{address}/transactions?api-key={api_key}"
            response = requests.get(url, params=params )
            data = response.json()
            return  data   
        except:
            print("error fetch_transactions_by_address: wait for 10 sec...")
            time.sleep(10)