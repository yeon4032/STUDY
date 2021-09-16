# step18_베타 계산하기
#베타를 구하는 방법을 알아보기 위해 주식시장에 대한 대용치로 KOSPI 200 ETF, 개별주식으로는 전통적 고베타주인 증권주를 이용하겠습니다.

library(quantmod)
library(PerformanceAnalytics)
library(magrittr)

symbols = c('102110.KS', '039490.KS')
getSymbols(symbols)
## [1] "102110.KS" "039490.KS"

prices = do.call(cbind,
                 lapply(symbols, function(x)Cl(get(x))))

ret = Return.calculate(prices)
ret = ret['2016-01::2018-12'] # xts 형식은 이런식으로 기간을 정할수 있다.

#KOSPI 200 ETF인 TIGER 200(102110.KS), 증권주인 키움증권(039490.KS)의 티커를 입력합니다.
#getSymbols() 함수를 이용하여 해당 티커들의 데이터를 다운로드 받습니다.
#lapply() 함수 내에 Cl()과 get()함수를 사용하여 종가에 해당하는 데이터만 추출하며, 리스트 형태의 데이터를 열의 형태로 묶어주기 위해 do.call() 함수와 cbind() 함수를 사용해 줍니다.
#Return.calculate() 함수를 통해 수익률을 계산해 줍니다.
#xts 형식의 데이터는 대괄호 속에 [‘시작일자::종료일자’]와 같은 형태로, 원하는 날짜를 편리하게 선택할 수 있으며, 위에서는 2016년 1월부터 2018년 12월 까지 데이터를 선택합니다.

# 시장과 주식 구분
rm = ret[, 1]
ri = ret[, 2]

# beta 구하기
reg = lm(ri ~rm)
summary(reg)
#Coefficients:
#  Estimate Std. Error t value Pr(>|t|)    
#(Intercept) 0.0003996  0.0007280   0.549    0.583    
#rm          1.7647216  0.0911312  19.365   <2e-16 ***

#독립변수는 첫 번째 열인 KOSPI 200 ETF의 수익률을 선택하며, 종속변수는 두번째 열인 증권주의 수익률을 선택합니다.
#lm() 함수를 통해 손쉽게 선형회귀분석을 실시할 수 있으며, 회귀분석의 결과를 reg 변수에 저장합니다.
#summary() 함수는 데이터의 요약 정보를 나타내며, 해당 예시에서는 회귀분석 결과에 대한 정보를 보여줍니다.


#베타 시각화
plot(as.numeric(rm), as.numeric(ri), pch = 4, cex = 0.3, 
     xlab = "KOSPI 200", ylab = "Individual Stock",
     xlim = c(-0.02, 0.02), ylim = c(-0.02, 0.02))
abline(a = 0, b = 1, lty = 2)
abline(reg, col = 'red')

#plot() 함수를 통해 그림을 그려주며, x축과 y축에 주식시장 수익률과 개별 주식 수익률을 입력합니다. pch는 점들의 모양을, cex는 점들의 크기를 나타내며, xlab과 ylab은 각각 x축과 y축에 들어갈 문구를 나타냅니다. xlim과 ylim은 x 축과 y축의 최소 및 최대 범위를 지정해줍니다.
#첫번째 abline()에서 a는 상수, b는 직선의 기울기, lty는 선의 유형을 나타냅니다. 이를 통해 기울기, 즉 베타가 1일 경우의 선을 점선으로 표현합니다.
#두번째 abline()에 회귀분석 결과를 입력해주면 자동적으로 회귀식을 그려줍니다.

























