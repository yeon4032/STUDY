#chap17_RandomForest

##################################################
#randomForest
##################################################
# 결정트리(Decision tree)에서 파생된 모델 
# 랜덤포레스트는 앙상블 학습기법을 사용한 모델
# 앙상블 학습 : 새로운 데이터에 대해서 여러 개의 Tree로 학습한 다음, 
# 학습 결과들을 종합해서 예측하는 모델(PPT 참고)
# DT보다 성능 향상, 과적합 문제를 해결


install.packages('randomForest')
library(randomForest) # randomForest()함수 제공 

data(iris)
str(iris)

# 1. 랜덤 포레스트 모델 생성 
# 형식) randomForest(y ~ x, data, ntree=500, mtry)
#ntree:생성할 tree 개수(기본 500개)
#mtry:설명변수의 개수 (분류트리sqrt(p) or 회귀트리:p/3) p는 변수 개수(x 개수)
mtry=sqrt(4)
#na.action:결측치 처리

#train/test split 과정없음
model = randomForest(Species~., data=iris, 
                     ntree=500, mtry=2,  na.action=na.omit)  
model
# ntree = 500 ->트리개수
# No. of variables tried at each split: 2 -> 설명변수 개수
# OOB estimate of  error rate: 5.33%

# Confusion matrix:
#   setosa versicolor virginica class.error
# setosa         50          0         0        0.00
# versicolor      0         47         3        0.06
# virginica       0          5        45        0.10

acc<-(50+47+45)/nrow(iris)
acc # 0.9466667 (1-err rate)

# 2. model 정보 확인 
names(model) # 19컬럼 제공 

#y예측치
model$predicted

#model 에러율 (500 개 트리하나하나의 오차 정보)
model$err.rate
dim(model$err.rate) #500   4

#OOB setosa versicolor  virginica
err<-model$err.rate
mean(err[,1])#OOB->0.05324401

#혼동행렬
con <- model$confusion

acc<-(con[1,1]+con[2,2]+con[3,3])/sum(con)
acc
err_rate<-1-acc
err_rate

#중요변수 정보
model$importance
#                MeanDecreaseGini
# Sepal.Length         9.144029
# Sepal.Width          2.245358
# Petal.Length        41.489969
# Petal.Width         46.384725

# 3. 중요 변수 생성  
model2 = randomForest(Species ~ ., data=iris, 
                      ntree=500, mtry=2, 
                      importance = T,
                      na.action=na.omit )
model2 

importance(model2)
#               setosa versicolor virginica  MeanDecreaseAccuracy  MeanDecreaseGini
# Sepal.Length  7.47021   8.078324 10.071664            12.124141        11.059597
# Sepal.Width   5.00220   1.072013  2.661823             4.471839         2.425592
# Petal.Length 21.70019  32.611679 27.447821            33.268227        42.275996
# Petal.Width  22.89791  30.408526 30.678634            33.195460        43.474621

#MeanDecreaseAccuracy:분류정확도 개선의 공헌도
#MeanDecreaseGini: 노드 불순도(불확실성) 개선의 공헌도

#시각화
varImpPlot(model2)


################################
## 회귀트리(y변수 : 비율척도)
################################
library(MASS)
data("Boston")
str(Boston)
#crim : 도시 1인당 범죄율 
#zn : 25,000 평방피트를 초과하는 거주지역 비율
#indus : 비상업지역이 점유하고 있는 토지 비율  
#chas : 찰스강에 대한 더미변수(1:강의 경계 위치, 0:아닌 경우)
#nox : 10ppm 당 농축 일산화질소 
#rm : 주택 1가구당 평균 방의 개수 
#age : 1940년 이전에 건축된 소유주택 비율 
#dis : 5개 보스턴 직업센터까지의 접근성 지수  
#rad : 고속도로 접근성 지수 
#tax : 10,000 달러 당 재산세율 
#ptratio : 도시별 학생/교사 비율 
#black : 자치 도시별 흑인 비율 
#lstat : 하위계층 비율 
#medv(y) : 소유 주택가격 중앙값 (단위 : $1,000)

p<- 13
mtry<-13/3 # 4.3333 so 4개 or 5개 설명변수

boston_model <- randomForest(medv ~ ., data = Boston,
                             mtree = 500, mtry = 5,
                             importance = T,
                             na.action=na.omit)

boston_model
#Number of trees: 500
#No. of variables tried at each split: 5

#Mean of squared residuals: 10.10571 -> MSE
#Var explained: 88.03 

names(boston_model)


pred<-boston_model$predicted
y_ture<-boston_model$y

err<-mean((y_ture-pred)^2) #MSE 값임
err#10.10571


# 중요변수 확인 
importance(boston_model)
#%IncMSE:
#IncNodePurity:
varImpPlot(boston_model)


################################
## 분류트리(y변수 : 범주형)
################################
titanic = read.csv(file.choose()) # titanic3.csv
str(titanic) 
# titanic3.csv 변수 설명
#'data.frame': 1309 obs. of 14 variables:
#1.pclass : 1, 2, 3등석 정보를 각각 1, 2, 3으로 저장
#2.survived : 생존 여부. survived(생존=1), dead(사망=0)
#3.name : 이름(제외)
#4.sex : 성별. female(여성), male(남성)
#5.age : 나이
#6.sibsp : 함께 탑승한 형제 또는 배우자의 수
#7.parch : 함께 탑승한 부모 또는 자녀의 수
#8.ticket : 티켓 번호(제외)
#9.fare : 티켓 요금
#10.cabin : 선실 번호(제외)
#11.embarked : 탑승한 곳. C(Cherbourg), Q(Queenstown), S(Southampton)
#12.boat     : (제외)Factor w/ 28 levels "","1","10","11",..: 13 4 1 1 1 14 3 1 28 1 ...
#13.body     : (제외)int  NA NA NA 135 NA NA NA NA NA 22 ...
#14.home.dest: (제외)


# 삭제 칼럼 : 3, 8, 10, 12~14
df <- titanic[, -c(3, 8, 10, 12:14)]

dim(df)  # 1309    8 

mtry<-sqrt(7) #2.645751
mtry # 2~4

names(df)
str(df) # survived: int  1 1 0 0 0 1 1 0 1 0 ...
#회귀분석이 아님으로 y변수로 쓸 변수는 factor 형으로 변환 해야됨

#y 변수 Factor형 변환
df$survived<-factor(df$survived)
str(df)

titanic_model<- randomForest(survived~., data=df,ntree=500,mtry=3,importance=T,
                             na.action=na.omit)
titanic_model
# randomForest(formula = survived ~ ., data = df, ntree = 500,      mtry = 3, importance = T, na.action = na.omit) 
# Type of random forest: classification
# Number of trees: 500
# No. of variables tried at each split: 3
# 
# OOB estimate of  error rate: 20.29%
# Confusion matrix:
#   0   1 class.error
# 0 541  77   0.1245955
# 1 135 292   0.3161593

#컨퓨젼 매트릭스와 정확도 오류
con<-titanic_model$confusion
con

acc<-(con[1,1]+con[2,2])/sum(con)
acc #0.7967931

err_rate1<-1-acc
err_rate1#0.2032069


#중요변수
varImpPlot(titanic_model)
#sex>pclass>fare>age 분류정확도 기여 변수 중요도
#sex>fare>age>pclass 



















