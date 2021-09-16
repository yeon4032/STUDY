# -*- coding: utf-8 -*-
"""
step02_csv_LinearRegression.py

csv file(DataFrame)+LinearRegress
"""

import pandas as pd #csv file read
from sklearn.linear_model import LinearRegression #model 생성
from sklearn.metrics import mean_squared_error,r2_score # model 평가
from sklearn.model_selection import train_test_split #dataset split

#1. dataset loading
path='C:/ITWILL/4_python-ll/data/'
iris=pd.read_csv(path+'iris.csv')
iris.info()

#2. 변수 선택*** step 01 과의 차이점 
'''
x =1,2,4
y=3
'''
cols=list(iris.columns)
cols #['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

y_col=cols.pop(2)#Petal.Length # 해당 객체를 꺼내고 객체 에서는 지운다.
cols #['Sepal.Length', 'Sepal.Width', 'Petal.Width', 'Species']

x_cols=cols[:3]
# ['Sepal.Length', 'Sepal.Width', 'Petal.Width']

X=iris[x_cols] #중첩 list
y=iris[y_col] # 단일 list

X.shape #(150, 3)
y.shape #(150,)


#3. train/test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=123) 

#4. model  생성
model = LinearRegression().fit(X_train,y_train)
X_train.head()

model.coef_ #array([ 0.75572271, -0.6715641 ,  1.43222782])
model.intercept_ #-0.3150495624708056


#114           5.8          2.8          2.4
x1, x2, x3=5.8,2.8,2.4
a1,a2,a3=0.75572271, -0.6715641 ,  1.43222782
b=-0.3150495624708056
#회귀반정식
y_fit= x1*a1+x2*a2+x3*a3+b
print('y fit=',y_fit)
#y fit= 5.625109443529194 <- 예측치

#정답
y=y_train[:1]
y#5.1

#5. model 평가: TEST set->validation set: 검증용
y_pred = model.predict(X=X_test)
y_true=y_test

#1)MSE
mse=mean_squared_error(y_true,y_pred)
print(mse) #0.12397491396059157

#2) r2 score
score=r2_score(y_true,y_pred)
print(score) #0.9643540833169766

#과적밯 유무 확인
train_score=model.score(X=X_train,y=y_train)
test_score=model.score(X=X_test, y=y_test)

train_score #0.9694825528782403
test_score  #0.9643540833169766



# 6.model 적용: new dataset(업무용)
import numpy as np
#임의로 new data x 값을 만든다
idx = np.random.choice(a=len(iris),size=int(len(iris)*0.5),
                 replace=False)

new_data=iris.iloc[idx]
new_data.shape # (75, 5)

new_X = new_data[x_cols]
new_y=new_data[y_col]


new_X.shape #(75, 3)
new_y.shape #(75,) <- 정답

#에측치
new_y_pred=model.predict(X= new_X)

#평가
score=r2_score(new_y,new_y_pred)
print(score) #0.9722221044415694











