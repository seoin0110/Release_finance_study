#2.3 문자열과 산술연산

print('Hello, world!')

#2.3.1 문자열

type('Hello, world!')
type("Hello, world!")

print('C:\Windows\System32\notepad.exe')
print(r'C:\Windows\System32\notepad.exe')
print('\"It\'s not that I\'m so smart; it\'s just that I stay with problems longer.\" Albert Einstein')
print('''"It's not that I'm so smart; it's just that I stay with problems longer." Albert Einstein''')
print('''Wake up, Neo...
The Matrix has you...
Follow the white rabbit.''')

word = 'Python'
print(len(word))
print(word[0] + word[1] + word[2] + word[3] + word[4] + word[5])
print(word[-6] + word[-5] + word[-4] + word[-3] + word[-2] + word[-1])

word = 'Python'
print(word[0:6])
print(word[0:])
print(word[:6])
print(word[:-1])

#2.3.2 산술 연산

print(1 + 2)
print(3 - 4)
print(5 * 6)
print(2 ** 8)
print(5 / 3)
print(5 // 3)
print(5 % 3)
x = 2
x += 1
print(x)

#2.3.3 흐름 제어

rsi = 88
if rsi > 70:
    print('RSI', rsi, 'means overbought.')
elif rsi < 30:
    print('RSI', rsi, 'means oversold')
else:
    print('...')

for i in [1, 3, 5]:
    print(i)
for i in range(1, 7, 2):
    print(i)
FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']
for idx, symbol in enumerate(FAANG, 1):
    print(idx, symbol)

i = 1
while i < 7:
    print(i)
    i += 2

i = 0
while i >= 0:
    i += 1
    if (i % 2) == 0:
        continue
    if i > 5:
        break
    print(i)
else:
    print('Contition is False.')

try:
    1/0
except Exception as e:
    print('Exception occured :', str(e))
