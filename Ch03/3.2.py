#3.2 팬더스 시리즈

#3.2.1 시리즈 생성

import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s)

#3.2.2 시리즈의 인덱스 변경

s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
s.index.name = 'MY_IDX'
print(s)
s.name = 'MY.SERIES'
print(s)

#3.2.3 데이터 추가

s[5.9] = 5.5
print(s)
ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
s = s.append(ser)
print(s)

#3.2.4 데이터 인덱싱

print(s.index[-1])
print(s.values[-1])
print(s.loc[8.0])
print(s.iloc[-1])
print(s.values[:])
print(s.iloc[:])

#3.2.5 데이터 삭제

print(s.drop(8.0))

#3.2.6 시리즈 정보 보기

print(s.describe())

#3.2.7 시리즈 출력하기

import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2])
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0])
s.index.name = 'MY_IDX'
s.name = 'MY_SERIES'
import matplotlib.pyplot as plt
plt.title("ELLIOTT_WAVE")
plt.plot(s, 'bs--')
plt.xticks(s.index)
plt.yticks(s.values)
plt.grid(True)
plt.show()
