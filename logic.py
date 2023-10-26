import gspread 
from google.oauth2.service_account import Credentials 
from datetime import datetime
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
rows = historical_data.get_all_values()

# ----------------------------------------------- Test prints and sample data
#  # sample data on row 93145 ['2023-10-19 00:00:00', '28300.878', '28345.3785']
test_date = "2023-10-19 00:00:00"
test_date = datetime.strptime(test_date, "%Y-%m-%d %H:%M:%S") # maybe datetime module will help from PY
print(test_date) # prints 2023-10-19 00:00:00
print("Last row in data:", rows[-1]) # prints Last row in data: ['2023-10-24 00:00:00', '32861.875', '33138.6295']


# ----------------------------------------------- Retrieve low and high

def retrieve_input_price(test_date):
    """Retrieve low and high prices from user chosen dates and times"""
    for row in rows[1:]:  # start from the second row, assuming first row is headers
        cell_value = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        
        if cell_value == test_date: # change the test var to a real var later
            low = float(row[1])
            high = float(row[2])
            print("Low:", low, "High:", high)
            return low, high

    print("Date-time not found in data.")
    return None, None 


retrieve_input_price(test_date)


# def calculate_price_fee()

# def validate_user_input()