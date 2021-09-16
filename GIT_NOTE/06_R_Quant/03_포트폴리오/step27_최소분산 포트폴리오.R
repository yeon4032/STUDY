#step27_최소분산 포트폴리오

library(quantmod)
library(PerformanceAnalytics)
library(magrittr)

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

#가격 정보 저장
prices = do.call(cbind,
                 lapply(symbols, function(x) Ad(get(x)))) %>%
  setNames(symbols)

# 수익률
rets = Return.calculate(prices) %>% na.omit()

#시각화(correlation)
library(tidyr)
library(dplyr)
library(corrplot)

cor(rets) %>%
  corrplot(method = 'color', type = 'lower',
           addCoef.col = 'black', number.cex = 0.7,
           tl.cex = 1, tl.srt = 0, tl.col = 'black',
           col =
             colorRampPalette(c('blue', 'white', 'red'))(200),
           mar = c(0,0,0.5,0))

#분산-공분산 행렬
covmat = cov(rets)


# 최소분산 포트폴리오
#optimalPortfolio() 함수를 이용한 최적화

#형식
#optimalPortfolio(Sigma, mu = NULL, semiDev = NULL,
#                 control = list())

#mu와 semiDev는 각각 기대수익률과 세미 편차(Semi Deviation)

#control 부분
#종류	입력값	내용
#type	minvol	최소분산 포트폴리오
#type	invvol	역변동성 포트폴리오
#type	erc	위험 균형 포트폴리오
#type	maxdiv	최대 분산효과 포트폴리오
#type	riskeff	위험-효율적 포트폴리오

#종류	    입력값	내용
#constraint	lo	최소 투자 비중이 0 보다 클것
#constraint	user	최소(LB) 및 최대 투자 비중(UB) 설정

library(RiskPortfolios)

w_3 = optimalPortfolio(covmat,
                       control = list(type = 'minvol',
                                      constraint = 'lo')) %>%
  round(., 4) %>%
  setNames(colnames(rets))

print(w_3)  
#SPY    IEV    EWJ    EEM    TLT    IEF    IYR    RWX    GLD    DBC 
#0.1406 0.0000 0.0011 0.0000 0.0000 0.7927 0.0000 0.0000 0.0000 0.0656 

#시각화
library(ggplot2)

data.frame(w_3) %>%
  ggplot(aes(x = factor(rownames(.), levels = rownames(.)),
             y = w_3)) +
  geom_col() +
  xlab(NULL) + ylab(NULL)

#문제점
#특정 자산에 대부분의 비중인 79.32%를 투자하는 편중된 결과가 나옵니다

#해결방법
#최소 및 최대 투자비중 제약조건
w_6 = optimalPortfolio(covmat,
                       control = list(type = 'minvol',
                                      constraint = 'user',
                                      LB = rep(0.05, 10),       # 10개의 상품에 최소 5% 투자
                                      UB = rep(0.20, 10))) %>%  # 10개의 상품에 최대 20% 투자
  round(., 4) %>%
  setNames(colnames(rets))

print(w_6)
# SPY  IEV  EWJ  EEM  TLT  IEF  IYR  RWX  GLD  DBC 
#0.05 0.05 0.05 0.05 0.20 0.20 0.05 0.05 0.20 0.10 

# 시각화
data.frame(w_4) %>%
  ggplot(aes(x = factor(rownames(.), levels = rownames(.)),
             y = w_4)) +
  geom_col() +
  geom_hline(aes(yintercept = 0.05), color = 'red') +
  geom_hline(aes(yintercept = 0.20), color = 'red') +
  xlab(NULL) + ylab(NULL)

# 각 자산별 제약조건의 추가
w_7 = optimalPortfolio(covmat,
                       control = list(type = 'minvol',
                                      constraint = 'user',
                                      LB = c(0.10, 0.10, 0.05, 0.05, 0.10, 0.10, 0.05, 0.05,0.03,0.03), # 10개의 상품에 가각 최소 최대 값을 입력하면 된다.    
                                      UB = c(0.25, 0.25, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.8, 0.8))) %>%  # 10개의 상품에 가각 최소 최대 값을 입력하면 된다.
  round(., 4) %>%
  setNames(colnames(rets))
print(w_7)
#SPY  IEV  EWJ  EEM  TLT  IEF  IYR  RWX  GLD  DBC 
#0.10 0.10 0.05 0.05 0.20 0.20 0.05 0.05 0.17 0.03

