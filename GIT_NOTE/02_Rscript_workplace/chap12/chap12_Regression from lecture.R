# chap12_Regression

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
head(df) # x y

# 회귀모델 생성 
result.lm <- lm(formula=y ~ x, data=df)
result.lm # 회귀계수 
#Coefficients:
#  (Intercept)=절편(b)   x=기울기(a)   
#     0.7789               0.7393 

# 회귀방정식 
a = 0.7393 # 기울기 
b = 0.7789 # 절편 
X = 4
y = X*a + b #+ 오차 
y # 3.7361
Y = 3

# 오차(잔차) 
err <- Y - y
err # -0.7361

# 12 칼럼 : 회귀분석 결과 
names(result.lm)
# "coefficients" : 회귀계수 
# "residuals" : 오차(잔차) 
# "fitted.values" : 적합치 = 회귀방정식 

result.lm$coefficients
#   0.7788583   0.7392762

result.lm$residuals[1] # -0.735963

mean(result.lm$residuals) # -5.617479e-17 = 0 

result.lm$fitted.values[1] # 3.735963


# 회귀모델 예측치 : 미지의 x값 -> y예측  
y_pred <- predict(result.lm, data.frame(x=5)) 


# (2) 선형회귀 분석 결과 보기
summary(result.lm)
# <분석절차>
# 1. 모델 통계적 유의성 검정 : F-검정 p-value < 0.05
# 2. 모델 설명력 : R-squared(1수렴 정도)
# 3. X변수의 유의성 검정 :  t-검정 p-value, * 강도 


# (3) 단순선형회귀 시각화
# x,y 산점도 그리기 
plot(formula=y ~ x, data=df)
# 회귀분석
result.lm <- lm(formula=y ~ x, data=df)
result.lm
# 회귀선 
abline(result.lm, col='red')


# 점수와 지능지수 
score_iq <- read.csv('score_iq.csv')
head(score_iq)

cor(score_iq[2:3]) # 0.882220


plot(score_iq$iq, score_iq$score) # (x, y)
model <- lm(score ~ iq, data = score_iq) # (y ~ x)
model
abline(model, col='red')

summary(model)

0.882220^2 # 0.7783121

range(score_iq$score) # 65 90


###################################
## 2. 다중회귀분석
###################################
# - 여러 개의 독립변수 -> 종속변수에 미치는 영향 분석
# 가설 : 음료수 제품의 적절성(x1)과 친밀도(x2)는 제품 만족도(y)에 정의 영향을 미친다.

product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)


# 1) 적절성 + 친밀도 -> 만족도  
y = product$'제품_만족도' # 종속변수
x1 = product$'제품_친밀도' # 독립변수1
x2 = product$'제품_적절성' # 독립변수2

df <- data.frame(x1, x2, y)

result.lm <- lm(formula=y ~ x1 + x2, data=df)
result.lm <- lm(formula=y ~ ., data=df) # . : y를 제외한 나머지 x변수 

# 계수 확인 
result.lm
#(Intercept)=b       x1=a1       x2=a2  
#     0.66731      0.09593      0.68522 

# 회귀방정식 
head(df, 1)
X1 = 3
X2 = 4
Y = 3
a1 = 0.09593
a2 = 0.68522 
b = 0.66731

y = X1*a1 + X2*a2 + b
print(y) # 3.69598

#y = (X %*% a) + b # 행렬곱
X <- matrix(data = c(3, 4), nrow = 1, ncol = 2)
X
a <- matrix(data = c(0.09593, 0.68522), nrow = 2, ncol = 1)
a
dim(X) # 1 2
dim(a) # 2 1

y = (X %*% a) + b
y # 3.69598
dim(y) # 1 1


names(result.lm)
result.lm$fitted.values[1] # 3.69598

# 다중회귀분석 결과 
summary(result.lm)

# 2) 102개 직업군 평판 dataset 이용 
#install.packages("car") # 다중공선성 문제 확인  
library(car)

Prestige # car 제공 dataset
class(Prestige) #  "data.frame"
names(Prestige) # 변수 추출 : 6개 
row.names(Prestige) # 행 이름 -> 102 직업군 이름 

# 102개 직업군의 평판 : 교육수준,수입,여성비율,평판(프레스티지),센서스(인구수=직원수)
str(Prestige)

Cor <- cor(Prestige[1:4])
Cor['income',] # 0.5775802  1.0000000 -0.4410593  0.7149057

# 종속변수 : income 
# 독립변수 : education + women + prestige 
model <- lm(income ~ education + women + prestige, data = Prestige)
model

summary(model)
#Coefficients:
#Estimate Std. Error t value Pr(>|t|)    
#(Intercept) -253.850   1086.157  -0.234    0.816    
#education    177.199    187.632   0.944    0.347      -> 영향력 없음 
#women        -50.896      8.556  -5.948 4.19e-08 ***  -> 부(-)의 영향력 
#prestige     141.435     29.910   4.729 7.58e-06 ***  -> 정(+)의 영향력 
# Adjusted R-squared:  0.6323

# 다중회귀분석 회귀선 시각화 
install.packages('psych')
library(psych)

newdata <- Prestige[c(2,1,3:4)] # income 기준 
head(newdata)

# stars : 상관계수 유의성, lm : 회귀선, ci : 회귀선 신뢰구간 
pairs.panels(newdata, stars = TRUE, lm = TRUE, ci = TRUE)
# 상관타원 : 타원의 폭이 좁을 수록 상관성 높다.

###################################
## 3. 변수 선택법 : ppt.24
###################################
# 전진선택법 : 절편만 포함시킨 model + 독립변수 1개씩 추가 
# 후진제거법 : model+모든 변수 -> 독립변수 1개씩 제거 
# 단계선택법 : 혼합법 

str(Prestige)

newdata <- Prestige[-6] # type 제외 
dim(newdata) # 102   5

model <- lm(income ~ ., data = newdata)
model


library(MASS)
step <- stepAIC(model, direction = 'both')

#AIC값이 낮을수록 방정식이 적절한것임
#Step:  AIC=1604.96
#income ~ women + prestige (마지막 테이블 값) +부호는 변수를 빼라는 의미

new_model <- lm(income ~ women + prestige, data = newdata)
new_model

summary(new_model)
# Adjusted R-squared:  0.6327 

# 차원의 저주 : 차원이 많으면, 과적합 현상 발생 
# - training dataset 정확도 높고, new dataset 정확도 낮게 


###################################
# 4. 다중공선성과 기계학습
###################################
# - 독립변수 간의 강한 상관관계로 인해서 회귀분석의 결과를 신뢰할 수 없는 현상
# - 생년월일과 나이를 독립변수로 갖는 경우
# - 해결방안 : 강한 상관관계를 갖는 독립변수 제거

# (1) 다중공선성 문제 확인
library(car)
names(iris)
fit <- lm(formula=Sepal.Length ~ Sepal.Width+Petal.Length+Petal.Width, data=iris)
vif(fit)
sqrt(vif(fit))>2 # root(VIF)가 2 이상인 것은 다중공선성 문제 의심 

# (2) iris 변수 간의 상관계수 구하기
cor(iris[,-5]) # 변수간의 상관계수 보기(Species 제외) 
#x변수 들끼 계수값이 높을 수도 있다. -> 해당 변수 제거(모형 수정) <- Petal.Width


###############################
## 기계학습 : train/test
###############################

dim(iris) # 150 5

# (1) 학습데이터와 검정데이터 분류
x <- sample(nrow(iris), 0.7*nrow(iris)) # 전체중 70%만 추출
x # 행번호 
train <- iris[x, ] # 학습데이터 추출
test <- iris[-x, ] # 검정데이터 추출

dim(train) # 105   5
dim(test) # 45  5
names(test)

# (2) model 생성 : Petal.Width 변수를 제거한 후 회귀분석 
result.lm <- lm(formula=Sepal.Length ~ Sepal.Width + Petal.Length, data=train)
result.lm
summary(result.lm)

# (3) model 예측치 : test dataset 
y_pred <- predict(result.lm, test) # test = Sepal.Width + Petal.Length
length(y_pred) # 45

y_true <- test$Sepal.Length # 관측치(정답)


# (4) model 평가

# 1) MSE = Mean Square Error 
# MSE = mean(err ^ 2)
err <- y_pred - y_true
MSE = mean(err ^ 2)
# 제곱(Square) : 부호 절대값, 패널티  
MSE # 0.1361803 -> 0 수렴정도 

# 2) RMSE : Root MSE 
RMSE <- sqrt(MSE)
RMSE # 0.369026

# 3) 상관계수 
cor(y_true, y_pred) # 0.9015176


# 4) real value vs pred value
plot(y_pred, col='red', pch = 18, type='o')
par(new = T) # 그래프 겹치기 
plot(y_true, col='blue', pch = 19, type='o',
     axes = FALSE, ann = FALSE)
# 범례
legend('topleft', legend = c('predict value', 'real value'),
       col = c('red', 'blue'), pch = c(18, 19), lty=1)



##########################################
##  5. 선형회귀분석 잔차검정과 모형진단
##########################################

# 1. 변수 모델링  
# 2. 회귀모델 생성 
# 3. 모형의 잔차검정 
#   1) 잔차의 등분산성 검정
#   2) 잔차의 정규성 검정 
#   3) 잔차의 독립성(자기상관) 검정 
# 4. 다중공선성 검사 
# 5. 회귀모델 생성/ 평가 


names(iris)

# 1. 변수 모델링 : y:Sepal.Length <- x:Sepal.Width,Petal.Length,Petal.Width
formula = Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width


# 2. 회귀모델 생성 
model <- lm(formula = formula,  data=iris)
model
names(model) # 12칼럼 

res <- model$residuals # 잔차(오차)
res


# 3. 모형의 잔차검정
plot(model)
#Hit <Return> to see next plot: 잔차 vs 적합값 -> 패턴없이 무작위 분포(포물선 분포 좋지않은 적합) 
#Hit <Return> to see next plot: Normal Q-Q -> 정규분포 : 대각선이면 잔차의 정규성 
#Hit <Return> to see next plot: 척도 vs 위치 -> 중심을 기준으로 고루 분포 
#Hit <Return> to see next plot: 잔차 vs 지렛대값 -> 중심을 기준으로 고루 분포 

# (1) 등분산성 검정 -> 자료추가 & 변수변환(변수선택, 정규화) 
plot(model, which =  1) 
methods('plot') # plot()에서 제공되는 객체 보기 

# (2) 잔차 정규성 검정 -> 자료추가
attributes(model) # coefficients(계수), residuals(잔차), fitted.values(적합값)
res <- residuals(model) # 잔차 추출 
shapiro.test(res) # 정규성 검정 - p-value = 0.9349 >= 0.05
# 귀무가설 : 정규성과 차이가 없다.

# 정규성 시각화  
hist(res, freq = F) 
qqnorm(res)

# (4) 잔차의 독립성(자기상관 검정 : Durbin-Watson) -> 비선형모델 & 변수변환
install.packages('lmtest')
library(lmtest) # 자기상관 진단 패키지 설치 
dwtest(model) # 더빈 왓슨 값(2~4)
# DW = 2.0604, p-value = 0.6013


# 4. 다중공선성 검사 
library(car)
sqrt(vif(model)) > 2 # TRUE 

# 5. 모델 생성/평가 
formula = Sepal.Length ~ Sepal.Width + Petal.Length 
model <- lm(formula = formula,  data=iris)
summary(model) # 모델 평가











