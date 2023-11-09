![BTC/USD Backtester](https://btc-usd-backtester-645f261abdd8.herokuapp.com/)

# BTC/USD Backtester

The BTC/USD Backtester is a simple command-line application for backtesting a hypothetical Bitcoin trade against historical pricing data.

## How to Use

1. Run the app.
2. Enter `1` to backtest a trade or `2` to exit when prompted.
3. Input the trade details (start date/time, end date/time, fee percentage).
4. View the results including starting price, ending price, fees, and profit/loss.

## Features

- Validates user inputs for proper datetime format and valid fee percentage.
- Retrieves historical 15 minute candles BTC/USD pricing data from a Google Sheet.
- Calculates profit or loss for the backtested trade including fees.
- Trade Fee is from 0 to 1% and note that this does not include crypto transaction gas fees. 
- Uses a simple flat fee mode and a trade input format YYYY-MM-DD HH:MM:SS
- Provides clear user prompting and error handling.


## Data Model

The app uses a Google Sheet with pricing data structured 
Timestamp	Low	High
2021-01-01 06:00:00	29237.45	29338.25


## User Stories

### Casual Crypto Enthusiast - Easy Backtest
- I want to: Understand how much profit (or loss) I would've made by buying and selling BTC on specific dates.
- So that: I can see how well I would've done if I'd acted on my hunches.

#### Acceptance Criteria
- The tool should allow me to easily input the buy and sell dates/times.
- It should display a simple breakdown: initial investment, final value, gross profit/loss, fee amount, and net profit/loss.
- There should be an easy and clear user guide that helps me understand how to use the tool without prior backtesting experience.

### Aspiring Trader - Impact of Fees
- I want to: Understand how much profit (or loss) I would've made by buying and selling BTC on specific dates.
- So that: I can see how even a single trade is influenced by fees, setting the foundation for my understanding before I scale up to multiple trades.

#### Acceptance Criteria
- The tool should allow me to input single trade (buy/sell pair).
- It should provide a breakdown of results for a trade, highlighting the fees.
- The tool should emphasize the difference between the gross outcome and net outcome (after fees).
- A brief note on the impact of fees and how they can add up with increased trading frequency would be educational.

### Researcher - Historical Price Exploration: reputable source 
- I want to: Explore historical BTC/USD prices for specific timeframes.
- So that: I can gather insights on price movements and volatility for my research.

#### Acceptance Criteria:
- The tool should allow me to input a start and end date/time.
- It should display the opening, closing, highest, and lowest prices within that timeframe.
- A simple visualization or chart (even if it's just a link to the Google Sheet's chart) would be a bonus.
- It would be beneficial to have a note or reference on where the historical data comes from to ensure its reliability.


## ISSUE I RAN INTO
- I used Alpaca API and alpaca-py library with a client and successfully retrieved data till 2021, but I would get empty lists after that date.  The free tier promised to give 5 + years of free historical data and I reached out to support. I have reached out to support who confired that they have data till 2021. 





