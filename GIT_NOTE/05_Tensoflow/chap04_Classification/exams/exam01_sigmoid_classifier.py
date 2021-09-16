'''
문) bmi.csv 데이터셋을 이용하여 다음과 같이 sigmoid classifier의 모델을 생성하시오. 
   조건1> bmi.csv 데이터셋 
       -> x변수 : 1,2번째 칼럼(height, weight) 
       -> y변수 : 3번째 칼럼(label)
   조건2> 딥러닝 최적화 알고리즘 : Adam
   조건3> learning rage = 0.01    
   조건4> 반복학습 : 2,000번, 200 step 단위로 loss 출력 
   조건5> 최적화 모델 테스트 :  분류정확도(Accuracy report) 출력 
   
 <출력결과>
step = 200 , loss = 0.532565
step = 400 , loss = 0.41763392
step = 600 , loss = 0.34404162
step = 800 , loss = 0.29450226
step = 1000 , loss = 0.25899038
step = 1200 , loss = 0.23218009
step = 1400 , loss = 0.2111086
step = 1600 , loss = 0.19401966
step = 1800 , loss = 0.17981105
step = 2000 , loss = 0.16775638
========================================
accuracy= 0.9894053767712886  
'''
import tensorflow as tf 
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import minmax_scale # x변수 정규화 
import numpy as np
import pandas as pd
 
# csv file load
bmi = pd.read_csv('C:\\ITWILL\\5_Tensoflow\\data/bmi.csv')
print(bmi.info())

bmi['label'].value_counts()
'''
normal    7677
fat       7425
thin      4898
Name: label, dtype: int64
'''
# subset 생성 : label에서 normal, fat 추출 
bmi = bmi[bmi.label.isin(['normal','fat'])]
print(bmi.head())

# 칼럼 추출 
col = list(bmi.columns)
print(col) 

# x,y 변수 추출 
x_data = bmi[col[:2]] # x변수(1,2칼럼)
y_data = bmi[col[2]] # y변수(3칼럼)
y_data # dtype: object

# 데이터 전처리 : label 더미변수 변환(normal -> 0, fat -> 1)
map_data = {'normal': 0,'fat' : 1}
y_data= y_data.map(map_data) # dict mapping
print(y_data) # 0/1
y_data.shape #(15102,)

dir(y_data)
# x_data 정규화 함수 
x_data = minmax_scale(x_data)

# numpy 객체 변환 (판다스 -> numpy)
np.array([y_data]).shape
x_data = np.array(x_data)
y_data = np.transpose(np.array([y_data])) # (1, 15102) -> (15102, 1)

print(x_data.shape) # (15102, 2)
print(y_data.shape) # (15102, 1)

################# X,Y 데이터 전처리 완료 #####################


# 1. X,Y 변수 정의   
X = tf.constant(x_data, tf.float32) 
Y = tf.constant(y_data, tf.float32)
 

# 2. w,b 변수 정의 : 초기값(정규분포 난수 )
w = tf.Variable(tf.random.normal([2, 1]))# [입력수,출력수]
b = tf.Variable(tf.random.normal([1])) # [출력수] 


# 3. 회귀방정식 
def linear_model(X) : # train, test
    y_pred = tf.linalg.matmul(X, w) + b 
    return y_pred # 2차원 


# 4. sigmoid 활성함수 적용 
def sig_fn(X):
    y_pred = linear_model(X)
    sig = tf.nn.sigmoid(y_pred) 
    return sig

# 5. 손실 함수 정의 : 손실계산식 수정 
def loss_fn() : #  인수 없음 
    sig = sig_fn(X) 
    loss = -tf.reduce_mean(Y*tf.math.log(sig)+(1-Y)*tf.math.log(1-sig))
    return loss


# 6. 최적화 객체 
opt = tf.optimizers.Adam(learning_rate=0.01)

# 7. 반복학습 
for step in range(2000):
    opt.minimize(loss=loss_fn, var_list=[w,b])
    
    # 10 배수 단위 출력
    if (step+1) % 200 == 0:
        print('step=',(step+1),",loss val =", loss_fn().numpy())
            
# 8. model 최적화 테스트
# cut off=0.5 적용 : T/F -> 1.0/0.0
print('='*30)
y_pred = tf.cast(sig_fn(X).numpy() > 0.5, dtype=tf.float32)

acc = accuracy_score(Y,y_pred)
print('accuracy =',acc)


report =classification_report(Y,y_pred)
print(report)




