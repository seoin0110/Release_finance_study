#2.7 객체지향 프로그래밍

#2.7.1 클래스

class MyFirstClass:
    clsVar = 'The best way to predict the future is to invent it.'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')
mfc = MyFirstClass()
print(mfc.clsVar)
mfc.clsMethod()

#2.7.2 상속

class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")
class B:
    def methodB(self):
        print("Calling B's methodB")
class C(A, B):
    def methodC(self):
        print("Calling C's methodC")
    def method(self):
        print("Calling C's overridden method")
        super().method()
c = C()
c.methodA()
c.methodB()
c.methodC()
c.method()

#2.7.3 클래스 변수와 인스턴스 변수

#2.7.4 클래스 메서드

class NasdaqStock:
    """Class for NASDAQ stocks"""
    count = 0
    def __init__(self, symbol, price):
        """Constructor for NaSdaqStock"""
        self.symbol = symbol
        self.price = price
        NasdaqStock.count += 1
        print('Calling __init__({}, {:.2f}) > count: {}'.format
              (self.symbol, self.price, NasdaqStock.count))
    def __del__(self):
        """Destructor for NasdaqStock"""
        print('Calling __del__({})'.format(self))
gg = NasdaqStock('GOOG', 1154.05)
del(gg)
ms = NasdaqStock('MSFT', 102.44)
del(ms)
amz = NasdaqStock('AMZN', 1746.00)
del(amz)

help(NasdaqStock)
