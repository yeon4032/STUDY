'''
교차검정(cross validation)
 - 검정셋과 훈련셋을 서로 교차하여 검정하는 방식
 - 전체 datasetd을 n등분
'''

from sklearn.datasets import load_digits
from sklearn.model_selection import cross_validate# cross validation 
from sklearn.ensemble import RandomForestClassifier # RM
from sklearn.metrics import accuracy_socre # 평가

# 1. dataset load 
digits = load_digits()

X = digits.data
y = digits.target

X.shape # (1797, 64) - (images,pixel 수)
y.shape # (1797,)
y # array([0, 1, 2, ..., 8, 9, 8])


# 2. model 생성 
rfc = RandomForestClassifier()
model = rfc.fit(X, y) 

# 예측치 : class
y_pred = model.predict(X=X) # image => 10 진수


# 예측치: 확률
y_pred_prob = model.predict_proba(X= X) # image -> 확률
y_pred_prob
'''
array([[1.  , 0.  , 0.  , ..., 0.  , 0.  , 0.  ], -> 0 (100%확률로 0이 나온다)
       [0.  , 0.97, 0.01, ..., 0.  , 0.01, 0.  ], -> 1 (97%확률로 1이 나온다 )
       [0.01, 0.06, 0.78, ..., 0.01, 0.13, 0.01], -> 2
       ...,
       [0.  , 0.03, 0.01, ..., 0.  , 0.93, 0.  ],
       [0.01, 0.  , 0.  , ..., 0.  , 0.03, 0.93],
       [0.  , 0.01, 0.03, ..., 0.  , 0.86, 0.03]])
'''

# 확률값이 가장 큰 값 index 반환: 10진수
y_pred2 = y_pred_prob.argmax(axis = 1 ) # 행 단위
y_pred2 # [0, 1, 2, ..., 8, 9, 8]


# model 평가
acc = accuracy_score(y_pred2,y)
acc # 1


# 3. 교차검정 : 균등분할 -> 교차검정 
score = cross_validate(model, X, y, cv=5) # 5겹 교차검정
print(score)
'''
{'fit_time': array([0.52996111, 0.68724394, 0.56545806, 0.58411646, 0.52263451]),
 'score_time': array([0.03586864, 0.02197504, 0.02645564, 0.02493238, 0.02490258]),
 'test_score': array([0.93611111, 0.91666667, 0.9637883 , 0.9637883 , 0.92200557])}
'''

print(score['test_score'])
# [0.93611111 0.91666667 0.9637883  0.9637883  0.92200557]

#test score 산술평균
print(score['test_score'].mean())
#0.9404719900959456

















