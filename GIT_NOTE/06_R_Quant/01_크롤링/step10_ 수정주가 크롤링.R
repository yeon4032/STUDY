#step10_ 수정주가 크롤링
#투자에 필요한 수정주가를 구할 수 있는 방법은 찾기 힘듭니다. 
#다행히 네이버 금융에서 제공하는 정보를 통해 모든 종목의 수정주가를 매우 손쉽게 구할 수 있습니다.


#url 찾기
#1. 금융에서 특정종목(예: 삼성전자)의 [차트] 탭1
#2. F12 
#3. 일봉클릭
#4. network에서 header의 3가지 파일중 1번째꺼를 더블 클릭하면 주가 인걸 알수있다.
#5. Request url 에서 url 가지고 오기 

library(stringr)

KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1)
print(KOR_ticker$'종목코드'[1])

# stringr 패키지의 str_pad() 함수를 사용해 6자리가 되지 않는 문자는 
# 왼쪽에 0을 추가해 강제로 6자리로 만들어주도록 합니다.
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, side = c('left'), pad = '0')

#첫 번째 종목인 삼성전자의 주가를 크롤링한 후 가공하는 방법
library(xts)

#data 폴더 내에 KOR_price 폴더를 생성합니다.
ifelse(dir.exists('data/KOR_price'), FALSE,
       dir.create('data/KOR_price'))
# i = 1을 입력합니다. 
# 향후 for loop 구문을 통해 i 값만 변경하면 모든 종목의 주가를 다운로드할 수 있습니다.
i = 1
name = KOR_ticker$'종목코드'[i] # 가지고 올 종목명 지정

#xts() 함수를 이용해 빈 시계열 데이터를 생성하며,
#인덱스는 Sys.Date()를 통해 현재 날짜를 입력합니다.
price = xts(NA, order.by = Sys.Date())
print(price)


# 데이터 받아 오기
library(httr)
library(rvest)
library(lubridate)
library(stringr)
library(readr)

from = (Sys.Date() - years(3)) %>% str_remove_all('-') # 시작일
to = Sys.Date() %>% str_remove_all('-') # 끝 나는 날

url = paste0('https://fchart.stock.naver.com/siseJson.nhn?symbol=', name,
             '&requestType=1&startTime=', from, '&endTime=', to, '&timeframe=day')

data = GET(url)
data_html = data %>% read_html %>%
  html_text() %>%
  read_csv()

print(data_html)

먼저 시작일(from)과 종료일(to)에 해당하는 날짜를 입력합니다. Sys.Date()를 통해 오늘 날짜를 불러온 후, 시작일은 years() 함수를 이용해 3년을 빼줍니다. (본인이 원하는 기간 만큼을 빼주면 됩니다.) 그 후 str_remove_all() 함수를 이용해 - 부분을 제거해 yyyymmdd 형식을 만들어 줍니다.
paste0() 함수를 이용해 원하는 종목의 url을 생성합니다. url 중 티커에 해당하는 6자리 부분에 위에서 입력한 name을 설정합니다.
GET() 함수를 통해 페이지의 데이터를 불러옵니다.
read_html() 함수를 통해 HTML 정보를 읽어옵니다.
html_text() 함수를 통해 텍스트 데이터만을 추출합니다.
read_csv() 함수로 csv 형태의 데이터를 불러옵니다.

#
library(readr)

price = read_delim(data_html,delim='|')
print(head(price))

#결과적으로 날짜 및 주가, 거래량, 외국인소진율 데이터가 추출됩니다.
#우리에게 필요한 날짜와 종가에 해당하는 열만 선택하고, 클렌징 작업을 해주도록 하겠습니다.
library(timetk)
library(lubridate)

price = data_html[c(1, 5)]
colnames(price) = (c('Date', 'Price'))
price = na.omit(price)
price$Date = parse_number(price$Date)
price$Date = ymd(price$Date) # price 변수의 Date 칼럼을 날짜 형식으로 변경
price = tk_xts(price, date_var = Date)

print(tail(price))


