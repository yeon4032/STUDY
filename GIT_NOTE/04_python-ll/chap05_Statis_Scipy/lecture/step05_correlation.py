'''
공분산 vs 상관계수 
- 공통점 : 변수 간의 상관성 분석
 
1. 공분산 : 두 확률변수 간의 분산(평균에서 퍼짐 정도)를 나타내는 통계
 - 식 : Cov(X,Y) = sum( (X-xmu) * (Y-ymu) ) / n
 
 - Cov(X, Y) > 0 : X가 증가할 때 Y도 증가
 - Cov(X, Y) < 0 : X가 증가할 때 Y는 감소
 - Cov(X, Y) = 0 : 두 변수는 선형관계 아님(서로 독립적 관계) 
 - 문제점 : 값이 큰 변수에 영향을 받는다.(값 큰 변수가 상관성 높음)
    
2. 상관계수 : 공분산을 각각의 표준편차로 나눈어 정규화한 통계
   - 공분산 문제점 해결 
   - 부호는 공분산과 동일, 값은 절대값 1을 넘지 않음(-1 ~ 1)    
   - 식 : Corr(X, Y) = Cov(X,Y) / std(X) * std(Y)
'''


import pandas as pd 
import os 

os.chdir('C:/ITWILL/4_python-ll/data')
score_iq = pd.read_csv('score_iq.csv')
print(score_iq)
print(score_iq.head())


# 1. 피어슨 상관계수 행렬 
corr = score_iq.corr(method='pearson')
corr
corr['score']
'''
sid       -0.014399
score      1.000000
iq         0.882220
academy    0.896265
game      -0.298193
tv        -0.819752
'''
# 칼럼 기준 상관계수 
score_iq['score'].corr(score_iq['iq']) # 0.88222034461347
score_iq['score'].corr(score_iq['academy']) # 0.8962646792534938

 
# 2. 공분산 행렬 
cov = score_iq.cov()
print(cov)
# [해설] 공분산은 값이 큰 변수에 영향을 받는다.
cov['score']
'''
sid        -4.100671
score      42.968412
iq         51.337539
academy     7.119911
game       -2.890201
tv         -7.214586
'''

# 특정 칼럼 기준 
score_iq['score'].cov(score_iq['iq']) # 51.33753914988811
score_iq['score'].cov(score_iq['academy']) # 7.11991051454138


# 3. 공분산 vs 상관계수 식 적용 

#  1) 공분산 : Cov(X, Y) = sum((X - muX) * (Y - muY)) / n
X = score_iq['score']
Y = score_iq['iq']

# 표본평균 
muX = X.mean()
muY = Y.mean()

# 표본의 공분산 
Cov = sum((X - muX) * (Y - muY)) / (len(X)-1)
print('Cov =', Cov) # Cov = 51.33753914988811


# 2) 상관계수 : Corr(X, Y) = Cov(X, Y) / std(X) * std(Y)
stdX = X.std()
stdY = Y.std()

Corr = Cov / (stdX * stdY)
print('Corr =', Corr) # Corr = 0.8822203446134699


# exam02









