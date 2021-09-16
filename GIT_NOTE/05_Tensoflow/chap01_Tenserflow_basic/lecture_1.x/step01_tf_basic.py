# -*- coding: utf-8 -*-
"""
step01_tf_basic.py

- 폴더 작성 : 탐색기
- 패키지와 모듈 작성 : spyder

- Python code vs Tensorflow code
- 상수 정의, 식 정의
"""

#.Pyhthon code
x = 10
y = 25.3
z = x+y

print('z=', z) # z= 35.3



# Tensorflow code
import tensorflow.compat.v1 as tf # ver1.x -> ver2.x 마이그레이션
tf. disable_v2_behavior() #ver2.x 사용 안함

# ver1 때에는 탄소플로는 모델 구성하는 거랑 모델 실행하는 것(할당이 필요)이 구분되어있다. 
''' 프로그램 정의 영역: 모델 구성 '''
# 상수 정의
string = tf.constant('string const') # 문자 상수
x=tf.constant(10) # 문자 상수
y=tf.constant(20) # 문자 상수
print('x=',x)#x= Tensor("Const_1:0", shape=(), dtype=int32)
print('y=',y)#y= Tensor("Const_2:0", shape=(), dtype=int32)
# 식 정의
z=tf.add(x,y) # z = x + y
print('z=',z) #z= Tensor("Add:0", shape=(), dtype=int32)
'''
grapth=node(+) + edge(x,y)
'''


'''프로그램 실행 영역: 모델 실행'''
sess = tf.Session() # cpu, gpu 할당

print('x=', sess.run(x)) # 상수 -> 처리기 할당 -> 상수 값 할당
#x= 10
print('y=',sess.run(y))
#y= 20

# 2개 이상 상수 할당
print(sess.run([x,y])) # [10, 20]
print('z=', sess.run(z)) # 식-> 처리기 할당 -> 연산
#z= 30

sess.close() # 세션 객체 닫기







































