# Stock-Trading-Strategy-
All of these scripts use moving average strategies to analyze stock price data, generate buy/sell signals, and simulate trading portfolios for different stocks and timeframes. These scripts analyze stock price data using moving averages, generate trading signals, and simulate portfolio performance for different strategies and stocks.

FInal-startegy-code.py

This script implements a moving average crossover trading strategy on McDonald's (MCD) tick data, using 2-minute intervals and both short-term (20 periods) and long-term (50 periods) moving averages. It downloads the required data, calculates buy/sell signals from crossovers, simulates portfolio performance with 100 shares per trade and $100,000 initial capital, and plots both price and portfolio value over time. It finally prints out the ending portfolio value.

Moving-avg-strat-SMA-LMA.py

This code is almost identical to the final strategy code, focusing on high-frequency MCD data. It implements the moving average crossover method with short (20) and long (50) windows, simulates trading based on crossovers, and visualizes both trading signals and the evolving portfolio value, reporting the final value at the end.

Moving-avg-strat-BOTH-SHOWN.py

This script shows two related strategies in one: first, a short-term moving average approach (price versus a 20-period SMA) and then a crossover strategy (20 vs 50-period SMA). For each, it generates buy/sell signals, simulates the portfolio changes, and plots both the price and the simulated portfolio value. It prints the final portfolio value for both strategies.

Moving-avg-strat-BOTH-variance.py

This code compares the volatility (variance) of two strategies on MCD high-frequency data. Strategy 1 is a short-term moving average, while strategy 2 uses a crossover approach. Both simulate trading and portfolio growth, then calculate and print the variance of each portfolio's total value, finally stating which approach was more volatile.

Moving-avg-strat-SMA.py

This implements a short-term moving average strategy on MCD stock: buy when price is above the 20-period SMA, sell otherwise. It downloads data, generates signals, simulates portfolio growth for 100 shares per trade, plots the strategy’s performance, and prints the final portfolio value.

test-1.py

This script provides another version of the moving average crossover strategy for MCD using high-frequency data. It calculates both short and long moving averages, generates buy/sell signals, simulates the portfolio value with 100 shares per trade and $100,000 initial capital, and plots both the trading signals and final portfolio value.

untitled0.py

This file targets Netflix (NFLX) and focuses on the last seven days of 2-minute interval data. It downloads price data, calculates fast (20) and slow (50) SMAs, generates buy/sell signals on crossovers, and prints the most recent trading signals and positions. The data can optionally be saved to CSV for further analysis.

Each script centers on technical analysis using moving averages and simulates trades with realistic portfolio accounting. The main differences are ticker used, moving average windows, whether portfolio variance is analyzed, and which signals trigger trades.
