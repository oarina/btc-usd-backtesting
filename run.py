import gspread # imports entire gspread library
from google.oauth2.service_account import Credentials # imports credentials class
from alpaca.data.historical import CryptoHistoricalDataClient # https://alpaca.markets/docs/python-sdk/market_data.html 

from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
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

print(data) #just worked! =) 

#Testing the Alpaca hsitorical data client 

# --1 USING THE CLIENT
crypto_client = CryptoHistoricalDataClient() 

client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD"],
                        timeframe=TimeFrame.Day,
                        start=datetime(2023, 10, 1),
                        end=datetime(2023, 10, 2)
                 )

bars = client.get_crypto_bars(request_params)


# access bars as list - important to note that you must access by symbol key
# even for a single symbol request - models are agnostic to number of symbols
bars["BTC/USD"]
print(bars)

# historical_datahe workseet of the test columns and a row. https://docs.gspread.org/en/latest/user-guide.html#clear-a-worksheet 
worksheet.clear() 
print(data)