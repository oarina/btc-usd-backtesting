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
#from alpaca_trade_api.rest import REST
#import alpaca_trade_api as tradeapi
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

# --------------------------------------------------------------------------------------------------- RETRIEVE AND CALCULATE

def retrieve_input_price(validated_start_date_time, validated_end_date_time): 
    '''Retrieve low and high prices from user chosen dates and times'''
    #from logic import retrieve_input_price # need to introduce module so that it recognises start_date_time

    validated_start_date_time = datetime.strptime(validated_start_date_time, "%Y-%m-%d %H:%M:%S")
    validated_end_date_time = datetime.strptime(validated_end_date_time, "%Y-%m-%d %H:%M:%S")
    print(validated_start_date_time, validated_end_date_time)

    for row in data[1:]:  # start from the second row, as first row is headers
        cell_value = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        
        if cell_value == validated_start_date_time: 
            start_low = float(row[1])
            start_high = float(row[2])
            print(" Start trade Low:", start_low, "Start trade High:", start_high)
            # return start_low

        if cell_value == validated_end_date_time:
            end_low = float(row[1])
            end_high = float(row[2])
            print(" End trade Low:", end_low, "End trade High:", end_high)
            # return end_low, end_high
    
    print("Date-time not found in data")
    return start_low, start_high, end_low, end_high



# Will take validated_start_date_time, validated_end_date_time, validated_trade_amount, validated_fee
# calc conservative approach: take the lowest amount of the two for the entry and highest for the exit and * by percentage.  - 
# calc the balanced approach: average out the candles
# calc fee trade_amount * fee_percentage. trade outcome - fee

# --------------------------------------------------------------------------------------------------- CALCULATE THE INPUT   
# def calculate_trade():

# 1. Average out the candle for start date|  low + high / 2 
# 2. Average out the candle for end date  |  low + high / 2 
# 3. Calculate the fee taken              |  Trade amount * fee
# 4. Calculate the amount of BTC bought   |  After fee Trade amount / Averedeg out start date price
# 5. Calculate the value at exit          |  Amount of BTC bought * Averaged out end date price
# 6. Calculate the prfit or loss          |  Value at exit - after fee trade amount



# --------------------------------------------------------------------------------------------------- REQUEST AND VALIDATE INPUT
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

    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
     # https://stackoverflow.com/questions/69806492/regex-d4-d2-d2 

    while True:
        start_date_time = input("Enter Trade start Date & Time (e.g., 2021-01-01 06:00:00) \n")
        
        entered_start_date_time = re.match(pattern, start_date_time) 

        if entered_start_date_time is None:
            print(f"{start_date_time} is an invalid format for start date and time. Please try again.\n")
        else:
            print("\n Inputs collected. Proceeding to next step...\n ")
            validated_start_date_time = entered_start_date_time.group() # thanks to Lead Craig Hudsom https://code-institute-room.slack.com/archives/C01DVU37QG4/p1701689116949349?thread_ts=1701688094.633659&cid=C01DVU37QG4 
            print(type(validated_start_date_time))
            print(validated_start_date_time)
            return validated_start_date_time

def get_trade_end_dates():
    """Requesting end trading date and time from the user"""

    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'

    while True:
        end_date_time = input("Enter Trade Exit Date & Time (e.g., 2021-01-01 07:00:00) \n")

        entered_end_date_time = re.match(pattern, end_date_time)

        if entered_end_date_time is None:
              print(f"{end_date_time} is an nvalid format for end date and time. Please try again.\n")
        else:
            print("\n Inputs collected. Proceeding to next step...\n")
            validated_end_date_time = entered_end_date_time.group()
            return validated_end_date_time

def get_trade_fee():
    """Requesting trading fee from a user"""
    
    pattern = r'^0(\.\d+)?|1(\.0+)?$' # stirng 

    while True:
        fee_amount = (input("Enter Trade Fee Percentage from 0% to 1% (eg., 0.5) \n")) # string
        
        if (re.match(pattern, fee_amount)) is None:
            print(f"{fee_amount} is an invalid percentage. Please try again.\n")
        else:
            print("\n Inputs collected. Proceeding to next step...\n")
            return fee_amount # this future float is still a string 

def get_trade_amount():
    """Requsting a trade amount in USD in range of 100$ to 1,000,000 $ from the user"""
    
    pattern =  pattern = r'^(?:100(?:\.0+)?|[1-9]\d{2,6}(?:\.\d+)?)$' #both accepts float and integer

    while True:
        trade_amount = input("Enter Trade amount in USD (e.g. 100) \n")
        
        if re.match(pattern, trade_amount) is None:
            print(f"{trade_amount} is an invalid amount. Please try again.\n")
        else:
            print("\n Inputs collected. Proceeding to next step...\n")
            return trade_amount

# --------------------------------------------------------------------------------------------------- CLI       
# --------------------------------------------------------------------------------------------------- CORE PATHWAYS/USER FLOW
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
   
    print("\n\n===============================================\n\n")
    print("---------BTC/USD Trade Backtesting Tool--------\n\n")
    print("===============================================\n")

    print("Please keep in mind that trade information should be provided in the following format: YYYY-MM-DD HH:MM:SS.")
    print("Additionally, please be aware that the available data is stored in 15-minute candles and starts from the year 2021.\n")

    print("===============================================")
    print("Please choose from one of the following options:")

    display_user_flow_options()

def display_user_flow_options():
    """Provides user with options to either a trade or exit"""

    choice = input("Enter 1 to backtest or 2 to exit: \n")
    if choice == "1":
        validated_start_date_time = get_trade_start_dates()
        validated_end_date_time = get_trade_end_dates()
        fee_amount = get_trade_fee()
        trade_amount = get_trade_amount()
        retrieve_input_price(validated_start_date_time, validated_end_date_time)

    elif choice == "2":
        display_end_program_message()
    else:
        print("!!! Not quite right. Please make sure your entry is 1 or 2 only\n")
        display_user_flow_options()

# Calling fumct
display_start_welcome_message()


    

