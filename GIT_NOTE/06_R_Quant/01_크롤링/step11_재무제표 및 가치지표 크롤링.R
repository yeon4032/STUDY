#step11_재무제표 및 가치지표 크롤링


#1.재무제표
library(httr)
library(rvest)

#Sys.setlocale() 함수를 통해 로케일 언어를 English로 설정합니다
Sys.setlocale("LC_ALL", "English")

#url
url = paste0('http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A005930')

#get
#user_agent() 항목에 웹브라우저 구별을 입력해줍니다. 해당 사이트는 크롤러와 같이 정체가 불분명한 웹브라우저를 통한 접속이 막혀 있어, 마치 모질라 혹은 
#크롬을 통해 접속한 것 처럼 데이터를 요청합니다. 다양한 웹브라우저 리스트는 아래 링크에 나와있습니다.
data = GET(url,
           user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'))
# 데이터 받아 오기
data = data %>%
  read_html() %>%
  html_table()

Sys.setlocale("LC_ALL", "Korean")

# 프린트 
lapply(data, function(x) {
  head(x, 3)})
#순서	내용
#1	포괄손익계산서 (연간)
#2	포괄손익계산서 (분기)
#3	재무상태표 (연간)
#4	재무상태표 (분기)
#5	현금흐름표 (연간)
#6	현금흐름표 (분기)

data_IS = data[[1]]
data_BS = data[[3]]
data_CF = data[[5]]

print(names(data_IS))

# 포괄손익계산서 테이블(data_IS)에는 전년동기, 전년동기(%) 열이 있는데 
#통일성을 위해 해당 열을 삭제합니다.이제 테이블을 묶은 후 클렌징하겠습니다.
data_IS = data_IS[, 1:(ncol(data_IS)-2)]

#이제 테이블을 묶은 후 클렌징하겠습니다.
data_fs = rbind(data_IS, data_BS, data_CF) %>% data.frame()
data_fs[, 1] = gsub('계산에 참여한 계정 펼치기',
                    '', data_fs[, 1])
data_fs = data_fs[!duplicated(data_fs[, 1]), ] # 중복 된내용은 제거

rownames(data_fs) = NULL
rownames(data_fs) = data_fs[, 1] #행이름을 첫번째 열에 추가 
data_fs[, 1] = NULL # 2번째 열 제거

data_fs = data_fs[, substr(colnames(data_fs), 7, 8) == '12'] # 12월 데이터만 가지고 와라

# 데이터 가 str 형에서 num 형으로 변경
library(stringr)

data_fs = sapply(data_fs, function(x) {
  str_replace_all(x, ',', '') %>%
    as.numeric()
}) %>%
  data.frame(., row.names = rownames(data_fs))

print(head(data_fs))

write.csv(data_fs,'B_S_practice.csv')

#2. 가치 지표
표 6.2: 가치지표의 종류
순서	분모
PER	Earnings (순이익)
PBR	Book Value (순자산)
PCR	Cashflow (영업활동현금흐름)
PSR	Sales (매출액)

#분모 부분에 해당하는 데이터만 선택
value_type = c('지배주주순이익',
               '자본',
               '영업활동으로인한현금흐름',
               '매출액')

value_index = data_fs[match(value_type, rownames(data_fs)),
                      ncol(data_fs)]
# 분모에 해당하는 항목을 저장한 후 match() 함수를 이용해 해당 항목이 위치하는 지점을 찾습니다.
# ncol() 함수를 이용해 맨 오른쪽, 즉 최근년도 재무제표 데이터를 선택합니다.

print(value_index)
#[1]  260908 2759480  652870 2368070


# 주가 가지고 오기
#가의 Xpath를 이용해 해당 데이터를 크롤링하겠습니다.
library(readr)

url = 'http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930'
data = GET(url,
           user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'))

price = read_html(data) %>%
  html_node(xpath = '//*[@id="svdMainChartTxt11"]') %>%  # F12 -> copy XPath ->//*[@id="svdMainChartTxt11"]
  html_text() %>%
  parse_number()

print(price)


# 보통주 수찾기
share = read_html(data) %>%
  html_node(
    xpath =
      '//*[@id="svdMainGrid1"]/table/tbody/tr[7]/td[1]') %>%
  html_text()

print(share)
#[1] "5,969,782,550/ 822,886,700"

# 보통주 우선주 구분 
share = share %>%
  strsplit('/') %>%
  unlist() %>%
  .[1] %>%
  parse_number()

#strsplit() 함수를 통해 /를 기준으로 데이터를 나눕니다. 해당 결과는 리스트 형태로 저장됩니다.
#unlist() 함수를 통해 리스트를 벡터 형태로 변환합니다.
#.[1].[1]을 통해 보통주 발행주식수인 첫 번째 데이터를 선택합니다.
#parse_number() 함수를 통해 문자형 데이터를 숫자형으로 변환합니다.

print(share)
#[1] 5969782550


# 가치지표를 계산
data_value = price / (value_index * 100000000 / share) # 주가 는원단위 / 제무제표는 억단이 그럼으로 매칭 해준다.
names(data_value) = c('PER', 'PBR', 'PCR', 'PSR')
data_value[data_value < 0] = NA # 가치지표가 음수인 경우는 NA로 변경해줍니다.

print(data_value)

#저장
write.csv(data_value, 'ratio_value.csv')
