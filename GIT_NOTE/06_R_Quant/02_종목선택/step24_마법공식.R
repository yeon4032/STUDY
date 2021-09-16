#step24_마법공식
#하나의 팩터만을 보고 투자하는 것보다, 둘 혹은 그 이상의 팩터를 결합해 투자해야 훨씬 좋은 포트폴리오를 구성할 수 있으며, 이러한 방법을 멀티팩터라고 합니다. 그중에서도 밸류와 퀄리티의 조합은 전통적으로 많이 사용된 방법이며,


#퀄리티와 밸류 간의 관계
library(stringr)
library(dplyr)

KOR_value = read.csv('data/KOR_value.csv', row.names = 1,
                     stringsAsFactors = FALSE)
KOR_fs = readRDS('data/KOR_fs.Rds')
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 

data_pbr = KOR_value['PBR']

if ( lubridate::month(Sys.Date()) %in% c(1,2,3,4) ) {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 2))
} else {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 1))
}

data_gpa =
  (KOR_fs$'매출총이익' / KOR_fs$'자산')[num_col] %>%
  setNames('GPA')

cbind(data_pbr, -data_gpa) %>%
  cor(method = 'spearman', use = 'complete.obs') %>% round(4)

##         PBR     GPA
## PBR  1.0000 -0.1737
## GPA -0.1737  1.0000

cbind(data_pbr, data_gpa) %>%
  mutate(quantile_pbr = ntile(data_pbr, 5)) %>%
  filter(!is.na(quantile_pbr)) %>%
  group_by(quantile_pbr) %>%
  summarise(mean_gpa = mean(GPA, na.rm = TRUE)) %>%
  ggplot(aes(x = quantile_pbr, y = mean_gpa)) +
  geom_col() +
  xlab('PBR') + ylab('GPA')

#설명
#ntile() 함수를 이용해 PBR을 5분위수로 나누어줍니다.
#PBR이 없는 종목은 제외합니다.
#group_by()함수를 통해 PBR의 분위수별 그룹을 묶어줍니다.
#각 PBR 그룹별 GPA의 평균값을 구해줍니다.
#ggplot() 함수를 이용해 시각화를 해줍니다


#마법공식 이해하기
#첫 번째 지표는 이율(Earnings Yield)로서 기업의 수익을 기업의 가치로 나는 값입니다.이는 PER의 역수와 비슷하며, 밸류 지표 중 하나입니다. 
#두 번째 지표는 투하자본 수익률(Return on Capital)로서 기업의 수익을 투자한 자본으로 나눈 값입니다. 
#마법공식은 이 두 가지 지표의 랭킹을 각각 구한 후 랭킹의 합 기준 상위 30개 종목을 1년간 보유한 후 매도하는 전략입니다.
#데이터를 수집하기 어려워 많은 투자자들이 이율 대신 PER를 사용하고, 투하자본 수익률 대신 ROE를 사용합니다. 

library(stringr)
library(dplyr)

#데이터
KOR_value = read.csv('data/KOR_value.csv', row.names = 1,
                     stringsAsFactors = FALSE)
KOR_fs = readRDS('data/KOR_fs.Rds')
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1,
                      stringsAsFactors = FALSE) 
# 코드 숫자 고정
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, 'left', 0)

# 계산
if ( lubridate::month(Sys.Date()) %in% c(1,2,3,4) ) {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 2))
} else {
  num_col = str_which(colnames(KOR_fs[[1]]), as.character(lubridate::year(Sys.Date()) - 1))
}

# 분자
magic_ebit = (KOR_fs$'지배주주순이익' + KOR_fs$'법인세비용' +
                KOR_fs$'이자비용')[num_col]

# 분모
magic_cap = KOR_value$PER * KOR_fs$'지배주주순이익'[num_col]      # 시가총액
magic_debt = KOR_fs$'부채'[num_col]                               # 총부채

magic_excess_cash_1 = KOR_fs$'유동부채' - KOR_fs$'유동자산' +     # 유동성자산    
  KOR_fs$'현금및현금성자산'
magic_excess_cash_1[magic_excess_cash_1 < 0] = 0
magic_excess_cash_2 =
  (KOR_fs$'현금및현금성자산' - magic_excess_cash_1)[num_col]

magic_ev = magic_cap + magic_debt - magic_excess_cash_2

# 이익수익률
magic_ey = magic_ebit / magic_ev


#투하 자본 수익률
magic_ic = ((KOR_fs$'유동자산' - KOR_fs$'유동부채') +
              (KOR_fs$'비유동자산' - KOR_fs$'감가상각비'))[num_col]
magic_roc = magic_ebit / magic_ic

# 두 지표를 활용해 마법공식 포트폴리오를 구성
invest_magic = rank(rank(-magic_ey) + rank(-magic_roc)) <= 30

KOR_ticker[invest_magic, ] %>%
  select(`종목코드`, `종목명`) %>%
  mutate(`이익수익률` = round(magic_ey[invest_magic, ], 4),
         `투하자본수익률` = round(magic_roc[invest_magic, ], 4))

























