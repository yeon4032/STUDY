#step20_모멘텀 포트폴리오 구하기: 12개월 모멘텀
#투자에서 모멘텀이란 주가 혹은 이익의 추세로서, 상승 추세의 주식은 지속적으로 상승하며 하락 추세의 주식은 지속적으로 하락하는 현상을 말합니다

#먼저 최근 1년 동안의 수익률이 높은 30종목을 선택하겠습니다.
library(stringr)
library(xts)
library(PerformanceAnalytics)
library(magrittr)
library(dplyr)

#데이터 로딩
KOR_price = read.csv('data/KOR_price.csv', row.names = 1,
                     stringsAsFactors = FALSE) %>% as.xts()
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 

# 코트 자리수 6자리 고정
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)


#수익률을 계산합니다. 
ret_12m = ret %>% sapply(., function(x) {
  prod(1+x) - 1
})

# 수익률 상위 30 개
ret_12m[rank(-ret_12m) <= 30]

#티커와 종목명, 누적수익률
invest_mom = rank(-ret_12m) <= 30
KOR_ticker[invest_mom, ] %>%
  select(`종목코드`, `종목명`) %>%
  mutate(`수익률` = round(ret_12m[invest_mom], 4))

############################################################################
##모멘텀 포트폴리오 구하기: 위험조정 수익률
#각종 테마나 이벤트에 따른 급등으로 인해 변동성이 지나치게 높은 종목이 있을 수도 있습니다.
#누적수익률을 변동성으로 나누어 위험을 고려해줄 경우, 이러한 종목은 제외되며 상대적으로 안정적인 모멘텀 종목을 선택할 수 있습니다.


#
ret = Return.calculate(KOR_price) %>% xts::last(252) 
ret_12m = ret %>% sapply(., function(x) {
  prod(1+x) - 1
})
std_12m = ret %>% apply(., 2, sd) %>% multiply_by(sqrt(252))
sharpe_12m = ret_12m / std_12m  #샤프지수

#최근 1년에 해당하는 수익률을 선택합니다.
#sapply()와 prod() 함수를 이용해 분자에 해당하는 누적수익률을 계산합니다.
#apply()와 multiply_by() 이용해 분모에 해당하는 연율화 변동성을 계산합니다.
#수익률을 변동성으로 나누어 위험조정 수익률을 계산해줍니다.

#수익률이 높으면서 변동성이 낮은 종목을 선정할 수 있습니다
invest_mom_sharpe = rank(-sharpe_12m) <= 30 
KOR_ticker[invest_mom_sharpe, ] %>%
  select(`종목코드`, `종목명`) %>%
  mutate(`수익률` = round(ret_12m[invest_mom_sharpe], 2),
         `변동성` = round(std_12m[invest_mom_sharpe], 2),
         `위험조정 수익률` =
           round(sharpe_12m[invest_mom_sharpe], 2)) %>%
  as_tibble() %>%
  print(n = Inf)

#티커와 종목명, 누적수익률, 변동성, 위험조정 수익률을 확인할 수 있습니다
intersect(KOR_ticker[invest_mom, '종목명'],
          KOR_ticker[invest_mom_sharpe, '종목명'])

#시각화
library(xts)
library(tidyr)
library(ggplot2)

KOR_price[, invest_mom_sharpe] %>%
  fortify.zoo() %>%
  gather(ticker, price, -Index) %>%
  ggplot(aes(x = Index, y = price)) +
  geom_line() +
  facet_wrap(. ~ ticker, scales = 'free') +
  xlab(NULL) +
  ylab(NULL) +
  theme(axis.text.x=element_blank(),
        axis.text.y=element_blank())

