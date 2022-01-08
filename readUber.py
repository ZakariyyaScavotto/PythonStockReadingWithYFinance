# Based on https://towardsdatascience.com/python-how-to-get-live-market-data-less-than-0-1-second-lag-c85ee280ed93

#Data manipulation
import numpy as np
import pandas as pd
#Data importing
import yfinance as yf
from yfinance import tickers

# plotting done based on https://compucademy.net/getting-stock-data-using-python-and-yfinance/
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def main():
    uberTicker = yf.Ticker('UBER')
    uberData = uberTicker.history('5y')['Close']
    plt.clf()
    sns.lineplot(data=uberData)
    sns.set_theme()
    plt.xticks(rotation=30)
    plt.title(f'Closing Uber Value')
    plt.savefig('uber.png')
    return uberData

if __name__ == '__main__':
    main()