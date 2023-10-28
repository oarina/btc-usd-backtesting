import re
from cli import get_trade_details
# Document designed for fuctions that would have otherwised been basspig between cli and logic docs - attempt to avoid circular passing and crashing
'''
def validate_date_time(start_date_time):
    """Validate user datetime format and return True if valid, else False"""
    # from cli import get_trade_details # trying to avoid circular passing from one function to another

    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$' # https://stackoverflow.com/questions/69806492/regex-d4-d2-d2  

    if re.match(pattern, start_date_time):
        return True
    return False

# return bool(re.match(pattern, input_str))
""