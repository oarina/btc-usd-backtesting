import gspread 
from google.oauth2.service_account import Credentials 
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime

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

# --1 USING THE CLIENT
#crypto_client = CryptoHistoricalDataClient()

client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD"],
    timeframe=TimeFrame(15, TimeFrameUnit.Minute), 
    start=datetime(2014, 1, 1),
    end=datetime(2014, 1, 2)
)

bars = client.get_crypto_bars(request_params)

bars["BTC/USD"]
print(bars) # prints what's in the client call
#print(data)  # prints whats in the google sheet
# ------------------------------------------------ TESTING WRITING ONTO GSHEET
'''
# historical_datahe workseet of the test columns and a row. https://docs.gspread.org/en/latest/user-guide.html#clear-a-worksheet
# worksheet.clear()
# so the command worked and it did delete the test data, but in the terminal it says:NameError: name 'worksheet' is not defined


# Extract the relevant data from Alpaca list of lists
data_to_insert = []
for data_point in bars["BTC/USD"]:
  
    timestamp_str = data_point.timestamp.strftime('%Y-%m-%d %H:%M:%S')  #formatting the timestamp https://stackoverflow.com/questions/41862525/valueerror-time-data-does-not-match-format-y-m-d-hms-f 
    low_value = data_point.low
    high_value = data_point.high

    row = [timestamp_str, low_value, high_value]
    data_to_insert.append(row)

# Heading for the first row
headers = ["Timestamp", "Low", "High"]
historical_data.insert_row(headers, index=1, value_input_option='RAW')

# Insert the data into the worksheet starting from row 2
historical_data.insert_rows(data_to_insert, row=2, value_input_option='RAW')
'''