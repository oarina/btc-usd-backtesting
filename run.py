import gspread  # imports entire gspread library
from google.oauth2.service_account import Credentials  # imports credentials class
# https://alpaca.markets/docs/python-sdk/market_data.html
from alpaca.data.historical import CryptoHistoricalDataClient

from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime

# constant var that tells computer what we are going to access
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

print(data)  # just worked! =)

# Testing the Alpaca hsitorical data client

# --1 USING THE CLIENT
crypto_client = CryptoHistoricalDataClient()

client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD"],
    timeframe=TimeFrame(15, TimeFrameUnit.Minute),  # Adjusted this line for 15 minutes
    start=datetime(2023, 10, 1),
    end=datetime(2023, 10, 2)
)

bars = client.get_crypto_bars(request_params)


# access bars as list - important to note that you must access by symbol key
# even for a single symbol request - models are agnostic to number of symbols
bars["BTC/USD"]
print(bars)

# historical_datahe workseet of the test columns and a row. https://docs.gspread.org/en/latest/user-guide.html#clear-a-worksheet
# worksheet.clear()
 # so the command worked and it did delete the test data, but in the terminal it says:NameError: name 'worksheet' is not defined
print(data)  
'''
# now testing out inserting few datapoints into the spreadsheet by taking empty list and assigning it values
data_to_insert = []
for data_point in bars["BTC/USD"]:
    # got an error TypeError(f'Object of type {o.__class__.__name__} '
    # TypeError: Object of type datetime is not JSON serializable
    # eed to convert the datetime object to a string format before inserting it into the Google Sheet
        timestamp_str = data_point.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        row = [
            timestamp_str,  # Access timestamp directly
            data_point.open,       # Access open price directly
            data_point.close      # Access close price directly
    ]
    data_to_insert.append(row)

# Insert the data into the worksheet
historical_data.insert_rows(data_to_insert, value_input_option='RAW')

# Need further investigation into: https://github.com/alpacahq/alpaca-trade-api-python 
# and https://alpaca.markets/docs/python-sdk/api_reference/data/models.html 
'''