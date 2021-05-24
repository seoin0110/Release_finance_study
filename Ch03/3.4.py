#3.4 주식 비교하기

#3.4.1 야후 파이낸스로 주식 시세 구하기

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
print(sec.head(10))
tmp_msft = msft.drop(columns='Volume')
print(tmp_msft.tail())
print(sec.index)
print(sec.columns)

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
import matplotlib.pyplot as plt
plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft.Close, 'r--', label='Microsoct')
plt.legend(loc='best')
plt.show()

#3.4.2 일간 변동률로 주가 비교하기

print(type(sec['Close']))
print(sec['Close'])
print(sec['Close'].shift(1))
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
print(sec_dpc.head())
sec_dpc.iloc[0] = 0
print(sec_dpc.head())

#3.4.3 주가 일간 변동률 히스토그램

import matplotlib.pyplot as plt
sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
plt.hist(sec_dpc, bins=18)
plt.grid(True)
plt.show()
print(sec_dpc.describe())

#3.4.4 일간 변동률 누적합 구하기

sec_dpc_cs = sec_dpc.cumsum()
print(sec_dpc_cs)

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
sec_dpc_cs = sec_dpc.cumsum()
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()
import matplotlib.pyplot as plt
plt.plot(sec.index, sec_dpc_cs, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()
