# -*- coding: utf-8 -*-
"""
step02_NB.py

Naive Bayes 이론에 근거한 통계적 분류기 
"""

# <조건부 확률>
# 사건 A 발생 확률 -> 사건 B 발생 영향
# 두 사건의 발생확률 사이의 관계 표현 

# P(B|A) =  P(A^B)/P(A) = P(A|B).P(B) / P(A) : 확률의 곱셈법칙  
'''
사전확률 = P(A), P(B) : 사전에 알고 있는 확률 
결합확률 = P(A|B) : 두 사건 A와 B가 동시 일어날 확률 
'''

# example : 날씨와 비 관계
'''
       yes   no  tot
맑은날  2    8   10 
흐린날  6    4   10
       8    12  20
'''

# 1. 사전확률 

# 비가 온 확률 
p_yes = 8 / 20 # 0.4

# 비가 안온 확률 
p_no = 12 / 20 # 0.6

# 2. 독립사건 : 전체 합 = 1
p_tot = p_yes + p_no
p_tot # 1.0


# 3. 조건부 확률  : P(B|A) =  P(A^B)/P(A) = P(A|B).P(B) / P(A)

# ex1) 맑은날(A) 비가 온(B) 확률
# P(yes|맑은날)  = P(맑은날|yes).P(yes) / P(맑은날)
'''
P(맑은날|yes) =   2/8 = 0.25
P(yes) = 8 / 20 = 0.4
P(맑은날) = 10 / 20 = 0.5
'''
p = (2/8) * p_yes / 0.5
p # 0.2

# ex2) 흐린날(A) 비가 온(B) 확률 
# P(yes|흐린날)  = P(흐린날|yes).P(yes) / P(흐린날)
'''
P(흐린날|yes) =  6/8 
P(yes) = 8 / 20 = 0.4
P(흐린날) = 10/20 = 0.5
'''
p = (6/8) * p_yes / 0.5
p # 0.6


from sklearn.datasets import load_iris # dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.naive_bayes import GaussianNB  # model 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report # 평가 

'''
GaussianNB : x변수가 연속형, 정규분포 경우 적용 
MultinomialNB : 고차원의 텍스트(DTM) 분류에 적용 
'''

# 1. dataset laod
X, y = load_iris(return_X_y=True)

X
y # 0~2 class 


# 2. train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. model 생성 
nb = GaussianNB()
model = nb.fit(X=X_train, y=y_train)


# 4. model 평가 
y_pred = model.predict(X = X_test)

acc = accuracy_score(y_test, y_pred)
print('accuracy =', acc)
# accuracy = 0.9555555555555556

con_mat = confusion_matrix(y_test, y_pred)
con_mat
'''
array([[18,  0,  0],
       [ 0, 10,  0],
       [ 0,  2, 15]],
'''

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        18
           1       0.83      1.00      0.91        10
           2       1.00      0.88      0.94        17

    accuracy                           0.96        45
   macro avg       0.94      0.96      0.95        45
weighted avg       0.96      0.96      0.96        45
'''

# f1-score 기준 
# 산술평균 
macro_avg =  (1.00 + 0.91 + 0.94) / 3 # 0.95
macro_avg # 0.95

# 각 클래스에 속하는 표본의 개수로 가중평균 = (score*가중치)/가중치합       
weighted_avg = (1.00*0.18 + 0.91*0.1 + 0.94*0.17) / (0.18+0.1+0.17)
weighted_avg # 0.957 -> 0.96


############################
### news groups 분류 
############################
from sklearn.naive_bayes import MultinomialNB # model - 문서분류 
from sklearn.datasets import fetch_20newsgroups # news 데이터셋 
from sklearn.feature_extraction.text import TfidfVectorizer # 단어생성기 


# 1. dataset 확인 
news = fetch_20newsgroups(subset='all') # train/test load

# dataset 설명문 
print(news.DESCR)
'''
**Data Set Characteristics:**

    =================   ==========
    Classes                     20 -> 20newsgroups
    Samples total            18846 -> news 문장 
    Dimensionality               1 -> 1차원
    Features                  text -> 자연어 
    =================   ==========
'''

class_names = news.target_names
print(class_names)
len(class_names) # 20

# 2. train set 선택 : 4개 뉴스 그룹 
news_train = fetch_20newsgroups(subset='train', categories=class_names[:4])

news_data = news_train.data # X변수 : news texts
news_target = news_train.target # y변수 : 0~3(4개 뉴스 그룹)

print(news_data) # news 영문 
print(news_target) # [3 2 2 ... 0 1 1] 


# 3. Sparse matrix : news 영문 -> DTM 
obj = TfidfVectorizer() # 단어생성기 
sp_mat = obj.fit_transform(news_data)
sp_mat.shape # (2245, 62227)


# 4. NB 모델 생성 
nb = MultinomialNB()
model = nb.fit(X = sp_mat, y=news_target)


# 5. test set 선택 : 4개 뉴스 그룹
news_test = fetch_20newsgroups(subset='test', categories=class_names[:4])

news_test_data = news_test.data # X변수 (영문) 
news_test_target = news_test.target # y변수(10진수) 

print(news_test_data) # 영문 
print(news_test_target) # [1 1 1 ... 1 3 3]

# 영문 -> 희소행렬 변경 
sp_mat_test = obj.transform(news_test_data)
'''
train 희소행렬 : obj.fit_transform()
test 희소행렬 : obj.transform()
'''


# 6. model 평가 
y_pred = model.predict(X = sp_mat_test)
y_true = news_test_target

acc = accuracy_score(y_true, y_pred)
print('accuracy =',acc)
# accuracy = 0.8520749665327979

con_mat = confusion_matrix(y_true, y_pred)
print(con_mat)
'''
[[312   2   1   4] - 0
 [ 12 319  22  36] - 1
 [ 16  26 277  75] - 2
 [  1   8  18 365]]- 3
'''

report = classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.91      0.98      0.95       319
           1       0.90      0.82      0.86       389
           2       0.87      0.70      0.78       394
           3       0.76      0.93      0.84       392

    accuracy                           0.85      1494
   macro avg       0.86      0.86      0.85      1494
weighted avg       0.86      0.85      0.85      1494
'''







