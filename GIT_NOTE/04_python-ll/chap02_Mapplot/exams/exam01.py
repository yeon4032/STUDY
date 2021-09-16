'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 5번 칼럼으로 색상 적용
            힌트) plt.scatter(x, y, c) 
'''

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np #별칭 -수치  data 생성


#<조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
os.chdir('C:/ITWILL/4_python-ll/data')
iris=pd.read_csv('iris.csv')
iris.info()


#<조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
plt.scatter(iris['Sepal.Length'],iris['Petal.Length'])
plt.show()






#<조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 5번 칼럼으로 색상 적용
#힌트) plt.scatter(x, y, c) 
dummy=pd.get_dummies(iris['Species'])
arr=np.array(dummy)
decoding=np.argmax(arr,axis=1)
decoding

plt.scatter(x=iris['Sepal.Length'],y=iris['Petal.Length'],c=decoding)
plt.show()





























#<조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
os.chdir('C:/ITWILL/4_python-ll/data')
iris = pd.read_csv('iris.csv')
iris

#<조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
data1=iris['Sepal.Length']
data2=iris['Petal.Length']

plt.scatter(data1,data2)
plt.show()

#<조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 5번 칼럼으로 색상 적용
#2진수
dummy=pd.get_dummies(iris['Species'])
print(dummy)

#pandas-> numpy
arr=np.array(dummy)


#10시수 변환
decoding=np.argmax(arr,axis=1)
decoding


plt.scatter(x = data1,y = data2,c = decoding)
plt.show()



