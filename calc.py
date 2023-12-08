'''2021-01-01 06:00:00 2021-01-01 06:00:00
 Start trade Low: 29237.45 Start trade High: 29338.25
 End trade Low: 29237.45 End trade High: 29338.25
Date-time not found in data

return start_low, start_high, end_low, end_high 
canle_start_low candle_start_high --- mybe? we'll see

vars are floats

1
<class 'str'>
100
<class 'str'>
'''



# 1. Average out the candle for start date|  low + high / 2 
# 2. Average out the candle for end date  |  low + high / 2 
# 3. Calculate the fee taken              |  Trade amount * fee
# 4. Calculate the amount of BTC bought   |  After fee Trade amount / Averedeg out start date price
# 5. Calculate the value at exit          |  Amount of BTC bought * Averaged out end date price
# 6. Calculate the prfit or loss          |  Value at exit - after fee trade amount

get_trade_amount = "100" # yes the conversion works with the string and integer =) happy days! =) 
validated_trade_amount = float(get_trade_amount)
print(validated_trade_amount) # 100.0
print(type(validated_trade_amount)) # <class 'float'>

fee = "1"
validated_fee = float(fee)
print(validated_fee) # 1.0
print(type(validated_fee)) # <class 'float'>

start_low = 29237.45 
start_high = 29338.25
end_low = 29237.45
end_high = 29338.25

def calculate_trade():
    "Function that calculates the outcome of a trade"

    averaged_start = (start_low + start_high) / 2  
    print(f"{averaged_start} 1. Average out the candle for start date \n") # 29287.85 1. Average out the candle for start date 

    averaged_end = (end_low + end_high) / 2                   #2
    print(f"{averaged_end} 2. Average out the candle for end date \n")   # 29287.85 2. Average out the candle for end date 

    fee_taken = validated_trade_amount * validated_fee
    print(f"{fee_taken} 3. Calculate the fee taken  \n") # 100.0 3. Calculate the fee taken 

    net_trade_amount = validated_trade_amount - fee_taken
    btc_bought = (validated_trade_amount - fee_taken) / averaged_start  #4
    print(f"{btc_bought} 4. Calculate the amount of BTC bought \n") # 0.0 4. Calculate the amount of BTC bought 

    value_at_exit = btc_bought * averaged_end 
    print(f"{value_at_exit} 5. Calculate the value at exit \n") # 0.0 5. Calculate the value at exit 

    profit_loss = value_at_exit - net_trade_amount
    print(f"{profit_loss}  6. Calculate the prfit or loss ") # -100.0  6. Calculate the prfit or loss 

calculate_trade()







