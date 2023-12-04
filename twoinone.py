import re
from time import sleep

'''
def cli_printing_processing_for_user():
    """visual effect of 3 dots printing one after the other after the input phrase as a visual effect for when user prints a valid requested input"""
 
    print("\nInputs collected. Proceeding to next step ", end="")

    for _ in range(3):  # Number of dots
        sleep(1) 
        print(".", end="", flush=True) # https://realpython.com/python-flush-print-output/ 
    print("\n")  # Move to the next line after the dots = jls_extract_def() = jls_extract_def()
'''



# this is an improved version - I will need to 1. finish the trade amount and 2. then make the data pull work
# --after that 3. I can update the original functions =) and 4 . 
# --use the 3 time.sleep dots for when computer is pulling data from the sheet and calculating! Dont use that on every function - it would be annoying
# ----------also - app goes in circles - maybe I need to add abort for those who are not bothered to go through with the whole flow? 

def two_in_one_funct():

    pattern = r'^0(\.\d+)?|1(\.0+)?$' 

    while True:
        fee_amount = input("Enter Trade Fee Percentage from 0% to 1% (eg., 0.5) \n") # at this point is a string
 
        if re.match(pattern, fee_amount) is None:
            print(f"{fee_amount} is an invalid percentage. Please try again.\n")
        else:
            print(" Inputs collected. Proceeding to next step ")
            return fee_amount # teturns that sweet sweet fee!

two_in_one_funct()

"""
def validate_start_time(start_date_time):
    # from cli import get_trade_start_dates # trying to avoid circular passing from one function to another
    
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'

    return bool(re.match(pattern, start_date_time))


def validate_end_time(end_date_time):
    """Validate user datetime format and float input"""
    # from cli import get_trade_dates # trying to avoid circular passing from one function to another
    
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'

    return bool(re.match(pattern, end_date_time))
"""

"""
def validate_trade_fee(fee_amount):

    pattern = r'^0(\.\d+)?|1(\.0+)?$'
    # must start with a 0 -

    if not re.match(pattern, fee_amount): 

        return False

  # Convert to float and check range  - this part is not necessary   
        fee = float(fee_amount)
    if fee < 0.0 or fee > 1.0:
        return False

        return True


def validate_trade_amount(trade_amount):
    """Validate user trade amount input"""
    # What trade amount range is acceptable? 100$ to 1,000,000 $ 
    # I don't want the user to input commas or $ sign for ease of use

    # what about the floatin
    # points? uhhhh! It could be both! Below REGEX should do that =) 
    pattern = r'^\d+(\.\d+)?$' 

    if not re.match(pattern, trade_amount):
        return False

    trade_amount = float(trade_amount)
    if trade_amount < 100 or trade_amount > 1000000:
        return False

        return True    


def funct():

    pattern = r'^(?:100(?:\.0+)?|[1-9]\d{2,6}(?:\.\d+)?)$'

    while True:
        fee = float(input("enter number")) #float
        print(fee)

        # String - if pattern match then move to next step
            #  string  - to float or int.? numeric
                # if in range 
      



funct()

'''  if re.match(pattern, fee):
            print("match:", fee)'''
               # pattern = r'^0(\.\d+)?|1(\.0+)?$' # this accespts a 1 =/

'''

Would the user need all those decimals if they are an aspiring trader?


'''

def validation():







"""