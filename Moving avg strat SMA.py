# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:39:57 2024

@author: user
"""

import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set the style for seaborn
sns.set()

# Download high-frequency (2-minute interval) stock price data for McDonald's
ticker = "MCD"
start_date = "2024-02-17"
end_date = "2024-04-16"

# Fetching the 2m interval data
data = yf.download(ticker, start=start_date, end=end_date, interval="2m")

# Check for missing data
data.dropna(inplace=True)

# Error handling if no data is retrieved
if data.empty:
    raise ValueError("No data retrieved. Please check the dates and ticker symbol.")

# Calculate short-term moving average (e.g., 20 periods)
data['Short_MA'] = data['Close'].rolling(window=20).mean()

# Plotting prices and short-term moving average
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['Short_MA'], label='Short MA', alpha=0.9)
plt.title(f'{ticker} Short-Term Moving Average Strategy')
plt.legend()
plt.show()

# Initialize portfolio with $100,000 and shares to hold
initial_capital = float(100000.0)

# Assuming the buy signal is when the price is above the short-term moving average
data['Signal'] = np.where(data['Close'] > data['Short_MA'], 1, 0)

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Holdings (the quantity of stocks in possession - assuming 100 shares per trade)
data['Holdings'] = data['Signal'] * data['Close'] * 100

# Subtract the initial capital by the holdings to get the amount of cash in the portfolio
data['Cash'] = initial_capital - (data['Position'] * data['Close'] * 100).cumsum()

# Get the total value of the portfolio (cash + holdings)
data['Total'] = data['Cash'] + data['Holdings']

# Plotting the portfolio value
plt.figure(figsize=(14, 7))
plt.plot(data['Total'], label='Portfolio value', alpha=0.5)
plt.title(f'{ticker} Short-Term Moving Average Strategy - Portfolio Value')
plt.legend()
plt.show()

# Print the final portfolio value
if not data['Total'].empty:
    final_portfolio_value = data['Total'].iloc[-1]
    print(f"Final Portfolio Value: ${final_portfolio_value:,.2f}")
else:
    print("Not enough data to calculate the final portfolio value.")
