# -*- coding: utf-8 -*-
"""
step06_regression.py

scipy 패키지 이용
1. 단순선형회귀분석
2. 다중선형회귀분석

"""

from scipy import stats # 선형회귀모델
import pandas as pd # csv fuke read
import os


os.chdir('C:/ITWILL/4_python-ll/data')
score_iq=pd.read_csv('score_iq.csv')
score_iq.head()
score_iq.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   sid      150 non-null    int64
 1   score    150 non-null    int64
 2   iq       150 non-null    int64
 3   academy  150 non-null    int64
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
'''

#1. 단순선형회귀분석
'''
x(독립변수) -> y(종속변수)
'''

#1) 변수 선택
x=score_iq['iq'] # 독립변수
y=score_iq['score']# 종속변수

#2) model 생성
model = stats.linregress(x,y) # y ~ x
print(model)
'''
LinregressResult(
    slope=0.6514309527270089,           -x 기울기
    intercept=-2.8564471221976504,      -y 절변
    rvalue=0.8822203446134709,          -설명력 (1에 가까울 수록 설명 잘한다)
    pvalue=2.8476895206666614e-50,      -F검정, 유의성 검정
    stderr=0.02857793440930536,         -표준오차
    intercept_stderr=3.546211918048528) - 
'''

a=model.slope # x 기울기
b=model.intercept # y절편

#관측치 1 개 대상 회귀 방정식-> y예측치
X=140
y = X*a+b # y=X*기울기 +절편
print('y=',y) # y= 88.3438862595836

# model 오차
Y=90
err=Y - y
print('err=',err) # err= 1.6561137404164015

#전체 관측치 대상
x=score_iq['iq'] # 독립변수
y=score_iq['score']# 종속변수

y_fit= (x*a)+b
len(y_fit) #150
y_fit#적합치 (예측치)
y#관측치

#관측치 vs 적합치
y.mean() #77.77333333333333
y_fit.mean() #77.77333333333334

y[:10] # 관측치 10개
y_fit[:10] # 예측치 10개 


# 2. 단순선형회귀분석 시각화
from pylab import plot, title, legend, show
'''
plot: 산점도
titile: 제목
legend: 범레
show:차트 보이기
'''

#산점도
plot(score_iq['iq'],score_iq['score'],'b.')
#회귀선
plot(score_iq['iq'], y_fit,'r-')
title('linear regression') # 제목추가
legend(['x y scatter','linear regression']) # 범례추가
show()



#3. 다중선형회귀분석: formula 형식:(y~x1+x2....)
'''
y~x1+x2+...
'''
from statsmodels.formula.api import ols # 함수

type(score_iq) #pandas.core.frame.DataFrame

#상관계수 행렬
corr=score_iq.corr()
print(corr)

'''
x=iq,academy,tv
y=score
'''

obj = ols(formula='score ~iq + academy + tv',data=score_iq)
model= obj.fit() # model 생성

#회귀분석 결과 제공
model.summary() 
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  score   R-squared:                       0.946
Model:                            OLS   Adj. R-squared:                  0.945 <- 설명력
Method:                 Least Squares   F-statistic:                     860.1 <- 크면 클수록 통계적으로 유의하다.
Date:                Mon, 21 Jun 2021   Prob (F-statistic):           1.50e-92 <- p_value
Time:                        15:06:31   Log-Likelihood:                -274.84
No. Observations:                 150   AIC:                             557.7
Df Residuals:                     146   BIC:                             569.7
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|         [0.025      0.975]
------------------------------------------------------------------------------
Intercept     24.7223      2.332     10.602      0.000         20.114      29.331
iq             0.3742      0.020     19.109      0.000 <-유의   0.335       0.413
academy        3.2088      0.367      8.733      0.000 <-유의   2.483       3.935     
tv             0.1926      0.303      0.636      0.526 <-유의x -0.406       0.791    <- tv는 y에 영향력이 없다.
==============================================================================
Omnibus:                       36.802   Durbin-Watson:                   1.905
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               57.833
Skew:                           1.252   Prob(JB):                     2.77e-13
Kurtosis:                       4.728   Cond. No.                     2.32e+03
==============================================================================

*기본 가정
x는 y에 영향력이 없다는 기본 가정이 있다. 그러나 iq 와 academy 는 pvalue가 alph 보다 작다 그럼으로 기본 가정이 기각된다.
즉 tv만 기본 가정이 기각되지 않고 나머지 두 변수는 기본 가정이 기각된다. 
'''
dir(model)

#회귀계수
model.params
'''
Intercept    24.722251 <- y절편
iq            0.374196 <- x1 기울기
academy       3.208802 <- x2 기울기
tv            0.192573 <- x3 기울기
dtype: float64
'''
#다중선형 회귀방정식
x1=140; x2=2; x3=0
y = x1*0.374196+x2*3.208802+x3*0.192573+24.722251
y #83.527295 (same as first y_fit)

#적합치(예측치)
y_fit = model.fittedvalues
y_fit
'''
0      83.527304
1      75.283280
2      73.604873
3      82.041469
4      64.783130
            : 
'''

#관측치(정답)
y_true = score_iq['score']
'''
0      90
1      75
2      77
3      83
4      65
       :
'''

#평균으로 적합치와 관측치 비교
y_fit.mean() #77.77333333333418
y_true.mean() # 77.77333333333333

#차트보기
import matplotlib.pyplot as plt

plt.plot(y_fit[:50], label='y fittedvalues')
plt.plot(y_true[:50], label='y real values')
plt.legend(loc='best')
plt.show()