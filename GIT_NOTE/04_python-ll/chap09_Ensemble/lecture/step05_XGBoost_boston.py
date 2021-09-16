# -*- coding: utf-8 -*-
"""
step05_XGBoost_boston.py

 - XGBoost 회귀트리 예 
"""

from xgboost import XGBRegressor #회귀트리 모델
from xgboost import plot_importance # 중요변수 시각화

from sklearn.datasets import load_boston #dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error,r2_score # 평가


# 1. dataset load
boston = load_boston()

x_names= boston.feature_names
x_names
#array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
#       'TAX', 'PTRATIO', 'B', 'LSTAT'], dtype='<U7')

X = boston.data
y = boston.target
X.shape #(506, 13)
y # 연속형 (비율척도)

# 2. train/test split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3)


# 3. model 생성
xgb = XGBRegressor()
model = xgb.fit(X=X_train,y=y_train)
print(model)

# 4. 중요변수 확인
fscore = model.get_booster().get_fscore()
print(fscore)
#{'f5': 376, 'f12': 339, 'f7': 282, 'f0': 710, 'f2': 88, 'f4': 157, 'f11': 254, 
# 'f10': 90, 'f6': 332, 'f8': 47, 'f9': 70, 'f3': 19, 'f1': 50}


# 5. 중요변수 시각화 : x변수명 없음
plot_importance(model,max_num_features=5)
#max_num_features=5 :상위 5 개 변수만 본다.

#############################################################################
### 중요변수 시각화에 x변수명 표시
#############################################################################
import pandas as pd

X = boston.data
y = boston.target

df = pd.DataFrame(X,columns=x_names)
df.shape #(506, 13)
df['traget']=y # y변수 추가

df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   CRIM     506 non-null    float64
 1   ZN       506 non-null    float64
'''

# 2. train/test split
X_train,X_test,y_train,y_test = train_test_split(df.iloc[:,0:-1], df.iloc[:,-1], test_size=0.3)

# 3. model 생성
xgb = XGBRegressor()
model = xgb.fit(X=X_train,y=y_train)

# 4. 중요변수 확인
fscore = model.get_booster().get_fscore()
print(fscore)
#{'LSTAT': 315, 'RM': 407, 'CRIM': 773, 'DIS': 275, 'AGE': 310, 'INDUS': 96, '
# B': 226, 'NOX': 168, 'PTRATIO': 64, 'TAX': 96, 'RAD': 47, 'ZN': 56, 'CHAS': 20}

# 5. 중요변수 시각화 : x변수명 없음
plot_importance(model,max_num_features=5)
# max_num_features=5 :상위 5 개 변수만 본다.

# model 평가
y_pred = model.predict(X=X_test) # 예측치
y_true = y_test # 관측치

mse=mean_squared_error(y_true, y_pred)
print('MSE=',mse) # MSE= 8.055027696474223

score = r2_score(y_true,y_pred)
print('r2 score=',score) # r2 score= 0.8972494852411734

# 6. model save & load
import pickle # binary file 

# model file save 
pickle.dump(model, open('xgb_model.pkl', mode ='wb')) # wb=write binary

# model file load
load_model = pickle.load(open('xgb_model.pkl', mode ='rb'))

y_pred=load_model.predict(X=X_test) # new test set < - model 형식이 여서 예측치 밋 기각화 평가가능 
y_pred[:10]
y_true[:10]


























