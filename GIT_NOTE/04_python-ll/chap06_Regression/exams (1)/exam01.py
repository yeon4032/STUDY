'''
문) load_boston() 함수를 이용하여 보스턴 시 주택 가격 예측 회귀모델 생성 
  조건1> train/test - 7:3비울
  조건2> y 변수 : boston.target
  조건3> x 변수 : boston.data
  조건4> 모델 평가 : MSE, r2_score
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

# 1. data load
boston = load_boston()
print(boston)

# 2. 변수 선택  




# 3. train/test split




# 4. 회귀모델 생성 : train set




# 5. 모델 평가 : test set


#MSE



#r2 score



import matplotlib.pyplot as plt












































# 2. 변수 선택  
X=boston.data
y=boston.target

# 3. train/test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=123)

# 4. 회귀모델 생성 : train set
lr=LinearRegression()
model = lr.fit(X=X_train,y=y_train)
model.coef_
model.intercept_

# 5. 모델 평가 : test set
y_pred = model.predict(X=X_test) #예측치
y_true=y_test #정답
#MSE
mse = mean_squared_error(y_true,y_pred)
mse #28.405854810508238

#r2 score
score = r2_score(y_true,y_pred)
print('r2 score=',score)
# r2 score= 0.6485645742370704

import matplotlib.pyplot as plt
fig= plt.figure()
chart= fig.add_subplot(1,1,1)
chart.plot(y_pred[:20],marker=r'o', color=u'blue', linestyle='-',label='~~')
chart.plot(y_true[:20],marker=r'+', color=u'red', linestyle='--',label='~~')

chart.set_title('~~')
plt.xlabel('index')
plt.ylabel('prediction')
plt.legend(loc='best')
plt.show()

