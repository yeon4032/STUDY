# -*- coding: utf-8 -*-
"""
step03_pivot_table.py

1.피벗테이블(pivot table) 
  - DF 객체를 대상으로 행과 열 그리고 교차 셀에 표시될 칼럼을 지정하여 만들어진 테이블 
   형식) pivot_table(DF, values='교차셀 칼럼',
                index = '행 칼럼', columns = '열 칼럼'
                ,aggFunc = '교차셀에 적용될 함수')   


2.명목형 변수



"""

import pandas as pd 

#csv file 가져오기
pivot_data=pd.read_csv('C:/ITWILL/4_python-ll/data/pivot_data.csv')
pivot_data.info()
'''
 0   year     8 non-null      int64 :년도
 1   quarter  8 non-null      object:분기
 2   size     8 non-null      object:매출규모
 3   price    8 non-null      int64 :매출액
'''

ptable = pd.pivot_table(data=pivot_data,
               values='price',
               index=['year','quarter'],
               columns='size',aggfunc='sum')



#핏벗테이블
print(ptable)
'''
size          LARGE  SMALL
year quarter              
2016 1Q        2000   1000
     2Q        2500   1200
2017 3Q        2200   1300
     4Q        2800   2300
''' 


#핏벗테이블 시각화
import matplotlib.pyplot as plt  

ptable.plot(kind='barh', stacked=True)
plt.show()


#2.명목형 변수 선택 & 시각화: object or category
import seaborn as sn

titanic = sn.load_dataset('titanic')
titanic.info()

#특정 칼럼의 자료형
titanic['sex'].dtype #dtype('O')
titanic['survived'].dtype #dtype('int64')

#전체 변수 반환
col_names = titanic.columns
col_names
'''
['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone']
'''

#list +for
category_var = [col for col in col_names if titanic[col].dtype=='O']
category_var
#['sex', 'embarked', 'who', 'embark_town', 'alive'] -> 5개의 object형 추출

#시각화
for col in category_var:
    titanic[col].value_counts().plot(kind='bar')
    plt.title(col)
    plt.show()














