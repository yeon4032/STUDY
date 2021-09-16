# -*- coding: utf-8 -*-
"""
step06_Entropy.py

Gini 불순도, Entropy
 Tree model에서 중요변수 선정 기준
 확률 변수 간의 불확실성을 나타내는 수치
 무질서의 양의 척도, 작을 수록 불확실성이 낮다.
 입력 변수(x)를 대상으로 중요 변수 선정 시 사용
 정보이득 = base 지수 - Gini 불순도 or entropy
 정보이득이 클 수록 중요변수로 본다.
 Gini impurity = sum(p * (1-p))
 Entropy = -sum(p * log(p))
"""


import numpy as np

#1. 불확실성이 큰 경우 (x1:앞면 ,x2:뒷면)
x1,x2 = 0.5,0.5 # 독립사건 = 1

gini = sum([x1*(1-x1), x2*(1-x2)])
print(gini) # 0.5

entropy = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])
print(entropy) # 1.0


#1. 불확실성이 작 경우 (x1:앞면 ,x2:뒷면)
x1,x2 = 0.9,0.1 # 독립사건 = 1

gini = sum([x1*(1-x1), x2*(1-x2)])
print(gini) # 0.18

entropy = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])
print(entropy) # 0.4689955935892812


base=0.89
info = base - gini #0.71 
info = base - entropy # 0.4210044064107188
#gini or entropy 가 크면 클수 록 info 는 작아진다.
#info 는 크면 클수록 중요하다
# info =정보 이득(정보 이득이라는게 얼마나 중요한 변수인지를 나타 내는 지표)



####################################################################
### dataset적용
####################################################################33

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    columns = ['dark_clouds','gust'] 
    return dataSet, columns

# 함수 호출
dataSet, columns = createDataSet()

#list->numpy
dataSet=np.array(dataSet)
dataSet.shape #(5, 3)
print(dataSet)
'''
[['1' '1' 'yes']
 ['1' '1' 'yes']
 ['1' '0' 'no']
 ['0' '1' 'no']
 ['0' '1' 'no']]
'''
print(columns) #['dark_clouds', 'gust']

X=dataSet[:,0:2]
X
'''
[['1', '1'],
['1', '1'],
['1', '0'],
['0', '1'],
['0', '1']]
'''

y=dataSet[:,-1]
y # ['yes', 'yes', 'no', 'no', 'no'],
 
# y변수 더미 변수 로 만들기(yes=1, no=0)
label=[1 if i=='yes' else 0 for i in y]
label #[1, 1, 0, 0, 0]


from sklearn.tree import DecisionTreeClassifier # model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가
#시각화 도구
from sklearn.tree import plot_tree, export_graphviz


# model 생성 (gini)
obj = DecisionTreeClassifier(criterion='gini')
model = obj.fit(X= X,y= label)

y_pred = model.predict(X)
print(y_pred) # [1 1 0 0 0]

con_mat = confusion_matrix(label,y_pred)
print(con_mat)
'''
[[3 0]
 [0 2]]
'''
# tree 시각화
plot_tree(model,feature_names=columns)



# model 생성(entropy)
obj = DecisionTreeClassifier(criterion='entropy')
model = obj.fit(X= X,y= label)

y_pred = model.predict(X)
print(y_pred) # [1 1 0 0 0]

con_mat = confusion_matrix(label,y_pred)
print(con_mat)
'''
[[3 0]
 [0 2]]
'''

# tree 시각화
plot_tree(model,feature_names=columns)


# tree graph
export_graphviz(decision_tree= model,
                out_file='tree_graph.dot',
                max_depth=3,
                feature_names=columns,
                class_names=True)

