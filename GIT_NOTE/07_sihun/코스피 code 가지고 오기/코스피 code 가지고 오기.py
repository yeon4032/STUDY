# -*- coding: utf-8 -*-
"""
 코스피 200 종목 코드 가지고 오기
"""

import pandas as pd
import urllib.request as req # 원격 서버 url 자료 요청


# 코스피 200 종목 코드 가지고 오기
url1='https://nextnormalone.tistory.com/76'
table1=pd.read_html(url1,encoding="utf-8")

table = table1[0]
T_code=table.iloc[:,2]


T_code1=list(T_code)

code2=[]
for code in T_code1:
    fixed_code=code.zfill(6)
    code2.append(fixed_code)
   
print(code2)    

code1=pd.DataFrame(code2)
table=table.iloc[:,0:2]
table['code']=code2
table
Final_table=table.iloc[:,1:3]

Final_table.to_excel(excel_writer='C:\\ITWILL\\sihun\\code.xlsx')
