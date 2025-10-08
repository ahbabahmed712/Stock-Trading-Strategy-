import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set the style for seaborn
sns.set()

# Download high-frequency (2-minute interval) stock price data for McDonald's
ticker = "MCD"
start_date = "2024-02-15"  # Assuming the last 60 days from the end of 2022
end_date = "2024-04-16"

# Fetching the 2m interval data
data = yf.download(ticker, start=start_date, end=end_date, interval="2m")

# Check for missing data
data.dropna(inplace=True)

# Calculate short-term and long-term moving averages (e.g., 20 periods and 50 periods)
data['Short_MA'] = data['Close'].rolling(window=20).mean()
data['Long_MA'] = data['Close'].rolling(window=50).mean()

# Initialize 'Signal' column to 0
data['Signal'] = 0


# np.where can handle the alignment internally, so we don't need to slice data['Signal']
data['Signal'] = np.where(data['Short_MA'] > data['Long_MA'], 1, 0)

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
#plt.plot(data['Short_MA'], label='Short MA', alpha=0.9)
#plt.plot(data['Long_MA'], label='Long MA', alpha=0.9)
plt.scatter(data.index[data['Position'] == 1], data['Close'][data['Position'] == 1], label='Buy Signal', marker='^', color='g')
plt.scatter(data.index[data['Position'] == -1], data['Close'][data['Position'] == -1], label='Sell Signal', marker='v', color='r')
plt.title(f'{ticker} Moving Average Crossover Trading Strategy')
plt.legend()
plt.show()


data.dropna(inplace=True)

# Calculate short-term and long-term moving averages (e.g., 20 periods and 50 periods)
data['Short_MA'] = data['Close'].rolling(window=20).mean()
data['Long_MA'] = data['Close'].rolling(window=50).mean()

# Initialize 'Signal' column to 0
data['Signal'] = 0

# Using np.where to assign signals
data['Signal'] = np.where(data['Short_MA'] > data['Long_MA'], 1, 0)

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Initialize portfolio with $100,000 and shares to hold
initial_capital = float(100000.0)
data['Holdings'] = data['Signal'] * data['Close'] * 100  # Assuming 100 shares per trade

# Subtract the initial capital by the holdings to get the amount of cash in the portfolio
data['Cash'] = initial_capital - (data['Position'].diff() * data['Close'] * 100).cumsum()

# Get the total value of the portfolio (cash + holdings)
data['Total'] = data['Cash'] + data['Holdings']

# Plotting the portfolio value
plt.figure(figsize=(14, 7))
plt.plot(data['Total'], label='Portfolio value', alpha=0.5)
plt.title(f'{ticker} Moving Average Crossover Trading Strategy - Portfolio Value')
plt.legend()
plt.show()

# Print the final portfolio value
final_portfolio_value = data['Total'].iloc[-1]
print(f"Final Portfolio Value: ${final_portfolio_value:,.2f}")
