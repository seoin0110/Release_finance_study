#2.3.3 흐름제어

#enumerate()
FAANG = ['FB','AMZN','AAPL','NFLX','GOOGL']
for idx, symbol in enumerate(FAANG,1): #반복자료형,인덱스의 시작값.
    print(idx,symbol)    
#while else와 for else ->break문에 의해 종료되면 실행되지 않음
i = 0
while i >=0:
    i +=1
    if(i%2)==0:
        continue
    if i>5:
        break
    print(i)
else:
    print('Condition is False')
#try except 예외처리
try:
    1/0
except Exception as e:
    print('Exception occured :',str(e))

#2.4.1 리스트
    
myList = 'Thoughts become things.'.split()
print(type(myList))
print(myList)
print(' '.join(myList))
li = [2,5,3,1,4]
li.sort() #리스트를 직접 정렬 None 반환
print(li)
li = [4,3,1,2,5]
li = sorted(li) #다른 반복 자료형에도 사용가능, 정렬한 걸 반환
L=[1,2]
L.append([3,4]) #자료형 상관없이 뒤에 그대로 추가
L.extend([3,4]) #반복자료형 각 원소를 추가
print('-'.join('2012/01/04'.split('/')))
print('2012/01/04'.replace('/','-'))
print(''.join('1,234,567,890'.split(',')))
print(format(1234567890,','))
nums = [1,2,3,4,5]
even_squares =[x**2 for x in nums if x%2 ==0]
print(even_squares)

#2.4.2 변경이 불가능한 튜플

myTuple = ('a','b','c',[10,20,30],abs,max)
print(myTuple[4](-100))
print(myTuple[5](myTuple[3]))

#2.4.3 {키:값} 형태 딕셔너리

crispr = {'EDIT': 'Editas Medecine','NTLA': 'Intellia Therapeutics'} #순서가 없음
print(crispr['NTLA'])
crispr['CRSP'] = 'CRISPR Therapeutics'

#2.4.4 문자열 포맷 출력

for x in crispr: # %기호 방식
    print('%s : %s' % (x,crispr[x]))
for x in crispr: # { } 기호 방식
    print('{} : {}' .format(x,crispr[x]))
for x in crispr: # f-strings 방식
    print(f'{x} : {crispr[x]}')

#2.4.5 중복 없는 셋(set)

s = {'a','p','p','l','e'}
print(s) #순서대로 저장되지 않음
if 'e' in s:
    print("'e' exists in",s)
s = set() #빈 set 생성


#2.4.6 타임잇으로 성능 측정하기

#순회 속도 비교
import timeit
iteration_test = """
for i in itr :
    pass
"""
print(timeit.timeit(iteration_test,setup = 'itr = list(range(10000))', number = 1000)) #timeit(테스트 구문, setup = 테스트 준비 구문, number = 테스트 반복 횟수)
print(timeit.timeit(iteration_test,setup = 'itr = tuple(range(10000))', number = 1000))
print(timeit.timeit(iteration_test,setup = 'itr = set(range(10000))', number = 1000))
#검색 속도 비교
search_test = """
import random
x = random.randint(0,len(itr)-1)
if x in itr:
    pass
"""
print(timeit.timeit(iteration_test,setup = 'itr = list(range(10000))', number = 1000))
print(timeit.timeit(iteration_test,setup = 'itr = tuple(range(10000))', number = 1000))
print(timeit.timeit(iteration_test,setup = 'itr = set(range(10000))', number = 1000))

#2.5.1 변수

s = 'string'
print(dir(s)) #dir() : 현재 셸에서 사용할 수 있는 객체
print(help('keywords')) #예약어

#2.5.2 함수

def getCAGR(first, last, years): #연평균 성장률 구하기
    return (last/first)**(1/years)-1
cagr = getCAGR(65300,2669000,20)
print("SEC CAGR: {:.2%}".format(cagr))
insertComma = lambda x : format(x,',') #람다는 이름없는 간단한 함수 lambda 인수 : 표현식
print(insertComma(1234567890))

#2.6.1 모듈

print(help('modules'))

#2.6.2 패키지

import urllib
print(type(urllib))
print(urllib.__path__)
print(urllib.__package__)
import this #파이썬의 선

#2.7.1 클래스

class MyFirstClass:
    clsVar = 'The best way to predict the future is to invent it.'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')
mfc = MyFirstClass() #인스턴스화
print(mfc.clsVar) #클래스 변수에 접근
print(mfc.clsMethod()) #클래스 메서드 호출

#2.7.2 상속

class A:
    def methodA(self):
        print("A's methodA")
    def method(self):
        print("A's method")
class B:
    def methodB(self):
        print("B's methodB")
class C(A,B):
    def methodC(self):
        print("C's methodC")
    def method(self):
        print("C's overidden method")
        super().method()
c = C()
c.methodA()
c.methodB()
c.methodC()
c.method()

#2.8.1 리퀘스트로 인터넷에서 이미지 파일 가져오기

import requests
url = 'http://bit.ly/2JnsHnT'
r = requests.get(url,stream = True).raw

#2.8.2 필로로 이미지 보여주기

from PIL import Image
img = Image.open(r)
img.show()
img.save('src.png')
print(img.get_format_mimetype)

#2.8.3 'with ~ as 파일 객체:'로 이미지 파일 복사

BUF_SIZE = 1024
with open('src.png','rb') as sf, open('dst.png','wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)

#2.8.4 SHA-256으로 파일 복사 검증하기

import hashlib
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()
with open('src.png','rb') as sf, open('dst.png','wb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())
print("src.png's hash : {}".format(sha_src.hexidigest()))
print("dst.png's hash : {}".format(sha_dst.hexidigest()))

#2.8.5 맷플롯립으로 이미지 가공하기

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
dst_img = mpimg.imread('dst.png')
print(dst_img)
pseudo_img = dst_img[:,:,0] #의사 색상 적용하기
print(pseudo_img)
plt.subtitle('Image Processing',fontsize =18)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))
plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img[:,:,0]
plt.imshow(pseudo_img)
plt.show()
