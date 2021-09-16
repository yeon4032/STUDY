# step04_크롤링 기본 

library(httr)
library(rvest)

i = 0
ticker = list()
url = paste0('https://finance.naver.com/sise/',
             'sise_market_sum.nhn?sosok=',i,'&page=1')
down_table = GET(url)

navi.final = read_html(down_table, encoding = 'EUC-KR') %>%
  html_nodes(., '.pgRR') %>%
  html_nodes(., 'a') %>%
  html_attr(., 'href')


navi.final = navi.final %>%
  strsplit(., '=') %>%
  unlist() %>%
  tail(., 1) %>%
  as.numeric()
#############################################################################
#네이버 금융 에서 전체 코스피 주식 정보 가지고 오기

i = 0 # 코스피
j = 1 # 첫번째 페이지
#URL 
url = paste0('https://finance.naver.com/sise/',
             'sise_market_sum.nhn?sosok=',i,"&page=",j)
down_table = GET(url)

Sys.setlocale("LC_ALL", "English")

# 가지고오기
table = read_html(down_table, encoding = "EUC-KR") %>% # URL 을 read_html로 읽는다
  html_table(fill = TRUE) # html_table을 사용해서  table 만 가지고 온다.
table = table[[2]] #2번째 table을 가지고와 table 이라는 변수에 저장한다.

Sys.setlocale("LC_ALL", "Korean")

print(head(table))

# 이 중 마지막 열인 토론실은 필요 없는 열이며, 첫 번째 행과 같이 
# 아무런 정보가 없는 행도 있습니다. 이를 다음과 같이 정리해줍니다.
table[, ncol(table)] = NULL
table = na.omit(table)
print(head(table))

#이제 필요한 정보는 6자리 티커입니다. 티커 역시 개발자 도구 화면을 통해 tbody → td → a 
#태그의 href 속성에 위치하고 있음을 알고 있습니다. 티커를 추출하는 코드는 다음과 같습니다.
symbol = read_html(down_table, encoding = 'EUC-KR') %>%
  html_nodes(., 'tbody') %>%
  html_nodes(., 'td') %>%
  html_nodes(., 'a') %>%
  html_attr(., 'href')

print(head(symbol, 10))

# 
library(stringr)
symbol = sapply(symbol, function(x) {
  str_sub(x, -6, -1)  # 뒤에 6자리 데이터를 뽑아라
})

symbol=unique(symbol)
print(head(symbol, 10))


table$N = symbol
colnames(table)[1] = '종목코드'

rownames(table) = NULL
ticker[[j]] = table
