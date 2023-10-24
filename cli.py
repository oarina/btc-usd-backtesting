# This module is for CLI related functions

def display_start_welcome_message():
    """Displays a welcome message to the user"""
    
    print("Welcome to the BTC/USD Trade Backtester!")
    print("Please choose from one of the following options:")
    print("===============================================")
    print("1. Backtest your trade")
    print("2. Exit")
    return input("Enter your choice (1/2): ")

display_start_welcome_message()

def display_trade_entry_example():
    """Gives a tade entry example to a user"""

    print("Please input your trade details like so:")
    print("===============================================")
    print("Start Date & Time: 2021-01-01 06:00:00")
    print("End Date & Time: 2021-01-02 06:00:00")
    print("Fee Percentage: 0.5")

display_trade_entry_example()

# def display_trade_calculation_result()

def display_go_again_ask_message():
    """Asks the user if they want to input another trade"""
    
    

def display_end_program_message():
    """Gives an exit message to the user"""

    print("Thank you for using the BTC/USD Trade Backtester. Happy Trading!")

display_end_program_message()
