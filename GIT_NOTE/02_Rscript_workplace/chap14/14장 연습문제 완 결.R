
#################################
## <제14장 연습문제>
################################# 

# 01. mpg 데이터 셋을 대상으로 7:3 비율로 학습데이터와 검정데이터로 각각 
# 샘플링한 후 각 단계별로 분류분석을 수행하시오.

# 조건) x,y 변수선택  
#       독립변수(설명변수) : displ + cyl + year 
#       종속변수(반응변수) : cty

library(rpart) # 분류모델 사용: 
#분류트리(y가 범주형),회귀트리(y가 연속형)
#-> 평가방법 
#분류트리: 혼동매트릭스(컨퓨전매트릭스), 
#회귀트리: MSE,RMSE,cor
library(ggplot2) # dataset 사용 
data(mpg)
str(mpg) 

# 단계1 : 학습데이터와 검정데이터 샘플링
# 2. 데이터 탐색 및 전처리 
idx<-sample(nrow(mpg),0.7*nrow(mpg))
train<-mpg[idx,]
test<-mpg[-idx,]


# 단계2 : 학습데이터 이용 분류모델 생성 
model1<-rpart(cty ~ displ + cyl + year, data=train)
model1#중요변수:displ

# 단계3 : 검정데이터 이용 예측치 생성 및 평가 
y_pred<-predict(model1,test)
y_true<-test$cty

cor(y_true,y_pred) #0.8854559
# 단계4 : 분류분석 결과 시각화
rpart.plot(model1)
prp(model1)

# 단계5 : 분류분석 결과 해설


# 02. weather 데이터를 이용하여 다음과 같은 단계별로 의사결정 트리 방식으로 분류분석을 수행하시오. 

# 조건1) rpart() 함수 이용 분류모델 생성 
# 조건2) y변수 : RainTomorrow, x변수 : Date와 RainToday 변수 제외한 나머지 변수로 분류모델 생성 
# 조건3) 모델의 시각화를 통해서 y에 가장 영향을 미치는 x변수 확인 
# 조건4) 비가 올 확률이 50% 이상이면 ‘Yes Rain’, 50% 미만이면 ‘No Rain’으로 범주화

# 단계1 : 데이터 가져오기
library(rpart) # model 생성 
library(rpart.plot) # 분류트리 시각화 

setwd("c:/ITWILL/2_Rwork/data")
weather = read.csv("weather.csv", header=TRUE) 
str(weather)

# 단계2 : 데이터 샘플링
weather.df<-weather[,c(-1,-14)]
x<-sample(nrow(weather.df),0.7*nrow(weather.df))
x
train<-weather.df[x,]
test<-weather.df[-x,]
dim(train) 
dim(test) 

# 단계3 : 분류모델 생성
model2<-rpart(RainTomorrow ~., data= train)
model2


# 단계4 : 분류모델 시각화 - 중요변수 확인
model2#Humidity
                            
# 단계5 : 예측 확률 범주화('Yes Rain', 'No Rain')
y_pred<-predict(model2,test)
y_pred
y_pred2<-ifelse(y_pred[,2]>=0.5,'Yes Rain','No Rain')
y_pred2
                            
y_true<-test$RainTomorrow
y_true
                            
tab<-table(y_true,y_pred2)
tab
                            
acc<-(tab[1,1]+tab[2,2])/sum(tab)
acc#0.8181818
# 단계6 : 혼돈 matrix 생성 및 분류 정확도 구하기
install.packages("gmodels") # gmodels 패키지 설치
library(gmodels) # CrossTable() 함수 사용
                            
CrossTable(x=y_true,y=y_pred2)
                            
                            
                            