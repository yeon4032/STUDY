# -*- coding: utf-8 -*-
"""
https://www.youtube.com/watch?v=3b_VMk3WlNY
"""

from urllib.parse import quote_plus #한글을 인터넷 에서 알아 먹을수 있는 걸로 변환 해준다.
from bs4 import BeautifulSoup
from selenium import webdriver


base_url='https://www.google.com/search?q='
plus_url= input('무엇을 검색할까요:')
url=base_url+quote_plus(plus_url)

print(url)
#https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC



##################################333
driver = webdriver.chrome()
driver.get(url)

html= driver.page_source
soup = BeautifulSoup(html)

r= soup.select('r') #<- 소스 보고 하기
print(type(r))

for i in r :
    print(i.select_one('.ellip').text)
    print(i.select_one('.iuh30.bc').text)
    print(i.a.attrs['href'])
    print()
    
driver.close()




























