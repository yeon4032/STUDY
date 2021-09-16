# -*- coding: utf-8 -*-
"""
step03_continous.py

연속형 변수 시각화: 산점도, 히스토그램, 박스플롯
"""
import numpy as np #별칭 -수치  data 생성
import matplotlib.pyplot as plt #별칭 -data 시각화

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'

# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 1.차트 자료 생성
data1 = np.arange(-3,7) #-3 ~ 6
data2 = np.random.randn(10) # N(0, 1)
print(data1)#이산변수
print(data2)#연속변수
# 2. 산점도
plt.scatter(x=data1, y=data2, c='r',marker='o')
plt.title('scatter plot')
plt.show()

# 여러가지 색 산점도: 집단변수(더미변수)
cdata = np.random.randint(1,4,10) # (1,4] :1~3 난수 정수 10개 생성
print(cdata)#[2 1 3 2 2 1 2 2 1 2]

plt.scatter(x=data1, y=data2, c=cdata,marker='o')
plt.title('scatter plot')
plt.show()

# 3.히스토그램: 대칭성 확인시 사용
data3 = np.random.normal(0,1,2000) # N(mean,sigma^2)=N(0,1) -> (평균,표준편차,난수 수)
print(data3) # 표준정규분포

data4 = np.random.normal(0,1,2000)
print(data4) 

#난수 통계
data3.mean() #0.019061729460503968
data3.std()  #1.0093588154459816

data4.mean() #-0.03231730688914348
data4.std()  #1.012165061470157

# 정규분포 시각화
plt.hist(data3,bins=100,density=True, 
         histtype='step',label='data3')

plt.hist(data4,bins=100,density=True, 
         histtype='step',label='data4')
plt.legend(loc='best') # 범례 
plt.show()
'''
loc속성값
lower left/right
center left/right
upper left/right
'''

#박스 플롯(box plot)
data5=np.random.random(100,) #0~1 사이의 100개 난수 # 패키지.모듈.함수()
print(data5)
print(data5.shape) #(100,) - 1차원

#data 요약통계량
import pandas as pd

#numpy-> pandas # describe 함수 쓰려고 바꾼거임 (numpy 과 pandas 둘다 1차원임)
dataset = pd.Series(data5)
dataset.describe()
'''
count    100.000000
mean       0.564981
std        0.295103
min        0.003417
25%        0.338021
50%        0.608759
75%        0.825487
max        0.992672
dtype: float64
'''

plt.boxplot(dataset)
plt.boxplot(data5)
plt.show()


# 범주형 변수 (집단변수) -> (더미변수)
'''
1. 집단변수를 x변수로 사용
 ex) X[x1=1, x2=0, x3=0] -> Y
2. 집단변수를 Y변수로 사용
 -> 이항 또는 다항분류 모델
 ex)X->Y(y1,y2,y3)
'''
music = pd.DataFrame({'id':[1,2,3,4,5],
                     'genre':['pop','disco','pop','disco','rock']},
                    columns=['id','genre'])   # columns는 순서를 고정 하는 기법
music
'''
   id  genre
0   1    pop
1   2  disco
2   3    pop
3   4  disco
4   5   rock
'''
music.info()
'''

 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   id      4 non-null      int64 
 1   genre   4 non-null      object

'''
#1) dummy 변수 생성
dummy=pd.get_dummies(music['genre']) # 2 진 표현 (0 or 1)
print(dummy)
'''
   disco  pop  rock
0      0    1     0 -> one hot encoding
1      1    0     0
2      0    1     0
3      1    0     0
4      0    0     1
'''

#2) decoding: 10진수 표현
#pandas->numpy
arr=np.array(dummy)

decoding=np.argmax(arr,1)
decoding
#a array([1, 0, 1, 0, 2], dtype=int64)



















































