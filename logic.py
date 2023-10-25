import gspread 
from google.oauth2.service_account import Credentials 
# This module will containt the logic for retrieval, validation and calculation of data

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

# ----------------------------------------------- Calculations
#  # ['2023-10-19 00:00:00', '28300.878', '28345.3785']
test_date = 2023-10-19 00:00:00

# def validate_user_input()

def retrieve_input_price(test_date):
    """Retrieve low and high prices from user chosen dates and times"""
    # data = historical_data.get_all_values
    for row in data:
           row == test_date:

    return low_value, high_value # those vars seem to be local in run.py - should be ok. double check
print(low_value, high_value)

# def calculate_price_fee()