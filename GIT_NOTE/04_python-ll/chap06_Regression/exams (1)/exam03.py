'''
문) load_wine() 함수를 이용하여 와인 데이터를 다항분류하는 로지스틱 회귀모델을 생성하시오. 
  조건1> train/test - 7:3비울
  조건2> y 변수 : wine.data 
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


# 1. wine 데이터셋 
wine = load_wine()

# 2. 변수 선택 


# 3. train/test split(7:3)




# 4. model 생성  : solver='lbfgs', multi_class='multinomial'




# 5. 모델 평가 : accuracy, confusion matrix
#분류정확도


#confusion matrix





































# 1. wine 데이터셋 
wine = load_wine()

# 2. 변수 선택 
wine_x = wine.data # x변수 
wine_y = wine.target # y변수

# 3. train/test split(7:3)
X_train,X_test,y_train,y_test=train_test_split(wine_x,wine_y,test_size=0.3,random_state=123)
'''
model을 생성할 때 마다 매번 다른 환경에서 만들어지기 때문에 예측결과도 달라집니다.
이러한 현상으로 막기 위해서 seed값을 지정하면 항당 동일한 환경에서 model이 생성되고 
따라서 예측결과도 동일하게 나타납니다. 이럴때 random_state에 시드값을 지정하여 사용합니다.
'''

# 4. model 생성  : solver='lbfgs', multi_class='multinomial'
lr=LogisticRegression(random_state=0, solver='lbfgs',
                      max_iter=200, multi_class='multinomial')

'''
hyper parameter : 사용자가 값을 지정하는 parameter
'''
model=lr.fit(X_train,y_train)


# 5. 모델 평가 : accuracy, confusion matrix
#분류정확도
acc= model.score(X_test,y_test)
print('accuracy=',acc) #accuracy= 0.9444444444444444

#confusion matrix
y_pred=model.predict(X=X_test)
y_true=y_test
con_max=metrics.confusion_matrix(y_true, y_pred)
print(con_max) # 행: 관측치 vs 열 : 예측치
'''
[[13  1  0]
 [ 1 17  0]
 [ 0  1 21]]
'''

score=metrics.accuracy_score(y_true,y_pred)
print(score) # 0.9444444444444444











