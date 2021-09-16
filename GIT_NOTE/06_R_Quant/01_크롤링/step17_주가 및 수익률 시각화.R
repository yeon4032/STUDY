#step17_주가 및 수익률 시각화


## 데이터 가지고 오기
library(quantmod)
getSymbols('SPY')
prices = Cl(SPY)

##그래프
#방법1
plot(prices, main = 'Price')

#방법2
library(ggplot2)

SPY %>%
  ggplot(aes(x = Index, y = SPY.Close)) +
  geom_line()

#인터랙티브 그래프 나타내기
library(highcharter)

# 왼쪽 상단의 기간을 클릭하면 해당 기간의 수익률만 확인할 수 있으며, 오른쪽 상단에 기간을 직접 입력할 수도 있습니다.
highchart(type = 'stock') %>%
  hc_add_series(prices) %>%
  hc_scrollbar(enabled = TRUE)

#Plotly
#R에서는 단순히 ggplot()을 이용해 나타낸 그림에 ggplotly() 함수를 추가하는 것만으로 인터랙티브한 그래프를 만들어줍니다.
library(plotly)

p = SPY %>%
  ggplot(aes(x = Index, y = SPY.Close)) +
  geom_line()

ggplotly(p)


##연도별 수익률 나타내기
library(PerformanceAnalytics)
library(dplyr)

ret_yearly = prices %>%
  Return.calculate() %>%
  apply.yearly(., Return.cumulative) %>%
  round(4) %>%
  fortify.zoo() %>%
  mutate(Index = as.numeric(substring(Index, 1, 4)))

ggplot(ret_yearly, aes(x = Index, y = SPY.Close)) +
  geom_bar(stat = 'identity') +
  scale_x_continuous(breaks = ret_yearly$Index,
                     expand = c(0.01, 0.01)) +
  geom_text(aes(label = paste(round(SPY.Close * 100, 2), "%"),
                vjust = ifelse(SPY.Close >= 0, -0.5, 1.5)),
            position = position_dodge(width = 1),
            size = 3) +
  xlab(NULL) + ylab(NULL)

#apply.yearly() 함수를 이용해 연도별 수익률을 계산한 뒤 반올림합니다.
#fortify.zoo() 함수를 통해 인덱스에 있는 시간 데이터를 Index 열로 이동합니다.
#mutate() 함수 내에 substring() 함수를 통해 Index의 1번째부터 4번째 글자, 즉 연도에 해당하는 부분을 뽑아낸 후 숫자 형태로 저장합니다.
#ggplot() 함수를 이용해 x축에는 연도가 저장된 Index, y축에는 수익률이 저장된 SPY.Close를 입력합니다.
#geom_bar() 함수를 통해 막대 그래프를 그려줍니다.
#scale_x_continuous() 함수를 통해 x축에 모든 연도가 출력되도록 합니다.
#geom_text()를 통해 막대 그래프에 연도별 수익률이 표시되도록 합니다. vjust() 내에 ifelse() 함수를 사용해 수익률이 0보다 크면 위쪽에 표시하고, 0보다 작으면 아래쪽에 표시되도록 합니다.
























