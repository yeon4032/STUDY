'''
t검정 : t 분포에 대한 가설검정  
t 검정 유형 
  1. 한 집단 평균 검정: 모평균 검정
  2. 두 집단 평균 검정: 
  3. 대응 두 집단
'''

from scipy import stats # test
import numpy as np # sampling
import pandas as pd # csv file read

# 1. 한 집단 평균 검정 : 남자 평균 키(모평균) : 175.5cm -> 29명 표본추출 
#귀무가설: 모평균 175 cm와 차이가 없다.
#대립가설: 모평균 175 cm와 차이가 있다.
sample_data = np.random.uniform(172,179, size=29) #172~179 인 29 명
print(sample_data)
print(len(sample_data),'명') 

# 기술통계 
print('평균 키 =', sample_data.mean()) # np.mean

# 단일집단 평균차이 검정 
one_group_test = stats.ttest_1samp(sample_data, 175) #(sample,모평균(mu))
print('t검정 통계량 = %.3f, pvalue = %.5f'%(one_group_test))
# t검정 통계량 = -0.006(-1.96~1.96), pvalue = 0.99498


# 2. 두 집단 평균 검정 : 남여 평균 점수 차이 검정 
female_score = np.random.uniform(50, 100, size=30) # 여성 
male_score = np.random.uniform(45, 95, size=30) # 남성 

two_sample = stats.ttest_ind(female_score, male_score)
#(statistic=0.9260080405465926, pvalue=0.358278964123807)
print(two_sample)
print('두 집단 평균 차이 검정 = %.3f, pvalue = %.3f'%(two_sample))
#[해설] 두집단 간 평균 차이 없다

# file 자료 이용 
sample = pd.read_csv('C:/ITWILL/4_python-ll/data/two_sample.csv')
print(sample.info())

two_df = sample[['method', 'score']]
print(two_df)

# 교육방법 기준 subset
method1 = two_df[two_df.method==1] #방법1
method2 = two_df[two_df.method==2] #방법2

# score 칼럼 추출 
score1 = method1.score #방법1 ->점수
score2 = method2.score #방법2 ->점수

# 두 집단 평균차이 검정 
two_sample = stats.ttest_ind(score1, score2)
print(two_sample)
#Ttest_indResult(statistic=nan, pvalue=nan) -> 결측치 score1 or score2 안에 결측치가 있다.

#결측치 처리:nan-> 평균 대체
score1=score1.fillna(score1.mean())
score2=score2.fillna(score2.mean())

# 두 집단 평균차이 검정 
two_sample = stats.ttest_ind(score1, score2)
print(two_sample)
# Ttest_indResult(statistic=-0.9468624993102985, pvalue=0.34466920341921115)
#[해설] 두집단 간 평균 차이 없다

# 3. 대응 두 집단 : 복용전 65 -> 복용후 60 몸무게 변환  
before = np.random.randint(60, 65, size=30)  
after = np.random.randint(59, 64,  size=30) 

paired_sample = stats.ttest_rel(before, after)
print(paired_sample)
print('t검정 통계량 = %.5f, pvalue = %.5f'%paired_sample)
#t검정 통계량 = 2.89230, pvalue = 0.00718
#[해설] 두집단 간 평균 차이 없다.

before.mean()#61.96666666666667
after.mean()#60.96666666666667

#[헤설] 복용전과 복용후 몸무게 변화는 없다.
 






