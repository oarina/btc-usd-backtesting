import re

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


# testing : put in 0, 10000000000000000000

'''   while True:
        trade_amount = input("Enter Trade amount in USD (e.g. 100) \n")
        
        if re.match(pattern, trade_amount):
            trade_amount = float(trade_amount) # trade amount must be a float
            if 100.00 <= trade_amount <= 10000000.00: 
                print(f"{trade_amount} is an invalid amount. Please try again.\n")
        else:
            print("\n Inputs collected. Proceeding to next step...\n")
            return trade_amount'''


'''   
    pattern =  pattern = r'^(?:100(?:\.0+)?|[1-9]\d{2,6}(?:\.\d+)?)$' #both accepts float and integer
    trade_amount = 0

    while 100 <= trade_amount <= 10000000:
        trade_amount = input("Enter Trade amount in USD (e.g. 100) \n")
        trade_amount = float(trade_amount) # trade amount must be a float
        
        if re.match(pattern, trade_amount) is None:
            print(f"{trade_amount} is an invalid amount. Please try again.\n")
        else:
            print("\n Inputs collected. Proceeding to next step...\n")
            return trade_amount'''