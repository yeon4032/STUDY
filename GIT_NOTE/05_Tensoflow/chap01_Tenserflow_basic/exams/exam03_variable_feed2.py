'''
문2) 다음과 같이 변수를 선언하여 회귀방정식을 계산하시오.
    조건1> X변수 : placeholder()이용 [None행 3열] 배열 선언
       -> X변수 값 할당 : [[1,2,3]]
    조건2> a변수 : Variable()이용 정규분포를 따르는 난수 [3행1열]배열 선언
    조건3> b변수 : Variable()이용 정규분포를 따르는 난수 [1행1열] 배열 선언    
    조건4> 계산식 : expr = (X * a) + b (단, Tensorflow 함수 이용) 
    
<<출력 결과 예시>>
X:
[[ 1.  2.  3.]]
a:
[[-0.27396601]
 [-0.04671069]
 [-0.41434833]]
b:
[[-0.64448267]]
expr:
[[-0.91844869 -1.19241476 -1.46638072]
 [-0.69119334 -0.73790407 -0.78461474]
 [-1.05883098 -1.47317934 -1.8875277 ]]    
'''

import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

# X변수 정의
X = tf.placeholder(dtype=tf.float32, shape=[None,3]) # 오류인듯
expr = tf.placeholder(dtype=tf.float32,shape=[None, 3])

# a,b 변수 정의 
a = tf.Variable(tf.random_normal([3, 1])) 
b = tf.Variable(tf.random_normal([1, 1]))
mul = tf.Variable(tf.random_normal([1, 1]))
#식 정의
mul=tf.multiply(X,a)
expr=tf.add(mul,b)

# session object
with tf.Session() as sess :
    
    #X:
    #x_data = sess.run(tf.random_normal([1,3]))
    x_data=sess.run(tf.random_normal([1,3]))
    x_re = sess.run(X, feed_dict={X : x_data})
    print('X:',x_re)

    #a
    a_data = sess.run(tf.random_normal([3,1]))
    a_re = sess.run(a, feed_dict={a:a_data})
    print('a:',a_re)


    #b
    b_data = sess.run(tf.random_normal([1,1]))
    b_re = sess.run(b, feed_dict={b:b_data})
    print('b:', b_re)

##################################################333
    #mul
    mul_data={X : [-0.5318893  2.0016959 -1.4105812], a :[[-1.0149273] [-1.1693135] [ 0.6665173]]}
    mul_re = sess.run(mul,feed_dict = mul_data) 
    
    #expr
    expr_data ={a : x_re*a_re, b : b}
    expr_re = sess.run(mul,feed_dict = expr_data) #공급형 변수 에 값 넣기 실행후 넣은 값은 사라진다.
    print('expr:',expr_re)
   

