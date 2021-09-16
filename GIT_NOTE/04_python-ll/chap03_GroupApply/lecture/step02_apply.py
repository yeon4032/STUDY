# -*- coding: utf-8 -*-
"""
step02_apply.py

1.그룹 객체에 외부함수 적용
2.data 정규화
"""

#1.그룹 객체에 외부함수 적용

'''
apply() vs agg()
-공통점: 객체에 외부함수 적용
-차이점: 적용할 함수 개수 차이 (apply:1개,agg:다수)
'''

import seaborn as sn #load dataset

iris=sn.load_dataset('iris')
iris.info()

# 특정 칼럼 1개 대상 그룹 
#iris.groupby('집단변수')이였으나 but iris 의 특정 컬럼의 집단변수이용이용시 형식이 변한다. 
iris_grp=iris['sepal_length'].groupby(iris['species'])
iris_grp.size()
'''
species
setosa        50
versicolor    50
virginica     50
'''

#사용자 함수
def avg(group):
    return group.mean()

def diff(group):
    return group.max()-group.min()

#apply(함수)
iris_grp.apply(sum) # 내장함수
iris_grp.apply(avg) #사용자함수
iris_grp.apply(max) #내장함수
iris_grp.apply(min) #내장함수
iris_grp.apply(diff)#사용자함수

#agg([함수1,함수2,...])
agg_func = iris_grp.agg([sum, avg, max, diff])
agg_func

iris_grp.sum()
iris.mean()

#2.data 정규화: 특정 변수의 값을 일정한 범위로 조정(0~1, -1~1, mean=0, sd=1)
from numpy import min, max

#사용자 정의함수: 0~1 사이 정규화
def normal(x):
    return (x - min(x))/(max(x)-min(x))

x=[100,2000,5000]
#1)정규화 함수:1차원
nor=normal(x)
print(nor) #[0.        0.3877551     1.       ]

#2)자연 log 함수:1차원
import numpy as np
np.log(x) #밑수 e 
#[4.60517019, 7.60090246, 8.51719319]
#주의: 음수와 영-> 결측치(nan),무한대(-inf)




#2차원 data 정규화
iris_x = iris.iloc[:,:4] # 4개 변수 선택
iris_x.shape #(150, 4)
iris_x

iris_nor = iris_x.apply(normal)
iris_nor.head()

iris_x.agg(['var','mean','max','min'])


'''
그럼 2차원 데이터 정규화 랑 1차원 데이터 정규화의 차이는 없는 건가요?
-정규화 결과는 동일합니다. 단지 호출 방식에 따라서 차이가 있습니다.
-함수 이름을 직접 호출하는 방법과 apply 함수를 이용하여 호출하는 방식이 다릅니다.
-1차원 normal(x)
-2차원  apply(normal)

'''


























