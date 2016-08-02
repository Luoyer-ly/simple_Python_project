# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:04:18 2016

@author: Administrator
"""

from matplotlib.finance import quotes_historical_yahoo_ohlc
from datetime import date
import pandas as pd

today=date.today();
start=(today.year-1,today.month,today.day)
quotes=quotes_historical_yahoo_ohlc('AAPL',start,today)
df=pd.DataFrame(quotes)
print df