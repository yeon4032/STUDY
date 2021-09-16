# -*- coding: utf-8 -*-
"""
step04_XGBoost_test.py

>pip install xgboost
"""
from xgboost import XGBClassifier # model
from xgboost import plot_importance # 중요변수(x) 시각화
from sklearn.datasets import make_blobs # dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score,classification_report # 평가

#1. dataset 생성
X, y = make_blobs(n_samples=2000, n_features=4, centers=2,
           cluster_std=2.5, random_state=123)
'''
n_samples=2000:표본 데이터 수 (디폴더=100)
n_features=4 : x변수 개수
centers=3 : y변수 label
cluster_std=2: 클러스터의 표준 편차(노이즈)
random_state=123:
'''

X.shape # (2000, 4)
y.shape # (2000,)
y # array([1, 1, 0, ..., 0, 0, 2])


# 2. split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3)

# 3. model 생성: 다항분류기(centers=3)
'''
xgb = XGBClassifier(objectvie='multi:softprob') # softmax 함수(활성함수)
model = xgb.fit(X_train,y_train, eval_metric='merror')
dir(model)
'''

# 3. model 생성: 이항분류기(centers=2)
xgb = XGBClassifier(objectvie='binary:logistic') # sigmoid 함수
model = xgb.fit(X_train,y_train, eval_metric='error')
'''
활성함수:model 의 예측값-> 출력 y로 활성화
    -sigmoid함수: 0~1 확률로 예측 -> cutoff=0.5
    -softmax함수: 0~1 확률 예측, 전체 확률 합 = 1

softmax함수 확률에 따라 3개로 분배 하기 때문에 multi 인거고 
sigmoid는 2개로 분배 하기 때문에 binary 인거군요?
'''

# 4. model 평가
y_pred=model.predict(X=X_test)
acc=accuracy_score(y_test, y_pred)
print(acc) # 0.9283333333333333

report=classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.90      0.88      0.89       185
           1       1.00      1.00      1.00       209
           2       0.89      0.91      0.90       206

    accuracy                           0.93       600
   macro avg       0.93      0.93      0.93       600
weighted avg       0.93      0.93      0.93       600
'''

# 5. 주요 변수 시각화
fscore = model.get_booster().get_fscore()
print(fscore) 
# {'f2': 953, 'f0': 775, 'f3': 794, 'f1': 875}
#위의 점수를 근거로 차트가 만들어 진다.

plot_importance(model)



















































