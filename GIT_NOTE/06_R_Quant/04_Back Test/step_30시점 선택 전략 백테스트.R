#step_30시점 선택 전략 백테스트
#방법
# 주가 > 10개월 이동평균 -> 매수
# 주가 < 10개월 이동평균 -> 매도 및 현금 보유
ibrary(quantmod)
library(PerformanceAnalytics)

#데이터
symbols = c('SPY', 'SHY') # S&P 500 수익률을 추종하는 SPY  &  미국 단기채 수익률을 추종하는 SHY
getSymbols(symbols, src = 'yahoo')

# 수익률 찾기
prices = do.call(cbind,
                 lapply(symbols, function(x) Ad(get(x))))
rets = na.omit(Return.calculate(prices))

# 매시점 투자 비중이 다르기 때문에 endpoint 함수를 사용해서 월말 을 찾는다.
ep = endpoints(rets, on = 'months')
print(ep)

#endpoints() 함수를 이용해 매월 말일의 위치를 구합니다. 
#해당 함수는 endpoints(x, on= 'months', k=1)의 형태로 이루어지며 x는 시계열 데이터, on은 원하는 기간, k는 구간 길이를 의미합니다. 즉, 시계열 데이터에서 월말에 
#해당하는 부분의 위치를 반환하며, 매월이 아닌 weeks, quarters, years도 입력이 가능합니다.


#시점별 비중이 입력될 wts를 공백의 리스트 형식으로 저장해주며,
#n개월 이동평균값에 해당하는 lookback 변수는 10을 입력합니다.
wts = list()
lookback = 10

#매월 말 과거 10개월 이동평균을 구한 후 매수 혹은 매도를 선택한 후 비중을 계산합니다.
#과거 10개월에 해당하는 가격의 이동평균이 필요하므로 처음 시작은 i+1 인 11부터 가능합니다

i = lookback + 1
sub_price = prices[ep[i-lookback] : ep[i] , 1] # 10개월치 수익률 # (11-1:10)인거임

sma = mean(sub_price) # 10 개월 평균
head(sub_price, 3)
tail(sub_price, 3)


#시점선택 조건 별 비중
#현재주가 > 10개월 이동평균
#현재 주가 < 10개월 이동평균
wt = rep(0, 2)
wt[1] = ifelse(last(sub_price) > sma, 1, 0) # 주식 부분
wt[2] = 1 - wt[1]                           # 현금

wts[[i]] = xts(t(wt), order.by = index(rets[ep[i]]))



#위 과정을 for loop 구문을 통해 전체 기간에 적용한 백테스트는 다음과 같습니다.
ep = endpoints(rets, on = 'months')
wts = list()
lookback = 10

for (i in (lookback+1) : length(ep)) {
  sub_price = prices[ep[i-lookback] : ep[i] , 1]
  sma = mean(sub_price)
  wt = rep(0, 2)
  wt[1] = ifelse(last(sub_price) > sma, 1, 0)
  wt[2] = 1 - wt[1]
  
  wts[[i]] = xts(t(wt), order.by = index(rets[ep[i]]))
}

wts = do.call(rbind, wts)
# 설명 
#매월 말 과거 10개월 이동평균을 구한 후 현재 주가와 비교해 주식 혹은 현금 투자비중을 구한 후 wts 리스트에 저장합니다.
#그 후 do.call() 함수를 통해 리스트를 테이블로 묶어줍니다.


#수익률 데이터와 비중 데이터가 구해졌으므로 Return.portfolio() 함수를 통해 포트폴리오의 수익률을 계산합니다.
Tactical = Return.portfolio(rets, wts, verbose = TRUE)
portfolios = na.omit(cbind(rets[,1], Tactical$returns)) %>%
  setNames(c('매수 후 보유', '시점 선택 전략'))

charts.PerformanceSummary(portfolios,
                          main = "Buy & Hold vs Tactical")


# turnover
turnover = xts(rowSums(abs(Tactical$BOP.Weight -
                             timeSeries::lag(Tactical$EOP.Weight)),
                       na.rm = TRUE),
               order.by = index(Tactical$BOP.Weight))

chart.TimeSeries(turnover)














