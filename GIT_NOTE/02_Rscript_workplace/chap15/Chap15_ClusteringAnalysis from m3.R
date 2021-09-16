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
#1.분류모델:kNN
#2.군집분석:kMeans
#3.추천모델:user or item 간 유사도 계산
#4.좌표 거리계산: 위도와 경도

################################################################
#### 1. 분류모델: kNN
################################################################

#1)dataset 생성:iris
idx<-sample(x=nrow(iris),size=nrow(iris)*0.7)
group <-iris[idx, ] #알려진 집단
test<-iris[-idx,]#알려지지 않은 집단 (분류대상)

dim(group) # 105   5
table(group$Species)
# setosa versicolor  virginica 
#   41         31         33 
dim(test) # 45 5

# 2)x,y변수 선정
group_x<-group[1:4] # 거리계산 ->2차원
group_y<- group$Species #집단 ->1차원

test_x<-test[1:4]# 거리계산
test_y<- test$Species#집단


#3) kNN 모델
library(class)
knn_model<-knn(group_x,test_x, group_y) #모델
knn_model #예측치


#모델 평가
table(test_y,knn_model)
#                      knn_model
# test_y       setosa versicolor virginica
# setosa          9          0         0
# versicolor      0         18         1
# virginica       0          1        16


###################################################################
####### 4.좌표 거리계산: 위도와 경도
###################################################################

#1) 서울 시청 위도/ 경도 찾기
seoul_lat<-37.541 #위도
seoul_lon<-126.986 #경도

#2) 서울지역 대학교 파일
university<-read.csv(file.choose()) #university.csv
university

#3) 유클리드 거리계산식 적용": sqrt(sum((위도-경도)^2))
distance<-sqrt((seoul_lat-university$LAT)^2 +(seoul_lon-university$LON)^2)
distance

min(distance)# 0.02238244
idx<-which(distance==min(distance))
university$학교명[idx] #"동국대학교"


########################################################################################
# 2. 계층적 군집분석(탐색적 분석)
# - 계층적 군집분석(Hierarchical Clustering)
# - 거리가 가장 가까운 대상부터 결합하여 나무모양의 
#   계층구조를 상향식(Bottom-up)으로 만들어가면서 군집을 형성 

# (1) 군집분석(Clustering)분석을 위한 패키지 설치
install.packages("cluster") # hclust() : 계층적 클러스터 함수 제공
library(cluster) # 일반적으로 3~10개 그룹핑이 적정

# (2) 데이터 셋 생성
r <- runif(15, min = 1, max = 50)
x <- matrix(r, nrow=5, by=T) 
x

# (3) matrix 대상 유클리드 거리 생성 함수
dis <- dist(x, method="euclidean") # method 생략가능
dis

# (4) 계층적 군집분석: 유클리드 거리 matrix를 이용한 클러스터링
hc <-  hclust(dis, method="complete") # 완전결합기준

# 군집 방법(Cluster method) 
# method = "complete" : 완전결합기준(최대거리 이용) <- default(생략 시)
# method = "single" : 단순결합기준(최소거리 이용) 
# method = "average" : 평균결합기준(평균거리 이용) 

help(hclust)
plot(hc,hang=-1) # 클러스터 플로팅(Dendrogram) -> 1과2 군집(클러스터) 형성
#hang=-1 : y=0

#####################################################################################
#<실습> 중1학년 신체검사 결과 군집분석
#---------------------------------------------
body <- read.csv("c:/ITWILL/2_Rwork/data/bodycheck.csv")
names(body)
dim(body)
body<-body[-1] #번호는 제외외
idist <- dist(body)#1.거리계산
idist

hc <- hclust(idist) #2. 군집분석

plot(hc, hang=-1) # 음수값 제외


# 3개 그룹 선정, 선 색 지정
rect.hclust(hc, k=3, border="red") # 3개 그룹 선정, 선 색 지정

#4. 군집별 특성분석
# (1)각 그룹별 서브셋 만들기
g1<- subset(body[c(10,4,8,1,15),])
g2<- subset(body[c(11,3,5,6,14),])
g3<- subset(body[c(2,9,13,7,12),])

# (2)각 그룹별 특성 분석
summary(g1)
# Mean   :25.6   Mean   :149.8   Mean   :36.6   Mean   :1    안경유무 1
summary(g2)
#Mean   :33.8   Mean   :161.2   Mean   :48.8   Mean   :1.4   안경유무 (1,2)
summary(g3)
#Mean   :40.6   Mean   :158.8   Mean   :56.8   Mean   :2     안경유무 2


#OR

#cutree 이용한 군집별 특성분석
# 형식) cutree(계층형군집결과, k=군집수) 
g_num<- cutree(hc, k=3) # stats 패키지 제공
g_num #1~3 

#(1)각 그룹별 서브셋 만들기
table(g_num)
# 1 2 3 ->그룹수
# 5 5 5-> 빈도수

g1<-which(g_num==1)
g2<-which(g_num==2)
g3<-which(g_num==3)

g1 #1  4  8 10 15
g2 #2  7  9 12 13
g3 #3  5  6 11 14
# (2)각 그룹별 특성 분석
summary(body[g1,])# Mean   :25.6   Mean   :149.8   Mean   :36.6   안경유무(mean)  :1
summary(body[g2,])
summary(body[g3,])

# 3. 계층형 군집분석과 군집 자르기 

# 1) 유클리드 거리 계산 
names(iris[1:4])#"Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width"  4개의 변수를 가지고 거리 계산
dist_re <- dist(iris[1:4]) # dist(iris[, -5])
dist_re

# 2) 계층형 군집분석(클러스터링)
hc <- hclust(dist_re)

#(3)군집분석 시각화:덴드로그램
plot(hc, hang=-1)
rect.hclust(hc, k=3, border="red") # 3개 그룹수 

# 3) 그룹수 만들기 : cutree()함수 -> 각 군집별로 군집 자르기
# 형식) cutree(계층형군집결과, k=군집수) 
ghc<- cutree(hc, k=3) # stats 패키지 제공
ghc 

table(ghc)
#  1  2  3 
# 50 72 28 



#row dataset 군집수 추가 
iris$ghc<-ghc
head(iris)
tail(iris)

#각 군집별 subset
g1<-subset(iris,ghc==1)
g2<-subset(iris,ghc==2)
g3<-subset(iris,ghc==3)

#각 군집별 특성분석
summary(g1)  
# Mean   :5.006   Mean   :3.428   Mean   :1.462   Mean   :0.246
summary(g2)
# Mean   :6.546   Mean   :2.964   Mean   :5.274   Mean   :1.85
summary(g3)
# Mean   :5.532   Mean   :2.636   Mean   :3.961   Mean   :1.229 



#####################################################################################
# 4. 비계층적 군집분석(확인적 분석)
# - 군집 수를 알고 있는 경우 이용하는 군집분석 방법

# 군집분석 종류 : 계층적 군집분석(탐색적), 비계층적 군집분석(확인적) 

# 1) data set 준비 
library(ggplot2)
data(diamonds)

nrow(diamonds) # [1] 53940
t <- sample(nrow(diamonds),1000) # 1000개 셈플링 

test <- diamonds[t, ] # 1000개 표본 추출
dim(test) # [1] 1000 10
test

# 데이터프레임 변환 
test_df <- as.data.frame(test)
head(test_df) # 검정 데이터
mydia <- test_df[c("price","carat", "depth", "table")] # 4개 칼럼만 선정
head(mydia)

# 2) 비계층적 군집분석(확인적 분석) - kmeans()함수 이용
# - 확인적 군집분석 : 군집의 수를 알고 있는 경우
model <- kmeans(mydia, 3)
model 
# K-means clustering with 3 clusters of sizes 302, 95, 603 - 군집수 
# Cluster means: 클러스터별 변수의 평균 
# Clustering vector: 1~3 클러스터 번호 
# Within cluster sum of squares by cluster: 각 군집내 응집도 
# Available components: 군집분석 결과의 구성요소(9개)

#모델 평가 척도
total_SS<-model$betweenss+model$tot.withinss
total_SS #17003735684
total_SS<-model$totss #군집간 분리도 (크면 좋은 모형)
total_SS #17003735684

between_SS<-model$betweenss
between_SS#15156651133
between_SS/total_SS #0.8913718

model$withinss # 각 군집 응집도 (작으면 좋은 모형)
model$tot.withinss #
model$size #군집수


#모델 정보 변수
model$cluster #1~3의 군집 
table(model$cluster)
# 1   2   3 
# 593 288 119 
model$centers #각각 의 군집에 중앙값
#     price     carat    depth    table
# 1  1460.981 0.4934401 61.71804 57.27234
# 2  5828.295 1.1290278 61.93924 57.83056
# 3 13343.471 1.7112605 61.78824 57.70504
modle$size #군집수
model$iter #반복수
 


# 3) 원형데이터에 군집수 추가
mydia$cluster <- model$cluster
head(mydia) # cluster 칼럼 확인 

#군집의 중앙값
model$centers

# 4) 변수 간의 상관성 보기 
plot(mydia[,-5])
cor(mydia[,-5], method="pearson") # 상관계수 보기 

#install.packages('corrgram')
library(corrgram) # 상관성 시각화 
corrgram(mydia[,-5], upper.panel=panel.conf) # 수치(상관계수) 추가(위쪽)


# 5) 비계층적 군집시각화
plot(mydia$carat, mydia$price, col=mydia$cluster)
# mydia$cluster 변수로 색상 지정(1,2,3)
#price-> 군집 분리도 공헌도 높다  (based on correlation value)<- 높으면 공헌도 높다.
#carat -> 군집 분리도 공헌도 낮다

# 각 그룹의 중심점에 포인트 추가 
points(model$centers[,c("carat", "price")], col=c(3,1,2), 
       pch=8, cex=5)
# names(result2) -> centers 칼럼 확인 
# col : color, pch : 중심점 문자, cex : 중심점 문자 크기
# pch(plotting character), cex(character expansion)


# 6) k-means model 시각화 
install.packages('factoextra')
library(factoextra)

fviz_cluster(model, data = mydia) #4개 차원 
#4개의 차원-> 2개 차원: 차원 축소(Dim1,Dim2)
#Dim1(56.9%):첫번째 차원의 공헌도 56.9% 
#Dim2(25.8%):두번째 차원의 공헌도 25.8% 

#cluster1:낮은 price군집
#cluster2:중간 price군집
#cluster3:높은 price군집

mydia[735,] #c1 cluster=1
mydia[179,] #c2 cluster=2
mydia[543,] #c3 cluster=3


############################
##군집수 찾기
############################

data(iris)

#data.fram-> matrix 
iris_max<-as.matrix(iris[-5])
dim(iris_max) #150   4

install.packages('NbClust')#군집수
library(NbClust)

?NbClust

nc <- NbClust(data = iris_max, distance = "euclidean", min.nc = 2, max.nc = 15, 
        method = 'complete', index = "all", alphaBeale = 0.1)

#                       ***** Conclusion *****                            
#   * According to the majority rule, the best number of clusters is  3 

names(nc)
# [1] "All.index"          "All.CriticalValues" "Best.nc"           
# [4] "Best.partition" 

table(nc$Best.nc[1,])
# 0  1  2  3  4  6 15 ->클러스터 
# 2  1  2 13  5  1  2 -> 빈도수
#빈도수가 클러스터 3이 가장 많다 그로 3개의 군집을 만드는 것이 가장 적절하다.

#BEST 클러스터 예측빈도
table(nc$Best.partition)
# 1  2  3 
# 50 72 28 










































