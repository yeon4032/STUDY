# -*- coding: utf-8 -*-
"""
step03_SVM.py

- 선형 SVM,비선형 SVM
- Hyper parameger:  kernel, C,gamma (사용자 지정)
"""

from sklearn.svm import SVC # SVM model 생성
from sklearn.datasets import load_breast_cancer # dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score

#1. dataset laod
X,y = load_breast_cancer(return_X_y=True)
X.shape
y.shape

#2. tarin/test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=123)


# 3. 비선형 SVM 모델
help(SVC)
'''
SVC(*, C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, 
    probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, 
    max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)
'''
obj=SVC(C=1.0,kernel='rbf',gamma='scale')
'''
defult parameter
 C=1.0: cost(오분류) 조절: 결정경계 조정
 -> C:float, defalult=0.1
 kernel='rbf':  커널트릭 함수
  -> kernel : {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}
 gamma='scale'
 -> {'scale', 'auto'} or float
 -> gamma='scale': 1 / (n_features * X.var())
 -> gamma='auto' : 1 / n_features
 -> gamma=0.1
 n_features:x변수 개수
'''

model = obj.fit(X=X_train,y=y_train)

# model 평가
y_pred = model.predict(X=X_test)
acc= accuracy_score(y_test,y_pred)
print('accuracy=',acc) # accuracy= 0.9005847953216374


# 4. 선형 SVM: 선형 분류 가능한 데이터 (noise 없는 데이터)
obj2=SVC(C=1.0,kernel='linear',gamma='scale')
model2 = obj2.fit(X=X_train , y=y_train)

# model 평가
y_pred = model2.predict(X=X_test)
acc= accuracy_score(y_test,y_pred)
print('accuracy=',acc) # accuracy= 0.9707602339181286



####################################################################3
####### Grid Search (최적의 파라미터 찾기)
####################################################################
'''
Grid Search: 최적의 매개변수(hyper parameters)를 찾는 방법,model 튜닝
'''
#C,gamma 파라미터
params = [0.001, 0.01, 0.1, 1, 10, 100] # 10e-3 ~ 10e+2
best_score=0 # 최고 분류확도 
best_parameters={} # 최적 파라미터

for kernel in ['rbf','linear']: # kernel 파라미터
    for gamma in params: # 감마 파라미터
        for C in params: # cost 파라미터
            obj=SVC(C=C,kernel=kernel,gamma=gamma) # model object
            model=obj.fit(X=X_train,y=y_train) # model
            score=model.score(X=X_test,y=y_test) # 평가 점수
            # 최적의 점수와 파라미터 갱신
            if best_score < score:
                best_score = score # 점수 갱신
                #최적의 파라미터 갱신
                best_parameters={'kernel':kernel,'C':C,'gamma':gamma}
            
print('best_score:',best_score)
#best_score: 0.9766081871345029

print('best_parameters:', best_parameters)
# best_parameters: {'kernel': 'linear', 'C': 10, 'gamma': 0.001}


#best parameters 적용: model 생성
obj=SVC(C=10,kernel='linear',gamma=0.001)
model = obj.fit(X=X_train,y=y_train)

train_score = model.score(X=X_train,y=y_train)
test_score = model.score(X=X_test,y=y_test)
print(train_score) # 0.949748743718593
print(test_score) # 0.9766081871345029


















































