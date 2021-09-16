# -*- coding: utf-8 -*-
"""
step04_NB_SVM.py

NB VS SVM
 - spam_train_test.npy
NB:연산속도 빠름
SVM: 정확도 높음
"""

import numpy as np # np.load(*.npy)
from sklearn.naive_bayes import MultinomialNB  # nb model 
from sklearn.svm import SVC # SVM model 생성
from sklearn.metrics import accuracy_score, confusion_matrix
import time # 시간 측정

path="C:/ITWILL/4_python-ll/workspace/chap07_TextMining/data/"

X_train, X_test, y_train, y_test = np.load(path + "/spam_train_test.npy", 
                                           allow_pickle=True)

#input(X):희소행렬(DTM)
X_train.shape # (3901, 5000)
X_test.shape  # (1673, 5000)

#Output(y):0(ham) or 1(spam)
y_train[:10]

##############################
####### NB model
##############################
nb = MultinomialNB()

chktime = time.time()
model=nb.fit(X=X_train,y=y_train)
chktime=time.time() - chktime
print('실행시간,:',chktime)
#실행시간,: 0.06286764144897461

y_pred = model.predict(X=X_test) # 예측치 
y_true = y_test # 관측치

acc=accuracy_score(y_test,y_pred)
print('NB 분류정확도=',acc)
# NB 분류정확도= 0.9772863120143455


con_mat = confusion_matrix(y_test,y_pred)
print(con_mat)
'''
      0    1 
0 [[1460    1]  =1461
1  [  37  175]] =212 
'''
ham_rate = 1460/1461
ham_rate  # 0.999315537303217
spam_rate=(175)/(37+175)
spam_rate # 0.8254716981132075


#################################################
### SVM model
#################################################
svm = SVC(kernel = 'linear')
model2=svm.fit(X=X_train,y=y_train)

chktime = time.time()
model2=svm.fit(X=X_train,y=y_train)
chktime=time.time() - chktime
print('실행시간,:',chktime)
#실행시간,: 16.31864857673645

y_pred2=model2.predict(X=X_test)

acc2=accuracy_score(y_test,y_pred2)
print('NB 분류정확도=',acc2)
#NB 분류정확도= 0.982068141063957

con_mat2 = confusion_matrix(y_test,y_pred2)
type(con_mat2) # numpy.ndarray
print(con_mat2)
'''
    0     1
0[[1460    1]
 1[  29  183]]
'''

ham_rate = 1460/1461
ham_rate  # 0.999315537303217
spam_rate=(183)/(29+183)
spam_rate # 0.8632075471698113

# 정확률: 예측치 yes(1)-> yes
p = con_mat2[1,1]/ (con_mat2[0,1] +con_mat2[1,1])
print('정확률=',p) #정확률= 0.9945652173913043

# 재현율: 관측치 YES->YES
r = con_mat2[1,1]/ (con_mat2[1,0] +con_mat2[1,1])
print('재현율=',r) #재현율= 0.8632075471698113

#특이도:관측치 NO(0) -> NO (0)
s=con_mat[0,0]/(con_mat[0,0]+con_mat[0,1])
print('특이도=',s)

# f1-score: 정확률과 재현율 조화 평균
f1_score = ((p*r)/(p+r))*2
print('f1 score=',f1_score) 
# f1 score= 0.9242424242424243














