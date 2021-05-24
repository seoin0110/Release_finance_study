#2.5 변수와 함수

#2.5.1 변수

i = 3
print(type(i))
f = 1.0
print(type(f))

googol = 10 ** 100
print(type(googol))
print(googol)

s = 'string'
print(type(s))
print(dir(s))

print(help('keywords'))

#2.5.2 함수

def getCAGR(first, last, years):
    return (last/first)**(1/years)-1
cagr = getCAGR(65300, 2669000, 20)
print("SEC CAGR : {:.2%}".format(cagr))

def func1():
    pass
def func2():
    return
def func3():
    return None
print(func1())
print(func2())
print(func3())
print(type(None))
print(func1() == None)
print(func1() is None)

def myFunc():
    var1 = 'a'
    var2 = [1, 2, 3]
    var3 = max
    return var1, var2, var3
print(myFunc())
s, l, f = myFunc()
print(s)
print(l)
print(f)

insertComma = lambda x : format(x, ',')
print(insertComma(1234567890))

abs = 1
#print(abs(-100))
