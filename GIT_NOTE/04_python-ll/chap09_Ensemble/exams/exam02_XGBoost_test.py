'''
 문) iris dataset을 이용하여 다음과 같은 단계로 XGBoost model을 생성하시오.
'''

import pandas as pd # file read
from xgboost import XGBClassifier # model 생성 
from xgboost import plot_importance # 중요변수 시각화  
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report # model 평가 


# 단계1 : data set load 
iris = pd.read_csv("C:\\ITWILL\\4_python-ll\\data/iris.csv")

# 변수명 추출 
cols=list(iris.columns)
col_x=cols[:4] # x변수명 
col_y=cols[-1] # y변수명 

# 단계2 : 훈련/검정 데이터셋 생성
train_set, test_set = train_test_split(iris, test_size=0.25)

X_train=train_set[col_x]
X_test=test_set[col_x]

y_train=train_set[col_y]
y_test=test_set[col_y]

# 단계3 : model 생성 : train data 이용
obj=XGBClassifier()
model = obj.fit(X_train,y_train)

# 단계4 :예측치 생성 : test data 이용  
y_pred=model.predict(X_test)

# 단계5 : 중요변수 확인 & 시각화 
fscore = model.get_booster().get_fscore()
print(fscore) 
#{'Petal.Length': 92, 'Petal.Width': 84, 'Sepal.Length': 123, 'Sepal.Width': 67} 
plot_importance(model)

# 단계6 : model 평가 : confusion matrix, accuracy, report
con_mat=confusion_matrix(y_test,y_pred)
con_mat

acc=accuracy_score(y_test,y_pred)
acc

report=classification_report(y_test,y_pred)
print(report)
