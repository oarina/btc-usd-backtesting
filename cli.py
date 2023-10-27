# This module is for Command Line Interface (CLI) related functions
import warnings
from utility import validate_date_time
warnings.simplefilter(action='ignore', category=DeprecationWarning) #deprecation warning fix attept 

# ----------------------------------------------------------------------- ----------------------- CLI
"""
def display_trade_entry_example():
    #Gives a tade entry example to a user

    print("Please input your trade details like so:")
    print("===============================================")
    print("Start Date & Time: 2021-01-01 06:00:00")
    print("End Date & Time: 2021-01-02 06:00:00")
    print("Fee Percentage: 0.5")
    display_trade_entry_example()
"""

# ---------------------------------------------------------------- get trade detail  start 

def get_trade_details():
    """2. Prompts the user to enter trade details with provided entry examples"""

    print("Please enter the Date & Time in the following format YYYY-MM-DD HH:MM:SS\n")
    start_date_time = input("Enter Start Date & Time (e.g., 2021-01-01 06:00:00) \n")

    return start_date_time

"""
def get_trade_details():

   # from logic import validate_date_time
    # from logic import retrieve_input_price

    print("Please enter the Date & Time in the following format YYYY-MM-DD HH:MM:SS\n")
    start_date_time = input("Enter Start Date & Time (e.g., 2021-01-01 06:00:00) \n")

    while not validate_date_time(start_date_time):
        print("Invalid format. Please enter the Date & Time in the following format YYYY-MM-DD HH:MM:SS\n")
        start_date_time = input("Enter Start Date & Time (e.g., 2021-01-01 06:00:00) \n")

    # end_date_time = input("Enter End Date & Time (e.g., 2021-01-02 06:00:00) \n")
    # fee_percentage = input("Enter Fee Percentage (e.g., 0.5): \n")

    return start_date_time # end_date_time, float(fee_percentage)
    """

# ---------------------------------------------------------------- get trade detail s end
# def display_trade_calculation_result()

def display_go_again_ask_message():
    """Asks the user if they want to input another trade"""

    while True:
        print("Would you like to backtest another trade?")
        print("===============================================")
        choice = input("Enter 1 to backtest again or 2 to exit: \n")

    if choice == "1":
        get_trade_details()
        return
    elif choice == "2":
        display_end_program_message()
        return
    else:
        print("Please make sure to enter 1 or 2 only. Go again.")
        display_go_again_ask_message()
        # so we have an issue where the fucntion is calling itself and it takes a long time to respond after i press 1. 

# display_go_again_ask_message()    

def display_end_program_message():
    """7. Gives an exit message to the user"""

    print("Thank you for using the BTC/USD Trade Backtester. Happy Trading!")
    # display_end_program_message()


# Put the beginning at the end because I needed to define all the functions that I will call below for it to work
def display_start_welcome_message():
    """1. Displays a welcome message to the user"""
    
    print("Welcome to the BTC/USD Trade Backtesting tool!")
    print("===============================================")
    print("Please choose from one of the following options:")
    choice = input("Enter 1 to backtest or 2 to exit: \n")

    if choice == "1":
        start_date_time = get_trade_details()
    elif choice == "2":
        display_end_program_message()
    else:
        print("Not quite right. Please make sure your entry is 1 or 2 only")
        display_start_welcome_message()

display_start_welcome_message()


'''
def get_trade_details():
    """2. Prompts the user to enter trade details with provided entry examples"""

    start_date_time = input("Enter Start Date & Time (e.g., 2021-01-01 06:00:00): \n")
    end_date_time = input("Enter End Date & Time (e.g., 2021-01-02 06:00:00): \n")
    fee_percentage = input("Enter Fee Percentage (e.g., 0.5): \n")

    return start_date_time, end_date_time, float(fee_percentage)


    
'''