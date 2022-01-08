# Based on https://towardsdatascience.com/python-how-to-get-live-market-data-less-than-0-1-second-lag-c85ee280ed93

#Data manipulation
import numpy as np
import pandas as pd
#Data importing
import yfinance as yf
from yfinance import tickers


#Ex: UBER
uberdata = yf.download(tickers='UBER', period='5d', interval='5m')
print(uberdata)

appledata = yf.download(tickers='AAPL', period='5d', interval='5m')
print(appledata)