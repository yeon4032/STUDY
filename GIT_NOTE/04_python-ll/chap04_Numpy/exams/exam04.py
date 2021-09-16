'''
문4) 다음 같은 입력 x와 가중치 w를 이용하여 hidden node를 구하시오.  
    <조건1> w(3,3) * x(3,1) = h(3,1)  
    <조건2> weight : 표준정규분포 난수  -9개
    <조건3> X : 1,2,3    -3개
'''

import numpy as np

print('weight data')
w=np.random.normal(0,1,(3,3))
w.shape
print('x data')
x=np.array([[1],[2],[3]])

print('hidden')
h=w@x
h






