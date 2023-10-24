# This module is for Command Line Interface (CLI) related functions

def display_start_welcome_message():
    """Displays a welcome message to the user"""
    
    print("Welcome to the BTC/USD Trade Backtester!")
    print("Please choose from one of the following options:")
    print("===============================================")
    print("1. Backtest your trade")
    print("2. Exit")
    return input("Enter your choice (1/2): ")

    if choice == "1":
        display_trade_entry_example()
    elif choice == "2":
        display_end_program_message()

display_start_welcome_message()

def display_trade_entry_example():
    """Gives a tade entry example to a user"""

    print("Please input your trade details like so:")
    print("===============================================")
    print("Start Date & Time: 2021-01-01 06:00:00")
    print("End Date & Time: 2021-01-02 06:00:00")
    print("Fee Percentage: 0.5")

display_trade_entry_example()

def get_trade_details():
    """Prompts the user to enter trade details"""

    start_date_time = input("Enter Start Date & Time (e.g., 2021-01-01 06:00:00): ")
    end_date_time = input("Enter End Date & Time (e.g., 2021-01-02 06:00:00): ")
    fee_percentage = input("Enter Fee Percentage (e.g., 0.5): ")

    return start_date_time, end_date_time, float(fee_percentage)


# def display_trade_calculation_result()

def display_go_again_ask_message():
    """Asks the user if they want to input another trade"""

    print("Would you like to backtest another trade?")
    print("===============================================")
    print("1. Backtest your trade again")
    print("2. Exit")
    return input("Enter your choice (1/2): ")
    
    if choice == "1":
        display_trade_entry_example()
    elif choice == "2":
        display_end_program_message()

display_go_again_ask_message()    

def display_end_program_message():
    """Gives an exit message to the user"""

    print("Thank you for using the BTC/USD Trade Backtester. Happy Trading!")

display_end_program_message()
