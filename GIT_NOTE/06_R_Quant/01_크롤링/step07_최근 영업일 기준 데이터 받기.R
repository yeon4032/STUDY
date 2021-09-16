#step07_최근 영업일 기준 데이터 받기

library(httr)
library(rvest)
library(stringr)

url = 'https://finance.naver.com/sise/sise_deposit.nhn'

biz_day = GET(url) %>%
  read_html(encoding = 'EUC-KR') %>%
  html_nodes(xpath =
               '//*[@id="type_1"]/div/ul[2]/li/span') %>%
  html_text() %>%
  str_match(('[0-9]+.[0-9]+.[0-9]+') ) %>%
  str_replace_all('\\.', '')

print(biz_day)

#페이지의 url을 저장합니다.
#GET() 함수를 통해 해당 페이지 내용을 받습니다.
#read_html() 함수를 이용해 해당 페이지의 HTML 내용을 읽어오며, 인코딩은 EUC-KR로 설정합니다.
#html_node() 함수 내에 위에서 구한 Xpath를 입력해서 해당 지점의 데이터를 추출합니다.
#html_text() 함수를 통해 텍스트 데이터만을 추출합니다.
#str_match() 함수 내에서 정규표현식11을 이용해 숫자.숫자.숫자 형식의 데이터를 추출합니다.
#str_replace_all() 함수를 이용해 마침표(.)를 모두 없애줍니다.

