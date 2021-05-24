#3.6 회귀 분석과 상관관계

#3.6.1 KOSPI와 다우존스 지수 비교

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
plt.plot(dow.index, dow.Close, 'r--', label='Dow Jones Industrial')
plt.plot(kospi.index, kospi.Close, 'b', label='KOSPI')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#3.6.2 지수화 비교

d = (dow.Close / dow.Close.loc['2000-01-04']) * 100
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
plt.plot(d.index, d, 'r--', label='Dow Jones Industrial Average')
plt.plot(k.index, k, 'b', label='KOSPI')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#3.6.3 산점도 분석

import pandas as pd
print(len(dow))
print(len(kospi))
#plt.scatter(dow, kospi, marker='.')
df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
print(df)
#plt.scatter(df['DOW'], df['KOSPI'], marker='.')
df = df.fillna(method='bfill')
print(df)

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')
import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()

#3.6.4 사이파이 선형 회귀 분석

#3.6.5 선형 회귀 분석

from scipy import stats
regr = stats.linregress(dfd['DOW'], df['KOSPI'])
print(regr)
