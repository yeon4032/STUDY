'''
 카이제곱 검정(chisquare test) ->독립성 검정
  - 확률변수의 적합성 검정 - 일원  (변수 하나)
  - 두 집단변수 간의 독립성 검정 - 이원 (변수 둘)
  - 검정통계량(기대비율) = sum( (관측값 - 기댓값)**2 / 기댓값 )
  - 검정통계량 채택역 : -1.96 ~ +1.96  
'''

from scipy import stats # 확률분포 검정 


# 1) 일원 chi-square(1개 변수 이용) : 적합성 검정 
# 귀무가설 : 관측치와 기대치는 차이가 없다.
# 대립가설 : 관측치와 기대치는 차이가 있다. 

#주사위 적합성 검정
real_data = [4, 6, 17, 16, 8, 9] # 관측치 - 관측도수
exp_data = [10,10,10,10,10,10] # 기대치 - 기대도수
chis = stats.chisquare(real_data, exp_data)
print(chis) # Power_divergenceResult(statistic=14.200000000000001, pvalue=0.014387678176921308)
print('statistic = %.3f, pvalue = %.3f'%(chis))  # statistic = 14.200, pvalue = 0.014
#해설: p-value is less than alph so reject H0 -> 게임에 적합하지 않다


'''
statistic(기대비율)=sum((관측값-기대값)**2/기댓값)
'''
import numpy as np
real_arr=np.array(real_data)
exp_arr=np.array(exp_data)

statis=sum((real_arr-exp_arr)**2/exp_arr)
print(statis)# 14.200000000000001

'''
statis:-1.96 ~+1.96 -> 채택역 
'''

# 2) 이원 chi-square(2개 변수 이용) : 교차행렬의 관측값과 기대값으로 검정
'''
 귀무가설 : 교육수준과 흡연율 간에 관련성이 없다.
 대립가설 : 교육수준과 흡연율 간에 관련성이 있다.
'''

# 파일 가져오기
import pandas as pd
import os
os.chdir('C:/ITWILL/4_python-ll/data')

smoke = pd.read_csv("smoke.csv")
smoke.info()

# <단계 1> 변수 선택 
print(smoke)# education, smoking 변수
education = smoke.education # smoke['education']
smoking = smoke.smoking # smoke['smoking']

# <단계 2> 교차분할표 
tab = pd.crosstab(index=education, columns=smoking)
print(tab) # 관측값 
'''
관측값
smoking     1   2   3
education            
1          51  92  68
2          22  21   9
3          43  28  21
'''

# <단계3> 카이제곱 검정 : 교차분할표 이용 
chi2, pvalue, df, evalue = stats.chi2_contingency(observed= tab) # 이원 chi-square 검정 
# contingency(컨틴젼시):부수적인(observed = 관측값 )
#df=(3-1)*(3-1) # (행수-1)*(열수-1)

# chi2 검정통계량, 유의확률, 자유도, 기대값  
print('chi2 = %.6f, pvalue = %.6f, d.f = %d'%(chi2, pvalue, df))
# chi2 = 18.910916, pvalue = 0.000818, d.f = 4
'''
(p <alph)
[해설] 유의미한 수준에서 교육수준과 흡연율 간에 관련성이 있다고 볼 수 있다. 
       기대치와 관찰치는 차이가 있다. 
'''


# <단계4> 기대값 
print(evalue)
'''
관측값
smoking     1   2   3
education            
1          51  92  68 -관측값
           69  84  58 -기대값
2          22  21   9 -관측값
           16  20  14 -기대값
3          43  28  21 -관측값
           30  36  25 -기대값

#기대값
[[68.94647887 83.8056338  58.24788732]
 [16.9915493  20.65352113 14.35492958]
 [30.06197183 36.54084507 25.3971831 ]]
'''

tab=pd.crosstab(index=education, columns=smoking, margins=True)
tab
'''
margins-> 합계정보 추가
smoking      1    2   3  All
education                   
1           51   92  68  211
2           22   21   9   52
3           43   28  21   92
All        116  141  98  355
'''

#기대값(evalue) 공식 = 행합계*열합계/총합 

'''
이원 chi2 기대비율= (기대비율)=sum((관측값ij-기대값ij)**2/기댓값ij)
'''
Ell_ratio =(51-68.94647887)**2/68.94647887 #4.6713930734394395
E33_ratio=(21-25.3971831)**2/25.3971831 #0.7613135338196465

