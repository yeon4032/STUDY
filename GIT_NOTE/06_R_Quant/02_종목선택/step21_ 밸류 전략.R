#step21_ 밸류 전략
#가치주 효과란 내재 가치 대비 낮은 가격의 주식(저PER, 저PBR 등)이, 내재 가치 대비 비싼 주식보다 수익률이 높은 현상(Basu 1977)을 뜻합니다.

#PBR을 이용한 포트폴리오를 구성
library(stringr)
library(ggplot2)
library(dplyr)

# 데이터 
KOR_value = read.csv('data/KOR_value.csv', row.names = 1,
                     stringsAsFactors = FALSE)
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 
#코드명 6자리 고정
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)

# rank()를 통해 PBR이 낮은 30종목을 선택
invest_pbr = rank(KOR_value$PBR) <= 30
KOR_ticker[invest_pbr, ] %>%
  select(`종목코드`, `종목명`) %>%
  mutate(`PBR` = round(KOR_value[invest_pbr, 'PBR'], 4))

## 각 지표 결합하기
#저PBR 하나의 지표만으로도 우수한 성과를 거둘 수 있음은 오랜 기간 증명되고 있습니다. 그러나 저평가 
#주식이 계속해서 저평가에 머무르는 가치 함정에 빠지지 않으려면 여러 지표를 동시에 볼 필요도 있습니다.
library(corrplot)

#먼저 mutate_all() 함수를 이용해 모든 열에 함수를 적용해주며, min_rank()를 통해 순위를 구합니다.
rank_value = KOR_value %>% 
  mutate_all(list(~min_rank(.)))

cor(rank_value, use = 'complete.obs') %>%  #NA 종목은 삭제해주기 위해 use = 'complete.obs'를 입력합니다.
  round(., 2) %>%
  corrplot(method = 'color', type = 'lower',
           addCoef.col = 'black', number.cex = 1,
           tl.cex = 1, tl.srt = 0, tl.col = 'black',
           col = colorRampPalette(
             c('blue', 'white', 'red'))(200),
           mar=c(0,0,0.5,0))
# 따라서 지표를 통합적으로 고려하면 분산효과를 기대할 수도 있습니다.


#rowSums() 함수를 이용해 종목별 랭킹들의 합을 구해줍니다. 
rank_sum = rank_value %>%
  rowSums()

# 합 기준 랭킹이 낮은 30종목을 선택
invest_value = rank(rank_sum) <= 30

#당 종목들의 티커, 종목명과 가치지표를 확인
KOR_ticker[invest_value, ] %>%
  select(`종목코드`, `종목명`) %>%
  cbind(round(KOR_value[invest_value, ], 2))

# PBR 과 모든 지표의합 기준 주식 선택
intersect(KOR_ticker[invest_pbr, '종목명'],
          KOR_ticker[invest_value, '종목명'])



















