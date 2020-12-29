#Description: This program ues an artificial recuuent neural network called Long Short Term Memory (LSTM) to predict the closing stock price of a corporation (here Apple) using the past 60 days stock price.

#import the Libraries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


#Get the stock quote
df= web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end='2019-12-17')

#show teh data

print(df)

#Get the number of rows and coloums in the data set
print(df.shape)

#Visualize the closing price history

plt.figure(figsize=(16,8))
plt.title('Close Price history')
plt.plot(df['Close'])
plt.xlable('Date', frontsize=18)
plt.ylable('Close Price USD ($)', frontsize=18)
plt.show()