# -*- coding: utf-8 -*-
'''
금융데이터 관리
'''
#1. 패키지
import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd

#link :https://finance.naver.com/sise/sise_market_sum.nhn  -> for naver 금융
#
# 네이버 금융에서 코스피와 코스탁 정보 다 가지고 오기 
marketType={"KOSPI":"0", "KOSDAQ":"1"}

stockName_Kospi=[]
for market,code in marketType.items():
    for page in range(1,5): # 나는 코스피 200 을 가지고 오고 싶어서 200등까지만 추출함 
        # 만약 다 가지고 오고 싶다면 page 수를 증가 시기삼 ->즉 range(1,36) 또는 36보다큰수를 넣어
        
        # 2. 데이터 요청 단계
        req = requests.get(f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={code}&page={page}")
        html=req.text
        soup=bs(html,"lxml")
        
        #3. 데이터 추출 (파싱1) 단계
        stockContents= soup.select("#contentarea > div.box_type_l > table.type_2 > tbody > tr")
        
        # note: selenum을 기반으로 한 BeautifulSoup에서는 nth-child 선택자를 지원하지 않는다. 
        #그럼으로 nth-child 선택자를 nth-of-type 으로 변경해야한다. 
        for stockContent in stockContents:
            try:
                stockRank = stockContent.select_one("td.no").text
                stockName = stockContent.select_one("td:nth-of-type(2) > a").text
                stockPrice= stockContent.select_one("td:nth-of-type(3)").text
                stockCap = stockContent.select_one("td:nth-of-type(7)").text
                print(f"{market} {stockRank}등 {stockName} 종목의 현재가는 {stockPrice}원이고, 시가총액은 {stockCap}억 원 입니다.")
                stockName_Kospi.append(stockName)
                
                
            except AttributeError:
                continue


#코스피 200 이름 저장
stockName_Kospi=pd.DataFrame(stockName_Kospi)
stockName_Kospi.to_excel(excel_writer='C:\\ITWILL\\sihun\\stockName_Kospi.xlsx')



















#주식 데이터 가져 와서 차트 그리기

'''
step

1. 한국 거래소 종목 가져오기
2. 주식 데이터 가져오기
3. 차트 그리기
'''
# 금융 데이터 일별 시세를 크롤링 해보기

import pandas as pd
import urllib.request as req # 원격 서버 url 자료 요청

#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]


#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
stock_code.code=stock_code.code.map('{:06d}'.format)


# 2. 주식 데이터 가지고 오기
'''
 https://www.youtube.com/watch?v=aZjdy7-KVYA
 https://www.youtube.com/watch?v=1uXNX5oE6Aw
'''
# 네이버 금융에서 LG화학 1패이지 일일 시세 가지고 오기
url1='https://finance.naver.com/item/sise.nhn?code=051910'
table1=pd.read_html(url1,encoding="cp949")

table1[1] #주요시세
table1[2] #호가
table1[3] #호가 정리
table1[4] #시가 총액
table1[5] # 시총 및 테이블
table1[6] #투자의견
table1[7] #PER같은 지수 
table1[8] # 동일 업종 PER & 등락률
table1[9] # 호가 10단계
table1[10] # 코스피
table1[11] # 코스탁

# 1페이지에 일일 시세 table 있으나 위의 방식으로는 데이터를 가지고 올수 없다.
#그럼으로 우리는 다시 url을 확인해 봐야 한다.

#순서: 왼쪼 마우스-> 검사-> Network-> Doc->page2-> 그럼 name 밑에 파일 생김->clik->Headers-> Request URL 를 사용한다.
url='https://finance.naver.com/item/sise_day.nhn?code=051910&page=1' 
table= pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text) # 왜지? 주피터는 안그
len(table)

temp=table[0]
'''
            날짜        종가      전일비        시가        고가        저가       거래량
0          NaN       NaN      NaN       NaN       NaN       NaN       NaN
1   2021.07.02  849000.0   4000.0  850000.0  856000.0  845000.0  131430.0
2   2021.07.01  845000.0   5000.0  851000.0  870000.0  843000.0  327945.0
3   2021.06.30  850000.0  11000.0  848000.0  863000.0  841000.0  309353.0
4   2021.06.29  839000.0   9000.0  840000.0  840000.0  830000.0  196036.0
5   2021.06.28  830000.0   8000.0  838000.0  839000.0  830000.0   89725.0
6          NaN       NaN      NaN       NaN       NaN       NaN       NaN
7          NaN       NaN      NaN       NaN       NaN       NaN       NaN
8          NaN       NaN      NaN       NaN       NaN       NaN       NaN
9   2021.06.25  838000.0   7000.0  841000.0  849000.0  835000.0  199611.0
10  2021.06.24  831000.0   4000.0  837000.0  839000.0  827000.0  188866.0
11  2021.06.23  835000.0   7000.0  846000.0  846000.0  825000.0  220075.0
12  2021.06.22  842000.0  20000.0  825000.0  844000.0  824000.0  243411.0
13  2021.06.21  822000.0      0.0  812000.0  826000.0  807000.0  144762.0
14         NaN       NaN      NaN       NaN       NaN       NaN       NaN
'''


temp.dropna() # 전처리
'''
            날짜        종가      전일비        시가        고가        저가       거래량
1   2021.07.02  849000.0   4000.0  850000.0  856000.0  845000.0  131430.0
2   2021.07.01  845000.0   5000.0  851000.0  870000.0  843000.0  327945.0
3   2021.06.30  850000.0  11000.0  848000.0  863000.0  841000.0  309353.0
4   2021.06.29  839000.0   9000.0  840000.0  840000.0  830000.0  196036.0
5   2021.06.28  830000.0   8000.0  838000.0  839000.0  830000.0   89725.0
9   2021.06.25  838000.0   7000.0  841000.0  849000.0  835000.0  199611.0
10  2021.06.24  831000.0   4000.0  837000.0  839000.0  827000.0  188866.0
11  2021.06.23  835000.0   7000.0  846000.0  846000.0  825000.0  220075.0
12  2021.06.22  842000.0  20000.0  825000.0  844000.0  824000.0  243411.0
13  2021.06.21  822000.0      0.0  812000.0  826000.0  807000.0  144762.0
'''



# 20페이지 lg화학 url 가지고오기'
import pandas as pd
import urllib.request as req
import requests
#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
stock_code.code=stock_code.code.map('{:06d}'.format)

#크롤링
company='LG화학'
code=stock_code[stock_code.company==company].code.values[0] # 한국 증권 거래소에서 가지고온 데이터

Date=[]
price=[]
for page in range(1,21):
    url=f'https://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'
    table= pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)
    temp=table[0]
    temp=temp.dropna() # temp 형식 DataFrame 
    date=temp.iloc[:,0]
    price_d=temp.iloc[:,1]
    price.extend(price_d) # append or extend
    Date.extend(date)

print(price)
print(Date)

#시각화
import matplotlib.pyplot as plt
plt.plot(Date[:5],price[:5],'b-')



"""
 Winner/Loser 모델을 
 
Winner/Loser 분류를 위한 사전 정보 (Training data)
1. KOSPI200종목의 매 분기별 펀더멘털 정보, 12분기치 
2. 각 샘플의 클래스(Winner, Loser) 분류기준: 주가의 다음 분기 상대수익률이 0% 이상이면
Winner, 다음 분기 상대수익률이 0% 미만이면 Loser로 분류
3. 속성(펀더멘털) 세부 데이터: 분기말 기준 Book to Price (P/B의 역수), 매출액 증가율, 목
표주가 괴리도, 주가 변동성, ROE → 총 5개의 속성을 사용함

"""




























