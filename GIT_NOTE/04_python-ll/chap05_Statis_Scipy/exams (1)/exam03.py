'''
문3) score 데이터셋을 이용하여 단순선형회귀모델을 이용하여 가설검정으로 수행하시오.

   귀무가설 : academy는 score에 영향을 미치지 않는다.
   대립가설 : academy는 score에 영향을 미친다.

   <조건1> y변수 : score, x변수 : academy      
   <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
   <조건3> 회귀선 적용 시각화 
'''

from scipy import stats
import pandas as pd
import os

os.chdir('C:\\ITWILL\\4_python-ll\\data')

# dataset 가져오기 
score = pd.read_csv('score_iq.csv')
print(score.info())
print(score.head())

# 1. x,y 변수 선택

# 2. 단순 선형회귀분석(stats)

# 3. 회귀선 시각화  
from scipy import polyval
from pylab import plot, title, legend, show

















































from scipy import stats
import pandas as pd
import os

os.chdir('C:/ITWILL/4_python-ll/data')

# dataset 가져오기 
score = pd.read_csv('score_iq.csv')
print(score.info())
print(score.head())

# 1. x,y 변수 선택
y=score['score']
x=score['academy']

# 2. 단순 선형회귀분석(stats)
model = stats.linregress(x,y) # y ~ x
print(model)
'''
LinregressResult(slope=4.847829398324453,
                 intercept=68.2392688499619,
                 rvalue=0.8962646792534947,
                 pvalue=4.036716755165522e-54,
                 stderr=0.19719368077532942,
                 intercept_stderr=0.45511458515001313)
'''
# 3. 회귀선 시각화  
from scipy import polyval
from pylab import plot, title, legend, show

a=model.slope # x 기울기
b=model.intercept # y절편
y_pred= (x*a)+b # 예측치

#시각화
#산점도
plot(x,y,'b.')
#회귀선
plot(x, y_pred,'r-') # y는안되는 건지?
title('linear regression') # 제목추가
legend(['x y scatter','linear regression']) # 범례추가
show()
