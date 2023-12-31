import gspread
#import pytz # this is to help talk to api and specifiy the timezone we mean 
#import json
#import requests
import os
from google.oauth2.service_account import Credentials 

from alpaca.data.historical import CryptoHistoricalDataClient
# from alpaca_trade_api.rest import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime
from alpaca_trade_api.rest import REST
import alpaca_trade_api as tradeapi
import traceback

import re
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning) #deprecation warning fix attept 

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

"""
# ------------------------------------------------- Alpaca hsitorical data client

def use_thsi_if_need_latest_data
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

# ------------------------------------------------  WRITING ONTO GSHEET


last_entry = historical_data.row_values(len(historical_data.col_values(1)))
print(last_entry) # ['2023-10-19 00:00:00', '28300.878', '28345.3785']

data_to_insert = []
for data_point in btc_bars["BTC/USD"]:
    timestamp_str = data_point.timestamp.strftime('%Y-%m-%d %H:%M:%S')  #formatting the timestamp https://stackoverflow.com/questions/41862525/valueerror-time-data-does-not-match-format-y-m-d-hms-f 
    low_value = data_point.low
    high_value = data_point.high

    row = [timestamp_str, low_value, high_value]
    data_to_insert.append(row)

 # Insert new rows after the last filled row.  - https://stackoverflow.com/questions/40781295/how-to-find-the-first-empty-row-of-a-google-spread-sheet-using-python-gspread
insert_into_last_empty_row = len(historical_data.col_values(1))  # counts through the rows till the last filled one and +1 find the next empty row
# it printed 2023-10-19 00:00:00 twice  and since I have asked to plus 1 here - len(historical_data.col_values(1)) + 1 it printed the 2023-10-19 00:00:00 on the next line. 
# I am removing the +1 so that It can print over the same date. 
# Furthermore - I will be calling only ecause it fills till 00:00:00 for the day

historical_data.insert_rows(data_to_insert, row=insert_into_last_empty_row, value_input_option='RAW')
"""

# --------------------------------------------------------------------------------------------------- LOGIC

def retrieve_input_price(validated_start_date_time, validated_end_date_time): # using start date time for now only
    '''Retrieve low and high prices from user chosen dates and times'''
    #from logic import retrieve_input_price # need to introduce module so that it recognises start_date_time

    for row in rows[1:]:  # start from the second row, assuming first row is headers
        cell_value = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        
        if cell_value == validated_start_date_time: 
            start_low = float(row[1])
            start_high = float(row[2])
            print(" Start trade Low:", start_low, "Start trade High:", start_high)
            return start_low, start_high

        if cell_value == validated_end_date_time:
            end_low = float(row[1])
            end_high = float(row[2])
            print(" End trade Low:", end_low, "End trade High:", end_high)
            return end_low, end_high

    print("Date-time not found in data")

def validate_start_time(start_date_time):
    """Validate user datetime format and float input"""
    # from cli import get_trade_start_dates # trying to avoid circular passing from one function to another
    
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    # https://stackoverflow.com/questions/69806492/regex-d4-d2-d2 

    return bool(re.match(pattern, start_date_time))

def validate_end_time(end_date_time):
    """Validate user datetime format and float input"""
    # from cli import get_trade_dates # trying to avoid circular passing from one function to another
    
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    # https://stackoverflow.com/questions/69806492/regex-d4-d2-d2 

    return bool(re.match(pattern, end_date_time))

def validate_trade_fee(fee_amount):
    """Validate user trade fee input"""
        if not re.match(r'^\d+\.\d+$', fee_amount):
        return False

  # Convert to float and check range    
        fee = float(fee_amount)
        if fee < 0.0 or fee > 1.0:
        return False

        return True


def validate_trade_amount():
    """Validate user trade amount input"""



# def calculate_trade():

# Will take validated_start_date_time, validated_end_date_time, validated_trade_amount, validated_fee
# calc itself: take the lowest amount of the two for the entry and highest for the exit and * by percentage. 
# calc fee trade_amount * fee_percentage. trade outcome - fee
# exit - entry

# --------------------------------------------------------------------------------------------------- CLI
'''
def get_trade_dates():
    """Requesting start and end trading dates and times from the user"""

    print("Please enter the trade in the following format YYYY-MM-DD HH:MM:SS\n")

    start_date_time = input("Enter Trade start Date & Time (e.g., 2021-01-01 06:00:00) \n")

    while not validate_start_time(start_date_time):
        print("Invalid format. Please enter the Date & Time in the following format YYYY-MM-DD HH:MM:SS\n")
        start_date_time = input("Enter Trade start Date & Time (e.g., 2021-01-01 06:00:00) \n")

    end_date_time = input("Enter Trade Exit Date & Time (e.g., 2022-01-02 06:00:00) \n")
    
    while not validate_end_time(end_date_time):
        print("Invalid format. Please enter the Date & Time in the following format YYYY-MM-DD HH:MM:SS\n")
        end_date_time = input("Enter Trade Exit Date & Time (e.g., 2022-01-02 06:00:00) \n")

    return start_date_time, end_date_time  # Return both start_date_time and end_date_time
'''
def get_trade_start_dates():
    """Requesting start trading date and time from the user"""

    while True:
        start_date_time = input("Enter Trade start Date & Time (e.g., 2021-01-01 06:00:00) \n")

        if validate_start_time(start_date_time):
            break  # Exit the loop if a valid start date and time is provided

        print("Invalid format for start date and time. Please try again.\n")

    return start_date_time

def get_trade_end_dates():
    """Requesting end trading date and time from the user"""

    while True:
        end_date_time = input("Enter Trade Exit Date & Time (e.g., 2022-01-02 06:00:00) \n")

        if validate_end_time(end_date_time):
            break  # Exit the loop if a valid end date and time is provided

        print("Invalid format for end date and time. Please try again.\n")

    return end_date_time  # Return both start_date_time and end_date_time


def get_trade_fee():
    """Requesting trading fee from a user"""

    # fee_percentage = input("Enter Fee Percentage (e.g., 0.5): \n"
    print("Plese enter the trade fee percentage amount")
    fee_amount = float(input("Input fee (eg., 0.5)"))
    return fee_amount

def get_trade_amount():
    """Requsting a trade amount in USD from the user"""

    
    print("Please enter the trade amount in USD")
    trade_amount = float(input("Enter Trade amount in USD (e.g. 100)"))
    return trade_amount

def display_go_again_ask_message():
    """Asks the user if they want to input another trade"""

    while True:
        print("Would you like to backtest another trade?")
        print("===============================================")
        choice = input("Enter 1 to backtest again or 2 to exit: \n")

    if choice == "1":
        get_trade_start_dates()
        return
    elif choice == "2":
        display_end_program_message()
        return
    else:
        print("Please make sure to enter 1 or 2 only. Go again.")
        display_go_again_ask_message()
        # so we have an issue where the fucntion is calling itself and it takes a long time to respond after i press 1

def display_end_program_message():
    """7. Gives an exit message to the user"""

    print("Thank you for using the BTC/USD Trade Backtester. Happy Trading!")
    # display_end_program_message()

# Put the beginning at the end because I needed to define all the functions that I will call below for it to work
def display_start_welcome_message():
    """1. Displays a welcome message to the user"""
    
    print("Welcome to the BTC/USD Trade Backtesting tool! Please keep in mind that trade information should be provided in the following format: YYYY-MM-DD HH:MM:SS. Additionally, please be aware that the available data starts from the year 2021 and is recorded at 15-minute intervals.\n")
    print("===============================================")
    print("Please choose from one of the following options:")
    choice = input("Enter 1 to backtest or 2 to exit: \n")

    if choice == "1":
        start_date_time = get_trade_start_dates()
        end_date_time = get_trade_end_dates()
        fee_amount = get_trade_fee()
        trade_amount = get_trade_amount()
    elif choice == "2":
        display_end_program_message()
    else:
        print("!!! Not quite right. Please make sure your entry is 1 or 2 only\n")
        display_start_welcome_message()

# Calling fumct
display_start_welcome_message()



    

