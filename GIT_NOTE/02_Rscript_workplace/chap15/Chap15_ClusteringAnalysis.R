#Chap15_ClusteringAnalysis


###################################################
# 군집분석(Clustering)
###################################################
# 유사성 거리에 의한 유사객체를 묶어준다.
# 거리를 측정하여 집단의 이질성과 동질성을 평가하고, 이를 통해서 
# 군집을 형성한다..
# 유사성 거리 : 유클리드 거리
# y변수가 없는 데이터 마이닝 기법
# 예) 몸, 키 관점에서 묶음 -> 3개 군집 <- 3개 군집의 특징 요약
# 주요 알고리즘 : hierarchical, k-means

# 그룹화를 통한 예측(그룹 특성 차이 분석-고객집단 이해)

# 1. 유클리드 거리
# 유클리드 거리(Euclidean distance)는 두 점 사이의 거리를 계산하는 
# 방법으로 이 거리를 이용하여 유클리드 공간을 정의한다.

# (1) matrix 생성
x <- matrix(1:9, nrow=3, by=T) 
x

# (2) matrix 대상 유클리드 거리 생성 함수
# 형식) dist(x, method="euclidean") -> x : numeric matrix, data frame
dist <- dist(x, method="euclidean") # method 생략가능
dist



# (3) 유클리드 거리 계산 식
# 관측대상 p와 q의 대응하는 변량값의 차의 제곱의 합에 sqrt 적용
#1행vs2행
distance<- sqrt(sum((x[1,]-x[2,])^2))
distance#5.196152 1행과 2행 거리

#1행vs3행
distance1<- sqrt(sum((x[1,]-x[3,])^2))
distance1# 10.3923 1행과 3행 거리



#(4)유클리드 거리 계산 식 활용분야
#1.분류모델
#2.군집분석
#3.추천모델
#
#
