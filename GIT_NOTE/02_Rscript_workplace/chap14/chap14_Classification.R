#chap14_DecsionTree

install.packages('rpart') # rpart() : 분류모델 생성 
install.packages("rpart.plot") # prp(), rpart.plot() : rpart 시각화
install.packages('rattle') # fancyRpartPlot() : node 번호 시각화 

library(rpart) 
library(rpart.plot) 
library(rattle) 

####################################
# 암 진단 분류 분석 : 이항분류
####################################
#범주가 2개 인 경우
# "wdbc_data.csv" : 유방암 진단결과 데이터 셋 분류

# 1. 데이터셋 가져오기 
wdbc_df <- read.csv('C:/itwill/2_Rwork/data/wdbc_data.csv')
str(wdbc_df)

# 3. 훈련데이터와 검정데이터 생성 : 7 : 3 비율 
set.seed(415) #똑같은 데이터 사용하것다.
idx = sample(1:nrow(wdbc_df), 0.7*nrow(wdbc_df))
wdbc_train = wdbc_df[idx, ] # 훈련 데이터 
wdbc_test = wdbc_df[-idx, ] # 검정 데이터 

# 4. rpart 분류모델 생성 
model_wdbc <- rpart(diagnosis ~ ., data = wdbc_train)
model_wdbc # - 가장 중요한 x변수? 

#  총  M  
# 1) root 398 136 B (0.65829146 0.34170854)  
# 전체 데이터(368) 에서 약66%가B(262) 나머지는 M(136) 주요레이블(불류비율)
table(wdbc_train$diagnosis)#262 136 

# 2) points_mean< 0.04923 255  10 B (0.96078431 0.03921569) *
#left node:분류조건(중요변수) 분류조건(관측치) :255의 데이터에서 10개를 제외한 나머지는 B 이다.
#차트:B-> 0.04 0 > 64%:주요분류레이블-> M분류 비율 -> 분류조건 분류비율
left_node<-subset(wdbc_train, points_mean<0.04923)
nrow(left_node)#255
table(left_node$diagnosis)#245  10

# 3) points_mean>=0.04923 143  17 M (0.11888112 0.88111888)  
#right node:분류조건(중요변수) 분류조건(관측치)
right_node<-subset(wdbc_train, points_mean>=0.04923)
nrow(right_node)#143
table(right_node$diagnosis)#17 126
17/143 #0.1188811
126/143 #0.8811189
# 차트:M->0.88 36%: :주요분류레이블 -> B분류 비율-> 분류조건 분류비율

#     6) concavity_worst< 0.2269 12   2 B (0.83333333 0.16666667) *
#     7) concavity_worst>=0.2269 131   7 M (0.05343511 0.94656489)  
#        14) area_worst< 710.2 8   3 B (0.62500000 0.37500000) *
#        15) area_worst>=710.2 123   2 M (0.01626016 0.98373984) *

# points_mean< 0.04923
# 이 분류조건에 의해서 만들어진 관측치가 255개 인데 그 안에는 'M'이 10개인 관측치가 포함된 경우입니다. 
#그래서  255에서 10개를 제외한 비율(0.96)은 B분류 결과이고, 나머지 10의 비율은 (0.03)은 M분류 결과입니다.
#*의미는 최종 결과 값이다 (더이낭 root 안 나온다.)

# tree 시각화 
rpart.plot(model_wdbc)
fancyRpartPlot(model_wdbc)

#5.모델 평가

#(1)class예측
y_pred<-predict(model_wdbc,wdbc_test, type='class') #Y class예측
y_pred #B or M-> vector 자료생성

y_true<-wdbc_test$diagnosis


tab<-table(y_true,y_pred)
tab

#         y_pred
# y_true  B  M
#    B   92  3
#    M   13 63


#################################################
#(2)비율로예측했을 경우 

y_pred2<-predict(model_wdbc,wdbc_test) #비율 예측
y_pred2 # B     M
#10  0.96078431 0.03921569

#2차원 ->1차원
y_pred2<-ifelse(y_pred2[,1]>0.5,'M','B') #연속형 데이터 범주형으로 변환
y_pred2

y_true<-wdbc$diagnosis
y_true

tab<-table(y_ture,y_pred2)
tab
#################################################

acc<-(tab[1,1]+tab[2,2])/sum(tab)
acc#0.9064327

92/95 #0.9684211
m<-63/76
m #0.8289474



################################
# iris 데이터셋 : 다항분류 
################################
#범주의 수가 2개 초과시
# 단계1. 실습데이터 생성 
data(iris)
set.seed(415)
idx = sample(1:nrow(iris), 0.7*nrow(iris))
train = iris[idx, ]
test = iris[-idx, ]
dim(train) # 105 5

dim(test) # 45  5

table(train$Species)
#37         33         35 

# 단계2. 분류모델 생성 
# rpart(y변수 ~ x변수, data)
model = rpart(Species~., data=train) # iris의 꽃의 종류(Species) 분류 
model

# 분류모델 시각화 - rpart.plot 패키지 제공 
prp(model) # 간단한 시각화   
rpart.plot(model) # rpart 모델 tree 출력
fancyRpartPlot(model) # node 번호 출력(rattle 패키지 제공)


# 단계3. 분류모델 평가  
pred <- predict(model, test) # 비율 예측 
pred <- predict(model, test, type="class") # 분류 예측 

# 1) 분류모델로 분류된 y변수 보기 
table(pred)

# 2) 분류모델 성능 평가 
tab<-table(test$Species,pred)

acc<-(tab[1,1]+tab[2,2]+tab[3,3])/sum(tab)
cat('accuracy=',acc)

####################
#확률예측(비율예측)
pred2 <- predict(model, test) # 비율 예측 
dim(pred2)
class(pred2)
colnames(pred2)

#class 변환
re_pred2<-ifelse(pred2[,1]>0.5,'setosa',
                 ifelse(pred2[,2]>0.5,'versicolor','virginica'))

# 1)분류모델 성능 평가
table(re_pred2)

# class 이용 
tab2<-table(test$Species,re_pred2)
#class 변환이용
acc1<-(tab2[1,1]+tab2[2,2]+tab2[3,3])/sum(tab2)
cat('accuracy=',acc1)


#############################################################
####### 가지치기 (CP)
#############################################################

#트리 가지치기: 과적합 문제 해결법
# cp 범위: 0 ~ 1, default = 0.01 (기본 값)
# cp가 0에 가까울 수록 tree depth 깊어짐, 오류율 감소, 과적합 증가
# cp가 1에 가까울 수록 tree depth 낮아짐, 오류율 증가, 과적합 감소

names(model1)

#현재 cp값 확인
model1$control
# $cp
# [1] 0.01

#cp상세 정보 제공
model$cptable
#         CP    nsplit  rel error     xerror        xstd
# 1 0.5147059      0    1.00000000   1.11764706   0.06737554
# 2 0.4558824      1    0.48529412   0.57352941   0.07281162 -> cP 조정: 과적합 은 해결되나 오차가 너무 증가함
# 3 0.0100000      2    0.02941176   0.02941176   0.02059824 -> 현재 cp:오차 가장 적음


#cp= 0.4558824
model2=rpart(Species~.,data=train,
             control = rpart.control(cp=0.4558824))
model2

prp(model2) #tree depth = 1



################################################################
#########교차검정
################################################################

install.packages('cvTools')
library(cvTools)

#단계1: k겹 교차검정을 위한 샘플링
cross <- cvFolds(nrow(iris), K=5)
cross #Fold(dataset 구분) Index(행번호)
# dataset1-> 192,47 .....136
# dataset5-> 8,115.....56
help(cvFolds)

names(cross)
cross$which

str(cross) #List of 5

dataset1<-cross$subsets[cross$which==1,1] #행번호가 1인 데이터를 가지고 와라
length(dataset1) #30
dataset1

dataset5<-cross$subsets[cross$which==5,1] #행번호가 5인 데이터를 가지고 와라
dataset5

#단계2:k겹 교차검정
K = 1:5
ACC<- numeric() #분류정확도
cnt<- 1

for(i in K){
  idx<-cross$subsets[cross$which==i,1] #행번호
  test<-iris[idx,] #검정데이터 셋
  train<-iris[-idx,] #훈련셋
  #모델생성
  model<-rpart(Species ~ ., data=train) #4개 셋
  #예측치
  y_pred<-predict(model,test,type='class') #1개 셋
  y_ture<-test$Species
  t<-table(y_ture,y_pred)
  #분류정확도
  ACC[cnt]<-(t[1,1]+t[2,2]+t[3,3])/sum(t)
  cnt<-cnt+1
} 

ACC

cat('분류정화도 산술평균=',mean(ACC))


##############################################
#### Entropy: 불확실성 척도
##############################################

#p1:앞면,p2:뒷면 -불확실성이 높은경우
p1=0.5; p2=0.5

e1<- -(p1*log2(p1)) +-(p2*log2(p2))
e1 #1 최대의 불확실성

#entropy=-sum(p*log(p))
e1<--sum((p1*log2(p1)),(p2*log2(p2)))
e1


#p1:앞면,p2:뒷면-불확실성이 낮은경우
p1=0.9; p2=0.1

e2<- -(p1*log2(p1)) +-(p2*log2(p2))
e2 #1 최대의 불확실성

#entropy=-sum(p*log(p))
e2<--sum((p1*log2(p1)),(p2*log2(p2)))
e2#0.4689956






