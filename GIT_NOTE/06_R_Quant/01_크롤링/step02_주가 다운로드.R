#step02_주가 다운로드
# 괄호 안에 다운로드하려는 종목의 티커를 입력하면 됩니다.
library(quantmod)
getSymbols('SPY')
head(SPY)
#SPY.Open SPY.High SPY.Low SPY.Close SPY.Volume SPY.Adjusted
#2007-01-03   142.25   142.86  140.57    141.37   94807600     105.7845
#2007-01-04   141.23   142.05  140.61    141.67   69620600     106.0090
#2007-01-05   141.33   141.40  140.38    140.54   76645300     105.1635
#2007-01-08   140.82   141.41  140.25    141.19   71655000     105.6499
#2007-01-09   141.31   141.60  140.40    141.07   75680100     105.5601
#2007-01-10   140.58   141.57  140.30    141.54   72428000     105.9117

Ad(SPY)
Cl(SPY)

chart_Series(SPY)
chart_Series((Ad(SPY)))
library(magrittr)
SPY %>% Ad %>% chart_Series


data = getSymbols('AAPL',
                  from = '2000-01-01', to = '2018-12-31',
                  auto.assign = FALSE)
# auto.assign = FALSE 이면 지정한 변수에 auto.assign = True 이면 심블이름으로 변수 지정

head(data)
# AAPL.Open AAPL.High AAPL.Low AAPL.Close AAPL.Volume AAPL.Adjusted
# 2000-01-03  0.936384  1.004464 0.907924   0.999442   535796800      0.859423
# 2000-01-04  0.966518  0.987723 0.903460   0.915179   512377600      0.786965
# 2000-01-05  0.926339  0.987165 0.919643   0.928571   778321600      0.798481
# 2000-01-06  0.947545  0.955357 0.848214   0.848214   767972800      0.729382
# 2000-01-07  0.861607  0.901786 0.852679   0.888393   460734400      0.763932
# 2000-01-10  0.910714  0.912946 0.845982   0.872768   505064000      0.750496


# 여러 종목을 받을수도 있다.
ticker = c('FB', 'NVDA') 
getSymbols(ticker)


# 국내 주가 도 가능  KS 코스피, KQ 코스닥
getSymbols('005930.KS',
           from = '2000-01-01', to = '2018-12-31')


#FED 에서 정보를 받을경우
getSymbols('DEXKOUS', src='FRED') # src 가 기본값으로느 야후이나 FED 사용시 는 'FRED 로 변경 해야 한다.
chart_Series(DEXKOUS)







