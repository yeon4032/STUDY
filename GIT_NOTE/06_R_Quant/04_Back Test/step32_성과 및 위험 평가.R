#step32_성과 및 위험 평가

#전략
#QMJ 팩터란 우량성이 높은 종목들을 매수하고, 우량성이 낮은 종목들을 공매도하는 전략


#할거
#팩터의 수익률을 통해 성과 및 위험을 평가

#시작
################################################
#### 데이터 
#########################################
#QMJ 팩터의 수익률은 AQR Capital Management의 Datasets18에서 엑셀 파일을 다운
library(dplyr)
library(readxl)
library(xts)
library(timetk)

url = 'https://images.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/Quality-Minus-Junk-Factors-Monthly.xlsx'

tf = tempfile(fileext = '.xlsx') #임시로 엑셀 파일을 만들기
download.file(url, tf, mode = 'wb') # url 파일을 tf 파일명에 저장하며

excel_sheets(tf) #함수를 통해 해당 엑셀의 시트명


#우리가 필요한 데이터 가지고오기
df_QMJ = read_xlsx(tf, sheet = 'QMJ Factors', skip = 18) %>% 
  select(DATE, Global)
df_MKT = read_xlsx(tf, sheet = 'MKT', skip = 18) %>%
  select(DATE, Global)
df_SMB = read_xlsx(tf, sheet = 'SMB', skip = 18) %>%
  select(DATE, Global)
df_HML_Devil = read_xlsx(tf, sheet = 'HML Devil',
                         skip = 18) %>%
  select(DATE, Global)
df_UMD = read_xlsx(tf, sheet = 'UMD', skip = 18) %>%
  select(DATE, Global)
df_RF = read_xlsx(tf, sheet = 'RF', skip = 18) 

#tf, sheet: 가지고올 칼럼명, skip:처음 18행 스킵
#select() 함수를 통해 날짜에 해당하는 DATE와 수익률에 해당하는 Global 열만을 선택합니다.  

#데이터셋 만들기
df = Reduce(function(x, y) inner_join(x, y, by = 'DATE'),
            list(df_QMJ, df_MKT, df_SMB,
                 df_HML_Devil,df_UMD, df_RF)) %>%
  setNames(c('DATE','QMJ', 'MKT', 'SMB',
             'HML', 'UMD', 'RF')) %>%
  na.omit() %>%
  mutate(DATE = as.Date(DATE, "%m/%d/%Y"),
         R_excess = QMJ - RF,
         Mkt_excess = MKT - RF) %>%
  tk_xts(date_var = DATE)

#설명
#inner_join() 함수를 통해 DATE를 기준으로 데이터를 묶어주어야 합니다. 해당 함수는 한 번에 두 개 테이블만을 선택할 수 있으므로, Reduce() 함수를 통해 모든 데이터에 inner_join() 함수를 적용합니다.
#setNames() 함수를 통해 열 이름을 입력합니다.
#각 팩터별 시작시점이 다르므로 na.omit() 함수를 통해 NA 데이터를 삭제해줍니다.
#mutate() 함수를 통해 데이터를 변형해줍니다. DATE 열은 mm/dd/yy의 문자열 형식이므로 이를 날짜 형식으로 변경해줍니다. QMJ 팩터 수익률에서 무위험 수익률을 차감해 초과수익률을 구해주며, 시장 수익률에서 무위험 수익률을 차감해 시장위험 프리미엄을 계산해줍니다.
#tk_xts() 함수를 이용해 티블 형태를 시계열 형태로 변경하며, 인덱스는 DATE 열을 설정합니다. 형태를 변경한 후 해당 열은 자동으로 삭제됩니다


##########################################
###결과 측정 지표
##########################################
##수익률 시각화
library(PerformanceAnalytics)
chart.CumReturns(df$QMJ)

#누적수익률
prod((1+df$QMJ)) - 1 

# 연율화 수익률(산술)
mean(df$QMJ) * 12

# 연율화 수익률(기하)
(prod((1+df$QMJ)))^(12 / nrow(df$QMJ)) - 1 


##패키리로 누적수익률,연율화 수익률(산술),연율화 수익률(기하)

Return.cumulative(df$QMJ) # 누적수익률
Return.annualized(df$QMJ, geometric = FALSE) # 연율화 수익률(산술)
Return.annualized(df$QMJ) # 연율화 수익률(기하)

##변동성
sd(df$QMJ) * sqrt(12) # 연율화 변동성
StdDev.annualized(df$QMJ) # 연율화 변동성 패키지
##샤프지수
SharpeRatio.annualized(df$QMJ, Rf = df$RF, geometric = TRUE)
#SharpeRatio.annualized() 함수를 이용하면 포트폴리오 수익률에서 무위험 수익률을 차감한
#geometric을 TRUE로 설정하면 기하평균 기준 연율화 수익률을


##낙폭과 최대낙폭

#낙폭 정보
table.Drawdowns(df$QMJ)
#From     Trough         To   Depth Length To Trough Recovery
#1 2002-10-31 2004-01-31 2008-08-31 -0.2135     71        16       55   #2002-10-31 에서 2004-01-31 까지 21.35%빠지고,2008-08-31에 겨우 회복 했다.
#2 2009-03-31 2009-09-30 2011-12-31 -0.1998     34         7       27
#3 2020-04-30 2021-02-28       <NA> -0.1507     16        11       NA
#4 1992-11-30 1993-08-31 1997-01-31 -0.1408     51        10       41
#5 1998-10-31 1999-04-30 2000-05-31 -0.0869     20         7       13

#최대낙폭
maxDrawdown(df$QMJ)
chart.Drawdown(df$QMJ) #시각화


#위험 조정 수익률 중 사용되는 지표 중 칼마 지수(Calmar Ratio)도 있습니다
CalmarRatio(df$QMJ)
#칼마 지수는 연율화 수익률을 최대낙폭으로 나눈 값으로서,
#안정적인 절대 수익률을 추구하는 헤지펀드에서 많이 참조하는 지표

#################################################################
### 연도별 수익률
#################################################################
apply.yearly(df$QMJ, Return.cumulative) %>% head()


library(lubridate)
library(tidyr)
library(ggplot2)

R.yr = apply.yearly(df$QMJ, Return.cumulative) %>%
  fortify.zoo() %>%
  mutate(Index = year(Index)) %>%
  gather(key, value, -Index) %>%
  mutate(key = factor(key, levels = unique(key)))

ggplot(R.yr, aes(x = Index, y = value, fill = key)) +
  geom_bar(position = "dodge", stat = "identity") +
  ggtitle('Yearly Return') +
  xlab(NULL) +
  ylab(NULL) +
  theme_bw() +
  scale_y_continuous(expand = c(0.03, 0.03)) +
  scale_x_continuous(breaks = R.yr$Index,
                     expand = c(0.01, 0.01)) +
  theme(plot.title = element_text(hjust = 0.5,
                                  size = 12),
        legend.position = 'bottom',
        legend.title = element_blank(),
        legend.text = element_text(size=7),
        axis.text.x = element_text(angle = 45,
                                   hjust = 1, size = 8),
        panel.grid.minor.x = element_blank() ) +
  guides(fill = guide_legend(byrow = TRUE)) +
  geom_text(aes(label = paste(round(value * 100, 2), "%"),
                vjust = ifelse(value >= 0, -0.5, 1.5)),
            position = position_dodge(width = 1),
            size = 3)

#설명
#apply.yearly() 함수를 통해 계산한 연도별 수익률에 ggplot() 함수를 응용하면 막대 그래프로 나타낼 수도 있으며, 시각화를 통해 포트폴리오의 수익률 추이가 더욱 쉽게 확인됩니다.

#간단한 방법
apply.yearly(df$QMJ, Return.cumulative) %>% barplot()

##################################################################
#### 승률 및 롤링 윈도우 값
################################################################
#(포트폴리오 수익률>밴치마크)일수/전체 기간
UpsideFrequency(df$QMJ, MAR = 0)
#UpsideFrequency() 함수는 벤치마크 대비 승률을 계산해줍니다
#MAR 인자는 0이 기본값으로 설정되어 있으며, 원하는 벤치마크가 있을 시 이를 입력해주면 됩니다.

#롤링 윈도우
#롤링 윈도우 승률은 무작위 시점에 투자했을 시 미래 n개월 동안의 연율화 수익률을 구하고, 해당 값이 벤치마크 대비 수익이 높았던 비율을 계산합니다.
roll_12 = df$QMJ %>% apply.monthly(., Return.cumulative) %>%
  rollapply(., 12, Return.annualized) %>% na.omit() %>%
  UpsideFrequency()

roll_24 = df$QMJ %>% apply.monthly(., Return.cumulative) %>%
  rollapply(., 24, Return.annualized) %>% na.omit() %>%
  UpsideFrequency()

roll_36 = df$QMJ %>% apply.monthly(., Return.cumulative) %>%
  rollapply(., 36, Return.annualized) %>% na.omit() %>%
  UpsideFrequency()

roll_win = cbind(roll_12, roll_24, roll_36)
print(roll_win)

#설명
#apply.*() 함수를 이용해 원하는 기간의 수익률로 변경하며, 위 예제에서는 월간 수익률로 변경했습니다.
#rollapply() 함수를 통해 원하는 기간의 롤링 윈도우 통곗값을 구해줍니다. 각각 12개월, 24개월, 36개월 기간에 대해 연율화 수익률을 계산해줍니다.
#계산에 필요한 n개월 동안은 수익률이 없으므로 na.omit()을 통해 삭제해줍니다.
#UpsideFrequency() 함수를 통해 승률을 계산합니다.


# 팩터 회귀분석 및 테이블로 나타내기
#4팩터 모형:CAPM, 사이즈 팩터(SMB), 밸류 팩터(HML),모멘텀 팩터(UMD)

# 회귀모형 
#QMJ−Rf=βm×[Rm−Rf]+βSMB×RSMB+βHML×RHML+βUMD×RUMD

#코딩
reg = lm(R_excess ~ Mkt_excess + SMB + HML + UMD, data = df)
# summary(reg)
summary(reg)$coefficient
##              Estimate Std. Error t value  Pr(>|t|)
## (Intercept)  0.002675  0.0007077   3.780 1.823e-04
## Mkt_excess  -0.259078  0.0163711 -15.825 1.285e-43 #음수 역관계   /t값이 -15.825로 충분히 유의합니다.
## SMB         -0.357021  0.0360893  -9.893 1.145e-20 #음수 역관계   /t값 역시 -9.893로 충분히 유의합니다.
## HML         -0.090912  0.0326987  -2.780 5.703e-03 #음수 역관계   /t값 역시 -2.78로 유의합니다.
## UMD          0.082672  0.0267214   3.094 2.123e-03 #양수 정의관계 /t값은 3.094로 유의하다고 볼 수 있습니다.


#tidy 함수
library(broom)
tidy(reg)
#tidy() 함수를 사용하면 분석 결과 중 계수에 해당하는 값만을 요약해서 볼 수 있습니다.

#stargazer 패키지
library(stargazer)
stargazer(reg, type = 'text', out = 'data/reg_table.html')











