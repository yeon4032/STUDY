#step06: 코스피 코스닥 데이터 


library(httr)
library(rvest)
library(readr)

#1.
gen_otp_url =
  'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
gen_otp_data = list(
  mktId = 'STK',
  trdDd = '20200327',
  money = '1',
  csvxls_isNo = 'false',
  name = 'fileDown',
  url = 'dbms/MDC/STAT/standard/MDCSTAT03901'
)
otp = POST(gen_otp_url, query = gen_otp_data) %>%
  read_html() %>%
  html_text()

# gen_otp_url에 원하는 항목을 제출할 URL을 입력합니다.
# 개발자 도구 화면에 나타는 쿼리 내용들을 리스트 형태로 입력합니다. 이 중 mktId의 STK는 코스피에 해당하는 내용이며, 코스닥 데이터를 받고자 할 경우 KSQ를 입력해야 합니다.
# POST() 함수를 통해 해당 URL에 쿼리를 전송하면 이에 해당하는 데이터를 받게 됩니다.
# read_html()함수를 통해 HTML 내용을 읽어옵니다.
# html_text() 함수는 HTML 내에서 텍스트에 해당하는 부분만을 추출합니다. 이를 통해 OTP 값만 추출하게 됩니다


#2.OTP를 제출하면, 우리가 원하는 데이터를 다운로드할 수 있습니다.

down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
down_sector_KS = POST(down_url, query = list(code = otp),
                      add_headers(referer = gen_otp_url)) %>%   #referer 를 이용행서 위의 url 을위해하여 왔다는걸 보여줌
  read_html(encoding = 'EUC-KR') %>%
  html_text() %>%
  read_csv()

#OTP를 제출할 URL을 down_url에 입력합니다.
#POST() 함수를 통해 위에서 부여받은 OTP 코드를 해당 URL에 제출합니다.
#add_headers() 구문을 통해 리퍼러(referer)를 추가해야 합니다. 리퍼러란 링크를 통해서 각각의 웹사이트로 방문할 때 남는 흔적입니다. 거래소 데이터를 다운로드하는 과정을 살펴보면 첫 번째 URL에서 OTP를 부여받고, 이를 다시 두번째 URL에 제출했습니다. 그런데 이러한 과정의 흔적이 없이 OTP를 바로 두번째 URL에 제출하면 서버는 이를 로봇으로 인식해 데이터를 반환하지 않습니다. 따라서 add_headers() 함수를 통해 우리가 거쳐온 과정을 흔적으로 남겨 야 데이터를 반환하게 되며 첫 번째 URL을 리퍼러로 지정해줍니다.
#read_html()과 html_text() 함수를 통해 텍스트 데이터만 추출합니다. EUC-KR로 인코딩이 되어 있으므로 read_html() 내에 이를 입력해줍니다.
#read_csv() 함수는 csv 형태의 데이터를 불러옵니다.

print(down_sector_KS)

# down_sector 변수에는 산업별 현황 데이터가 저장되었습니다. 
#코스닥 시장의 데이터도 다운로드 받도록 하겠습니다.

gen_otp_data = list(
  mktId = 'KSQ', # 코스닥으로 변경
  trdDd = '20210108',
  money = '1',
  csvxls_isNo = 'false',
  name = 'fileDown',
  url = 'dbms/MDC/STAT/standard/MDCSTAT03901'
)
otp = POST(gen_otp_url, query = gen_otp_data) %>%
  read_html() %>%
  html_text()

down_sector_KQ = POST(down_url, query = list(code = otp),
                      add_headers(referer = gen_otp_url)) %>%
  read_html(encoding = 'EUC-KR') %>%
  html_text() %>%
  read_csv()

#코스피 데이터와 코스닥 데이터를 하나로 합치도록 합니다
down_sector = rbind(down_sector_KS, down_sector_KQ)

#csv 파일로 
ifelse(dir.exists('data'), FALSE, dir.create('data'))
write.csv(down_sector, 'data/krx_sector.csv')
