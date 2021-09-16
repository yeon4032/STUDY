#chap10_Ttest_Anova 

#example
#표본수=20 , 알파=0.05
#귀무가설: 모평균 =6.7과 차이가 없다

#표본추출
x<-runif(n=20, min=5, max=10) #확률변수x #5보다 크고 10보다 작은 임의의 수.
x

#T검정
t.test(x,mu=6.7) #평균차이 검정
#t = 2.3462 (검정통계량), df = 19(지유도), p-value = 0.02997 
#방법1:p-value=0.02997 <알파=0.05 :가설 기각
#방법2:t=2.3462 > 임계값(t분표포)=2.093 : 가설 기각

# 95 percent confidence interval: 95%
#   6.78567 8.20243 :신뢰구간
#모평균(6.7)이 신뢱구간에 들어 오지 않아서 가서은 기각됨

# mean of x 
# 7.49405 :x 실제 평균

mu=6.7#모평균
x_mu<- mean(x) #x의 산술평균
S=sd(x) #표본 표준편차
t<-(x_mu-mu)/(S/sqrt(length(x)))
t #2.3462


###########################
# 1. 1. 단일표본 T검정
###########################
# - 신규 집단의 평균이 기존 집단의 평균 값과 차이가 있는지를 검증

# 1. 실습파일 가져오기
setwd('C:/ITWILL/2_Rwork/data')

data <- read.csv("one_sample.csv", header=TRUE)
str(data) # 150
head(data)
x <- data$time
head(x)

# 2. 기술통계량 평균 계산
summary(x) # NA-41개
mean(x) # NA
mean(x, na.rm=T) # NA 제외 평균(방법1)

x1 <- na.omit(x) # NA 제외 평균(방법2)
mean(x1)#5.556881

# 3. 정규분포 검정
# 정규분포(바른 분포) : 평균에 대한 검정 
# 정규분포 검정 귀무가설 : 정규분포와 차이가 없다.
shapiro.test(x) # 정규분포 검정 함수
# W = 0.99137, p-value = 0.7242 >0.05 이면 정규분포라 할수 있다. 

# 4. 가설검정 - 모수/비모수
# 정규분포(모수검정) -> t.test()
# 비정규분포(비모수검정) -> wilcox.test()

# 1) 양측검정 - 정제 데이터와 5.2시간 비교
t.test(x1, mu=5.2) 
t.test(x1, mu=5.2, alter="two.side", conf.level=0.95) #기본가정임 
# t = 3.9461, df = 108, p-value = 0.0001417
# p(=0.0001417)< 알파값 -> 귀무가설 기각

# 2) 방향성이 있는 대립가설 검정 : x1> 5.2
t.test(x1, mu=5.2, alter="greater", conf.level=0.95) #one side or 방향성 있는 대립가설
# t = 3.9461, df = 108, p-value = 7.083e-05 <0.05: 귀무가설 기각

# 2) 방향성이 있는 대립가설 검정 : x1< 5.2
t.test(x1, mu=5.2, alter="less", conf.level=0.95) #one side or 방향성 있는 대립가설
# t = 3.9461, df = 108, p-value = 0.9999 >0.05: 귀무가설 인정


############################
#  2. 독립표본 T검정
############################
# 연구가설(H1) : 교육방법에 따른 두 집단 간 실기시험의 평균에 차이가 있다.
# 귀무가설(H0) : 교육방법에 따른 두 집단 간 실기시험의 평균에 차이가 없다다.


# 1. 실습파일 가져오기
data <- read.csv("two_sample.csv")
data 
head(data) #4개 변수 확인
summary(data) # score - NA's : 73개
table(data$method)
#  1   2 
# 150 150 


# 2. 두 집단 subset 작성(데이터 정제,전처리)
#result <- subset(data, !is.na(score), c(method, score))
dataset <- data[c('method', 'score')]
table(dataset$method)


# 3. 데이터 분리
# 1) 교육방법 별로 분리
method1 <- subset(dataset, method==1) #방법1
method2 <- subset(dataset, method==2) #방법2

# 2) 교육방법에서 점수 추출
method1_score <- method1$score
method2_score <- method2$score

# 3) 기술통계량 
length(method1_score); # 150
length(method2_score); # 150

mean(method1_score,na.rm=T) #5.556881
mean(method2_score,na.rm=T) #5.80339

# 4. 등분산성 검정 : 두 집단의 분포모양 일치 여부 검정
var.test(method1_score, method2_score) 
# F = 1.2158, num df = 108, denom df = 117, p-value = 0.3002
# 동질성 분포 : t.test()
# 비동질성 분포 : wilcox.test()

# 5. 가설검정 - 두집단 평균 차이검정
t.test(method1_score, method2_score)
t.test(method1_score, method2_score, alter="two.sided", conf.int=TRUE, conf.level=0.95)
# t = -2.0547, df = 218.19, p-value = 0.0411 <0.05 -> 가설기각

#대립가설 채택
# # 방향성이 있는 대립가설 검정 :방법1>방법2 (x)
t.test(method1_score, method2_score, alter="greater", conf.int=TRUE, conf.level=0.95)
#t = -2.0547, df = 218.19, p-value = 0.0411

# # 방향성이 있는 대립가설 검정 :방법1<방법2 (o)
t.test(method1_score, method2_score, alter="less", conf.int=TRUE, conf.level=0.95)
# t = -2.0547, df = 218.19, p-value = 0.02055

###############################
# 3. 대응표본 T검정
###############################
# 조건 : A집단  독립적 B집단 -> 비교대상 독립성 유지
# 대응 : 표본이 짝을 이룬다. -> 한 사람에게 2가지 질문
# 사례) 다이어트식품 효능 테스트 : 복용전 몸무게 -> 복용후 몸무게 

# 1. 실습파일 가져오기
data <- read.csv("paired_sample.csv", header=TRUE)

# 2. 두 집단 subset 작성

# 1) 데이터 정제
#result <- subset(data, !is.na(after), c(before,after))
dataset <- data[ c('before',  'after')]
dataset

# 2) 적용전과 적용후 분리
before <- dataset$before# 교수법 적용전 점수
after <- dataset$after # 교수법 적용후 점수
before; after

# 3) 기술통계량 
length(before) # 100
length(after) # 100
mean(before) # 5.145
mean(after, na.rm = T) # 6.220833 


# 3. 등분산성 검정 
var.test(before, after, paired=TRUE) 
# 동질성 분포 : t.test()
# 비동질성 분포 : wilcox.test()
# F = 1.1575, num df = 99, denom df = 95, p-value = 0.4738

# 4. 가설검정
t.test(before, after, paired=TRUE)
# t = -13.642, df = 95, p-value < 2.2e-16

# 방향성이 있는 대립가설 검정 : before > after 
t.test(before, after, paired=TRUE,alter="greater",conf.int=TRUE, conf.level=0.95) 

#  방향성이 있는 대립가설 검정 : before < after
t.test(before, after, paired=TRUE,alter="less",conf.int=TRUE, conf.level=0.95) 




############################################
#  4. 분산분석 : 세 집단 이상 분산 차이 검정 
############################################
# 세 집단 이상 평균차이 검정 = 분산분석(집단별 분산의 차이) : 분산의 비율 차이  
# 용도 : 정규분포를 따르는 세 집단 이상의 분산에 대한 가설검정
# 독립변수 : 범주형(집단), 종속변수 : 연속형




##############################################
##일원 배치 분산 분석: y~x
###############################################
#aov(종속변수 ~ 독립변수,data=dataset)

#기본 가절: 각집단의 분산은 동일하다. (등분산성)
#기본 가설: 각 집단별 평균의 차이가 없다. 
#대립 가설: 적어도 한 집단에 평균 차이가 있다.



# 1. 파일 가져오기
data <- read.csv("three_sample.csv")
head(data)

# 2. 데이터 정제/전처리 - NA, outline 제거
data <- subset(data, !is.na(score), c(method, score)) 
data # method, score

# (1) 차트이용 - ontlier 보기(데이터 분포 현황 분석)
plot(data$score) # 차트로 outlier 확인 : 50이상과 음수값
barplot(data$score) # 바 차트
mean(data$score) # 14.45

# (2) outlier 제거 - 평균(14) 이상 제거
length(data$score)#91
data2 <- subset(data, score <= 14) # 14이상 제거
length(data2$score) #88(3개 제거)
plot(data2$score)


# (3) 정제된 데이터 보기 
x <- data2$score
boxplot(x)
plot(x)

# 3. 집단별 subset 작성
# method: 1:방법1, 2:방법2, 3:방법3
data2$method2[data2$method==1] <- "방법1" 
data2$method2[data2$method==2] <- "방법2"
data2$method2[data2$method==3] <- "방법3"

table(data2$method2) # 교육방법 별 빈도수 


# 4. 등분산성 검정 : 동질성 검정 
# bartlett.test(종속변수 ~ 독립변수) # 독립변수(세 집단)
bartlett.test(score ~ method2, data=data2)
# Bartlett's K-squared = 3.3157, df = 2, p-value = 0.1905

# 귀무가설 : 집단 간 분포의 모양이 동질적이다.

# 동질한 경우 : aov() - Analysis of Variance(분산분석)
# 동질하지 않은 경우 - kruskal.test()

# 5. 분산검정(집단이 2개 이상인 경우 분산분석이라고 함)
# aov(종속변수 ~ 독립변수, data=data set)

# 귀무가설 : 집단 간 평균에 차이가 없다.
result <- aov(score ~ method2, data=data2)

# aov()의 결과값은 summary()함수를 사용해야 p-value 확인 
summary(result) 
#             Df Sum Sq   Mean Sq  F value   Pr(>F)    
# method2      2  99.37   49.68    43.58     9.39e-14 ***
# Residuals   85  96.90    1.14                     

#f-value( 43.58) 값이 1.96에 비해 너무 크다 그럼으로 H0 는 기각된다. 
#p-value (9.39e-14) 는 알파 보다 작다 그럼으로 H0 는 긱각된다.
# 적어도  한 집단 이상에서 평균 차이가 있다.

# 6. 사후검정 : 세부적인 집단 간 차이 검정
TukeyHSD(result)

#               diff        lwr        upr     p adj    p adj<0.05 인겨우 차이가 있다 /  차이의 정도는 diff 에서 알수 있다.
# 방법2-방법1  2.612903  1.9424342  3.2833723 0.0000000 -> 차이가 있다 (p adj따르면)  /  가장 큰 차이를 본인다..
# 방법3-방법1  1.422903  0.7705979  2.0752085 0.0000040 -> 차이가 있다 (p adj따르면)  /  2등
# 방법3-방법2 -1.190000 -1.8656509 -0.5143491 0.0001911 -> 차이가 있다 (p adj따르면)  /  3등

#용어
#diff:집단간 차이
#95% 신뢰구간(하안값(lwr)~상안값(upr))
#p adj:유의확률

plot(TukeyHSD(result))
#95% 신뢰구간 :0을 포함하지 않은경우 :기각
#95% 신뢰구간 :0을 포함한 경우 :채택

###############################################
## 그룹별 통계 : 분산분석 사후검정에서 이용 
###############################################
#install.packages('dplyr')
library(dplyr)

# 형식) 
# df %>% group_by('범주형변수')
#   %>% summarize(var_name = function(column_name))

# function : sum, mean, median, sd, var, min, max 등 

# 교육방법별 점수 평균 
data2 %>% group_by(method2) %>% summarize(avg = mean(score))
#  method2   avg
#   <chr>   <dbl>
# 1 방법1    4.19
# 2 방법2    6.8 
# 3 방법3    5.61

#select avg(score) from data2 group by method2;


#df %>% func
data2 %>% head()

data2 %>% group_by(method2) %>% summarize(var=var(score))

#  method2   var
#   <chr>   <dbl>
# 1 방법1   1.49 
# 2 방법2   0.732
# 3 방법3   1.15 

###########################################################3
## 비모수 검정 : iris 적용
###########################################################

str(iris)
names(iris)
#Species:독립변수 (집단변수인것을씀)- 주의: 요인형 or 문자형
#Sepal.Width종속변수(연속형 변수) - 숫자

#1.등분산성 검정: 각집단별 분산 차이 검사 (가정: 집단변 분포는 동일하다)
bartlett.test(Sepal.Length ~ Species,data=iris)
#p-value = 0.0003345


#2. 분산 분석: 비모수 검정
result<-kruskal.test(Sepal.Length ~ Species,data=iris)
#p-value < 2.2e-16 -> 집단 차이가 있다. 

#3. 사후검정: 
# df %>% group_by('범주형변수') %>% summarize(var_name = function(column_name))
library(dplyr)

iris %>% group_by(Species) %>% summarize(avg = mean(Sepal.Length))

#   Species      avg
#   <fct>      <dbl>
# 1 setosa      5.01
# 2 versicolor  5.94
# 3 virginica   6.59




##############################################
## 이원배치 분산 분석: y~x1+x2
###############################################
#aov(종속변수 ~ 독립변수1+독립변수2,data=dataset)

#쇼핑몰 고객의 연령대(20,30,40)별, 시간대별(오전/오후)별 구매현황 분석
#종속변수: 구매수량 
#독립변수1:연령대별
#독립녀수2:시간대별

#1. dataset 생성
age<- round(runif(100,min=20, max=49)) #20~49
age
time <- round(runif(100,min=0,max=1))
time #오전 (0)/오후 (1)
buy<-round(runif(100,min=1,max=10))
buy


datas<-data.frame(age,time,buy)
datas
head(datas)

#연령대 리코딩
datas$age2[datas$age<=29]<-20
datas$age2[datas$age>29 & datas$age<=39]<-30
datas$age2[datas$age>39]<-40
str(datas)

#독립변수: 요인형 변환
datas$age2<-as.factor(datas$age2)
datas$time<- as.factor(datas$time)

unique(datas$ages2)
unique(datas$time)

#2.등분산성 검정
bartlett.test(buy~age2,data=datas)
#Bartlett's K-squared = 0.895, df = 2, p-value = 0.6392
bartlett.test(buy~time,data=datas)
#Bartlett's K-squared = 1.8934, df = 1, p-value = 0.1688


#3. 분산분석: 이원배치 분산분석
model1<-aov(buy ~ age2+time,data=datas)

#4. 분석 결과 해석
summary(model1)
#             Df  Sum Sq  Mean Sq  F value  Pr(>F)
# age2         2    9.2   4.594     0.708   0.495 <- 연령대별 차이 없다
# time         1    2.8   2.758     0.425   0.516 <- 연령대별 차이 없다
# Residuals   96  623.4   6.493   


#5. 사후검정 
TukeyHSD(model1)

# $age2
#            diff       lwr      upr     p adj
# 30-20  0.37517934 -1.186149 1.936507 0.8353102
# 40-20 -0.09658537 -1.804652 1.611482 0.9900604
# 40-30 -0.47176471 -2.245184 1.301655 0.8021846
# 
# $time
#          diff       lwr       upr     p adj
# 1-0   -0.2480407 -1.370786 0.8747045 0.6619878


#연령대별 subset->mean
sub_age20 <- subset(datas,age2==20)
mean(sub_age20$buy) #5.536585
sub_age30 <- subset(datas,age2==30)
mean(sub_age30$buy) # 5.536585
sub_age40 <- subset(datas,age2==40)
mean(sub_age40$buy) #5.536585

library(dplyr)
datas %>% group_by(age2) %>%summarise(avg=mean(buy))
#   age2    avg
#  <fct>   <dbl>
# 1 20     5.54
# 2 30     5.91
# 3 40     5.44

datas%>%group_by(time)%>%summarise(avg=mean(buy))

#  time    avg
#  <fct>  <dbl>
# 1  0    5.78
# 2  1    5.51














