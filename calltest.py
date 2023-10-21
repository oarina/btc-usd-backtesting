from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import datetime

client = CryptoHistoricalDataClient()

# Creating request object
request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD"],
    timeframe=TimeFrame.Day,
    start=1697493600000,
    end=1697798043263
)

"""
request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD"],
    timeframe=TimeFrame.Day,
    start="2022-09-01T00:00:00Z",  # ISO 8601 format with "T" and "Z" for UTC timezone
    end="2022-09-07T00:00:00Z"
)

tried this and also did not work:  start=datatime(2021, 1, 1, 0, 0, 0),
    end=datatime(2021, 1, 2, 0, 0, 0)
"""
# Retrieve daily bars for Bitcoin in a DataFrame and printing it
btc_bars = client.get_crypto_bars(request_params)
# Convert to dataframe - as per example
btc_bars.df
print(btc_bars)

