# step19_저변동성 전략
#금융 시장에서 변동성은 수익률이 움직이는 정도로서, 일반적으로 표준편차가 사용됩니다.

#먼저 최근 1년 일간 수익률 기준 변동성이 낮은 30종목을 선택하겠습니다.
library(stringr)
library(xts)
library(PerformanceAnalytics)
library(magrittr)
library(ggplot2)
library(dplyr)

KOR_price = read.csv('data/KOR_price.csv', row.names = 1,
                     stringsAsFactors = FALSE) %>% as.xts()
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 
# 코스 숫자 6자리 고정
KOR_ticker$'종목코드' = 
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)

ret = Return.calculate(KOR_price)
std_12m_daily = xts::last(ret, 252) %>% apply(., 2, sd) %>%
  multiply_by(sqrt(252))


#저장해둔 가격 정보와 티커 정보를 불러옵니다. 가격 정보는 as.xts() 함수를 통해 xts 형태로 변경합니다.
#Return.calculate() 함수를 통해 수익률을 구합니다.
#last() 함수는 마지막 n개 데이터를 선택해주는 함수이며, 1년 영업일 기준인 252개 데이터를 선택합니다. dplyr 패키지의 last() 함수와 이름이 같으므로, xts::last() 형식을 통해 xts 패키지의 함수임을 정의해줍니다.
#apply() 함수를 통해 sd 즉 변동성을 계산해주며, 연율화를 해주기 위해 multiply_by() 함수를 통해  √252를 곱해줍니다.


#시각화
std_12m_daily %>% 
  data.frame() %>%
  ggplot(aes(x = (`.`))) +
  geom_histogram(binwidth = 0.01) +
  annotate("rect", xmin = -0.02, xmax = 0.02,
           ymin = 0,
           ymax = sum(std_12m_daily == 0, na.rm = TRUE) * 1.1,
           alpha=0.3, fill="red") +
  xlab(NULL)

# 변동성이 0 인종모은 거래 정지 종목이기 때문에 삭제 한다.
std_12m_daily[std_12m_daily == 0] = NA


#변동성이 낮은 30개 종목 가지고 온다.
std_12m_daily[rank(std_12m_daily) <= 30]

# 30개 종목 시각화
std_12m_daily[rank(std_12m_daily) <= 30] %>%
  data.frame() %>%
  ggplot(aes(x = rep(1:30), y = `.`)) +
  geom_col() +
  xlab(NULL)

#이번에는 해당 종목들의 티커 및 종목명을 확인하겠습니다.
invest_lowvol = rank(std_12m_daily) <= 30
KOR_ticker[invest_lowvol, ] %>%
  select(`종목코드`, `종목명`) %>%
  mutate(`변동성` = round(std_12m_daily[invest_lowvol], 4))

########################################################################
#주간 변동성을 기준으로 저변동성 종목을 선택하겠습니다.
std_12m_weekly = xts::last(ret, 252) %>%
  apply.weekly(Return.cumulative) %>%
  apply(., 2, sd) %>% multiply_by(sqrt(52))
#apply.weekly() 함수 내 Return.cumulative를 입력해 주간 수익률을 계산하며

#변동성 0 제거
std_12m_weekly[std_12m_weekly == 0] = NA 

#랭킹 
std_12m_weekly[rank(std_12m_weekly) <= 30]

# 주간 수익률의 변동성이 낮은 30종목을 선택해 종목코드, 종목명, 연율화 변동성을 확인합니다.
invest_lowvol_weekly = rank(std_12m_weekly) <= 30
KOR_ticker[invest_lowvol_weekly, ] %>%
  select(`종목코드`, `종목명`) %>%
  mutate(`변동성` =
           round(std_12m_weekly[invest_lowvol_weekly], 4))

#intersect() 함수를 통해 일간 변동성 기준과 주간 변동성 기준 모두에 포함되는 종목을 찾을 수 있습니다.
intersect(KOR_ticker[invest_lowvol, '종목명'],
          KOR_ticker[invest_lowvol_weekly, '종목명'])




