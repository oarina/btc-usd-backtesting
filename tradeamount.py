import re

def get_trade_amount():
    """Requsting a trade amount in USD from the user"""
    
    pattern = r'^\d+(\.\d+)?$' 
    
    while True:
        trade_amount = (input("Enter Trade amount in USD (e.g. 100) \n"))

        if re.match(pattern, trade_amount):
            if trade_amount < 100 or trade_amount > 1000000:
                return False
            print(f"{trade_amount} is an invalid amount. Please try again.\n")
        else:
            print("\n Inputs collected. Proceeding to next step...\n")
            return trade_amount
'''
def validate_trade_amount(trade_amount):
    """Validate user trade amount input"""
    # What trade amount range is acceptable? 100$ to 1,000,000 $ 
    # I don't want the user to input commas or $ sign for ease of use

    # what about the floating points? uhhhh! It could be both! Below REGEX should do that =) 
    pattern = r'^\d+(\.\d+)?$' 

    if not re.match(pattern, trade_amount):
        return False

    trade_amount = float(trade_amount)
    if trade_amount < 100 or trade_amount > 1000000:
        return False

        return True    
'''
get_trade_amount()


# testing : put in 0, 10000000000000000000, characters