#4.1 팬더스로 상장법인 목록 읽기

#4.1.1 엑셀 파일 내용 확인하기

#4.1.2 read_html() 함수로 파일 읽기

import pandas as pd
krx_list = pd.read_html('D:/2021 봄학기/Release/finance_study/Ch04/상장법인목록.xls')
print(krx_list[0])
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:6d}'.format)
print(krx_list[0])
