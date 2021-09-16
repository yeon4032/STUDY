# -*- coding: utf-8 -*-
"""
step06_random.py

np.random 모듈 - 난수 생성 함수 제공
- 용도: 모집단 -> 표본 추출(sampling)
"""

import numpy as np

#1. 난수 실수와 정수

#1) 난수 실수: [0,1) -> 0 <= r <1
data = np.random.rand(5,3)
print(data)
'''
[[0.49274944 0.91876273 0.89955642]
 [0.8596312  0.41692496 0.70604838]
 [0.29000829 0.98087898 0.59946931]
 [0.25837788 0.38653016 0.83162302]
 [0.28612879 0.13954686 0.49938156]]
'''

data.shape #(5,3)
#난수 통계 
data.min()
data.max()
data.mean()

#2)난수 정수:[1,b) -> a<= r < b
data=np.random.randint(165,175,size=50)
print(data)
data.shape #(50,)

#난수 통계
data.min()#165
data.max()#174
data.mean()#169.58

#2. 정규분포와 표준정규분포

#1)정규분포: N(평균, 표준편차^2,size)
height=np.random.normal(173,5,2000) #N(173,5^2) 2000개 난수 생성
height #1d
'''
array([169.92295876, 175.30928705, 176.51482267, ..., 180.59027205,
       175.4049776 , 167.75405861])
'''

height2 = np.random.normal(173,5,(500,4)) #N(173,5^2) 2000개 난수를 2차원으로 생성
height2 #2d
'''
array([[178.76477214, 174.19937501, 170.05008957, 180.35645778],
       [179.34913229, 168.96406681, 174.35773284, 176.99159585],
       [172.02194463, 170.30334126, 175.76618888, 167.05523168],
       ...,
       [167.0904213 , 172.91972068, 176.75761896, 172.94264437],
       [173.28131976, 176.73752743, 169.81155617, 174.44511009],
       [165.98966828, 176.70809619, 162.67889861, 166.82924262]])
'''

#난수 통계
height.mean() # 172.97458308526805
height.std() # 5.196576213704453

height2.mean() # 173.03105760682655
height2.std() # 5.051289864451016

# 정규분포 시각화
import matplotlib.pyplot as plt

plt.hist(x=height, bins=100, density=True)
plt.show()

plt.hist(x=height, bins=100, density=True, histtype='step')
plt.show()


#2) 표준정규분포: N(0,1)
st_nor = np.random.randn(500,3)
st_nor


# 난수 통계
st_nor.mean() #0.015403991285264615
st_nor.std() #0.9930363931580656

#or
st_nor2 = np.random.normal(0,1,(500,3))
st_nor2

st_nor2.mean() # -0.01450908031725158
st_nor2.std() #1.001158671441443

#표준정규분포 시각화
plt.hist(x=st_nor[:,0], bins=100, density=True, histtype='step',label='col1')
plt.hist(x=st_nor[:,1], bins=100, density=True, histtype='step',label='col2')
plt.hist(x=st_nor[:,2], bins=100, density=True, histtype='step',label='col3')
plt.legend(loc='best')
plt.show()

#st_nor 가 500행 3열 이기 때문데 3가지 그래프가 나온다.

#3. Dataset sampling
import pandas as pd 
import os 

os.chdir('C:/ITWILL/4_python-ll/data')
wdbc=pd.read_csv('wdbc_data.csv')
wdbc.info()
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

#1) seed값 적용
np.random.seed (123)

#2) DF.sample()
wdbc_test=wdbc.sample(400)
wdbc_test.shape #(400, 32)

wdbc_test.head()
wdbc_test.tail()

#3) trainset vs test set sample

#train index
help(np.random.choice)
#choice(a, size=None, replace=True, p=None)

idx = np.random.choice(a=len(wdbc),size=int(len(wdbc)*0.7),replace=False)

'''
a:전체 관측치
size:샘플 크기
replace: 복원(True) or 비복원(False)
'''
len(idx) # 398
idx

#train set: 398
train_set=wdbc.iloc[idx,:]
train_set.shape #(398, 32)


#test set:30%(171)
test_idx=[ i for i in range(len(wdbc)) if not i in idx]
len(test_idx)#171

test_set=wdbc.iloc[test_idx,:]
test_set.shape#(171, 32)

test_set.head()
test_set.tail()
