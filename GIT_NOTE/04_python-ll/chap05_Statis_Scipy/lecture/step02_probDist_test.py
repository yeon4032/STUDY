# -*- coding: utf-8 -*-
"""
step02_probDist_test.py

확률분포와 검정(test)
 - 확률분포 : 확률 + 데이터 분포
     ex) 동전 1000번 시행 -> 앞(1) or 뒷 (0) 확률 (이산활률분포: 정수형) / 연속(소수점)
"""

'''
========================
Continuous distributions : 연속확률분포 
beta : 알파와 베타 구간의 연속확률분포
chi2 : 극단값을 허용하는 멱분포이며, 표본 수가 많을수록 대칭 모양을 갖는 분포 
f : 두 chi2분포를 각각의 자유도(d.f)로 나눈 비율을 나타낸 분포
norm : 정규분포, 좌우 대칭분포 (가우시안)
t : 표본수가 작은 경우(30개 미만) 정규분포 대신 사용하는분포
uniform : 균등하게 나타나는 확률분포

========================
Discrete distributions : 이산확률분포 
bernoulli(베루누이) : 이항 범주(성공 or 실패)를 갖는 이산확률분포 (독립시행 1번) 
binom(이항) : 이항 범주(성공 or 실패)를 갖는 이산확률분포 (독립시행 n번)  
geom(기하) : 최초 성공할 때 까지 실패한 횟수를 갖는 분포, 
poisson(포아송) : 특정한 사건의 발생 가능성이 매우 작은 확률분포((예 : 특정 시점에서 번개에 맞을 확률))
======================
'''

from scipy import stats # 확률분포 + 검정
import numpy as np # 분포곡선 vector data
import matplotlib.pyplot as plt # 정규분포 시각화

#1.정규분포와 검정(정규성 검정) # norm

# 1) 표준정규분포 객체 생성
mu,sigma=0,1
norm_obj=stats.norm(mu,sigma) #N(0,1)

#2) 확률변수 X: 시행룃수 N을 이용하여 정규분포의 확률변수 
N=1000 # sample 수
X_var=norm_obj.rvs(size=N) # N번 시뮬레이션하여 X_var=확률변수 생성 
# Random Variable sampling-> n 번 시뮬레이션을 하여 n개의 데이터를 모아 셈플로 만들어라.
print(X_var)

'''
obj=stats.class()
obj.rvs(N) # 표본추출 
'''

# 3) 확률분포 시각화 
from scipy.stats import norm # 확률밀도함수(pdf) 확률변수에 대한 크기 와 밀도 측정하고 그래프생성.

#분포곡선 vector생성
arr = np.arange(1, 5.5, 2)# 2:step
arr # arry([1.,3., 5.])
line = np.linspace(1, 5.5, 2) #2-> size(원소 2개 가지고오라) 
line # array([1. , 5.5])
line2 = np.linspace(1, 5.5, 3) #3-> size(원소 3개 가지고오라) 
line2 # array([1.  , 3.25, 5.5 ])

line3=np.linspace(min(X_var),max(X_var),100) # list 형식의 난수를 생성
line3

# 히스토그램 +활률밀도분포곡선
plt.hist(X_var,bins='auto', density=True) # 히스토그램
plt.plot(line3, norm.pdf(line3,mu,sigma),color='red') # 확률밀도분포곡선, norm.pdf(data,평균,편차)
plt.show()


# 4) 정규성 검정
# 귀뮈가설(H0):정규분포와 차이가 없다.

statistic, pvalue = stats.shapiro(X_var)                                    
print('검정통계량=',statistic)
#검정통계량= 0.9983817934989929
print('유의확률=',pvalue)
#유의확률= 0.47987085580825806 >알파 (0.05) so accept H0.

alpha=0.05 # 유의수준(알파)

if pvalue >= alpha:
    print('정규분포와 차이가 없다-가설 채택')
else:
    print('정규분포와 차이가 있다.-가설 기각')

#정규분포와 차이가 없다-가설 채택


# 2. 이향분포와 검정(이항검정)
# - 이항분포를 이용한 가설검정
# - 이항분포 : 2가지 범주(성공(1) or 실패(0))를 갖는 이산확률분포

#이항분포: 베르누이분포, 이항분포

'''
공통점
베르누이분포, 이항분포는 둘다 이항분포이다 그래서 2가지 범주(성공(1) or 실패(0))를 갖는다.

차이점
베르누이분포:B(N=1,P) -> 모수 - P:성공확률 -> 베르누이 시행 (한번시행) -> 1번 시행한거
이항분포:B(N=n,P) -> N:시행횟수, P:성공확률 (n 번시행) -> 베르누이 시행을 n 번 시행한 확률분포
'''

# 1) 이항분포 객체 생성

# (1)동전 확률시험 : 베르누이분포(p=0.5) # n=1 은 생략됨
ber_obj=stats.bernoulli(p=0.5) # 1. 객체 생성
sample1=ber_obj.rvs(size=10) # 2.표본 10개 추출
print(sample1) #[1 1 1 1 1 1 0 0 1 1]

# 객체 + 표본추출 (위의 두단계 하나로 합친것)
sample1 = stats.bernoulli.rvs(p=0.5,size=10)
print(sample1) #[0 1 1 0 1 1 0 1 0 1]


# (2)동전 확률시험 : 이항분포(n=1번,p=0.5)
bin_obj = stats.binom(n=1, p=0.5) # 1. 객체 생성
sample2 = bin_obj.rvs(size = 10) # 표본 10개 추출
print(sample2) #[1 1 1 0 0 1 0 1 1 1]

# (3)동전 확률시험 : 이항분포(n=10번,p=0.5)
bin_obj = stats.binom(n=10, p=0.5) # 1. 객체 생성
sample2 = bin_obj.rvs(size = 10) # 표본 10개 추출
print(sample2) #[6 6 9 6 7 4 8 7 3 3] 6이란 10번 던져서 6번 성공함(앞면이 성공)

# (3)객체 + 표본추출  (이항분포(n=5번,p=0.5))
sample3=stats.binom.rvs(n=5, p=0.5,size=10)
print(sample3) #[2 2 2 2 4 1 2 1 4 3]

# (4) 주사위 확률시험: 이항분포 (n=10,p=1/6)
sample4 = stats.binom.rvs(n=10,p=1/6,size = 10)
print(sample4) #[1 1 1 2 1 1 3 0 1 2]
# 독립시행 10번으로 특정 눈금이 나올 성공횟수

# 2) 이항 검정(binom test): 이항분포에 대한 가설검정
'''
연구환경: 게임에 이길 확률(P) 40% 일때, 게임을 100번 한 경우
        95% 신뢰수준에서 검정
귀무가설: 게임에 이길 확률(P) 40%와 차이가 없다.
'''

# 단계1: 표본추출(100개)
p = 0.4 # 모수(p)

# 이항분포 -> 표본 추출
X_var = stats.binom.rvs(n=1,p=0.4,size=100)
print(X_var)

# 성공횟수 
x = np.count_nonzero(X_var) #38
print('성공횟수=',x) # 성공횟수= 38

n=100 # 시행횟수 n >= x

#이항검정
pvlaue = stats.binom_test(x=43,n=100,p=0.4,alternative='two-sided')#양측검정
'''
x:성공횟수
n:시행횟수
p:성공확률
alternative =양측검정 or 단측검정
'''
if pvalue >= alpha:
    print('게임에 이길 확률(P) 40%와 차이가 없다.-가설 채택')
else:
    print('게임에 이길 확률(P) 40%와 차이가 있다..-가설 기각')

#게임에 이길 확률(P) 40%와 차이가 없다.-가설 채택

##############################################################################
##이항검정 example
##############################################################################33
'''
1.연구환경
    150명의 합격자 중에서 남자 합격자가 62명 일 때 99%신뢰수준에서
    남여 합격률에 차이가 있다고 할수 있는가?
    
2.귀무가설: 남여 합격률에 차이가 없다. (p=0.5)
'''

x=62 #성공횟수
n=150 #시행횟수

#이항검정
pvlaue = stats.binom_test(x=62,n=150,p=0.5,alternative='two-sided')#양측검정
print(pvlaue) #0.040868493866493945

alpha=0.01 #유의수준(알파) -> 99%신뢰수준 = 1-알파
if pvalue >= alpha:
    print('남여 합격률에 차이가 없다.-가설 채택')
else:
    print('남여 합격률에 차이가 있다.-가설 기각')

#남여 합격률에 차이가 없다.-가설 채택

































