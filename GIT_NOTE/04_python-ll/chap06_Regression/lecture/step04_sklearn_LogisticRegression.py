# -*- coding: utf-8 -*-
"""
step04_sklearn_LogisticRegression.py

-y 변수가 범주형인 경우
"""
from sklearn.datasets import load_breast_cancer,load_iris # dataset
from sklearn.linear_model import LogisticRegression # model
from sklearn.model_selection import train_test_split #dataset split
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가 도구


###############################################################################
### 이항 분류: binary class
###############################################################################

#1. dataset loading
X, y = load_breast_cancer(return_X_y=True)
X.shape # (569, 30)
y.shape # (569,) < -범주형 변수 0 or 1

# 2. train/test split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3)


#3. model
lr=LogisticRegression()
help(LogisticRegression)
'''
random_state=None,: 난수 seed 값 지정
solver='lbgs': 최적화에 상용되는 알고리즘
max_iter=100: 반복학습 횟수
multi_class='auto' :다항분류(multinomial)
'''

model=lr.fit(X=X_train,y=y_train)

#4. model 평가
y_pred=model.predict(X=X_test)
y_true=y_test
con_max=confusion_matrix(y_true, y_pred)
print(con_max) # 행: 관측치 vs 열 : 예측치
'''
[[ 53   9]
 [  4 105]]
'''
len(y_true)

#불류정확도 
#방법1
acc=(con_max[0,0]+con_max[1,1])/len(y_true) # len(y_true)= con_max.sum()
print('acc=',acc)#acc= 0.9239766081871345

acc=accuracy_score(y_true,y_pred)
print('acc=',acc) #acc= 0.9239766081871345

#방법2 
train_score=model.score(X=X_train,y=y_train)#<- train set 분류 정확도
train_score #0.957286432160804

test_score = model.score(X=X_test,y=y_test) #<- test set 분류 정확도
test_score #0.92397660818713450

#####################################################################33
### multi class
######################################################################3
X,y=load_iris(return_X_y=True)
X.shape #(150, 4)
y.shape #0~2: 3개 범주


# 2.model 생성
lr=LogisticRegression(random_state=123,
                   solver='lbfgs',
                   max_iter=200,
                   multi_class='multinomial')
model = lr.fit(X=X,y=y)                  

#3. model 평가
y_pred = model.predict(X = X)

#혼동 행렬
con_mat = confusion_matrix(y, y_pred)
con_mat
'''
array([[50,  0,  0],
       [ 0, 47,  3],
       [ 0,  1, 49]], dtype=int64)
'''

score= accuracy_score(y,y_pred)
print(score) # 0.9733333333333334

import seaborn as sn # heatmap
import matplotlib.pyplot as plt

# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_mat, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map »ö»ó 
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 18)
plt.show()










