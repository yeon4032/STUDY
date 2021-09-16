'''
문) weatherAUS.csv 파일을 시용하여 NB 모델을 생성하시오
  단계1> NaN 값을 가진 모든 row 삭제 
  단계2> 1,2,8,10,11,22,23 칼럼 제외 
  단계3> 7:3 비율 train/test 데이터셋 구성 
  단계4> 변수 선택  : y변수 : RainTomorrow, x변수 : 나머지 변수(16개)
  단계5> GaussianNB 모델 생성 
  단계6> model 평가 : accuracy, confusion matrix, f1 score
'''
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report # 모델 평가 
from sklearn.naive_bayes import GaussianNB  #model


import pandas as pd
from sklearn.model_selection import train_test_split 

data = pd.read_csv('C:/ITWILL/4_Python-II/data/weatherAUS.csv')
print(data.head())
print(data.info())

# 단계1> NaN 값을 가진 모든 row 삭제
data=data.dropna()
print(data.head())

# 조건2> 1,2,8,10,11,22,23 칼럼 제외 
cols = list(data.columns) # 전체 칼럼 추출 
colnames = [] # 사용할 칼럼 저장 

for i in range(24) :
    if i not in [0,1,7,9,10,21,22] : # 해당 칼럼 제외 
        colnames.append(cols[i]) 
    
new_data = data[colnames]
print(new_data.info())


# 단계3> 7:3 비율 train/test 데이터셋 구성
train_set, test_set = train_test_split(
new_data, test_size=0.3, random_state=0) # seed값 

# 단계4> x, y변수 선택

# 단계5> GaussianNB 모델 생성 
  
# 단계6> model 평가 : accuracy, confusion matrix, f1 score
















































data = pd.read_csv('C:\\ITWILL\\4_python-ll\\data/weatherAUS.csv')
print(data.head())
print(data.info())

# 단계1> NaN 값을 가진 모든 row 삭제
data=data.dropna()
print(data.head())

# 조건2> 1,2,8,10,11,22,23 칼럼 제외 
cols = list(data.columns) # 전체 칼럼 추출 
colnames = [] # 사용할 칼럼 저장 

for i in range(24) :
    if i not in [0,1,7,9,10,21,22] : # 해당 칼럼 제외 
        colnames.append(cols[i]) 
    
new_data = data[colnames]
print(new_data.info())


# 단계3> 7:3 비율 train/test 데이터셋 구성
train_set, test_set = train_test_split(
new_data, test_size=0.3, random_state=0) # seed값 

# 단계4> x, y변수 선택
# X변수: 1~16
# y변수: 17

X_train=train_set.iloc[:,0:16]
y_train=train_set.iloc[:,16]

X_test=test_set.iloc[:,0:16]
y_test=test_set.iloc[:,16]


# 단계5> GaussianNB 모델 생성 
nb=GaussianNB()
model=nb.fit(X=X_train,y=y_train)  
# 단계6> model 평가 : accuracy, confusion matrix, f1 score
y_pred=model.predict(X=X_test)
y_pred

acc=accuracy_score(y_test,y_pred)
acc

con=confusion_matrix(y_test,y_pred)
con

report=classification_report(y_test,y_pred)
print(report)
'''
              precision    recall  f1-score   support

          No       0.91      0.83      0.87      4067
         Yes       0.54      0.70      0.61      1147

    accuracy                           0.81      5214
   macro avg       0.73      0.77      0.74      5214
weighted avg       0.83      0.81      0.81      5214

'''














