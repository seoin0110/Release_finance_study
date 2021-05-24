#Chapter 3 팬더스를 활용한 데이터 분석

#3.1 넘파이 배열

import numpy as np
A = np.array([[1,2],[3,4]])
print(A)
print(type(A))
print(A.ndim) #배열의 차원
print(A.shape) #배열 크기
print(A.dtype) #원소 자료형

#3.2 팬더스 시리즈

import pandas as pd
s = pd.Series([0.0,3.6,2.0,5.8,4.2,8.0]) #리스트로 시리즈 생성
s.index = pd.Index([0.0,1.2,1.8,3.0,3.6,4.8]) #인덱스 변경
s.index.name = 'MY_IDX' #인덱스명 설정
s[5.9] = 5.5
ser = pd.Series([6.7,4.2],index = [6.8,8.0]) #ser 시리즈를 새엇ㅇ
s = s.append(ser) #기존 s 시리즈에 신규 ser 시리즈를 추가
s.index[-1]
s.values[-1] #복수 개일 때 배열로 반환
s.loc[8.0] #로케이션 인덱서
s.iloc[-1] #인티저 로케이션 인덱서 #복수 개일 때 시리즈로 반환
s.drop(8.0) #s.drop(s.index[-1])과 같다 (데이터 삭제)
print(s)
print(s.describe()) #원소 개수, 평균, 표준편차, 최솟값, 사분위수, 최댓값
import matplotlib.pyplot as plt #s 시리즈 시각화
plt.title("EELLIOTT_WAVE")
plt.plot(s,'bs--') #시리즈를 bs--(푸른 사각형과 점선) 형태로 출력
plt.xticks(s.index) #x축의 눈금값을 s 시리즈의 인덱스값으로 설정
plt.yticks(s.values) #y축의 눈금값을 s 시리즈의 데이터값으로 설정
plt.grid(True)
plt.show()

#3.3 팬더스 데이터프레임

import pandas as pd
df = pd.DataFrame({'KOSPI' : [1915,1961,2026,2467,2041],'KOSDAQ' : [542,682,631,798,675]}, index = [2014,2015,2016,2017,2018])
print(df)
print(df.describe())
df.info() #데이터프레임의 인덱스 정보, 칼럼 정보, 메모리 사용량 등 알려줌
for row in df.itertuples(name='KRX'): #itertuples(): 데이터프레임의 각 행을 이름있는 튜플 형태로 반환
    print(row)
for idx, row in df.iterrows(): #iterrows(): 데이터프레임의 각 행을 인덱스와 시리즈 조합으로 반환
    print(idx,row[0],row[1])

#3.4 주식 비교하기
    #get_data_yahoo(조회할 주식 종목[, start = 조회 기간 시작일][, end = 조회 기간 종료일]
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
sec = pdr.get_data_yahoo('005930.KS',start = '2018-05-04')
msft = pdr.get_data_yahoo('MSFT',start = '2018-05-04')
sec.head(10) #맨 앞 10행
tmp_msft = msft.drop(columns = 'Volume')
tmp_msft.tail() #맨 뒤 5행
    #plot(x, y, 마커 형태 [, label = 'Label'])
import matplotlib.pyplot as plt
plt.plot(sec.index, sec.Close, 'b', label = 'Samsung Electronics')
plt.plot(msft.index,msft.Close,'r--',label = 'Microsoft')
plt.legend(loc = 'best')
plt.show()
sec_dpc = (sec['Close']/sec['Close'].shift(1)-1)*100 #삼성전자 일간 변동률
sec_dpc.iloc[0] = 0
print(sec_dpc.head())
msft_dpc = (msft['Close']/msft['Close'].shift(1)-1)*100 #마이크로소프트 일간 변동률
msft_dpc.iloc[0] = 0
print(msft_dpc.head())
#주가 일간 변동률 히스토그램
plt.hist(sec_dpc,bins = 18)
plt.grid(True)
plt.show()
sec_dpc.describe() #평균과 표준편차
sec_dpc_cs = sec_dpc.cumsum() #일간 변동률의 누적합을 구한다
msft_dpc_cs = msft_dpc.cumsum()
plt.plot(sec.index,sec_dpc_cs, 'b', label = 'Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--',label = 'Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc = 'best')
plt.show()

#3.5 최대 손실 낙폭

#MDD(최대 손실 낙폭) : 특정 기간에 발생한 최고점에서 최저점까지의 가장 큰 손실
#시리즈.rolling(윈도우 크기 [, min_periods = 1])[.집계 함수()]
kospi = pdr.get_data_yahoo('^KS11', '2004-01-04') #KOSPI 지수 데이터 다운로드(^KS11)
window = 252 #산정 기간에 해당하는 window 값은 1년 개장일 252일로 어림잡아 설정
peak = kospi['Adj Close'].rolling(window,min_periods = 1).max() #1년 기간 단위로 최고치 peak를 구한다
drawdown = kospi['Adj Close']/peak - 1.0 #최고치 대비 현재 KOSPI 종가가 얼마나 하락했는지
max_dd = drawdown.rolling(window, min_periods = 1).min() #최저치 max_dd-> 최대 손실 낙폭
plt.figure(figsize=(9,7))
plt.subplot(211) #2행 1열 중 1행에 그린다
kospi['Close'].plot(label='KOSPI',title='KOSPI MDD',grid=True,legend=True)
plt.subplot(212) #2행 1열 중 2행에 그린다
drawdown.plot(c='blue',label='KOSPI DD',grid=True,legend=True)
max_dd.plot(c='red',label='KOSPI MDD',grid=True,legend=True)
plt.show()
print(max_dd[max_dd==max_dd.min()]) #MDD를 기록한 기간

#3.6 회귀 분석과 상관관계

#단순비교
dow = pdr.get_data_yahoo('^DJI','2000-01-04') #다우존스 지수(^DJI)
kospi = pdr.get_data_yahoo('^KS11','2000-01-04')
plt.figure(figsize=(9,5))
plt.plot(dow.index,dow.Close,'r--',label='Dow Jones Industrial') #r-- : 붉은 점선
plt.plot(kospi.index,kospi.Close,'b',label='KOSPI') #b : 푸른 실선
plt.grid(True)
plt.legend(loc='best')
plt.show()
#지수화 비교
d = (dow.Close / dow.Close.loc['2000-01-04'])*100
k = (kospi.Close / kospi.Close.loc['2000-01-04'])*100
plt.figure(figsize=(9,5))
plt.plot(d.index,d,'r--',label='Dow Jones Industrial') #r-- : 붉은 점선
plt.plot(k.index,k,'b',label='KOSPI') #b : 푸른 실선
plt.grid(True)
plt.legend(loc='best')
plt.show()
#산점도 분석
df = pd.DataFrame({'DOW':dow['Close'],'KOSPI':kospi['Close']})#비어있는 데이터는 NaN으로 채워줌
df = df.fillna(method='bfill') #bfill: NaN가 뒤에 있는 값으로 채워짐 
df = df.fillna(method='ffill') #ffill:  앞의 값으로 덮어씀
plt.figure(figsize =(7,7))
plt.scatter(df['DOW'],df['KOSPI'],marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()
from scipy import stats
#model = stats.linregress(독립변수 x,종속변수 y)
regr = stats.linregress(df['DOW'],df['KOSPI']) #선형 회귀식 구하기 #기울기, y절편, r값, p값, 표준편차

# 3.7 상관계수에 따른 리스크 완화

df.corr() #상관계수 구하는 함수
r_value = df['DOW'].corr(df['KOSPI']) #상관계수
r_squared = r_value ** 2 #결정계수
df = pd.DataFrame({'X':dow['Close'],'Y':kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')
regr = stats.linregress(df.X,df.Y)  #다우존스 지수 X와 KOSPI 지수 Y로 선형회귀 모델 객체 regr 생성
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}' #범례에 회귀식 표시하는 레이블
plt.figure(figsize = (7,7))
plt.plot(df.X,df.Y,'.') #산점도 표시
plt.plot(df.X, regr.slope*df.X + regr.intercept,'r') #회귀선 표시
plt.legend(['DOW x KOSPI', regr_line])
plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
plt.xlabel('DOW Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()

# Chapter 4 팬더스를 활용한 데이터 분석

# 4.1 팬더스로 상장법인 목록 읽기

krx_list = pd.read_html('상장법인목록.xls')
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)

# 4.2 HTML 익히기

# 4.3 웹에서 일별 시세 구하기

# 4.4 뷰티풀 수프로 일별 시세 읽어오기

#find_all(['검색할 태그'][, class_='클래스 속성값'][,id='아이디 속성값'][,limit=찾을 개수])
#find(['검색할 태그'][, class_='클래스 속성값'][,id='아이디 속성값'])
#맨 뒤 페이지 숫자 구하기
from bs4 import BeautifulSoup
from urllib.request import urlopen
import mplfinance as mpf
url='https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
with urlopen(url) as doc:
    html = BeautifulSoup(doc,'lxml')
    pgrr = html.find('td',class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

# 4.5 OHLC와 캔들 차트

#전체 페이지 읽어오기
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
for page in range(1,int(last_page)+1):
    page_url = '{}&page={}'.format(sise_url,page)
    df = df.append(pd.read_html(page_url,header=0)[0])
#차트 출력을 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by='날짜')
#날짜, 종카 칼럼으로 차트 그리기
plt.title('Celltrion (close)')
plt.xticks(rotation=45)
plt.plot(df['날짜'], df['종가'],'co-')
plt.grid(color = 'gray',linestyle='--')
plt.show()
#캔들 차트 출력을 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:30]
df = df.rename(columns={'날짜':'Date','시가':'Open','고가':'High','저가':'Low','종가':'Close','거래량':'Volume'})
df = df.sort_values(by='Date') #날짜 오름차순으로 변경
df.index - pd.to_datetime(df.Date)
df = df[['Open','High','Low','Close','Volume']] #데이터프레임 구조 변경
#엠피엘파이낸스로 캔들 차트 그리기
kwargs = dict(title='Celltrion candle chart',type='candle',mav=(2,4,6),volume=True,ylabel='ohlc candles')
mc = mpf.make_marketcolors(up='r',down='b',inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df,**kwargs,style=s)