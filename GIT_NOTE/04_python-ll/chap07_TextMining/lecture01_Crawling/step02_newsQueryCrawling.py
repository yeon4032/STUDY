# -*- coding: utf-8 -*-
"""
step02_newsQueryCrawling.py

URL+Query 이용
1.url: http://media.daum.net -> 바로가기: 배열이력
2. https://news.daum.net/newsbox -> 특정 날짜 선택
3. https://news.daum.net/newsbox?regDate=20210601   #URL~~~?Query -> 특정 페이지
4. https://news.daum.net/newsbox?regDate=20210601&tab_cate=NE&page=5   #URL~~~? Query(날짜) & Query (페이지)
"""

import urllib.request as req # 원격 서버 url 자료 요청
from bs4 import BeautifulSoup # source -> html 파싱
'''
query 이용-> news crawling
date:2021.2.1~2021.2.28
page:1~10
'''

# 1. url query 만들기
base_url="https://news.daum.net/newsbox?regDate="

date =list(range(20210201,20210229)) # 2.1 ~ 2.28
date

# regDate=20210201 ~ 20210228

# 1) data 생성 : 변수=[실행문 for문]
url_list = [base_url + str(d) for d in date]
url_list

# 2) page 생성: &page=1 ~ &page=10
pages=['&page='+str(p) for p in range(1,11)]
pages

# 3) final url: url_list(1) vs pages(10)
final_url = []

for url in url_list: # url_list(1)
    for page in pages: # page(10)
        final_url.append(url+page)
    
print(final_url)
len(final_url) #280= 28일 * 10page

# 2. Crawling function
def newsCrawler(url):
    #1. url 요청
    res = req.urlopen(url)
    src = res.read() # source 
    data = src.decode('utf-8') # 디코딩 적용
    
    # 2.html 파싱
    html = BeautifulSoup(data, 'html.parser')
    
    # 3. tag 요소 추출
    #1) tag element 수집
    a_tag = html.select('a[class="link_txt"]')
    
    # 2) 자료수집
    page_news=[] #new 저장
    for a in a_tag:
        cont = str(a.string)# tag의 내용 가져오기-> 문자열 로변환
        page_news.append(cont.strip())
       
    return page_news

# 1page test
page_news = newsCrawler(final_url[0])

len(page_news)#134

today= page_news[40] # 많은 본 뉴스 제외
today


# 3. Crawler 호출
month_news=[] # 1개월 news 저장

cnt=0
for url in final_url:
    cnt+=1
    print('페이지 번호:',cnt)
    try: # 예외처리 -> url 없는 경우    
        page_news = newsCrawler(url) # 함수 호출(1page 반환)
        #month_news.append(page_news[:40]) # [[1page],[2page],...,[280page]]
        month_news.extend(page_news[:40]) # [1page,2page,...,280page]
    except:
        print('해당 url 없음:',url)
    
    
#280*40=11200
len(month_news) #11200


month_news[:40] #extend = month_news[0] # append
'''
append vs extend 1페이지 뉴스
month_news[0] -> append
month_news[:40] -> extend
'''

# file save (크로링한 파일 저장)
path="C:/ITWILL/4_python-ll/workspace/chap07_TextMining/data"

type(month_news) # list

import pickle # list ->  binary file save -> load (list)

# 1) file save
file = open(path + '/new_data.pkl', mode = 'wb') # binary save
pickle.dump(month_news, file) 
print('file saved..')
file.close()

# 2) file load
file = open(path + '/new_data.pkl', mode = 'rb') # binary load
news_data = pickle.load(file)
news_data


