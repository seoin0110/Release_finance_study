#2.6 모듈과 패키지

#2.6.1 모듈

print(help('modules'))
print(help('modules time'))
print(help('datetime'))

import keyword
print(keyword.kwlist)

print(keyword.__file__)

import calendar
print(calendar.month(2020, 1))
from calendar import month
print(month(2020, 1))

import datetime
print(datetime.datetime.now())
from datetime import datetime as dt
print(dt.now())

#2.6.2 패키지

import urllib.request
print(type(urllib.request))

import urllib
print(type(urllib))
print(urllib.__path__)
print(urllib.__package__)

def functionA():
    print('FUNCTION_A')
print('MODULE_A :', __name__)
def functionB():
    print('FUNCTION_B')
print('MODULE_B :', __name__)

import this
