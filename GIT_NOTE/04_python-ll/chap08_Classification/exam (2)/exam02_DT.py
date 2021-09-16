'''
 문) load_breast_cancer 데이터 셋을 이용하여 다음과 같이 Decision Tree 모델을 생성하시오.
 <조건1> 75:25비율 train/test 데이터 셋 구성 
 <조건2> y변수 : cancer.target, x변수 : cancer.data
 <조건3> tree 최대 깊이 : 5 
 <조건4> 중요변수 확인 

'''
from sklearn import model_selection
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree.export import export_text # tree 텍스트 출력 
from sklearn.tree import plot_tree # tree 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.tree import plot_tree, export_text 

# 데이터 셋 load 
cancer = load_breast_cancer()
print(cancer)
print(cancer.DESCR)

# 변수 선택 
X = cancer.data
y = cancer.target

# <조건1> 75:25비율 train/test 데이터 셋 구성 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=123)
































# 데이터 셋 load 
cancer = load_breast_cancer()
print(cancer)
print(cancer.DESCR)

# 변수 선택 (<조건2> y변수 : cancer.target, x변수 : cancer.data)
X = cancer.data
y = cancer.target

x_names=list(cancer.feature_names)
# <조건1> 75:25비율 train/test 데이터 셋 구성 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=123)


#<조건3> tree 최대 깊이 : 5 
obj=DecisionTreeClassifier(max_depth=5,
                            random_state=123)

model= obj.fit(X=X_train,y=y_train)
model.get_depth() # 5 

# <조건4> 중요변수 확인 
tree_text = export_text(model,feature_names=x_names) # tree text 출력
print(tree_text) 
#worst radius <= 16.80

plot_tree(model, feature_names= x_names)# tree 시각화 도구






