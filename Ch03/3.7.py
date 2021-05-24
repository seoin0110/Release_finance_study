#3.7 상관계수에 따른 리스크 완화

#3.7.1 데이터프레임으로 상관계수 구하기

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
dow=pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')
df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
print(df.corr())

#3.7.2 시리즈로 상관계수 구하기

print(df['DOW'].corr(df['KOSPI']))

#3.7.3 결정계수 구하기

r_value = df['DOW'].corr(df['KOSPI'])
print(r_value)
r_squared = r_value ** 2
print(r_squared)

#3.7.4 다우존스 지수와 KOSPI의 회귀 분석

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
from scipy import stats
import matplotlib.pylab as plt
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')
df = pd.DataFrame({'X': dow['Close'], 'Y': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')
regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}'
plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['DOW x KOSPI', regr_line])
plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()

#3.7.5 상관계수에 따른 리스크 완화

import pandas as pd
s1 = pd.Series([+10, -20, +30, -40, +50])
s2 = pd.Series([ +1,  -2,  +3,  -4,  +5])
s3 = pd.Series([-10, +20, -30, +40, -50])
df = pd.DataFrame({'S1': s1, 'S2': s2, 'S3': s3})
print(df)
print(df.corr())
