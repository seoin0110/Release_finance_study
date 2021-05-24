#4.4 뷰티풀 수프로 일별 시세 읽어오기

#4.4.1 파서별 장단점

#4.4.2 find_all() 함수와 find() 함수 비교

#4.4.3 맨 뒤 페이지 숫자 구하기

from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    print(pgrr.a['href'])
print(pgrr.prettify())
print(pgrr.text)
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

#4.4.4 전체 페이지 읽어오기

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
for page in range(1, int(last_page)+1):
    page_url = '{}&page={}'.format(sise_url, page)
    df = df.append(pd.read_html(page_url, header=0)[0])
df = df.dropna()
print(df)
