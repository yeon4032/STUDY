'''
문) 다음 조건과 <출력 결과>를 참고하여 a와 b변수를 정의하고, 브로드캐스팅 연산을 
    수행한 결과를 출력하시오.
    <조건1> a변수 : list 이용 
    <조건2> b변수 : Variable() 이용
    <조건3> c변수 계산식 : c = a * b 
         -> multiply()이용 
    <조건4> a,b,c변수 결과 출력     

< 출력 결과 > 
a= [ 1.  2.  3.] 
b= [[ 0.123]     
    [ 0.234]
    [ 0.345]]
    
c= [[ 0.123       0.24600001  0.36900002]  : 3x3
   [ 0.234       0.46799999  0.70200002]
   [ 0.345       0.69        1.03499997]]
'''

import tensorflow as tf

a = [ 1.,  2.,  3.]
print(a)


b=tf.Variable([[ 0.123],[ 0.234],[0.345]])
print(b.numpy())

c = a * b 
print('c=',c.numpy())
print(c.get_shape()) #(3, 3)
# or
c2=tf.math.multiply(x=a, y=b)
print(c2.numpy())









