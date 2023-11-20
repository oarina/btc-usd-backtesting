
import re

def get_trade_fee():
    """Requesting trading fee from a user"""

    # fee_percentage = input("Enter Fee Percentage (e.g., 0.5) \n"

    while True:
        fee_amount = float(input("Enter Trade Fee Percentage from 0% to 1% (eg., 0.5) \n"))

        if validate_trade_fee(fee_amount):
             print("\n Inputs collected. Proceeding to next step...\n")
             break
        
        else:
            print("Invalid percentage. Please try again.\n")

    return fee_amount

def validate_trade_fee(fee_amount):
        """Validate user trade fee input. This fuction will accept anything from 0 to 1 including a floating numbers. It will feed to get_trade_detais() and print a CLI message if needed"""
        
        pattern = r'^0(\.\d+)?|1(\.0+)?$'

        '''
        if not isinstance(fee_amount, (float, int)):
            return False

        if not re.match(pattern, str(fee_amount)): 
            return False

        fee = float(fee_amount)
        if fee < 0.0 or fee > 1.0:
            return True
        else:
            return True
        '''

get_trade_fee()



"""
def trade_fee():
    '''Let's try validate and intake fee at the same time'''

    fee_amount = input("Enter Trade Fee Percentage from 0% to 1% (eg., 0.5) \n") # at this point is a string
    pattern = r'^0(\.\d+)?|1(\.0+)?$' # https://www.youtube.com/watch?v=5d3vQ8N0MJg - re match regex python; https://www.youtube.com/watch?v=nxjwB8up2gI
    
    if re.match(pattern, fee_amount) is None:
        print("Invalid percentage. Please try again.\n")
    else:
        print("\n Inputs collected. Proceeding to next step...\n")
        return fee_amount

trade_fee()
"""

# if input is a letter or space or character - print invalid and ask to input again 
# if a number - should be a float or integer in range of 0.0 to 1.0. Anything other - print invalid and ask to input again
# can it pretend loading and give . then . then . ?

"""

def cli_printing_processing_for_user():
        print("\n Inputs collected.")
        time.sleep(1)
        print("\n Inputs collected. Proceeding to next step...\n")
        time.sleep(1)
        print("\n Inputs collected. Proceeding to next step...\n")
    
"""