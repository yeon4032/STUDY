# chap11_Correlation

##################################################
# chap11. 상관관계 분석(Correlation_Analysis)
##################################################
#-변수 간 관련성 분석
#-관련함수: cor(),cov(),cov2cor()
setwd('C:/ITWILL/2_Rwork/data')
product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

# 기술통계량
summary(product) # 요약통계량

sd(product$제품_친밀도); sd(product$제품_적절성); sd(product$제품_만족도)
# 변수 간의 상관관계 분석 

# 형식) cor(x,y, method) # x변수, y변수, method(pearson): 방법

# 1) 상관계수(coefficient of correlation) : 두 변량 X,Y 사이의 상관관계 정도를 나타내는 수치(계수)
cor(product$제품_친밀도, product$제품_적절성) # 0.4992086 -> 다소 높은 양의 상관관계
cor(product$제품_친밀도, product$제품_만족도) # 0.467145 -> 다소 높은 양의 상관관계

# 전체 변수 간 상관계수 보기 :상관계수 행렬
Cor<-cor(product, method="pearson") # 피어슨 상관계수 - default
Cor #상관계수 행렬
class(Cor) #matrix
Cor['제품_만족도',]

# 방향성 있는 색생으로 표현 - 동일 색상으로 그룹화 표시 및 색의 농도 
install.packages("corrgram")   
library(corrgram)
corrgram(product) # 색상 적용 - 동일 색상으로 그룹화 표시
corrgram(product, upper.panel=panel.conf) # 수치(상관계수) 추가(위쪽)
corrgram(product, lower.panel=panel.conf) # 수치(상관계수) 추가(아래쪽)
#or
install.packages('corrplot')
library(corrplot)
corrplot(Cor)

# 차트에 곡선과 별표 추가
install.packages("PerformanceAnalytics") 
library(PerformanceAnalytics) 

# 상관성,p값(*),정규분포 시각화 - 모수 검정 조건 
chart.Correlation(product, histogram=, pch="+") 

# spearman : 서열척도 대상 상관계수
#형식)cor(x,method="spearman")



# 2) 공분산(covariance) : 두 변량 X,Y의 관계를 나타내는 양
cor(product)
cov(product)

cov2cor(cov(product)) # 공분산 행렬 -> 상관계수 행렬 변환(기존 상관계수와 동일함) 


#3) 상관 계수 vs 공분산
#0.5463331 :제품_적절성(X) vs 제품_만족도 (Y) 
X<-product$'제품_적절성'
Y<-product$'제품_만족도'

X_mean<-mean(X)
Y_mean<-mean(Y)

#Cov(X,Y) = sum( (X-???????) * (Y-???????) ) / n
Cov_xy<-mean((X-X_mean)*(Y-Y_mean))
Cov_xy# 0.5442637

# (2)상관계수
#0.7668527:제품_적절성(X) vs 제품_만족도(Y)

Cor_xy <- Cov_xy/(sd(X)*sd(Y))
Cor_xy #0.7668527


#점수와 지능지수 관계 
score_iq<-read.csv('score_iq.csv')
head(score_iq)

# score vs iq(100단위) + academy(1단위)
cov(score_iq[2:4])
#           score        iq    academy
# score   42.968412 51.337539 7.119911
# iq      51.337539 78.807338 7.227293
# academy  7.119911  7.227293 1.468680

cor(score_iq[2:4])
#           score        iq    academy
# score   1.0000000 0.8822203 0.8962647
# iq      0.8822203 1.0000000 0.6717826
# academy 0.8962647 0.6717826 1.0000000

#cov의 문제점으로 인해 cov 에서 상관성이 월들이 높아 보인다. 그러나 cor 에서는 둘이 비슷하다.(academy가 더 높다)


#표준화:공식 z=(X-산술평균)/sigma
scale_score<-scale(score_iq) #mean=0,sd=1 로 마춘다. 
summary(scale_score)

Cov<-cov(scale_score)
Cov['score',] #0.88222034(cov(score,iq))  0.89626468 (cov(score,acadmey))

#표준화 시키고 난후에 공분산(cov)하면 상관계수(cor)과 같은 값이 나온다. 














































