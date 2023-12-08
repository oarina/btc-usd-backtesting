'''2021-01-01 06:00:00 2021-01-01 06:00:00
 Start trade Low: 29237.45 Start trade High: 29338.25
 End trade Low: 29237.45 End trade High: 29338.25
Date-time not found in data'''

 def calculate_trade():

# 1. Average out the candle for start date|  low + high / 2 
# 2. Average out the candle for end date  |  low + high / 2 
# 3. Calculate the fee taken              |  Trade amount * fee
# 4. Calculate the amount of BTC bought   |  After fee Trade amount / Averedeg out start date price
# 5. Calculate the value at exit          |  Amount of BTC bought * Averaged out end date price
# 6. Calculate the prfit or loss          |  Value at exit - after fee trade amount


