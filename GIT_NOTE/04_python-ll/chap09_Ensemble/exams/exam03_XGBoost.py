'''
외식업종 관련 dataset 분석

문) food를 대상으로 다음과 같이 xgboost 모델을 생성하시오.
   <조건1> 6:4 비율 train/test set 생성 
   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
   <조건3> 중요변수에 대한  f1 score 출력
   <조건4> 중요변수 시각화  
   <조건5> accuracy와 model report 출력 
'''

import pandas as pd
from sklearn import model_selection, metrics
from sklearn.preprocessing import minmax_scale # 정규화 함수 
from xgboost import XGBClassifier # xgboost 모델 생성 
from xgboost import plot_importance # 중요변수 시각화  

# 중요변수 시각화 
from matplotlib import pyplot
from matplotlib import font_manager, rc # 한글 지원
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 외식업종 관련 data set
food = pd.read_csv("C:\\ITWILL\\4_python-ll\\data/food_dataset.csv",
                   encoding="utf-8",thousands=',')

col_names =list(food.columns)
# 결측치 제거
food=food.dropna()  
print(food.info())
'''
 <class 'pandas.core.frame.DataFrame'>
Int64Index: 68796 entries, 0 to 70170
Data columns (total 21 columns):
'''

#y변수 확인 (signo or softmax)
food['폐업_2년'].value_counts()
'''
0    54284
1    14512
'''
# 정규화
food_nor = minmax_scale(food) # DF
type(food_nor) # numpy.ndarray
food_nor.shape #(68796, 21)

#numpy-> pandas 변환
food_df = pd.DataFrame(food_nor,columns=col_names)
food_df.head()

#my work
#   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
#   <조건1> 6:4 비율 train/test set 생성 
X=food.iloc[:,0:-1]
y=food.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.4)


#   <조건3> 중요변수에 대한  f1 score 출력
obj=XGBClassifier(objectvie='binary:logistic')
model=obj.fit(X=X_train,y=y_train,eval_metric='error')

fscore = model.get_booster().get_fscore()

#   <조건4> 중요변수 시각화  
plot_importance(model,max_num_features=5)



#   <조건5> accuracy와 model report 출력 
y_pred = model.predict(X=X_test) # 예측치
y_true = y_test # 관측치

con_mat=pd.crosstab(y_pred,y_true,rownames=["예측치"],colnames=["관측치"])
con_mat
'''
관측치      0     1
예측치             
0    21168  5246
1      570   535
'''
acc=metrics.accuracy_score(y_true, y_pred)
acc # 0.7886551110142084

report= metrics.classification_report(y_true, y_pred)
print(report)


#or




#lecture work(정규화 된거 사용)
#   <조건1> 6:4 비율 train/test set 생성 
train_set,test_set= model_selection.train_test_split(food_df,test_size=0.4)

#   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
y_name = col_names.pop(-1)
print('y변수:',y_name)

x_name = col_names
print("기존 x변수 객수",len(x_name))

#   <조건3> 중요변수에 대한  f1 score 출력
obj=XGBClassifier(objectvie='binary:logistic')
model=obj.fit(X=train_set[x_name],y=train_set[y_name],eval_metric='error')


#   <조건4> 중요변수 시각화 
fscore = model.get_booster().get_fscore() 
plot_importance(model,max_num_features=5)

#   <조건5> accuracy와 model report 출력 
y_pred = model.predict(test_set[x_name]) # 예측치
y_true = test_set[y_name] # 관측치

acc=metrics.accuracy_score(y_true, y_pred)
acc #0.791017115447509

report= metrics.classification_report(y_true, y_pred)
print(report)


















