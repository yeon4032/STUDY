# step22_퀄리티 전략
#기업의 우량성
#요소
#Profitability (수익성)
#Earnings stability (수익의 안정성)
#Capital structure (기업 구조)
#Growth (수익의 성장성)
#Accounting quality (회계적 우량성)
#Payout/dilution (배당)
#Investment (투자)


#저PBR 종목 중 재무적으로 우량한 기업을 선정해 투자한다면 성과를 훨씬 개선할 수 있다고 보았습니다.

###F-Score 구하기
library(stringr)
library(ggplot2)
library(dplyr)

#데이터
KOR_fs = readRDS('data/KOR_fs.Rds')
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 
# 코드 숫자 고정
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)


# 수익성
ROA = KOR_fs$'지배주주순이익' / KOR_fs$'자산'
CFO = KOR_fs$'영업활동으로인한현금흐름' / KOR_fs$'자산'
ACCURUAL = CFO - ROA

# 재무성과
LEV = KOR_fs$'장기차입금' / KOR_fs$'자산' (부체/자산)
LIQ = KOR_fs$'유동자산' / KOR_fs$'유동부채'
OFFER = KOR_fs$'유상증자' 

# 운영 효율성
MARGIN = KOR_fs$'매출총이익' / KOR_fs$'매출액'
TURN = KOR_fs$'매출액' / KOR_fs$'자산'

#설명
#ROA는 지배주주순이익을 자산으로 나누어 계산합니다.
#CFO는 영업활동현금흐름을 자산으로 나누어 계산합니다.
#ACCURUAL은 CFO와 ROA의 차이를 이용해 계산합니다.
#LEV(Leverage)는 장기차입금을 자산으로 나누어 계산합니다.
#LIQ(Liquidity)는 유동자산을 유동부채로 나누어 계산합니다.
#우리가 받은 데이터에서는 발행주식수 데이터를 구할 수 없으므로, OFFER에 대한 대용치로 유상증자 여부를 사용합니다.
#MARGIN은 매출총이익을 매출액으로 나누어 계산합니다.
#TURN(Turnover)은 매출액을 자산으로 나누어 계산합니다.

#각 지표들이 조건을 충족하는지 여부를 판단해, 지표별로 1점 혹은 0점을 부여합니다.
if ( lubridate::month(Sys.Date()) %in% c(1,2,3,4) ) {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 2))
} else {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 1))
}

F_1 = as.integer(ROA[, num_col] > 0)
F_2 = as.integer(CFO[, num_col] > 0)
F_3 = as.integer(ROA[, num_col] - ROA[, (num_col-1)] > 0)
F_4 = as.integer(ACCURUAL[, num_col] > 0) 
F_5 = as.integer(LEV[, num_col] - LEV[, (num_col-1)] <= 0) 
F_6 = as.integer(LIQ[, num_col] - LIQ[, (num_col-1)] > 0)
F_7 = as.integer(is.na(OFFER[,num_col]) |
                   OFFER[,num_col] <= 0)
F_8 = as.integer(MARGIN[, num_col] -
                   MARGIN[, (num_col-1)] > 0)
F_9 = as.integer(TURN[,num_col] - TURN[,(num_col-1)] > 0)

#설명
#ROA가 양수면 1점, 그렇지 않으면 0점
#영업활동현금흐름이 양수면 1점, 그렇지 않으면 0점
#최근 ROA가 전년 대비 증가했으면ROA[, num_col] > 0 1점, 그렇지 않으면 0점
#ACCURUAL(CFO - ROA)이 양수면 1점, 그렇지 않으면 0점
#레버리지가 전년 대비 감소했으면 1점, 그렇지 않으면 0점
#유동성이 전년 대비 증가했으면 1점, 그렇지 않으면 0점
#유상증자 항목이 없거나 0보다 작으면 1점, 그렇지 않으면 0점
#매출총이익률이 전년 대비 증가했으면 1점, 그렇지 않으면 0점
#회전율이 전년 대비 증가했으면 1점, 그렇지 않으면 0점

# 합계
F_Table = cbind(F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9) 
F_Score = F_Table %>%
  apply(., 1, sum, na.rm = TRUE) %>%
  setNames(KOR_ticker$`종목명`)

#설명
#cbind() 함수를 통해 열의 형태로 묶어줍니다.
#apply() 함수를 통해 종목별 지표의 합을 더해 F-Score를 계산해줍니다.
#setNanmes() 함수를 통해 종목명을 입력합니다.

#분포 
(F_dist = prop.table(table(F_Score)) %>% round(3))

# 분포 시각화
F_dist %>%
  data.frame() %>%
  ggplot(aes(x = F_Score, y = Freq,
             label = paste0(Freq * 100, '%'))) +
  geom_bar(stat = 'identity') +
  geom_text(color = 'black', size = 3, vjust = -0.4) +
  scale_y_continuous(expand = c(0, 0, 0, 0.05),
                     labels = scales::percent) +
  ylab(NULL) +
  theme_classic() 



# 9점짜리 종목 가지고 오기
invest_F_Score = F_Score %in% c(9)
#출력
KOR_ticker[invest_F_Score, ] %>% 
  select(`종목코드`, `종목명`) %>%
  mutate(`F-Score` = F_Score[invest_F_Score])


#각 지표를 결합하기->(자기자본이익률(ROE), 매출총이익(Gross Profit), 영업활동현금흐름(Cash Flow From Operating)입니다)
library(stringr)
library(ggplot2)
library(dplyr)
library(tidyr)

KOR_fs = readRDS('data/KOR_fs.Rds')
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 

KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)

if ( lubridate::month(Sys.Date()) %in% c(1,2,3,4) ) {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 2))
} else {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 1))
}

# 각각 계산
quality_roe = (KOR_fs$'지배주주순이익' / KOR_fs$'자본')[num_col]
quality_gpa = (KOR_fs$'매출총이익' / KOR_fs$'자산')[num_col]
quality_cfo =
  (KOR_fs$'영업활동으로인한현금흐름' / KOR_fs$'자산')[num_col]

# 합치기
quality_profit =
  cbind(quality_roe, quality_gpa, quality_cfo) %>%
  setNames(., c('ROE', 'GPA', 'CFO'))

#순위 지정
rank_quality = quality_profit %>% 
  mutate_all(list(~min_rank(desc(.))))

# 순위 correlation 지정
cor(rank_quality, use = 'complete.obs') %>%
  round(., 2) %>%
  corrplot(method = 'color', type = 'lower',
           addCoef.col = 'black', number.cex = 1,
           tl.cex = 1, tl.srt = 0, tl.col = 'black',
           col =
             colorRampPalette(c('blue', 'white', 'red'))(200),
           mar=c(0,0,0.5,0))



