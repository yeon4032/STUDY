# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:11:12 2021

@author: sihun
"""

import requests
from bs4 import BeautifulSoup
import re

#크롤러 (for one page)
word="국제유가"

def CR(word):
    start_date = '20100101'     # 검색 희망 시작일
    end_date = '20210831'       # 검색 희망 종료일
        
    url = 'https://search.naver.com/search.naver?where=news&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2010.01.01&de=2021.08.31&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3A' \
                +start_date+'000000&ed='+end_date+'235959&p=1'
    response= requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links=soup.select(".news_tit") # list 형으로 경과 나옴
    return links

for link in links:
    title = link.text # 태그 안에 텍스트 요소를 가지고옴
    url = link.attrs['href'] # href의 속성값 을가지고옴 (url)
    print(title)
    #print(title,url)


# 크롤링

sentences=[] 
a=1
for b in range(1,5):
    start_date = '20100201'     # 검색 희망 시작일
    end_date = '20210831'       # 검색 희망 종료일

    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds=2010.01.01&de=2021.08.31&cluster_rank=40&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from{start_date}to{end_date},a:all&start={a}'
    response= requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links=soup.select(".news_tit") # list 형으로 경과 나옴
    a+=10
    for link in links:
        title = link.text # 태그 안에 텍스트 요소를 가지고옴
        url = link.attrs['href'] # href의 속성값 을가지고옴 (url)
        sentences.append(title)
len(sentences) #7990


https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds=2010.01.01&de=2021.08.31&cluster_rank=40&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20100101to20210831,a:all&start=1
https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds=2010.01.01&de=2021.08.31&cluster_rank=19&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20100101to20210831,a:all&start=11
https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds=2010.01.01&de=2021.08.31&cluster_rank=59&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20100101to20210831,a:all&start=21


import requests
from bs4 import BeautifulSoup
import re

sentences=[] 
a=1
for b in range(1,5):
    start_date = '20180101'     # 검색 희망 시작일
    end_date = '20210831'       # 검색 희망 종료일

    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds=2010.01.01&de=2021.08.31&cluster_rank=40&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from{start_date}to{end_date},a:all&start={a}'
    response= requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links=soup.select(".news_tit") # list 형으로 경과 나옴
    a+=10
    for link in links:
        title = link.text # 태그 안에 텍스트 요소를 가지고옴
        url = link.attrs['href'] # href의 속성값 을가지고옴 (url)
        sentences.append(title)
        
len(sentences)



import requests
from bs4 import BeautifulSoup
import re

sentences=[] 
a=1

for b in range(1,5):
    try:
        start_date1='2016.01.01'
        start_date = '20160101'     # 검색 희망 시작일
        end_data1 = '2020.08.31'    # 검색 희망 종료일
        end_date = '20200831'

        url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds={start_date1}&de={end_data1}&cluster_rank=40&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from{start_date}to{end_date},a:all&start={a}'
        response= requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        links=soup.select(".news_tit") # list 형으로 경과 나옴
        a+=10
        for link in links:
            title = link.text # 태그 안에 텍스트 요소를 가지고옴
            url = link.attrs['href'] # href의 속성값 을가지고옴 (url)
            sentences.append(title)
    except:
        print("기사가 더이상 없습니다.")

https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds=2016.01.01&de=2021.08.31&cluster_rank=40&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20160101to20210831,a:all&start=1
https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B5%AD%EC%A0%9C%EC%9C%A0%EA%B0%80&sort=0&photo=0&field=0&pd=3&ds=2010.01.01&de=2021.08.31&cluster_rank=40&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20100101to20210831,a:all&start=1
