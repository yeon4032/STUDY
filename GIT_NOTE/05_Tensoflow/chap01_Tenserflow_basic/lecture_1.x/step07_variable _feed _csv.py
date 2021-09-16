# -*- coding: utf-8 -*-
"""
step07_variable _feed _csv.py

csv file -> 공급 변수에 자료 공급

tensorflow 가상환경에서 scikit-learn 설치
(base) > conda activate tensorflow
(tensorflow) > conda install -c conda-forge scikit-learn
(tensorflow) > conda install -c conda-forge pandas
"""

import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

import pandas as pd # csv file load
from sklearn.model_selection import train_test_split # dataset split

#1. dataset load
iris = pd.read_csv('C:\\ITWILL\\5_Tensoflow\\data/iris.csv')
print(iris.info())

# 2. X,y 공급 data 생성
X_data = iris.iloc[:,:4]
y_data = iris.iloc[:, -1]
X_data.shape # (150, 4)
y_data.shape # (150,)

# 3. X, y 변수 정의 
X = tf.placeholder(dtype=tf.float32, shape=[None, 4]) # x_data 공급
y = tf.placeholder(dtype=tf.string, shape=[None]) # y_data

# 4. data split
X_train,X_test,y_train,y_test = train_test_split(
    X_data , y_data, test_size=0.3) # 4.working will apply for X,y( working 3)
X_train.shape # (105, 4) 
X_test.shape # (45, 4)

# 5. session object
with tf.Session() as sess:
    # 1. 훈련셋 data 공급
    X_val,y_val = sess.run([X, y],feed_dict={X:X_train, y: y_train})
    print(X_val.shape)# (105, 4)
    print(y_val.shape)# (105,)
    
    # 2. 검정셋 data 공급
    X_val2,y_val2 = sess.run([X, y],feed_dict={X:X_test, y: y_test})
    print(X_val2)# (105, 4)
    print(y_val2)# (105,)
    

    print(X_val.mean(axis=0))
    #[5.899048  3.074286  3.8923807 1.2580951]
    
    #numpy -> pandas 변경
    y_ser=pd.Series(y_val2)
    print(y_ser.value_counts()) # 범주별 빈도수 
    '''
    setosa        18
    virginica     15
    versicolor    12
    dtype: int64
    '''
    









































