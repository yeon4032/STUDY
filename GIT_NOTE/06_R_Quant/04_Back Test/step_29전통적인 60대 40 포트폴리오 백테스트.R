#step_29전통적인 60대 40 포트폴리오 백테스트

library(quantmod)
library(PerformanceAnalytics)
library(magrittr)

#데이터 가지고 오기
ticker = c('SPY', 'TLT')
getSymbols(ticker) # 변수 생성("SPY" "TLT")


#가격 
prices = do.call(cbind,
                 lapply(ticker, function(x) Ad(get(x))))
#리턴값
rets = Return.calculate(prices) %>% na.omit()

# correlation
cor(rets)

# 전통적인 60대 40 포트폴리오 백테스트
portfolio = Return.portfolio(R = rets,
                             weights = c(0.6, 0.4),
                             rebalance_on = 'years',
                             verbose = TRUE)
#설명
#자산의 수익률인 R에는 수익률 테이블인 rets를 입력합니다.
#리밸런싱 비중인 weights에는 60%와 40%를 의미하는 c(0.6, 0.4)를 입력합니다.
#리밸런싱 시기인 rebalance_on에는 연간 리밸런싱에 해당하는 years를 입력합니다. 
#리밸런싱 주기는 이 외에도 quarters, months, weeks, days도 입력이 가능합니다.
#결과물들을 리스트로 확인하기 위해 verbose를 TRUE로 설정합니다.

# 결과값 확인
portfolio$returns
portfolio$BOP.Weight
portfolio$EOP.Weight
portfolio$BOP.Value

# 여러 상품 을 같이 차트로 시각화
portfolios = cbind(rets, portfolio$returns) %>%
  setNames(c('주식', '채권', '60대 40'))

charts.PerformanceSummary(portfolios,
                          main = '60대 40 포트폴리오')
#charts.PerformanceSummary() 함수는 기간별 수익률을 입력 시 누적수익률, 일별 수익률, 드로우다운(낙폭) 그래프를 자동으로 그려줍니다.


# Turnover
#주식 거래량회전율 (Turnover Ratio) 입니다. 거래량회전율이란 일정기간 동안 주식시장에서 주식 매매를 통한 주식 유통 정도를 산출하는 지표입니다.
turnover = xts(
  rowSums(abs(portfolio$BOP.Weight -
                timeSeries::lag(portfolio$EOP.Weight)),
          na.rm = TRUE),
  order.by = index(portfolio$BOP.Weight))

chart.TimeSeries(turnover)


#timeSeries::lag(portfolio$EOP.Weight : 한단개식 뒤로 미루어 주기


