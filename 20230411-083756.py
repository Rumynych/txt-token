import os
from binance.client import Client
import talib
import numpy as np
import pandas as pd

# Placeholder for API key and secret
api_key = "INSERT_YOUR_API_KEY_HERE"
api_secret = "INSERT_YOUR_API_SECRET_HERE"

# Initialize Binance client
client = Client(api_key, api_secret)

# Get historical klines data for a given symbol and interval
symbol = "BTCUSDT"
interval = Client.KLINE_INTERVAL_1HOUR
start_date = "1 Jan, 2022"
end_date = "1 Apr, 2022"

klines = client.get_historical_klines(symbol, interval, start_date, end_date)

# Convert klines data to Pandas DataFrame
columns = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"]
df = pd.DataFrame(klines, columns=columns)
df = df.drop(columns=["Ignore"])

# Convert data types to appropriate format
df["Open time"] = pd.to_datetime(df["Open time"], unit="ms")
df[["Open", "High", "Low", "Close", "Volume", "Quote asset volume", "Taker buy base asset volume", "Taker buy quote asset volume"]] = df[["Open", "High", "Low", "Close", "Volume", "Quote asset volume", "Taker buy base asset volume", "Taker buy quote asset volume"]].apply(pd.to_numeric)

# Calculate Moving Average Convergence Divergence (MACD) indicator
close_prices = df["Close"].to_numpy()
macd, macdsignal, macdhist = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)

# Calculate Relative Strength Index (RSI) indicator
rsi = talib.RSI(close_prices, timeperiod=14)

# Calculate Moving Average (MA) indicator
ma = talib.MA(close_prices, timeperiod=20)

# Print results
print(f"MACD: {macd[-1]:.2f}, MACD Signal: {macdsignal[-1]:.2f}, MACD Hist: {macdhist[-1]:.2f}")
print(f"RSI: {rsi[-1]:.2f}")
print(f"MA: {ma[-1]:.2f}")
