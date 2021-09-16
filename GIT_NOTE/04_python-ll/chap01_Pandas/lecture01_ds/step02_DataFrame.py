# -*- coding: utf-8 -*-
"""
step02_DataFrame.py

DataFrame 자료구조 특징
 -2차원 행렬 구조(DB의 Table 구조와 동일함)
 -칼럼 단위 상이한 자료형
 -Series -> DataFrame
"""
import pandas as pd #별칭 -> pd.DataFrame()
from pandas import DataFrame #DataFrame()

# 1. DataFrame 객체 생성

#1) list,dict 이용
names= ['hong','lee','kim','park']
ages=[35,45,55,25]
pays=[250,350,450,250]

#key-> 칼럼명,value-> 칼럼값
frame = pd.DataFrame({'name':names, 'age':ages, 'pay':pays})
print(frame)
'''
   name  age  pay
0  hong   35  250
1   lee   45  350
2   kim   55  450
3  park   25  250
'''
x=frame['name','age']
type(x)
y=frame['name']
type(y)
#객체 정보
frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3        -> 관측치
Data columns (total 3 columns):      -> 칼럼
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object : 문자형
 1   age     4 non-null      int64  : 정수형
 2   pay     4 non-null      int64  : 정수형
dtypes: int64(2), object(1)
memory usage: 224.0+ bytes
'''

frame.shape #(4, 3) - (행,열) 2차원구조
 
#DF 칼럼 추가:Series 객체 이용
gender = pd.Series(['M','M','F','F'])
frame['gender']=gender#칼럼 추가
print(frame)
'''
   name  age  pay gender
0  hong   35  250      M
1   lee   45  350      M
2   kim   55  450      F
3  park   25  250      F
'''

name = frame['name'] #특정 컬럼 추출
type(name)#pandas.core.series.Series -> 즉 series 객체임 


#2) numpy 객체 이용
import numpy as np

data=np.arange(12) # 0-11
print(data,data.shape) #[ 0  1  2  3  4  5  6  7  8  9 10 11]  (12,)<- 1차원

data=np.arange(12).reshape(3,4)
print(data,data.shape)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]   (3, 4)<-2차원(3행,4열)
'''

# numpy -> pandas
frame2=pd.DataFrame(data,columns=['a','b','c','d'])
frame2
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

# 행/열 통계
frame2.mean(axis=0) # 행축:열단위 (기본-> default -> 행축 값 생략시 1이 적용됨) 
print('열단위 평균:\n',frame2.mean(axis=0))
'''
열단위 평균:
 a    4.0
b    5.0
c    6.0
d    7.0
dtype: float64
'''

frame2.mean(axis=1) #열출:행단위
print('행단위 평균:\n',frame2.mean(axis=1))
'''
행단위 평균:
 0    1.5
1    5.5
2    9.5
dtype: float64
'''


# 2. DF 칼럼 참조
import os 
os.chdir('C:/ITWILL/4_python-ll/data') #경로변경

emp = pd.read_csv("emp.csv",encoding='utf-8')
print(emp.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 248.0+ bytes
None
'''


#1) 단일 칼럼:단일 list
'''
DF.column   - 방법1
DF['column']- 방법2 (점이포함된 컬럼 에 사용 가능 )
'''

no = emp.No #방법1
name=emp['Name'] #방법2
print(no)
print(name)
print(name[1:])

pay= emp.Pay[2:] #방법1
print(pay)
'''
2    500
3    350
4    400
Name: Pay, dtype: int64
'''
emp[:4,]
pay=emp['Pay'] # 방법2
type(pay) #Series

pay.plot() # 선그래프 기본
print('급여 평균:', pay.mean())
#급여 평균: 370.0

#2) 복수 컬럼: 중첩 list
df=emp[['No','Pay']]
#emp[[no:pay]] error 나옴
print(df)

'''
    No  Pay
0  101  150
1  102  450
2  103  500
3  104  350
4  105  400
'''

df.plot() # 2d:선그래프

col=['No','Pay']
print(emp[col])
'''
    No  Pay
0  101  150
1  102  450
2  103  500
3  104  350
4  105  400
'''

#3. subset 만들기:old DF-> new DF 

#1) 특정 칼럼 제외: 특정 칼럼 선택(칼럼 수가 작은 경우)
subset1 = emp[['Name','Pay']]
'''
old DF:emp
new DF: subset1
'''
print(subset1)
'''
  Name  Pay
0  홍길동  150
1  이순신  450
2  강감찬  500
3  유관순  350
4  김유신  400
'''
subset4=emp[[1,2]]


#2) 특정 행 제외
subset2= emp.drop(1)# 2행을 제외한 나머지 
print(subset2)
'''
    No Name  Pay
0  101  홍길동  150
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
두번째 행이 제거됨
'''

# 3) 조건식으로 행 선택
# ex) 급여가 350 이하 관측치 제외
subset3=emp[emp.Pay>350]
print(subset3)
'''
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
4  105  김유신  400
350초과 급여수령자만 프린트 한다.
'''


#4) columns 이용 : 칼럼이 많은 경우
iris = pd.read_csv('iris.csv')
print(iris.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object 
'''

sepal_len=iris['Sepal.Length'] #방버2
sepal_len

#list 생성
col_names=list(iris.columns)
col_names

#list 이용해서 컬럼선택
iris_x = iris[col_names[:4]]
#list[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']]

iris_y=iris[col_names[-1]]
#list[' Species']

iris_x.shape #(150, 4) -> 2차원
iris_y.shape #(150,)   -> 1차원


#4. DataFrame 행열 참조
'''
DF.loc[행,열]: label based: 명칭기반
DF.iloc[행,열]: integer position based : 숫자 위치 기반
'''

print(emp)
'''
column:label
row:integer
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''

#1) loc 속성:명칭 기반
#형식) DF.loc[해label,열label]

emp.loc[0,:] # 1행 전체 선택
emp.loc[0] # 위 와 같음 (열 생략 가능)
emp.loc[0:2] #1행 부터 3행 전체

#숫자->명칭 해석
emp.loc[:,'Name':'Pay'] # 연속 칼럼
emp.loc[:,['No','Pay']] # 비연속 칼럼
#emp.loc[:[0:2]] #error

#2) iloc속성: 숫자 위치 기반
#형식) DF.iloc[행integer,열integer]
emp.iloc[0]#1행 전체
emp.iloc[0:2] 
emp.iloc[:,1:] #2번째 칼럼 이후 연속 칼럼 선택
emp.iloc[:,[0,2]] # 비연속 칼럼
emp.iloc[[0,2,4],[0,2]] # 행열 비연속 선택
'''
    No  Pay
0  101  150
2  103  500
4  105  400
'''
#emp.iloc[:,'Name':'Pay'] #error


