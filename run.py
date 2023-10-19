import gspread
import pytz # this is to help talk to api and specifiy the timezone we mean 
import json
import requests
import os
from google.oauth2.service_account import Credentials 

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime

from alpaca_trade_api.rest import REST, TimeFrame
import alpaca_trade_api as tradeapi

# --------- Alpaca setup

def load_alpaca_credentials(filename="cred2.json"):
    """Load Alpaca API credentials from a json file"""
    
    with open('creds2.json', 'r') as file:
        creds2 = json.load(file)
       #  print(creds2) test - successfully linked to my account
        api_key = creds2['ALPACA_API_KEY']
        api_secret = creds2['ALPACA_API_SECRET']
    return api_key, api_secret

# Load the API credentials
API_KEY, API_SECRET = load_alpaca_credentials() 
alpaca =  tradeapi.REST(API_KEY, API_SECRET, base_url='https://paper-api.alpaca.markets')
account = alpaca.get_account()
# print(account) - checking if account is linked

"""
with open('cred2.json') as f:
    cred2 = json.load(f)
    api_key = cred2['ALPACA_API_KEY']
    api_secret = cred2['ALPACA_API_SECRET']

alpaca = tradeapi.REST(api_key, api_secret)
api = REST()
"""

# --------- Gspread setup

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('btc_usd_backtesting')

# setting up to read the tab in the sheet
historical_data = SHEET.worksheet('historical_data')
data = historical_data.get_all_values()

# ------------------------------------------------- Testing the Alpaca hsitorical data client

#bars = alpaca.get_bars("BTC/USD", tradeapi.TimeFrame.Hour, "2021-06-07", "2021-06-08", adjustment='raw').df
#print(bars)

'''


# --1 USING THE CLIENT
#crypto_client = CryptoHistoricalDataClient()
try:
    client = CryptoHistoricalDataClient()

    request_params = CryptoBarsRequest(
        symbol_or_symbols=["BTC/USD"],
        timeframe=TimeFrame(15, TimeFrameUnit.Minute),
        start=datetime(2021, 1, 1),
        end=datetime(2021, 1, 2) 
        # data needs to fill till 6pm on the 1st, but below will be a rule to break fill afte that
        #  end=datetime(2021, 1, 2) 
    )

    bars = client.get_crypto_bars(request_params)
    print(bars) 
    # prints what's in the client call
    # print(data)  prints whats in the google sheet
except Exception as e:
    print(f"An error occurred during Alpaca client call for data")
    exit()



  timeframe=TimeFrame(15, TimeFrameUnit.Minute),
        start=datetime(2021, 1, 1),
        end=datetime(2021, 1, 2) 
        so I am not able to get any lower than 2021 for minutes. I will try daily
'''

# ------------------------------------------------ TESTING WRITING ONTO GSHEET

# historical_datahe workseet of the test columns and a row. https://docs.gspread.org/en/latest/user-guide.html#clear-a-worksheet
# worksheet.clear()
# so the command worked and it did delete the test data, but in the terminal it says:NameError: name 'worksheet' is not defined
"""

# Extract the relevant data from Alpaca list of lists
data_to_insert = []
for data_point in bars["BTC/USD"]:
  
    timestamp_str = data_point.timestamp.strftime('%Y-%m-%d %H:%M:%S')  #formatting the timestamp https://stackoverflow.com/questions/41862525/valueerror-time-data-does-not-match-format-y-m-d-hms-f 
    low_value = data_point.low
    high_value = data_point.high

    # My last sheet entry is 2021-01-01 06:00:00, so 21/1/1 only needs to fill till then 
    if data_point.timestamp > datetime(2021, 1, 1, 6, 0, 0,  tzinfo=pytz.UTC):
        break

    row = [timestamp_str, low_value, high_value]
    data_to_insert.append(row)
'''
# Heading for the first row
headers = ["Timestamp", "Low", "High"]
historical_data.insert_row(headers, index=1, value_input_option='RAW')
'''

# Insert the data into the worksheet starting from row 2
historical_data.insert_rows(data_to_insert, row=2, value_input_option='RAW')
# OK I really hope it will incert into the 2nd row and not touch the existing info. 

"""