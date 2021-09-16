#step26_멀티팩터 포트폴리오

# 퀄리티: 자기자본이익률, 매출총이익, 영업활동현금흐름
# 밸류: PER, PBR, PSR, PCR
# 모멘텀: 3개월 수익률, 6개월 수익률, 12개월 수익률
# 변경 가능

library(xts)
library(stringr)

# 데이터
KOR_fs = readRDS('data/KOR_fs.Rds')
KOR_value = read.csv('data/KOR_value.csv', row.names = 1,
                     stringsAsFactors = FALSE)
KOR_price = read.csv('data/KOR_price.csv', row.names = 1,
                     stringsAsFactors = FALSE) %>% as.xts()

KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)


#재무제표, 가치지표, 주가 데이터 계산
if ( lubridate::month(Sys.Date()) %in% c(1,2,3,4) ) {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 2))
} else {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 1))
}

# ROE,GPA,CFO
quality_roe = (KOR_fs$'지배주주순이익' / KOR_fs$'자본')[num_col]
quality_gpa = (KOR_fs$'매출총이익' / KOR_fs$'자산')[num_col]
quality_cfo =
  (KOR_fs$'영업활동으로인한현금흐름' / KOR_fs$'자산')[num_col]

## quality 

# quality_P
quality_profit =
  cbind(quality_roe, quality_gpa, quality_cfo) %>%
  setNames(., c('ROE', 'GPA', 'CFO'))

# quaility 지표 합산
factor_quality = quality_profit %>%
  mutate_all(list(~min_rank(desc(.)))) %>%
  mutate_all(list(~scale(.))) %>%
  rowSums()

# 시각화
factor_quality %>% 
  data.frame() %>%
  ggplot(aes(x = `.`)) +
  geom_histogram()


## value

#rowSums() 함수를 통해 계산된 Z-Score를 종목별로 합쳐줍니다
factor_value = KOR_value %>%
  mutate_all(list(~min_rank(.))) %>%
  mutate_all(list(~scale(.))) %>%
  rowSums()

# 시각화
factor_value %>% 
  data.frame() %>%
  ggplot(aes(x = `.`)) +
  geom_histogram()


##수익률 Momentum
library(PerformanceAnalytics)
library(dplyr)

ret_3m = Return.calculate(KOR_price) %>% xts::last(60) %>%
  sapply(., function(x) {prod(1+x) - 1})
ret_6m = Return.calculate(KOR_price) %>% xts::last(120) %>%
  sapply(., function(x) {prod(1+x) - 1})
ret_12m = Return.calculate(KOR_price) %>% xts::last(252) %>%
  sapply(., function(x) {prod(1+x) - 1})

# 합치기
ret_bind = cbind(ret_3m, ret_6m, ret_12m) %>% data.frame()

#정규화
factor_mom = ret_bind %>%
  mutate_all(list(~min_rank(desc(.)))) %>%
  mutate_all(list(~scale(.))) %>%
  rowSums()

#시각화
factor_mom %>% 
  data.frame() %>%
  ggplot(aes(x = `.`)) +
  geom_histogram()

#상관관계 확인
library(corrplot)

cbind(factor_quality, factor_value, factor_mom) %>%
  data.frame() %>%
  setNames(c('Quality', 'Value', 'Momentum')) %>%
  cor(use = 'complete.obs') %>%
  round(., 2) %>%
  corrplot(method = 'color', type = 'lower',
           addCoef.col = 'black', number.cex = 1,
           tl.cex = 1, tl.srt = 0, tl.col = 'black',
           col =
             colorRampPalette(c('blue', 'white', 'red'))(200),
           mar=c(0,0,0.5,0))


factor_qvm =
  cbind(factor_quality, factor_value, factor_mom) %>%
  data.frame() %>%
  mutate_all(list(~scale(.))) %>%
  mutate(factor_quality = factor_quality * 0.33, # 강도
         factor_value = factor_value * 0.33,     # 강도
         factor_mom = factor_mom * 0.33) %>%     # 강도
  rowSums()

#랭킹 기준 상위 30종목
invest_qvm = rank(factor_qvm) <= 30

#포트폴리오 내 종목들을 대상으로 팩터별 대표적인 지표인 ROE, PBR, 12개월 수익률을 나타냈습니다.
KOR_ticker[invest_qvm, ] %>%
  select('종목코드', '종목명') %>%
  cbind(round(quality_roe[invest_qvm, ], 2)) %>%
  cbind(round(KOR_value$PBR[invest_qvm], 2)) %>%
  cbind(round(ret_12m[invest_qvm], 2)) %>%
  setNames(c('종목코드', '종목명', 'ROE', 'PBR', '12M'))

#마지막으로 포트폴리오 내 종목들의 지표별 평균을 계산한 값입니다
cbind(quality_profit, KOR_value, ret_bind)[invest_qvm, ] %>% 
  apply(., 2, mean) %>% round(3) %>% t()
