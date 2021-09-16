'''  
문4) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
   <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정   
      iris.columns = iris.columns.str.replace('.', '_')   
   <조건2> model의 formula 구성 
      y변수 : 1번째 칼럼, x변수 : 2 ~ 3번째 칼럼       
   <조건3> 회귀계수 확인    
   <조건4> 회귀모델 결과 확인 및 해석  : summary()함수 이용 
'''

import pandas as pd
import os
from statsmodels.formula.api import ols # 함수
os.chdir('C:\\ITWILL\\4_python-ll\\data')


# dataset 가져오기  
iris = pd.read_csv('iris.csv')
print(iris.head())

# 1. iris 칼럼명 수정 

# 2. formula 구성 및 다중회귀모델 생성  


# 3. 회귀계수 확인 


# 4. 회귀모델 결과 확인 및 해석 


















































import pandas as pd
import statsmodels.formula.api as ols # 다중회귀모델 
import os

os.chdir('C:/ITWILL/4_python-ll/data')


# dataset 가져오기  
iris = pd.read_csv('iris.csv')
print(iris.head())

# 1. iris 칼럼명 수정 
iris.columns = iris.columns.str.replace('.', '_')  
iris

# 2. formula 구성 및 다중회귀모델 생성  
obj = ols(formula='Sepal_Length ~Sepal_Width + Petal_Length',data=iris)
model= obj.fit() # model 생성

# 3. 회귀계수 확인 
dir(model)
model.params
'''
Intercept       2.249140
Sepal_Width     0.595525
Petal_Length    0.471920
'''
# 4. 회귀모델 결과 확인 및 해석 
model.summary()
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           Sepal_Length   R-squared:                       0.840
Model:                            OLS   Adj. R-squared:                  0.838
Method:                 Least Squares   F-statistic:                     386.4
Date:                Mon, 21 Jun 2021   Prob (F-statistic):           2.93e-59
Time:                        16:06:32   Log-Likelihood:                -46.513
No. Observations:                 150   AIC:                             99.03
Df Residuals:                     147   BIC:                             108.1
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        2.2491      0.248      9.070      0.000       1.759       2.739
Sepal_Width      0.5955      0.069      8.590      0.000       0.459       0.733
Petal_Length     0.4719      0.017     27.569      0.000       0.438       0.506
==============================================================================
Omnibus:                        0.164   Durbin-Watson:                   2.021
Prob(Omnibus):                  0.921   Jarque-Bera (JB):                0.319
Skew:                          -0.044   Prob(JB):                        0.853
Kurtosis:                       2.792   Cond. No.                         48.3
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
#adj R^2f을 보면 회귀모델은 높은 정확도(84%)를 보인다.
#p-value(8.59e-62) <alph so reject H0
#모든 x변수는 y절편에 영향을 미친다
