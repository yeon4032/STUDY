# -*- coding: utf-8 -*-
"""
web 크롤링

유튜브
https://www.youtube.com/watch?v=A-kYNsqJc_o <- 다음 강의임 듣자
"""

# 1. 크롤러만들기 
import requests
from bs4 import BeautifulSoup

def get_bs_obj():
    url='https://finance.naver.com/item/sise.nhn?code=051910'
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    return bs_obj

bs_obj =get_bs_obj()
print(bs_obj)
#모든 html 가지고 온다.



# 2. Naver 금융 주식 데이터 수집하기(현재 주식가격 가지고 오기)
import requests
from bs4 import BeautifulSoup

def get_bs_obj():
    url='https://finance.naver.com/item/sise.nhn?code=051910'
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    return bs_obj

bs_obj =get_bs_obj
no_today =bs_obj.find("p",{"class" : "no_today"}) 
blind_now = no_today.find("span", {"class" : "blind"})
print(no_today)
'''
<p class="no_today">
<em class="X">
<span class="blind">835,000</span>
<span class="no8">8</span><span class="no3">3</span><span class="no5">5</span><span class="shim">,</span><span class="no0">0</span><span class="no0">0</span><span class="no0">0</span>
</em>
</p>
'''
print(blind_now) #<span class="blind">835,000</span>
print(blind_now.text) #835,000

# bs_obj를 받아서 price를 return 하게
def get_price(bs_obj):
    no_today =bs_obj.find("p",{"class" : "no_today"}) # find 함수를 이용해서 class가 no_today 찾기
    blind_now = no_today.find("span", {"class" : "blind"}) # class rk no_today 에서 span 의 blind 에 있는 정보 가지고 오기
    return blind_now.text

bs_obj = get_bs_obj()
price = get_price(bs_obj)
print(price)


# 3.가격 받아오기
# 1)특정 종목의 가격 받아오기
def get_bs_obj(company_code):
    url='https://finance.naver.com/item/sise.nhn?code='+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# bs_obj를 받아서 price를 return 하게
def get_price(bs_obj):
    no_today =bs_obj.find("p",{"class" : "no_today"})
    blind_now = no_today.find("span", {"class" : "blind"})
    return blind_now.text

bs_obj = get_bs_obj("005930")
price = get_price(bs_obj)
print(price)


# 2) 여러 종목의 각격 받아오기
def get_bs_obj(company_code):
    url='https://finance.naver.com/item/sise.nhn?code='+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# bs_obj를 받아서 price를 return 하게
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today =bs_obj.find("p",{"class" : "no_today"})
    blind_now = no_today.find("span", {"class" : "blind"})
    return blind_now.text

price = get_price("005930")
print(price)

# 한번에 여러 주식 현제가격 가지고 오기
company_code=["005930","000660","005680"]
for item in company_code:
    price=get_price(item)
    print(price)

#특정 종목의 봉차트 데이터(open, close, high, low) 받아오기
#Close price
def get_bs_obj(company_code):
    url='https://finance.naver.com/item/sise.nhn?code='+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# bs_obj를 받아서 price를 return 하게
def get_candel_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)
    
    td_first = bs_obj.find("td", {"class":"first"})
    blind=td_first.find("span", {"class" : "blind"})
    
    # close 종가 (전일)
    close= blind.text
    
    return close

# sk하이닉스 
camdle_chart_data = get_candel_chart_data("000660")
print(camdle_chart_data)


# find.All 사용법
html="""
    <html>
        <table>
            <tr>
                <td class='first'>100</td>
                <td>200</td>
            </tr>
            <tr>
                <td>300</td>
                <td>400</td>
            </tr>
        </table>
    </html>
"""
bs_obj = BeautifulSoup(html, "html.parser")
#print(bs.obj)

#100
td_first = bs_obj.find("td", {"class":"first"})
print(td_first.text)

# 200
table = bs_obj.find("table")
tr= table.find("tr")
tds = tr.findAll("td") # list 형으로 반환된다.
print(tds[0].text) # 100
print(tds[1].text) # 200

# 300
trs = table.findAll("tr")
print(trs[0])
print(trs[1])

second_tr=trs[1]
td_300 = second_tr.find("td")
print(td_300.text)

# 400
trs = table.findAll("tr")
second_tr=trs[1]
second_tr_tds = second_tr.findAll("td")
print(second_tr_tds) #[<td>300</td>, <td>400</td>]
td_400 = second_tr_tds[1]
print(td_400.text) # 400



# 특정 종목 봉차트 데이터(open, close, high, low) 받아오기
def get_bs_obj(company_code):
    url='https://finance.naver.com/item/sise.nhn?code='+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# bs_obj를 받아서 price를 return 하게
def get_candel_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)
    
    td_first = bs_obj.find("td", {"class":"first"})
    blind=td_first.find("span", {"class" : "blind"})
    
    # close 종가 (전일)
    close= blind.text
    
    # high 고가
    table = bs_obj.find("table",{"class":"no_info"})
    trs = table.findAll("tr")
    first_tr =trs[0]
    first_tr_tds = first_tr.findAll("td")
    first_tr_tds_second_td =first_tr_tds[1]
    high = first_tr_tds_second_td.find("span",{"class","blind"}).text # text 붙임으로 숫자만 나온다.
    
    #open
    table = bs_obj.find("table",{"class":"no_info"})
    trs = table.findAll("tr")  
    second_tr=trs[1]
    sceond_tr_td_first=second_tr.find("td",{"class":"first"})
    blind_open = sceond_tr_td_first.find("span", {"class":"blind"})
    open=blind_open.text
    
    #low
    table = bs_obj.find("table",{"class":"no_info"})
    trs = table.findAll("tr")  
    second_tr=trs[1]
    second_tr_tds=second_tr.findAll("td")
    second_tr_second_td = second_tr_tds[1]
    blind_low = second_tr_second_td .find("span", {"class":"blind"})
    low = blind_low.text
    
    
    return {"close" : close, "hight": high, "open":open, "low":low}
 
# sk하이닉스 
camdle_chart_data = get_candel_chart_data("000660")
print(camdle_chart_data)
# {'close': '116,000', 'hight': '115,500', 'open': '115,000', 'low': '112,500'}





