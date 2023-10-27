import gspread 
from google.oauth2.service_account import Credentials 
from datetime import datetime
import re
from utility import validate_date_time
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


# -------------------------------------------------- Validating user input test
def validate_date_time(start_date_time):
    """Validate user datetime format and float input"""
    # from cli import get_trade_details # trying to avoid circular passing from one function to another
    
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    # https://stackoverflow.com/questions/69806492/regex-d4-d2-d2 

    if re.match(pattern, start_date_time):
        return True
    return False


'''
# ----------------------------------------------- Test prints and sample data
#  # sample data on row 93145 ['2023-10-19 00:00:00', '28300.878', '28345.3785']
test_date = "2023-10-19 00:00:00"
test_date = datetime.strptime(test_date, "%Y-%m-%d %H:%M:%S") # maybe datetime module will help from PY
print(test_date) # prints 2023-10-19 00:00:00
print("Last row in data:", rows[-1]) # prints Last row in data: ['2023-10-24 00:00:00', '32861.875', '33138.6295']
'''

# ----------------------------------------------- Retrieve low and high

def retrieve_input_price(start_date_time): # using start date time for now only
    '''Retrieve low and high prices from user chosen dates and times'''
    from logic import retrieve_input_price # need to introduce module so that it recognises start_date_time

    for row in rows[1:]:  # start from the second row, assuming first row is headers
        cell_value = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        
        if cell_value == start_date_time: 
            low = float(row[1])
            high = float(row[2])
            print("Low:", low, "High:", high)
            return low, high

    print("Date-time not found in data.start_date_time") 


# retrieve_input_price(start_date_time)


# def calculate_price_fee()