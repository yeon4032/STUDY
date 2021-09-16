#step_31동적 자산배분 백테스트
#동적 자산배분을 이용한 포트폴리오는 다음과 같이 구성됩니다.
#1.글로벌 10개 자산 중 과거 12개월 수익률이 높은 5개 자산을 선택합니다.
#2.최소분산 포트폴리오를 구성하며, 개별 투자비중은 최소 10%, 최대 30% 제약조건을 설정합니다.
#3.매월 리밸런싱을 실시합니다.


# 데이터 로딩 & 리턴값 찾기
library(quantmod)
library(PerformanceAnalytics)
library(RiskPortfolios)
library(tidyr)
library(dplyr)
library(ggplot2)

symbols = c('SPY', # 미국 주식
            'IEV', # 유럽 주식 
            'EWJ', # 일본 주식
            'EEM', # 이머징 주식
            'TLT', # 미국 장기채
            'IEF', # 미국 중기채
            'IYR', # 미국 리츠
            'RWX', # 글로벌 리츠
            'GLD', # 금
            'DBC'  # 상품
)
getSymbols(symbols, src = 'yahoo')

prices = do.call(cbind, lapply(symbols, function(x) Ad(get(x)))) %>%
  setNames(symbols)

rets = Return.calculate(prices) %>% na.omit()

#매월 말일의 위치 구하고 & 과거 n기간을 12개월
ep = endpoints(rets, on = 'months')  # 매월 말일의 위치 구하
wts = list()
lookback = 12 # n기간을 12개월
wt_zero = rep(0, 10) %>% setNames(colnames(rets))

#for loop 구문을 통해 매월 말 과거 12개월 수익률을 구한 후 비중을 계산
for (i in (lookback+1) : length(ep)) {
  sub_ret = rets[ep[i-lookback] : ep[i] , ] # 12개월간 수익을 177-13 번 한다.
  cum = Return.cumulative(sub_ret) # 10개 자산의 누적 수익률
  
  K = rank(-cum) <= 5 # True 이면 랭킹안
  covmat = cov(sub_ret[, K]) # True 인 5개만 cov 만들기
  
  wt = wt_zero
  # 최소분산 포트폴리오 만들기
  # wt[K] => k번째 값에 가치를 넣는다. #중요
  wt[K] = optimalPortfolio(covmat,
                           control = list(type = 'minvol',
                                          constraint = 'user',
                                          LB = rep(0.10, 5),
                                          UB = rep(0.30, 5)))
  
  # 투자 비중 allocation
  wts[[i]] = xts(t(wt), order.by = index(rets[ep[i]]))
}

wts = do.call(rbind, wts)

#설명
#for loop 구문을 통해 매월 말 과거 12개월 수익률을 구한 후 비중을 계산하므로, 처음 시작은 i+1인 13부터 가능합니다.

#ep[i]는 현재시점 수익률의 위치를, ep[i-lookback]는 현재부터 12개월 전 수익률의 위치를 의미합니다. 이를 통해 과거 12개월 간 수익률을 찾은 후 sub_ret에 저장합니다.
#Return.cumulative() 함수를 통해 해당 기간의 자산별 누적수익률을 구합니다.
#rank() 함수를 통해 수익률 상위 5개 자산을 선택하며, 내림차순으로 정렬해야하므로 마이너스(-)를 붙여줍니다.
#cov() 함수를 통해 수익률 상위 5개 자산의 분산-공분산 행렬을 구하도록 합니다.
#임시로 비중이 저장될 wt 변수에 위에서 만든 0벡터(wt_zero)를 입력한 후 optimalPortfolio() 함수를 통해 최소분산 포트폴리오를 구성하는 해를 찾습니다. 개별 투자비중의 제한은 최소 10%, 최대 30%를 설정하며, 구해진 해를 wt의 K번째 값에 입력합니다.
#위에서 만들어진 벡터를 xts()를 통해 시계열 형태로 바꾼 후 wts의 i번째 리스트에 저장합니다.
#for loop 구문이 끝난 후 do.call() 함수를 통해 투자비중이 저장된 리스트를 테이블 형태로 바꿔줍니다.

#시각화
GDAA = Return.portfolio(rets, wts, verbose = TRUE)
charts.PerformanceSummary(GDAA$returns, main = '동적자산배분')

#turnover
GDAA$turnover = xts(
  rowSums(abs(GDAA$BOP.Weight -
                timeSeries::lag(GDAA$EOP.Weight)),
          na.rm = TRUE),
  order.by = index(GDAA$BOP.Weight))

chart.TimeSeries(GDAA$turnover)


# 기존에 살펴본 방법으로 회전율을 계산한다면 매월 상당한 매매회전이 발생함이 확인됩니다
#매수 혹은 매도당 발생하는 세금, 수수료, 시장충격 등 총 비용을 0.3%로 가정합니다. 
#포트폴리오 수익률에서 회전율과 총 비용의 곱을 빼면, 비용 후 포트폴리오의 순수익률이 계산됩니다.

# 수수료 고려 수익률
fee = 0.0030
GDAA$net = GDAA$returns - GDAA$turnover*fee

#
cbind(GDAA$returns, GDAA$net) %>%
  setNames(c('No Fee', 'After Fee')) %>%
  charts.PerformanceSummary(main = 'GDAA')


























