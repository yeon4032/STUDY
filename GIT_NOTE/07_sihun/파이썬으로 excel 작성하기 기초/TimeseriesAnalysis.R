# chap17_TimeseriesAnalysis

############################
# 시계열분석
############################
# 시계열(Time-Series) : 관측치 또는 통계량의 변화를 시간의 움직임에 
# 따라서 기록하고, 이것을 계열화한 것을 의미한다.
# 시계열 데이터 : 통계숫자를 시간의 흐름에 따라 일정한 간격마다
# 기록한 통계열을 의미한다.

# 관련분야 : 경기예측, 판매예측, 주식시장분석, 예산분석, 투자연구 등
# 현상 이해 -> 가까운 미래 예측

# [단계1] 주식가격 시계열 자료 
setwd('C:\\ITWILL')
library(readxl) # in memory
dataset <- read_excel('price_Date_Dataset4.xlsx')
dim(dataset) # 200   7
print(dataset)

# (1) 시계열 자료 : 주식가격 데이터
Dong_price=dataset$Dong_price
Sin_price=dataset$Sin_price
Han_price=dataset$Han_price
Han_price

Han_price <- Sin_price

#(2) 시계열객체 생성
tsdata <- ts(Han_price) 
tsdata  
# Start = 1 
# End = 200 
# Frequency = 1
#<해설> stats 패키지에서 제공하는 ts()함수를 이용하여 벡터 자료(input)를 대상으로 시계열 객체(tsdata) 생성

#(3) 추세선 시각화
plot(tsdata, type="l", col='red')
# 비정상성시계열로 판단되어 차분을 통해서 정상성시계열로 변경할 필요

# [단계2] 평균 정상화 : 차분 적용   
# 차분을 통해서 비정상성시계열을 정상성시계열로 변환한다. 

# 최적의 차분수 확인 
par(mfrow=c(1,2))
ts.plot(tsdata)
ndiffs(tsdata) # 1

dif <- diff(tsdata) # 1차 차분(현재 시점-이전 시점) - 평균정상화 
plot(dif) # 차분 : 현시점에서 이전시점의 자료를 빼는 연산
# [해설] 비정상성 시계열을 차분하여 평균 0을 중심으로 정상성 시계열로 만든다.
print(dif)

# [실습] 정상성 시계열 여부 확인 
library(tseries) 
adf.test(dif) # # p-value < 0.05 일때 : 정상성 시계열 
# [해설] 유의미한 수준에서 정상성 시계열이라고 할 수 있다.



#[단계3] 모형 식별과 추정 

### 1) 자기상관함수 이용  
acf(na.omit(tsdata), main="자기상관함수", col="red") # 시차 1에서 선형 감소
# 부분자기상관함수 시각화
pacf(na.omit(tsdata), main="부분자기상관함수", col="red") # lag 1에서 유의미한 값 1개 
# ARIMA 모형 식별 - ARIMA(0,1,0)


### 2) auto.arima함수 이용 
# forecast 패키지에서 제공되는 auto.arima() 함수는 시계열 모형을 식별하는 
# 알고리즘에 의해서 최적의 모형과 파라미터를 추정하여 제공   
library(forecast)

arima <- auto.arima(tsdata) # 비정상성 시계열 데이터 이용 
arima
#Series: tsdata 
#ARIMA(0,1,0) -> : 1번 차분한 결과가 정상성시계열 ARMA(0,0) 모형식별

# [실습]차분된 시계열 데이터 모형 식별 
auto.arima(dif) # 1번 차분한 결과 ARIMA(0,0,0) 모형 식별 - 
# 백색자음 : 자기회귀계수와 이동평균회귀계수 모두 0 



#[단계4] 모형 생성 
model <- arima(tsdata, c(2, 1, 0))
model


#[단계5] 모형 진단(모형 타당성 검정)

# (1) 자기상관함수에 의한 모형 진단
tsdiag(model)

# (2)Box-Ljung에 의한 잔차항 모형 진단
Box.test(model$residuals, lag=1, type = "Ljung")
# H0 : 데이터가 독립적인 분포를 가진다.
# # 융박스 p-값이 0.05 이상이면 채택 

# [단계6] 미래 예측
par(mfrow=c(1,2))
fore <- forecast(model, h=3) # 2년 예측 
plot(fore)
fore2 <- forecast(model, h=6) # 6개월 예측 
plot(fore2)

