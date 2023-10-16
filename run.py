import gspread # imports entire gspread library
from google.oauth2.service_account import Credentials # imports credentials class
from alpaca.data.historical import CryptoHistoricalDataClient 

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
# Writing this for a commit test