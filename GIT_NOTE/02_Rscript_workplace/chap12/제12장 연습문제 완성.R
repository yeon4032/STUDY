#################################
## <제12장 연습문제>
################################# 

# 01. mpg의 엔진크기(displ)가 고속도록주행마일(hwy)에 어떤 영향을 미치는가?    
# <조건1> 단순선형회귀모델 생성 
# <조건2> 회귀선 시각화 
# <조건3> 회귀분석 결과 해석 : 모델 유의성검정, 설명력, x변수 유의성 검정  

library(ggplot2)
data(mpg) # 자동차연비 
str(mpg)

x <- mpg$displ # 독립변수 
y <- mpg$hwy # 종속변수 

# 데이터프레임 만들기 
df <- data.frame(x, y) 
head(df)

mpg_lm <- lm(y ~ x, data = df)
mpg_lm
mpg_lm$fitted.values[1:6]

plot(x, y, data = df)
abline(mpg_lm, col = 'red')

summary(mpg_lm)
# 모델 유의성검정 : 통계적으로 유의함  
# 설명력 : 0.585  
# x변수 유의성 검정  
# : 유의미한 수준에서 엔진크기는 주행마일수에 영향을 미친다.


# 02. product 데이터셋을 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.
product <- read.csv("product.csv", header=TRUE)

#  단계1 : 학습데이터(train),검정데이터(test)를 7 : 3 비율로 샘플링
idx <- sample(1:nrow(product), 0.7*nrow(product))
train <- product[idx,] # result중 70%
dim(train) # [1] 184   3
train # 학습데이터
test <- product[-idx, ]
dim(test) # 80  3

#  단계2 : 학습데이터 이용 회귀모델 생성 
#           변수 모델링) y변수 : 제품_만족도, x변수 : 제품_적절성, 제품_친밀도
model <- lm(formula = 제품_만족도 ~ ., data = train)


#  단계3 : 검정데이터 이용 모델 예측치 생성 
y_pred <- predict(model, test)
y_true <- test$'제품_만족도'


#  단계4 : 모델 평가 : cor()함수 이용  
cor(y_true, y_pred) # 0.7534773

y_true[1:10]
y_pred[1:10]

mse <- mean( (y_true - y_pred)^2 )
cat('MSE =', mse)


# 03. ggplot2패키지에서 제공하는 diamonds 데이터 셋을 대상으로 
# carat, table, depth 변수 중 다이아몬드의 가격(price)에 영향을 
# 미치는 관계를 다중회귀 분석을 이용하여 예측하시오.
#조건1) 다이아몬드 가격 결정에 가장 큰 영향을 미치는 변수는?
#조건2) 다중회귀 분석 결과를 정(+)과 부(-) 관계로 해설

library(ggplot2)
data(diamonds)

# diamonds에서 비율척도 대상으로 식 작성 
formula <- price ~ carat +  table + depth
head(diamonds)
model <- lm(formula, data=diamonds) 
summary(model) # 회귀분석 결과

# <해설>carat은 price에 정(+)의 영향을 미치지만, table과 depth는 부(-)의 영향을 미친다.



