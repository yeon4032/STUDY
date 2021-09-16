# chap13_Logistic Regression

# 1. 로짓 변환 : y값을 0 ~ 1로 조정하는 과정 

# 단계1 : 오즈비(Odds ratio) : [실패(0)에 대한] 성공(1) 비율(0:fail, 1:success)
# ex) Odds of ten to one -> 10대 1의 배당률(성공 비율 1/10) 
p = 0.5 # success
1 - p # fail
odds_ratio = p / (1-p) 


# 단계2 : 로짓변환 : 오즈비에 log 적용 
p = 0.5 # 성공 50%
odds_ratio = p / (1-p) 
logit1 = log(odds_ratio) 

p = 1 # 성공 100% 
odds_ratio = p / (1-p)  
logit2 = log(odds_ratio)

# 단계3 : 시그모이드 함수 
# sigmoid_function = (1 / (1 + exp(-로짓값)))
1 / (1 + exp(-(logit1))) # logit=0 -> 0.5
1 / (1 + exp(-(logit2))) # logit=Inf -> 1

# 로지스틱 회귀분석(Logistic Regression) 모델 

# 단계1. 데이터 가져오기 
setwd('C:/itwill/2_Rwork/data')
weather = read.csv("weather.csv") 
dim(weather)  # 366  15
head(weather)
str(weather)

# chr 칼럼, Date, RainToday 칼럼 제거 
weather_df <- weather[, c(-1, -6, -8, -14)]
str(weather_df)

# RainTomorrow 칼럼 -> 로지스틱 회귀분석 결과(0,1)에 맞게 더미변수 생성      
weather_df$RainTomorrow[weather_df$RainTomorrow=='Yes'] <- 1
weather_df$RainTomorrow[weather_df$RainTomorrow=='No'] <- 0
weather_df$RainTomorrow <- as.numeric(weather_df$RainTomorrow)
head(weather_df)


#  단계2.  데이터 셈플링
idx <- sample(nrow(weather_df), nrow(weather_df)*0.7)
train <- weather_df[idx, ]
test <- weather_df[-idx, ]


#  단계3.  로지스틱  회귀모델 생성 : 학습데이터 
weater_model <- glm(RainTomorrow ~ ., data = train, family = 'binomial')
weater_model 
summary(weater_model) 

# 단계4. 로지스틱  회귀모델 예측치 생성 : 검정데이터 
# newdata=test : 새로운 데이터 셋, type="response" : 0~1 확률값으로 예측 
pred <- predict(weater_model, newdata=test, type="response")  
pred 
summary(pred)
str(pred)

#cutofff=0.5
y_pred<-ifelse(pred>0.5,1,0)
y_true<-test$RainTomorrow

#5단계 model평가
tab<-table(y_pred,y_true)
tab
#         y_true
# y_pred  0  1
#    0   90  6 90/96 ->0.9375
#    1   2  11  2/13 ->0.1538462

prop.table(table(y_true)) # 0.8454545 0.1545455 

# 분류정확도
acc<-(tab[1,1]+tab[2,2])/sum(tab)
cat('accuracy=', acc) # 0.9266055

#2)정확률(precision):model(yes)->YES
p<-tab[2,2]/sum(tab[,2])
p #0.6470588

#3)재현율(민감도,recall):read(yes)->Yes
r<-tab[2,2]/sum(tab[2,])
r# 0.8461538

#4) 특이도 :real(NO)->NO
s<-tab[1,1]/sum(tab[1,])
s#0.9375

#5) f1 score
f1<-2*((p*r)/(p+r))
f1 #0.7333333


### ROC Curve를 이용한 모형평가(분류정확도)  ####
# Receiver Operating Characteristic
install.packages("ROCR")
library(ROCR)

# ROCR 패키지 제공 함수 : prediction() -> performance
pr <- prediction(pred, test$RainTomorrow) #(예측치, 관측치)
#에러: 'predictions' contains NA.
#결측지 확인
summary(pred)
length(pred) #110

#결측치 찾기
which(is.na(pred))
# 349 <-행번호
# 105 <-index

#결측치 제거
#re_pred<-pred[-c(65,79,87)] -결측치가 여러개인 경우
re_pred<-pred[-105] #예측치에서 제거
length(re_pred) #109

y_true<-test$RainTomorrow[-105] #관측치에서 제거

pr<-prediction(re_pred,y_true)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)


##################################################################3
#######다항형 로지스틱 회귀분석: nnet
##################################################################

install.packages('nnet')
library(nnet)

unique(iris$Species) #setosa versicolor virginica 

#70vs30
idx<-sample(1:nrow(iris),0.7*nrow(iris)) #행번호

train<-iris[idx,] #105
test<-iris[-idx,]

# 활성함수
#이항:sigmoid func,다항:softmax function

#1.model 생성
model<-multinom(Species ~.,data=train) # weights:  18 (10 variable)
#if converged 가 나온다면 100 반복전에 오차가 0에 수렴함.

#  weights:  18 (10 variable)
# initial  value 115.354290 <- 처음 오차
# iter  10 value 15.785704<- 10번 반복시 오차
# iter  20 value 5.061652 <- 20번 반복시 오차
# iter  30 value 4.955119
# iter  40 value 4.861970
# iter  50 value 4.842887
# iter  60 value 4.842232
# final  value 4.842211 
names(model)
model$fitted.values #적합치
#         setosa     versicolor    virginica 
# 103 1.314016e-20  2.663673e-05  9.999734e-01 <- 나올수 있는 확율

#2.예측치:확률로 예측
pred<-predict(model,test,type='probs')
pred

#예측치:y class
pred2<-predict(model,test,type='class')
pred2

#관측치
y_true<-test$Species

#3.평가
tab<-table(y_true,pred2)
tab
#                         pred2
# y_true       setosa versicolor virginica
# setosa         14          0         0
# versicolor      0         13         1
# virginica       0          0        17

acc<-(tab[1,1]+tab[2,2]+tab[3,3])/sum(tab)
cat('accuracy=',acc)#accuracy= 0.9777778

#오분류표
#FPR=FP/(FP+TN) : 거짓 양성 비율(위양성) -1종오류(가설 채택-> 기각)
#FNR FN/(TP+FN): 거짓 음성 비율(위음성) -2종오류(가설 기각-> 채택)
















