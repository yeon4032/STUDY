# -*- coding: utf-8 -*-
"""
문) california 주택가격을 대상으로 다음과 같은 단계별로 선형회귀분석을 수행하시오.
"""

# california 주택가격 데이터셋 
'''
캘리포니아 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1990년 캘리포니아의 각 행정 구역 내 주택 가격의 중앙값

•특징 변수(8) 
MedInc : 행정 구역 내 소득의 중앙값
HouseAge : 행정 구역 내 주택 연식의 중앙값
AveRooms : 평균 방 갯수
AveBedrms : 평균 침실 갯수
Population : 행정 구역 내 인구 수
AveOccup : 평균 자가 비율
Latitude : 해당 행정 구역의 위도
Longitude : 해당 행정 구역의 경도
'''

from sklearn.datasets import fetch_california_housing # dataset load
import pandas as pd # DataFrame 생성 
from sklearn.linear_model import LinearRegression  # model
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error, r2_score # model 평가 
import matplotlib.pyplot as plt 

# 캘리포니아 주택 가격 dataset load 
california = fetch_california_housing()
print(california.DESCR)

X = california.data
type(X) # numpy.ndarray
y=california.target

# 단계1 : 특징변수(8개)와 타켓변수(MEDV)를 이용하여 DataFrame 생성하기  
#  numpy -> DataFrame 
cal_df = pd.DataFrame(california.data, 
                      columns=california.feature_names)
cal_df["MEDV"] = california.target # y변수 추가 
print(cal_df.tail())
print(cal_df.info()) 

type(cal_df) # pandas.core.frame.DataFrame

# 단계2 : 타켓변수와 가장 상관관계가 높은 특징변수 확인하기  
# 힌트 : DF.corr()


# 단계3 : california 데이터셋을 대상으로 1만개 샘플링하여 서브셋 생성하기  
# 힌트 : 20,640 -> DF.sample(10000) 


# 단계4 : 75%(train) vs 25(test) 비율 데이터셋 split 


# 단계5 : 회귀모델 생성


# 단계6 : 모델 검정(evaluation)  : 과적합(overfitting) 확인  
#과적합(overfitting)



# 단계7 : 모델 평가(test) : new dataset 적용 
import numpy as np
# 조건1) 단계3의 서브셋 대상으로 30% 샘플링 자료 이용

# 조건2) 평가방법 : MSE, r2_score


#MSE


#r2_score


# 단계8 : 예측치 100개 vs 정답 100개 비교 시각화 
#자료형 통일









# 6.model 적용: new dataset(업무용)



















# 단계2 : 타켓변수와 가장 상관관계가 높은 특징변수 확인하기  
# 힌트 : DF.corr()
corr=cal_df.corr() 
corr['MEDV']# MedInc


# 단계3 : california 데이터셋을 대상으로 1만개 샘플링하여 서브셋 생성하기  
# 힌트 : 20,640 -> DF.sample(10000) 
cal_df_sam=cal_df.sample(10000)
cal_df_sam.info()

# 단계4 : 75%(train) vs 25(test) 비율 데이터셋 split 
X=cal_df_sam.iloc[:,:8]
y=cal_df_sam.iloc[:,9]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,)

# 단계5 : 회귀모델 생성
model = LinearRegression().fit(X=X_train,y=y_train)


# 단계6 : 모델 검정(evaluation)  : 과적합(overfitting) 확인  
y_pred=model.predict(X=X_test)

#MSE
mse=mean_squared_error(y_test,y_pred)
print(mse) #0.5557435067226455
#R^2
score=r2_score(y_test,y_pred)
print(score) #0.5961454766075245
#과적합
train_score=model.score(X=X_train,y=y_train)
test_score=model.score(X=X_test, y=y_test)
train_score # 0.6055264923223738
test_score  # 0.5961454766075245



# 단계7 : 모델 평가(test) : new dataset 적용 
import numpy as np
# 조건1) 단계3의 서브셋 대상으로 30% 샘플링 자료 이용
idx = np.random.choice(a=len(cal_df_sam),size=int(len(cal_df_sam)*0.3),
                 replace=False)
cal_sub=cal_df.iloc[idx]
cal_sub.shape # (3000, 9)

new_X = cal_sub.iloc[:,0:8]
new_y = cal_sub.iloc[:,8]

# 조건2) 평가방법 : MSE, r2_score
y_pred=model.predict(X=new_X)

#MSE
mse=mean_squared_error(new_y,y_pred)
print(mse) #0.5685377615772519

#R^2
score=r2_score(new_y,y_pred)
print(score) #0.5941512253282387



# 단계8 : 예측치 100개 vs 정답 100개 비교 시각화 
type(new_y) # pandas.core.series.Series <- 정답
type(y_pred) #numpy.ndarray <-예측치

#자료형 통일
new_y=np.array(new_y)

import matplotlib.pyplot as plt
fig= plt.figure()
chart= fig.add_subplot()
chart.plot(y_pred[:100],marker=r'o', color=u'blue', linestyle='-',label='~~')
chart.plot(new_y[:100],marker=r'+', color=u'red', linestyle='--',label='~~')

chart.set_title('~~')
plt.xlabel('index')
plt.ylabel('prediction')
plt.legend(loc='best')
plt.show()


# 6.model 적용: new dataset(업무용)




















