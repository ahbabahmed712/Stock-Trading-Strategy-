# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:07:30 2024

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

# Fetching the 2m interval data for both strategies
data_strategy1 = yf.download(ticker, start=start_date, end=end_date, interval="2m")
data_strategy2 = data_strategy1.copy()

# Check for missing data and handle errors if no data is retrieved
for data in [data_strategy1, data_strategy2]:
    data.dropna(inplace=True)
    if data.empty:
        raise ValueError("No data retrieved. Please check the dates and ticker symbol.")

# Calculate the short-term moving average for the first strategy
data_strategy1['Short_MA'] = data_strategy1['Close'].rolling(window=20).mean()

# Initialize portfolio with $100,000 and shares to hold for the first strategy
initial_capital = float(100000.0)
data_strategy1['Signal'] = np.where(data_strategy1['Close'] > data_strategy1['Short_MA'], 1, 0)
data_strategy1['Position'] = data_strategy1['Signal'].diff()
data_strategy1['Holdings'] = data_strategy1['Signal'] * data_strategy1['Close'] * 100
data_strategy1['Cash'] = initial_capital - (data_strategy1['Position'] * data_strategy1['Close'] * 100).cumsum()
data_strategy1['Total'] = data_strategy1['Cash'] + data_strategy1['Holdings']

# Calculate both short-term and long-term moving averages for the second strategy
data_strategy2['Short_MA'] = data_strategy2['Close'].rolling(window=20).mean()
data_strategy2['Long_MA'] = data_strategy2['Close'].rolling(window=50).mean()
data_strategy2['Signal'] = np.where(data_strategy2['Short_MA'] > data_strategy2['Long_MA'], 1, 0)
data_strategy2['Position'] = data_strategy2['Signal'].diff()
data_strategy2['Holdings'] = data_strategy2['Signal'] * data_strategy2['Close'] * 100
data_strategy2['Cash'] = initial_capital - (data_strategy2['Position'] * data_strategy2['Close'] * 100).cumsum()
data_strategy2['Total'] = data_strategy2['Cash'] + data_strategy2['Holdings']

# Calculate the variance of the 'Total' column for both strategies
variance1 = data_strategy1['Total'].var()
variance2 = data_strategy2['Total'].var()

# Print the results
print(f"Variance of Portfolio 1 (Short-term MA strategy): {variance1:.2f}")
print(f"Variance of Portfolio 2 (MA Crossover strategy): {variance2:.2f}")

# Compare the variances
if variance1 > variance2:
    print("Portfolio 1 is more volatile than Portfolio 2.")
elif variance1 < variance2:
    print("Portfolio 2 is more volatile than Portfolio 1.")
else:
    print("Both portfolios have the same level of volatility.")