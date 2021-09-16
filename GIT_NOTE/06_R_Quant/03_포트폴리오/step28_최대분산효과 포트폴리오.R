#step28_최대분산효과 포트폴리오
library(RiskPortfolios)

w = optimalPortfolio(covmat,
                     control = list(type = 'maxdiv',
                                    constraint = 'lo')) %>%
  round(., 4)

print(w)
##  [1] 0.1446 0.0148 0.0451 0.0000 0.2387 0.3449 0.0289 0.0000 0.0717 0.1113

#최소 및 최대 투자비중 제약조건
w_6 = optimalPortfolio(covmat,
                       control = list(type = 'maxdiv',
                                      constraint = 'user',
                                      LB = rep(0.05, 10),       # 10개의 상품에 최소 5% 투자
                                      UB = rep(0.20, 10))) %>%  # 10개의 상품에 최대 20% 투자
  round(., 4) %>%
  setNames(colnames(rets))



#각 자산별 제약조건의 추가
w_7 = optimalPortfolio(covmat,
                       control = list(type = 'maxdiv',
                                      constraint = 'user',
                                      LB = c(0.10, 0.10, 0.05, 0.05, 0.10, 0.10, 0.05, 0.05,0.03,0.03), # 10개의 상품에 가각 최소 최대 값을 입력하면 된다.    
                                      UB = c(0.25, 0.25, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.8, 0.8))) %>%  # 10개의 상품에 가각 최소 최대 값을 입력하면 된다.
  round(., 4) %>%
  setNames(colnames(rets))
print(w_7)
