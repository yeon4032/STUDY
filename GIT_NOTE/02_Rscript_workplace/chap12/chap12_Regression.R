#chap12_Regression

######################################################
# 회귀분석(Regression Analysis)
######################################################
# - 특정 변수(독립변수:설명변수)가 다른 변수(종속변수:반응변수)에 어떠한 영향을 미치는가 분석

###################################
## 1. 단순회귀분석 
###################################
# - 독립변수와 종속변수가 1개인 경우

# 단순선형회귀 모델 생성  
# 형식) lm(formula= y ~ x 변수, data) 

setwd("C:/ITWILL/2_Rwork/data")
product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

str(product) # 'data.frame':  264 obs. of  3 variables:
y = product$'제품_만족도' # 종속변수
x = product$'제품_적절성' # 독립변수
df <- data.frame(x, y)
head(df) #x=제품_적절성, y=제품_만족도

# 회귀모델 생성 
result.lm <- lm(formula=y ~ x, data=df)
result.lm # 회귀계수 
# Coefficients:
#   (Intercept)      x  
#     0.7789       0.7393  

#회귀방정식
a= 0.7393 #기울기
b= 0.7789 #절편
X=4
y=a*X+b #+ 오차
Y=3

#오차(잔차)
err<-Y-y
err # -0.7361
#12개의 컬럼: 회귀분석 결과
names(result.lm)
#"conefficient":회귀계수
#"residual":오차(잔차)
#"fitted.values":접합치 = 회귀방정식

result.lm$coefficients
# (Intercept)     x 
# 0.7788583   0.7392762 

result.lm$residuals[1] #-0.735963
mean(result.lm$residuals) #5.617479e-17 = 0
result.lm$fitted.values[1] #3.735963

# 회귀모델 예측 :미지의 x값 -> y예측 
y_pred<-predict(result.lm, data.frame(x=5)) 

# (2) 선형회귀 분석 결과 보기
summary(result.lm)
#<분석절차>
#1.모델 통계적 유의성 검정 :F-검정 통되량 유의확률 (p-value)<0.05
#2.모델 설명력:R-squarded: 1에 수렴정도 (1에 가까우면 예측력 이 좋다)
#3.x변수의 유의성 검정 : t-검정 통계량에 근거한 p-value,*강도

# (3) 단순선형회귀 시각화
# x,y 산점도 그리기 
plot(formula=y ~ x, data=df)
# 회귀분석
result.lm <- lm(formula=y ~ x, data=df)
# 회귀선 
abline(result.lm, col='red')

#점수와 지능지수
score_iq<-read.csv('score_iq.csv')
cor(score_iq[2:3])#0.8822203

plot(score_iq$iq,score_iq$score,)
model<-lm(formula=score ~iq,data=score_iq)
abline(model,col='red')

summary(model)



###################################
## 2. 다중회귀분석
###################################
# - 여러 개의 독립변수 -> 종속변수에 미치는 영향 분석
# 가설 : 음료수 제품의 적절성(x1)과 친밀도(x2)는 제품 만족도(y)에 정의 영향을 미친다.

product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)


# 1) 적절성 + 친밀도 -> 만족도  
y = product$'제품_만족도' # 종속변수
x1 = product$'제품_친밀도' # 독립변수2
x2 = product$'제품_적절성' # 독립변수1

df <- data.frame(x1, x2, y)

result.lm <- lm(formula=y ~ x1 + x2, data=df)
result.lm <- lm(formula=y ~ ., data=df) #y를 제외한 나머지를 x변수로 쓴다. 

# 계수 확인 
result.lm

summary(result.lm)
# (Intercept)   x1=a1        x2=a2  
# 0.66731      0.09593      0.68522  

#회귀방정식
head(df,1)
X1=3
X2=4
Y=3
a1=0.09593
a2=0.68522
b=0.66731

y = X1*a1 + a2*X2 + b
print(y)#3.69598

#y = (X %*% a) + b #행렬곱
X<-matrix(data=c(3,4),nrow=1,ncol=2)
X
a<-matrix(data=c(0.09593,0.68522),nrow = 2,ncol=1) #수 일치 중요
a
dim(X)#1 2
dim(a)#2 1

y=(X%*%a)+b
y #3.69598
dim(y) #1 1

names(result.lm)
result.lm$fitted.values[1]

#다중회귀분석 결과
summary(result.lm)


# 2) 102개 직업군 평판 dataset 이용 
install.packages("car") # 다중공선성 문제 확인  
library(car)

Prestige # car 제공 dataset
class(Prestige)#data.frame
names(Prestige)#변수 추출
row.names(Prestige) #행 이름->102직업군 이름

# 102개 직업군의 평판 : 교육수준,수입,여성비율,평판(프레스티지),센서스(인구수=직원수)
str(Prestige)

#종속변수:income
#독립변수:education+women+prestige

model<-lm(income ~education + women + prestige, data = Prestige )
model

summary(model)
# Coefficients:
#           Estimate Std. Error t value Pr(>|t|)    
# (Intercept) -253.850   1086.157  -0.234    0.816  
# education    177.199    187.632   0.944    0.347    <-영향력없음
# women        -50.896      8.556  -5.948 4.19e-08 ***<-부(-)의 영향
# prestige     141.435     29.910   4.729 7.58e-06 ***<-정(+)의 영향





