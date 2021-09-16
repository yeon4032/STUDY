#step23_섹터 중립 포트폴리오
#12개월 모멘텀을 이용한 포트폴리오 구성 방법


#12개월 수익률을 구해 상위 30종목을 선택합니다
library(stringr)
library(xts)
library(PerformanceAnalytics)
library(dplyr)
library(ggplot2)

KOR_price = read.csv('data/KOR_price.csv', row.names = 1,
                     stringsAsFactors = FALSE) %>% as.xts()
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)

ret = Return.calculate(KOR_price) %>% xts::last(252) 
ret_12m = ret %>% sapply(., function(x) {
  prod(1+x) - 1
})

invest_mom = rank(-ret_12m) <= 30


#해당 종목들의 섹터 정보를 추가로 살펴보기
KOR_sector = read.csv('data/KOR_sector.csv', row.names = 1,
                      stringsAsFactors = FALSE)
KOR_sector$'CMP_CD' =
  str_pad(KOR_sector$'CMP_CD', 6, 'left', 0)
data_market = left_join(KOR_ticker, KOR_sector,    #left_join() 함수를 이용해 티커와 결합해 data_market에 저장합니다
                        by = c('종목코드' = 'CMP_CD',
                               '종목명' = 'CMP_KOR'))

#섹터별 종목수를 계산
data_market[invest_mom, ] %>%
  select(`SEC_NM_KOR`) %>%
  group_by(`SEC_NM_KOR`) %>%
  summarize(n = n()) %>%
  ggplot(aes(x = reorder(`SEC_NM_KOR`, `n`),
             y = `n`, label = n)) +
  geom_col() +
  geom_text(color = 'black', size = 4, hjust = -0.3) +
  xlab(NULL) +
  ylab(NULL) +
  coord_flip() +
  scale_y_continuous(expand = c(0, 0, 0.1, 0)) + 
  theme_classic()

#이러한 섹터 쏠림 현상을 제거한 섹터 중립 포트폴리오를 구성해보겠습니다.
sector_neutral = data_market %>%
  select(`종목코드`, `SEC_NM_KOR`) %>%
  mutate(`ret` = ret_12m) %>%
  group_by(`SEC_NM_KOR`) %>%
  mutate(scale_per_sector = scale(`ret`),
         scale_per_sector = ifelse(is.na(`SEC_NM_KOR`),
                                   NA, scale_per_sector))

#설명
#data_market에서 종목코드와 섹터 정보를 선택합니다.
#mutate() 함수를 통해 미리 계산한 12개월 수익률 정보를 새로운 열에 합쳐줍니다.
#group_by() 함수를 통해 섹터별 그룹을 만들어줍니다
#scale() 함수를 이용해 그룹별 정규화를 해줍니다.
#섹터 정보가 없을 경우 NA로 변경합니다.


#따라서 섹터별 정규화 과정을 거친 값으로 비교 분석을 한다면, 섹터 효과가 제거된 포트폴리오를 구성할 수 있습니다.
invest_mom_neutral =
  rank(-sector_neutral$scale_per_sector) <= 30

data_market[invest_mom_neutral, ] %>%
  select(`SEC_NM_KOR`) %>%
  group_by(`SEC_NM_KOR`) %>%
  summarize(n = n()) %>%
  ggplot(aes(x = reorder(`SEC_NM_KOR`, `n`),
             y = `n`, label = n)) +
  geom_col() +
  geom_text(color = 'black', size = 4, hjust = -0.3) +
  xlab(NULL) +
  ylab(NULL) +
  coord_flip() +
  scale_y_continuous(expand = c(0, 0, 0.1, 0)) + 
  theme_classic()

#처럼 group_by() 함수를 통해 손쉽게 그룹별 중립화를 할 수 있으며, 
#글로벌 투자를 하는 경우에는 지역, 국가, 섹터별로도 중립화된 포트폴리오를 구성하기도 합니다.
