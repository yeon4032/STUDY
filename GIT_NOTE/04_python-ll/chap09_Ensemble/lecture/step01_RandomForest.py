# -*- coding: utf-8 -*-
"""
step01_RandomForest.py
"""

from sklearn.ensemble import RandomForestClassifier # model 
from sklearn.datasets import load_wine # dataset
#평가 도구
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# 1. dataset load
wine=load_wine()

x_names= wine.feature_names
print(x_names)

X,y= wine.data,wine.target
X.shape #(178, 13)
y.shape #(178,)

# 2. model 생성
help(RandomForestClassifier())
'''
n_estimators=100 : tree 개수
criterion='gini' : 중요변수 선정 기준
max_depth=None :
min_samples_split=2:
'''

obj=RandomForestClassifier()
model=obj.fit(X=X,y=y) # full dataset 적용
'''
전체 데이터셋을 대상으로 복원추출하여 지정한 개수만큼 다수의 모델을 생성하기 위해서 입니다.
'''


# 3. test set 생성
import numpy as np
idx = np.random.choice(a=len(X), size =100, replace=False)
idx

X_test,y_test = X[idx],y[idx]
X_test.shape # (100,13)


# 4. model 평가
y_pred = model.predict(X= X_test)

con_mat = confusion_matrix(y_test,y_pred)
print(con_mat)
'''
[[34  0  0]
 [ 0 38  0]
 [ 0  0 28]]
'''

acc = accuracy_score(y_test,y_pred) 
acc#y_test,y_pred

report = classification_report(y_test,y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        34
           1       1.00      1.00      1.00        38
           2       1.00      1.00      1.00        28

    accuracy                           1.00       100
   macro avg       1.00      1.00      1.00       100
weighted avg       1.00      1.00      1.00       100

'''


# 5. 중요변수 시각화
dir(model)

print('중요도:',model.feature_importances_)

'''
중요도: [0.09389196 0.03384828 0.01564293 0.03057694 0.02960943 0.03954496
 0.18696324 0.01449541 0.01869179 0.17954935 0.05895195 0.13583374
 0.16240003]

순서(x_names= wine.feature_names)
['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium',
 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins',
 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
'''
x_names # x변수
x_size=len(x_names)

import matplotlib.pyplot as plt

# 가로막대
plt.barh(range(x_size),model.feature_importances_) #(y, x)
# y축 눈금 :x변수 변경
plt.yticks(range(x_size), x_names)
plt.xlabel('feature_importances')
plt.show()














