import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Companies/Industry names
apple= yf.download("AAPL", start="2023-01-01", end="2025-01-01")
microsoft= yf.download("MSFT", start="2023-01-01", end="2025-01-01")
nvidia= yf.download("NVDA", start="2023-01-01", end="2025-01-01")
amazon= yf.download("AMZN", start="2023-01-01", end="2025-01-01")
google= yf.download("GOOG", start="2023-01-01", end="2025-01-01")
meta= yf.download("META", start="2023-01-01", end="2025-01-01")
aramco= yf.download("2222.SR", start="2023-01-01", end="2025-01-01")
broadcom= yf.download("AVGO", start="2023-01-01", end="2025-01-01")
taiwam_semiconductor=yf.download("TSM", start="2023-01-01", end="2025-01-01")
berkshire_hathaway=yf.download("BRK.A", start="2023-01-01", end="2025-01-01")
tesla= yf.download("TSLA", start="2023-01-01", end="2025-01-01")
lilly = yf.download("LLY", start="2023-01-01", end="2025-01-01")
jpmorgan = yf.download("JPM", start="2023-01-01", end="2025-01-01")
wallmart = yf.download("WMT", start="2023-01-01", end="2025-01-01")
visa = yf.download("V", start="2023-01-01", end="2025-01-01")

nvidia.head()
taiwam_semiconductor.head()
broadcom.head()
berkshire_hathaway.head()
microsoft.head()
google.head()
amazon.head()
tesla.head()
meta.head()
lilly.head()
jpmorgan.head()
wallmart.head()
visa.head()
apple.head()
aramco.head()

# Daily Returns
# At Opening price
nvidia['Daily Return'] = nvidia['Open'].pct_change()
aramco['Daily Return'] = aramco['Open'].pct_change()
apple['Daily Return'] = apple['Open'].pct_change()
taiwam_semiconductor['Daily Return'] = taiwam_semiconductor['Open'].pct_change()
berkshire_hathaway['Daily Return'] = berkshire_hathaway['Open'].pct_change()
broadcom['Daily Return'] = broadcom['Open'].pct_change()
microsoft['Daily Return'] = microsoft['Open'].pct_change()
google['Daily Return'] = google['Open'].pct_change()
amazon['Daily Return'] = amazon['Open'].pct_change()
tesla['Daily Return'] = tesla['Open'].pct_change()
meta['Daily Return'] = meta['Open'].pct_change()
lilly['Daily Return'] = lilly['Open'].pct_change()
jpmorgan['Daily Return'] = jpmorgan['Open'].pct_change()
wallmart['Daily Return'] = wallmart['Open'].pct_change()
visa['Daily Return'] = visa['Open'].pct_change()

# At Closing Price
nvidia['Daily Return'] = nvidia['Close'].pct_change()
aramco['Daily Return'] = aramco['Close'].pct_change()
apple['Daily Return'] = apple['Close'].pct_change()
taiwam_semiconductor['Daily Return'] = taiwam_semiconductor['Close'].pct_change()
berkshire_hathaway['Daily Return'] = berkshire_hathaway['Close'].pct_change()
broadcom['Daily Return'] = broadcom['Close'].pct_change()
microsoft['Daily Return'] = microsoft['Close'].pct_change()
google['Daily Return'] = google['Close'].pct_change()
amazon['Daily Return'] = amazon['Close'].pct_change()
tesla['Daily Return'] = tesla['Close'].pct_change()
meta['Daily Return'] = meta['Close'].pct_change()
lilly['Daily Return'] = lilly['Close'].pct_change()
jpmorgan['Daily Return'] = jpmorgan['Close'].pct_change()
wallmart['Daily Return'] = wallmart['Close'].pct_change()
visa['Daily Return'] = visa['Close'].pct_change()


# Moving Averages
# At Opening
nvidia['MA50'] = nvidia['Open'].rolling(50).mean()
apple['MA50'] = apple['Open'].rolling(50).mean()
taiwam_semiconductor['MA50'] = taiwam_semiconductor['Open'].rolling(50).mean()
berkshire_hathaway['MA50'] = berkshire_hathaway['Open'].rolling(50).mean()
broadcom['MA50'] = broadcom['Open'].rolling(50).mean()
microsoft['MA50'] = microsoft['Open'].rolling(50).mean()
google['MA50'] = google['Open'].rolling(50).mean()
amazon['MA50'] = amazon['Open'].rolling(50).mean()
tesla['MA50'] = tesla['Open'].rolling(50).mean()
meta['MA50'] = meta['Open'].rolling(50).mean()
lilly['MA50'] = lilly['Open'].rolling(50).mean()
jpmorgan['MA50'] = jpmorgan['Open'].rolling(50).mean()
wallmart['MA50'] = wallmart['Open'].rolling(50).mean()
visa['MA50'] = visa['Open'].rolling(50).mean()


# At Closing
nvidia['MA50'] = nvidia['Close'].rolling(50).mean()
apple['MA50'] = apple['Close'].rolling(50).mean()
taiwam_semiconductor['MA50'] = taiwam_semiconductor['Close'].rolling(50).mean()
berkshire_hathaway['MA50'] = berkshire_hathaway['Close'].rolling(50).mean()
broadcom['MA50'] = broadcom['Close'].rolling(50).mean()
microsoft['MA50'] = microsoft['Close'].rolling(50).mean()
google['MA50'] = google['Close'].rolling(50).mean()
amazon['MA50'] = amazon['Close'].rolling(50).mean()
tesla['MA50'] = tesla['Close'].rolling(50).mean()
meta['MA50'] = meta['Close'].rolling(50).mean()
lilly['MA50'] = lilly['Close'].rolling(50).mean()
jpmorgan['MA50'] = jpmorgan['Close'].rolling(50).mean()
wallmart['MA50'] = wallmart['Close'].rolling(50).mean()
visa['MA50'] = visa['Close'].rolling(50).mean()

# Graph pllotting

# at Opening
plt.figure(figsize=(10,6))
plt.plot(nvidia['Open'], label="NVIDIA")
plt.plot(apple['Open'], label="Apple")
plt.plot(taiwam_semiconductor['Open'], label="TWS")
plt.plot(berkshire_hathaway['Open'], label="BRK")
plt.plot(broadcom['Open'], label="Broadcom")
plt.plot(microsoft['Open'], label="Microsoft")
plt.plot(google['Open'], label="Google")
plt.plot(amazon['Open'], label="Amazon")
plt.plot(tesla['Open'], label="Tesla")
plt.plot(meta['Open'], label="Meta")
plt.plot(lilly['Open'], label="Reliance")
plt.plot(jpmorgan['Open'], label="TCS")
plt.plot(wallmart['Open'], label="INFY")
plt.plot(visa['Open'], label="HDFC")
plt.legend()
plt.title("Stock Prices (Company/Industry)")

# At Closing
plt.figure(figsize=(10,6))
plt.plot(nvidia['Close'], label="NVIDIA")
plt.plot(apple['Close'], label="Apple")
plt.plot(taiwam_semiconductor['Close'], label="TWS")
plt.plot(berkshire_hathaway['Close'], label="BRK")
plt.plot(broadcom['Close'], label="Broadcom")
plt.plot(microsoft['close'], label="Microsoft")
plt.plot(google['Close'], label="Google")
plt.plot(amazon['Close'], label="Amazon")
plt.plot(tesla['Close'], label="Tesla")
plt.plot(meta['Close'], label="Meta")
plt.plot(lilly['Close'], label="Reliance")
plt.plot(jpmorgan['Close'], label="TCS")
plt.plot(wallmart['Close'], label="INFY")
plt.plot(visa['Close'], label="HDFC")
plt.legend()
plt.title("Stock Prices (Company/Industry)")



plt.figure(figsize=(10,6))
plt.plot(apple['Close'], label="Reliance Price")
plt.plot(apple['MA50'], label="Reliance 50-Day MA")
plt.legend()
plt.title("Reliance Stock with 50-Day Moving Average")


apple['Daily Return'].hist(bins=50, figsize=(8,5))
plt.title("Reliance Daily Returns Distribution")





