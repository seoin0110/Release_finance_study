#2.4 반복 자료형

#2.4.1 리스트

ls = ['one', 'two', 'three', 4, 5, 6]
print(ls[0])
print(ls[-1])
L = [[1, 2], [3, 4]]
print(L[0])
print(L[1])
print(L[0][0])
print(L[0][1])
print(L[1][0])
print(L[1][1])
print(L + L)
print(L * 3)

myList = 'Thoughts become things.'.split()
print(type(myList))
print(myList)

print(myList)
print(' '.join(myList))

li = [2, 5, 3, 1, 4]
li.sort()
print(li)
li = [4, 3, 1, 2, 5]
print(sorted(li))
print(li)

L = [1, 2]
L.append([3, 4])
print(L)
L = [1, 2]
L.extend([3, 4])
print(L)

print('-'.join('2012/01/04'.split('/')))
print('2012/01/04'.replace('/', '-'))

print(''.join('1,234,567,890'.split(',')))
print('1,234,567,890'.replace(',', ''))
print(format(1234567890, ','))

myList = ['Thoughts', 'become', 'things.']
newList = myList[:]
print(newList)

newList[-1] = 'actions.'
print(newList)
print(myList)

nums = [1, 2, 3, 4, 5]
squares = []
for x in nums:
    squares.append(x**2)
print(squares)
nums = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in nums]
print(squares)
nums = [1, 2, 3, 4, 5]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

#2.4.2 변경이 불가능한 튜플

myTuple = ('a', 'b', 'c', [10, 20, 30], abs, max)
print(myTuple[3])
print(myTuple[4](-100))
print(myTuple[5](myTuple[3]))
#myTuple[0] = 'A'

#2.4.3 {키:값} 형태 딕셔너리

crispr = {'EDIT': 'Editas Medicine', 'NTLA': 'Intellia Therapeutics'}
#print(crispr[1])
print(crispr['NTLA'])
crispr['CRSP'] = 'CRISPR Therapeutics'
print(crispr)
print(len(crispr))

#2.4.4 문자열 포맷 출력

for x in crispr:
    print('%s : %s' % (x, crispr[x]))

for x in crispr:
    print('{} : {}'.format(x, crispr[x]))

for x in crispr:
    print(f'{x} : {crispr[x]}')

#2.4.5 중복 없는 셋

s = {'A', 'P', 'P', 'L', 'E'}
print(s)
mySet = {'B', 6, 1, 2}
print(mySet)
if 'B' in mySet:
    print("'B' exists in", mySet)
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}
print(setA & setB)
print(setA | setB)
print(setA - setB)
print(setB - setA)
ls = []
d = {}
t = ()
s = set()
ls = [1, 3, 5, 2, 2, 3, 4, 2, 1, 1, 1, 5]
print(list(set(ls)))

#2.4.6 타임잇으로 성능 측정하기
import timeit
iteration_test = """
for i in itr :
    pass
"""
print(timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000))
print(timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=1000))
print(timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=1000))

search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr :
    pass
"""
print(timeit.timeit(search_test, setup='itr = set(range(10000))', number=1000))
print(timeit.timeit(search_test, setup='itr = list(range(10000))', number=1000))
print(timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=1000))
