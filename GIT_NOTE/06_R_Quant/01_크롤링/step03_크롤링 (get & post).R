#step03_크롤링 (get & post)

#네이버 금융 속보 크롤링 (get 방식)

library(rvest)
library(httr)

url = 'https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258'
data = GET(url)

print(data)

data_title = data %>%
  read_html(encoding = 'EUC-KR') %>%
  html_nodes('dl') %>%                #  dl 
  html_nodes('.articleSubject') %>%   # class를 지정 -> . 을사용해야한다.
  html_nodes('a') %>%                 # 태그 
  html_attr('title')                  # 속성 찾을겨우 attr / 링클를 원할경우 title 대신 href 사용

print(data_title)


# POST 방식

library(httr)
library(rvest)

# 기본 언어를 영어로 변경
Sys.setlocale("LC_ALL", "English")

# post 형식 사이트에서 URL 찾는방법
# F12 -> Network -> 찾고 싶은 날짜나 정보 클릭 -> Network -> Name -> Request URL
url = 'https://dev-kind.krx.co.kr/disclosure/todaydisclosure.do'  # F12 -> Network -> 찾고 싶은 날짜나 정보 클릭 -> Network -> Name -> Request URL

# Form Data를 body에 기입 해야한다 (URL 찾은 곧 및에 있음)
data = POST(url, body = 
              list(
                method = 'searchTodayDisclosureSub',
                currentPageSize = '15',
                pageIndex = '1',
                orderMode = '0',
                orderStat = 'D',
                forward = 'todaydisclosure_sub',
                chose = 'S',
                todayFlag = 'Y',
                selDate = '2020-03-24'
              ))

data = read_html(data) %>%
  html_table(fill = TRUE) %>%   # html_table : 테이블 정보만 가지고 와라
  .[[1]]

Sys.setlocale("LC_ALL", "Korean") # 다시 언어 한국어로

data













