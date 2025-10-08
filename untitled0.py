import yfinance as yf
import pandas as pd

# Define the ticker symbol for Netflix
ticker = 'NFLX'

# Define the end date as today and the start date as 7 days before today
end_date = pd.Timestamp.now()
start_date = end_date - pd.DateOffset(days=60)

# Download the "2m" interval stock price data for the last 7 days
data = yf.download(ticker, start=start_date, end=end_date, interval='2m')

# Save the data to a CSV file (optional)
data.to_csv('NFLX_recent_2m_data.csv')

# Assuming you want to use Simple Moving Averages (SMA) for your strategy
# Calculate SMAs with two different windows (fast and slow)
data['SMA_fast'] = data['Close'].rolling(window=20).mean()  # e.g., 20 periods for fast SMA
data['SMA_slow'] = data['Close'].rolling(window=50).mean()  # e.g., 50 periods for slow SMA

# Generate buy/sell signals based on SMA crossovers
data['Signal'] = 0  # Default no position
data['Signal'][data['SMA_fast'] > data['SMA_slow']] = 1  # Buy signal
data['Signal'][data['SMA_fast'] < data['SMA_slow']] = -1  # Sell signal

# Assuming we will enter trades on the next '2m' interval after the crossover
data['Position'] = data['Signal'].shift(1)

# Print the tail of the dataframe to check recent signals and positions
print(data.tail())

