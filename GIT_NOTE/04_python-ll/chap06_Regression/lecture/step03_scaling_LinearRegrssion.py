# -*- coding: utf-8 -*-
"""
step03_scaling_LinearRegrssion.py

data scaling: 정규화 or 표준화
- 특징변수(x변수)의 값에 따라서 model에 영향을 미치는 경우
    ex) 범죄율(0~100), 하위계층비율(0 ~ 0.9)
- 정규화: 0~1 or -1~1: x변수
- 표준화: mu=0, std = 1 :y 변수
- data scaling: x변수 대상
"""

from sklearn.datasets import load_boston #dataset
from sklearn.model_selection import train_test_split #dataset split
from sklearn.linear_model import LinearRegression #model
from sklearn.metrics import mean_squared_error,r2_score # model 평가

#data scaling
from sklearn.preprocessing import minmax_scale #정규화(0~1)
from scipy.stats import zscore # 표준화(mu=1,std=1)

#1. dataset loading
X,y=load_boston(return_X_y=True)

X.shape #(506, 13)
y.shape #(506, )

#scaling 필요 유무 확인
X.mean() #70.07396704469443 <- 정규화 안됨  (0 근처이면 정규화 된걸로 본다.)
X.mean(axis=0) # 각 컬럼 평균
'''
array([3.61352356e+00, 1.13636364e+01, 1.11367787e+01, 6.91699605e-02,
       5.54695059e-01, 6.28463439e+00, 6.85749012e+01, 3.79504269e+00,
       9.54940711e+00, 4.08237154e+02, 1.84555336e+01, 3.56674032e+02,
       1.26530632e+01]) <-각각의 변수 별 차이가 있다.
'''
y.mean() #22.532806324110677
y

# 2. X,y 변수 scaling 
#x는 정규화 꼭해야됨
X_nor = minmax_scale(X) # 정규화
X_nor.mean() # 0.3862566314283195
X_nor.min() # 0.0
X_nor.max() # 1.0

#y는 필수느 아니다 그러나 MSE쓰려면 할필요있음
y_nor=zscore(y) # 표준화 (평균=0, 표준편차=1)
'''
z=(x-mu)/sigma
'''
y_nor.mean() # -5.195668225913776e-16
y_nor.std()  # 0.9999999999999999


#3. train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_nor,y_nor,test_size=0.25) # 기본값=025 so 생략가능


#4.model 생성
model = LinearRegression().fit(X=X_train,y=y_train)

#5. model 평가
y_pred=model.predict(X=X_test)

mse=mean_squared_error(y_test,y_pred)
print(mse) #0.3088535359131019

score=r2_score(y_test,y_pred)
print(score) #0.7035051751302852






