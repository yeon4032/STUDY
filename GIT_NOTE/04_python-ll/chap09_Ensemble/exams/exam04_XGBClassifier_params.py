# -*- coding: utf-8 -*-
"""
문) wine dataset을 이용하여 다음과 같이 다항분류 모델을 생성하시오. 
 <조건1> tree model 200개 학습
 <조건2> tree model 학습과정에서 조기 종료 100회 지정
 <조건3> model의 분류정확도와 리포트 출력   
"""
from xgboost import XGBClassifier # model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine # 다항분류
from sklearn.metrics import accuracy_score, classification_report


#################################
## 1. XGBoost Hyper Parameter
#################################

# 1. dataset load
wine=load_wine()

#X변수
x_names=wine.feature_names
print(x_names,len(x_names)) #30

# y변수
y_label=wine.target_names
y_label # ['malignant', 'benign'] : 이항

X, y = load_wine(return_X_y=True)
# 2. train/test 생성 
X_train, X_test,y_train,y_test=train_test_split(X, y, test_size=0.3)

# 3. model 생성 : 다항분류 
xgb = XGBClassifier(objectvie='multi:softprob',n_estimators=200)
 

# 4. model 학습 조기종료 
eval_set=[(X_test,y_test)] # 평가셋

model = xgb.fit(X_train,y_train, 
                eval_set=eval_set,
                eval_metric='merror',
                early_stopping_rounds=100)





# 5. model 평가 
y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print(acc) 
#0.9814814814814815

report=classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      0.95      0.97        19
           1       0.95      1.00      0.97        18
           2       1.00      1.00      1.00        17

    accuracy                           0.98        54
   macro avg       0.98      0.98      0.98        54
weighted avg       0.98      0.98      0.98        54
'''
