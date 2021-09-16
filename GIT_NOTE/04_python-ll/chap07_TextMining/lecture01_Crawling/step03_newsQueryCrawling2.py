# -*- coding: utf-8 -*-
"""
step03_newsQueryCrawling2.py

년도별 주스 수집:10년간 뉴스 수집
    ex)202011011 ~ 20210330
"""

import urllib.request as req # 원격 서버 url 자료 요청
from bs4 import BeautifulSoup # source -> html 파싱
import pandas as pd #날짜 생성

#1. 수집기간 생성: 시계열 자료 이용
date = pd.date_range(start="2020-11-01",end="2021-03-31") # 5개월
print(date)
len(date) # 151

'''
https://news.daum.net/newsbox?regDate=20210601&tab_cate=NE&page=5 
'''
import re #sub('-','',string)
sdate=[]
for d in date:
    print(re.sub('-','',str(d))[:8]) #"2020-11-01"->"20201101"
    sdate.append(re.sub('-','',str(d))[:8])

print(sdate)

# 2. crawler(date,page=5) 함수 생성
def newsCrawler(date,pages=5): #page 수 =5페이지 고정
    day_news=[] #1일 news
    for page in range(1,pages+1): # 1~5 page
        #1) 최종 url 구성:regDate=20201101, page=1
        url=f"https://news.daum.net/newsbox?regDate={date}&tab_cate=NE&page={page}" 
        
        #2) url 요청 
        res = req.urlopen(url)
        src = res.read() # source 
        data = src.decode('utf-8') # 디코딩 적용
        
        #3) HTML 파싱
        html = BeautifulSoup(data, 'html.parser')
        
        #4) tag 기반 자료 수집
        #1) tag element 수집
        a_tag = html.select('a[class="link_txt"]')
    
        # 2) 자료수집
        page_news=[]
        for a in a_tag:
            cont = str(a.string)# tag의 내용 가져오기-> 문자열 로변환
            page_news.append(cont.strip()) # 1page news 저장
            
        day_news.extend(page_news[:40]) # 1일 news 추가 저장
        #1일 news: [1page(40),2page(40),...,5page(40)]
       
    return day_news

#함수 호출
day_news = newsCrawler(sdate[0]) # 20201101, 5page
print(day_news)
len(day_news) #200= 5*40

#list 내포
crawling_news=[newsCrawler(day) for day in sdate]
len(crawling_news) #151
crawling_news#[[day1],[day2],...,[day151]

#1day news
crawling_news[0] # 200 문장 으로 구성 되어 있다.

#151 day news
crawling_news[-1]# 200 문장 으로 구성 되어 있다.

#전체 무장수
#200*151=30200
