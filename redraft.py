import re
from time import sleep
# references:  sleep(1) # pauses for 1 sec # https://docs.python.org/3/library/time.html  /  https://realpython.com/python-sleep/#:~:text=The%20time%20module%20has%20a,however%20many%20seconds%20you%20specify.&text=If%20you%20run%20this%20code,new%20statement%20in%20the%20REPL. 
# reference: throwaway variable _: https://www.studytonight.com/python-howtos/how-to-use-single-underscore-_-in-python-variable 
'''
def cli_printing_processing_for_user():
    """visual effect of 3 dots printing one after the other after the input phrase as a visual effect for when user prints a valid requested input"""
 
    print("\nInputs collected. Proceeding to next step ", end="")

    for _ in range(3):  # Number of dots
        sleep(1) 
        print(".", end="", flush=True) # https://realpython.com/python-flush-print-output/ 
    print("\n")  # Move to the next line after the dots = jls_extract_def() = jls_extract_def()
'''
def cli_printing_processing_for_user():
    '''Function that adds a 3 dot visual effect with a second pause during dot print after valid user input'''
    
    for dot in range(3):
        sleep(1)
        print(".", end="", flush=True)

    print(" Inputs collected. Proceeding to next step ")

0

def trade_fee():
    '''Let's try validate and intake fee at the same time - this function will go in circles until the user makes a valid input'''

    pattern = r'^0(\.\d+)?|1(\.0+)?$' # https://www.youtube.com/watch?v=5d3vQ8N0MJg - re match regex python; https://www.youtube.com/watch?v=nxjwB8up2gI
    
    while True:
        fee_amount = input("Enter Trade Fee Percentage from 0% to 1% (eg., 0.5) \n") # at this point is a string
 
        if re.match(pattern, fee_amount) is None:
            print(f"{fee_amount} is an invalid percentage. Please try again.\n")
        else:
            cli_printing_processing_for_user()
            return fee_amount

trade_fee()


# this is an improved version - I will need to 1. finish the trade amount and 2. then make the data pull work
# --after that 3. I can update the original functions =) and 4 . 
# --use the 3 time.sleep dots for when computer is pulling data from the sheet and calculating! Dont use that on every function - it would be annoying
# ----------also - app goes in circles - maybe I need to add abort for those who are not bothered to go through with the whole flow? 