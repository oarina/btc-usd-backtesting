import re


def get_trade_start_dates():
    """Requesting start trading date and time from the user"""

    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
     # https://stackoverflow.com/questions/69806492/regex-d4-d2-d2 

    while True:
        start_date_time = input("Enter Trade start Date & Time (e.g., 2021-01-01 06:00:00) \n")

        entered_start_date_time = re.match(pattern, start_date_time) 

        if entered_start_date_time is None:
            print("Invalid format for start date and time. Please try again.\n")
            
        else:    
            print("\n Inputs collected. Proceeding to next step...\n ")
            # print(entered_start_date_time) # <re.Match object; span=(0, 19), match='2021-01-01 06:00:00'>
            #validated = "" # this fixsed naming match error
            validated = entered_start_date_time.group()
            # print(validated)
            return validated


get_trade_start_dates()
'''
learning here is that I have not converted the re.match maybe, 
but at least, declaring var beforehand with "" sting assignmnet fixes the NameError 
that I got previously
'''