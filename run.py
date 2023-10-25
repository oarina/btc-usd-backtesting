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
from alpaca_trade_api.rest import REST
import alpaca_trade_api as tradeapi
import traceback


# ------------------------------------------------ Gspread API setup

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

# ------------------------------------------------- Alpaca hsitorical data client
# Reference: https://alpaca.markets/docs/market-data/getting-started/ 

client = CryptoHistoricalDataClient()
request_params = CryptoBarsRequest(
        symbol_or_symbols=["BTC/USD"],
        timeframe=TimeFrame(15, TimeFrameUnit.Minute),
        start=datetime(2023, 10, 19),
        end=datetime(2023, 10, 24)
        )
btc_bars = client.get_crypto_bars(request_params)
btc_bars.df
print(btc_bars)


# ------------------------------------------------ TESTING WRITING ONTO GSHEET

# historical_datahe workseet of the test columns and a row. https://docs.gspread.org/en/latest/user-guide.html#clear-a-worksheet
# worksheet.clear()
# so the command worked and it did delete the test data, but in the terminal it says:NameError: name 'worksheet' is not defined


'''
# Extract the relevant data from Alpaca list of lists and then insert it into the google sheet. 
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
    

# Heading for the first row
headers = ["Timestamp", "Low", "High"]
historical_data.insert_row(headers, index=1, value_input_option='RAW')

# Insert the data into the worksheet starting from row 2
historical_data.insert_rows(data_to_insert, row=2, value_input_option='RAW')
# OK I really hope it will incert into the 2nd row and not touch the existing info. 
'''


last_entry = historical_data.row_values(len(historical_data.col_values(1)))
print(last_entry) # ['2023-10-19 00:00:00', '28300.878', '28345.3785']

data_to_insert = []
for data_point in btc_bars["BTC/USD"]:
    timestamp_str = data_point.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    low_value = data_point.low
    high_value = data_point.high

    row = [timestamp_str, low_value, high_value]
    data_to_insert.append(row)

 # Insert new rows after the last filled row.  - https://stackoverflow.com/questions/40781295/how-to-find-the-first-empty-row-of-a-google-spread-sheet-using-python-gspread
insert_into_last_empty_row = len(historical_data.col_values(1)) + 1  # counts through the rows till the last filled one and +1 find the next empty row
# it printed 2023-10-19 00:00:00 twice  and since I have asked to plus 1 here - len(historical_data.col_values(1)) + 1 it printed the 2023-10-19 00:00:00 on the next line. 
# I am removing the +1 so that It can print over the same date. 
# Furthermore - I will be calling only for a day before because it fills till 00:00:00 for the day

historical_data.insert_rows(data_to_insert, row=insert_into_last_empty_row, value_input_option='RAW')





