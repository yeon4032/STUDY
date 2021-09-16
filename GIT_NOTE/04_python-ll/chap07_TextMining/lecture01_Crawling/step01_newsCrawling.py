# -*- coding: utf-8 -*-
"""
step01_newsCrawling.py

"""
import urllib.request as req # 원격 서버 url 자료 요청
from bs4 import BeautifulSoup # source -> html 파싱

url = "http://media.daum.net"

#1. url 요청
res = req.urlopen(url)

# object.method()
src = res.read() # source 
print(src) # xec\x9e\x90\xeb\xa3\x8c\ : 유니코드 -> 아스키  (즉 한글이 깨진거)

# 디코딩 적용 (한글깨짐 현상을 복구)
data = src.decode('utf-8') # 디코딩 적용
print(data)

# 2.html 파싱
html = BeautifulSoup(data, 'html.parser')
print(html) 
'''
<태그속성='값'> 내용 </태그>
<a href='www.naver.com'> 네이버 </a>
'''

# 3. tag 요소 추출
'''
select("tag[속성='값']")
'''

#1) tag element 수집
a_tag=html.select('a[class="link_txt"]')
len(a_tag) # 62

a_tag[0]
type(a_tag[0]) #bs4.element.Tag

# 2) 자료수집
crawling_data=[] #new 저장

cnt=0
for a in a_tag:
    cont = str(a.string)# tag의 내용 가져오기-> 문자열 로변환
    print(cnt,cont,sep='->')
    cnt+=1
    crawling_data.append(cont.strip())
    #str.string(): 문단 끝 불용어(\n,\t,\r) 제거

# 46 -> 코스피

print(crawling_data)

crawling_data = crawling_data[:46] # 코스피, 바로잡기 삭제
print(crawling_data)























