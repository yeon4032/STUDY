# -*- coding: utf-8 -*-
"""
step01_sklearn_LinearRegression.py

"""

from sklearn.datasets import load_diabetes,load_iris #dataset (실습용자료)
from sklearn.linear_model import LinearRegression # model 생성
from sklearn.metrics import mean_squared_error,r2_score # model 평가도구
from sklearn.model_selection import train_test_split # dataset split

#1. dataset loading
dataset = load_diabetes()
X=dataset.data #독립변수(input)
Y=dataset.target # 종속변수(output)
type(X) #numpy.ndarray
type(Y) #numpy.ndarray

X.shape # (442, 10) #2d
Y.shape #(442,) #1d

#2. 변수 특징 분석
X.mean() #-1.6638274468590581e-16  -> 정규화 됨
Y.mean() #152.13348416289594 -> 정규화 (x)

# 3.train/test split (70:30)
idx=int(len(X)*0.7) # 309

X_train=X[:idx] #0~308
X_test = X[idx:]#309~442

Y_train=Y[:idx] #0~308
Y_test = Y[idx:]#309~442

X_train.shape#(309,10) -훈련셋
X_test.shape#(133,10) - 검정셋

#4. model 생성
lr=LinearRegression() # 생성자
model = lr.fit(X=X_train,y=Y_train)

dir(model)# coef_,intercept_,predict,score... etc

print('기울기=', model.coef_)
'''
기울기= [  -3.89994262 -267.20726163  547.2428539   279.6840414  -394.02524002
  115.31952954  -28.18780172  183.22398716  627.70958412  105.8876159 ]
'''
print('절편=',model.intercept_)
#절편= 152.68215576594528

#5. model 평가
y_pred=model.predict(X=X_test) #검정데이터 사용
y_pred # model 에서의 예측치
len(y_pred) #133

y_true=Y_test # 관측치(정답)

# 1) MSE:y정규화 되면 사용  -> 0에 수렴 정도가 기준
mse=mean_squared_error(y_true,y_pred) #2722.170821603729
'''
working
error =y_ture-y_pred
squared=error**2
mse=square.mean()
'''
print('mse=',mse) #mse= 2722.170821603729 <- 이경우 y가 정규화 되어 있지 않았음으로 값이 커진다.

# 2) 계정계수:r^2 -> y정규화(x) -> 1의 수렴정도가 기준
score=r2_score(y_true,y_pred)
print('r2_score=',score) # r2_score= 0.5172474671249085


# 4) score() 메서드 : 과적합 확인
train_score=model.score(X=X_train,y=Y_train)
test_score=model.score(X=X_test,y=Y_test)
print('train_score:',train_score) # train_score: 0.5117388684800468
print('test_score:',test_score) # test_score: 0.5172474671249085

# test_score와 train_score와의 차이가 크지 않다면 오버 피팅(과접합)이 없다.


##############################################################################################################
## iris dataset
###############################################################################################################

#1. dataset loading
X,y=load_iris(return_X_y=True)
X.shape #(150, 4)
y.shape #(150,)


# 2. 변수 특징 분석
X # [5.1, 3.5, 1.4, 0.2]
y # 0 ~ 2 - dummy 변수

#3. train/test split (7:3)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=123)

X_train.shape # (105, 4)
X_test.shape  # (45, 4)
y_train.shape # (105,)
y_test.shape  # (45,)

# 4. model 생성
lr = LinearRegression() # 생성자
model = lr.fit(X=X_train, y=y_train)

model.coef_
# array([-0.12562409, -0.04786676,  0.24405498,  0.5730085 ])
model.intercept_
#0.25025520367096477

# 5. model 평가
y_pred = model.predict(X=X_test) #예측치
y_true=y_test #정답

# 1)MSE:0에 가까울 수록 좋은 model
mse=mean_squared_error(y_true,y_pred)
print('MSE=',mse)
#MSE= 0.04473327237231243
err=y_true-y_pred
squared_err=err**2
mse=squared_err.mean()
mse#MSE= 0.04473327237231243

# 2) r2 score : 1에 가까울수록 좋은 model(좋은 예측력)
score = r2_score(y_true,y_pred)
print('r2 score=',score)
#r2 score= 0.9424492525070314

#3) score():과적합 확인
train_score=model.score(X=X_train,y=y_train)
test_score=model.score(X=X_test,y=y_test)
print(train_score)#0.9219438937692478
print(test_score)#0.9424492525070314

# 6. 시각화 평가
import matplotlib.pyplot as plt

plt.plot(y_pred,color='r',label='predict values')
plt.plot(y_true,color='b',label='real values')
plt.legend(loc='upper left')
plt.show()

