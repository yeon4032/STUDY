# -*- coding: utf-8 -*-
"""
문) tree_data.csv 파일의 변수를 이용하여 아래 조건으로 DecisionTree model를 생성하고,
    의사결정 tree 그래프를 시각화하시오.
    
 <변수 선택>   
 x변수 : iq수치, 나이, 수입, 사업가유무, 학위유무
 y변수 : 흡연유무
 
 <그래프 저장 파일명> : smoking_tree_graph.dot
"""
from sklearn.tree import DecisionTreeClassifier # model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가
from sklearn.model_selection import train_test_split # dataset split
import pandas as pd
from sklearn.tree import plot_tree, export_graphviz
tree_data = pd.read_csv("C:/ITWILL/4_python-ll/data/tree_data.csv")
print(tree_data.info())
'''
iq         6 non-null int64 - iq수치
age        6 non-null int64 - 나이
income     6 non-null int64 - 수입
owner      6 non-null int64 - 사업가 유무
unidegree  6 non-null int64 - 학위 유무
smoking    6 non-null int64 - 흡연 유무
'''
x_names=tree_data.columns
dir(tree_data)

#변수 선정
X=tree_data.iloc[:,0:5]
y=tree_data.iloc[:,-1]

#model 생성
obj = DecisionTreeClassifier(criterion='gini')
model = obj.fit(X= X,y= y)


#model 평가
y_pred = model.predict(X)
print(y_pred)
model_acc=accuracy_score(y,y_pred)

#시각화
plot_tree(model,feature_names=x_names)

# tree graph
export_graphviz(decision_tree= model,
                out_file='smoking_tree_graph.dot',
                max_depth=3,
                feature_names=x_names[0:5],
                class_names=True)












