# -*- coding: utf-8 -*-
"""
step05_DecisionTree.py

Decision Tree 모델
 - 중요변수 선택 기준: gni,entropy
"""

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor # model(DecisionTreeClassifier-> 분류트리(범주), DecisionTreeRegressor->회귀 트리(연속) )
from sklearn.datasets import load_iris, load_wine # dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score # 평가

# 시각화 도구
from sklearn.tree import plot_tree, export_text # tree 시각화

iris = load_iris(return_X_y=False)
dir(iris)
'''
['DESCR',         <- dataset 설명문
 'data',          <- X변수
 'feature_names', <- X변수 이름
 'filename',
 'frame',
 'target',        <- y변수 
 'target_names']  <- y변수 class이름
'''

x_names = iris.feature_names
x_names
'''
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']
'''

y_label= iris.target_names
y_label #array(['setosa', 'versicolor', 'virginica'], dtype='<U10')


help(DecisionTreeClassifier)
'''
criterion='gini' : 중요변수 선정 기준
 -> 'gini'or 'entropy'
splitter='best:각 노드 분할 전략
max_depth=None : 트리 최대 깊이
 -> 과적합 제어 역할 : 값이 클수록 과대적합, 적을 수록 과소적합
 -> max_depth=3 : 사용자 정의
 ->max_depth=None : min_samples_split 보다 작을 때가지 tree 생성
min_samples_split=2: 내부 노드를 분할하는 데 필요한 최소 샘플수
 ->과저합 제어 역할 
'''

# 1. model1: 중요변수: 'gini', max_depth=None
obj=DecisionTreeClassifier(criterion='gini',
                            max_depth=None,
                            min_samples_split=2,
                            random_state=123)

model= obj.fit(X=iris.data,y=iris.target)
dir(model)
model.get_depth() # 5 -> level5 깊이 까지 생성
model.min_samples_leaf # 마지막 sample 개수는 1 

#시각화
tree_text = export_text(model, feature_names= x_names) # tree text 출력
print(tree_text)

plot_tree(model)# tree 시각화 도구


#mode12: 중요변수 ='entropy', max_depth=3
obj2=DecisionTreeClassifier(criterion='entropy',
                            max_depth=3,
                            random_state=123)

model2=obj2.fit(X=iris.data,y=iris.target)

#시각화
tree_text = export_text(model2, feature_names= x_names) # tree text 출력
print(tree_text)

plot_tree(model2)# tree 시각화 도구

plot_tree(model2,feature_names= x_names) # 색인 데신 변수 이름 나옴


#################################################################################
### load_wine
#################################################################################

wine=load_wine()

x_names = wine.feature_names
x_names
len(x_names) #13

y_labels=wine.target_names
y_labels # ['class_0', 'class_1', 'class_2']

wine_x = wine.data
wine_y = wine.target 

wine_x.shape # (178, 13)
wine_y.shape # (178,)
wine_y # 0~2

# train/test split
X_train,X_test,y_train,y_test = train_test_split(wine_x,wine_y,test_size=0.3, random_state=123)

obj3=DecisionTreeClassifier(random_state=123)
model3 = obj3.fit(X=X_train,y=y_train)

obj4=DecisionTreeClassifier(tree_depth=3, random_state=123)
model4=obj4.fit(X=X_train,y=y_train)

train_score = model3.score(X=X_train,y=y_train)
test_score = model3.score(X=X_test,y=y_test)
print(train_score) # 1.0
print(test_score)  # 0.9444444444444444

train_score2 = model4.score(X=X_train,y=y_train)
test_score2 = model4.score(X=X_test,y=y_test)
print(train_score2) # 1.0
print(test_score2)  # 0.9444444444444444


# tree 시각화 
plot_tree(model,feature_names=x_names)
plot_tree(model2,feature_names=x_names)







