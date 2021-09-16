# -*- coding: utf-8 -*-
"""
step06_XGBoost_parameter.py

1.XGBoost Hyper parameters: ppt.19
2.model 학습 조기 종료
3. Best Hyper parameters
"""
from xgboost import XGBClassifier # model
from xgboost import plot_importance # 중요변수(x) 시각화
from sklearn.datasets import load_breast_cancer # 이항분류 dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score,classification_report # 평가

#1.XGBoost Hyper parameters

#1) dataset laod
cancer = load_breast_cancer()

# x 변수
x_names=cancer.feature_names
print(x_names,len(x_names)) #30

# y변수
y_label=cancer.target_names
y_label # ['malignant', 'benign'] : 이항

X, y = load_breast_cancer(return_X_y=True)

#2) train/test split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3)

# 3) model 생성
xgb = XGBClassifier()
model = xgb.fit(X_train,y_train)

print(model) # defualt parameters
'''
XGBClassifier
(base_score=0.5, booster='gbtree', colsample_bylevel=1,
colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
importance_type='gain', interaction_constraints='',
learning_rate=0.300000012, max_delta_step=0, max_depth=6,
min_child_weight=1, missing=nan, monotone_constraints='()',
n_estimators=100, n_jobs=4, num_parallel_tree=1, random_state=0,
reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
tree_method='exact', validate_parameters=1, verbosity=None)

1.colsample_bytree=1 : 트리 모델 생성 시 훈련셋 샘플링 비율(보통 : 0.6 ~ 1)
2.learning_rate=0.3 : 학습율(보통 : 0.01~0.1) =0의 수렴속도 (오차가 영이 되는 시점을 찾는다.)
3.max_depth=6 : 트리의 깊이(클 수록 성능이 좋아짐, 과적합 영향)
4.min_child_weight=1 : 자식 노드 분할을 결정하는 가중치(Weight)의 합
- 값을 크게하면 더 많은 자식 노드 분할(과적합 영향)
5. n_estimators=100 결정 트리 개수(default=100), 많을 수록 고성능
6. objective='binary:logistic' : 'reg:linear', 'multi:softmax'(num_class 지정)
'''

# 2.model 학습 조기 종료
xgb = XGBClassifier(colsample_bytree=1,
                    learning_rate=0.3,
                    max_depth=6,
                    min_child_weight=1,
                    n_estimators=500) # 500 개의 tree

eval_set = [(X_test,y_test)] # model 평가 dataset

model = xgb.fit(X=X_train, y=y_train, 
                eval_set=eval_set,
                eval_metric='error', 
                early_stopping_rounds=80,
                verbose=True)
'''
X=X_train, y=y_train -#훈련셋
eval_set=eval_set # 평가셋(검정셋)
eval_metric='error' # 평가방법( error기준:이항분류시, merror:다항분류시) 
early_stopping_rounds=80 # 80번 돌렸을때 큰 변화 없으면 조기 종료(조기종료 라운드 수)
verbose=True # 학습과정 콘솔 출력
'''


# 3. model 평가
y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print(acc) #0.9649122807017544

report=classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.95      0.95      0.95        61
           1       0.97      0.97      0.97       110

    accuracy                           0.96       171
   macro avg       0.96      0.96      0.96       171
weighted avg       0.96      0.96      0.96       171
'''

# 3. Best Hyper parameter
from sklearn.model_selection import GridSearchCV # class

# default parameters 
xgb=XGBClassifier()

params={'olsample_bytree':[0.5,0.7,1],
        'learning_rate': [ 0.01, 0.3, 0.5],
        'max_depth': [5, 6, 7],
        'min_child_weight':[1, 3, 5],
        'n_estimators':[100, 200, 300]} # dict

gs = GridSearchCV(estimator= xgb,
             param_grid=params,
             cv=5)

model = gs.fit(X=X_train, y=y_train, eval_metric='error', eval_set= eval_set,verbose=True )

dir(model)
'''
best_params_
best_score_
'''

print('best score',model.best_score_)
#best score 0.9596835443037974

print('best params',model.best_params_)
'''
best params {'learning_rate': 0.3, 
             'max_depth': 5, 
             'min_child_weight': 1, 
             'n_estimators': 100, 
             'olsample_bytree': 0.5}
'''


























































