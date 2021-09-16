# -*- coding: utf-8 -*-
"""
step03_RF_parameter_GridSearch.py

1. RandForest Parameters
2. GridSearch : best parameters
"""

from sklearn.ensemble import RandomForestClassifier #model 
from sklearn.datasets import load_digits # dataset
from sklearn.model_selection import GridSearchCV # best parameters

#1. dataset load
X,y = load_digits(return_X_y=True)

#2.model 생성
rfc = RandomForestClassifier()
'''
n_estimators=100 : 결정 트리 개수, 많을 수록 성능이 좋아짐
criterion='gini' : 노드 불순도 - 중요변수 선정기준:{gini, entropy}
max_depth=None :  min_samples_split의 샘플 수 보다 적을 때 까지 tree 깊이 생성
min_samples_split=2 : 내부 node 분할에 사용할 최소 sample 수
max_features='auto' : 최대 사용할 x변수 개수: {auto,sqrt,log2}
n_jobs=None : cpu 사용 수
min_samples_leaf : leaf node를 만드는데 필요한 최소한의 sample 수
'''

model = rfc.fit(X=X,y=y)

# 3. GridSearch model
# - best parameters 

parmas = {'n_estimators' : [100,150,200],
          'max_depth' : [None, 3, 5, 7],
          'min_samples_split' : [2,3,4],
          'max_features' : ["auto", "sqrt"],
          'min_samples_leaf' : [1, 2, 3]} # dict 정의

grid_model = GridSearchCV(model, param_grid=parmas,scoring='accuracy',
                          cv=5,n_jobs= -1)
'''
cv 교차검정에 대한 파라미터이고, n_job 사용할 cpu 개수를 지정하는 파라미터 입니다
cv=5 의미
전체 자료를 5등분한 후 4개는 훈련셋으로 사용하고 1개는 검정셋으로 사용하여 5회 상호비교하여 5번 검정을 수행합니다.

n_jobs=-1의미
-1를 지정하면 사용 가능한 모든 cpu를 사용할 수 있습니다.
'''


grid_model = grid_model.fit(X,y)


# 4. Best score & parameters 
dir(grid_model)

print('best score=',grid_model.best_score_)
#best score= 0.9410244506344785

print('best parameters=', grid_model.best_params_)
'''
best parameters= 
{'max_depth': None, 'max_features': 'auto', 'min_samples_leaf': 1,
'min_samples_split': 2, 'n_estimators': 150}
'''








































































