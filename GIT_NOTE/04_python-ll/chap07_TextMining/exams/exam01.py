'''
 문) 아래 url을 이용하여 어린이날(20210505)에 제공된 뉴스 기사를 
   1~5페이지 크롤링하는 크롤러 함수를 정의하고 크롤링 결과를 확인하시오.
   
   base_url = "https://news.daum.net/newsbox?regDate="   
   
   <조건1> 크롤러 함수의 파라미터(page번호, 날짜)
   <조건2> 크롤링 대상  : <a> 태그의 'class=link_txt' 속성을 갖는 내용 
   <조건3> 크롤링 결과 확인  : news 개수와  news 출력  
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

base_url = "https://news.daum.net/newsbox?regDate="

crawling_news = [] # news 저장 


# 클로러 함수(페이지수, 검색날짜) 
def crawler_func(pages, date):
    pass # 내용 채우기    





# 클로러 함수 호출 
crawler_func(5, '20210505') # (페이지수, 검색날짜)

print('크롤링 news 개수 =', len(crawling_news))
print('크롤링 news') 
print(crawling_news)










































import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

base_url = "https://news.daum.net/newsbox?regDate="

crawling_news = [] # news 저장 


# 클로러 함수(페이지수, 검색날짜) 
def crawler_func(pages, date):
    base_url = "https://news.daum.net/newsbox?regDate="
    crawling_news = [] # news 저장 
    
    url = base_url + date
    
    for page in range(1,pages+1):
        p='&page'+str(page)
        url+=p
        
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
        
        cnt=0
        a1=0
        for a in a_tag:
            cnt+=1
            print(cnt,a)
            cont = str(a.string)# tag의 내용 가져오기-> 문자열 로변환
            page_news.append(cont.strip())
            a1+=1
            print(a1,page_news)
           
        crawling_news.extend(page_news[:40])
       
    return crawling_news

   



# 클로러 함수 호출 
crawling_news = crawler_func(5, '20210505') # (페이지수, 검색날짜)

print('크롤링 news 개수 =', len(crawling_news)) # 200=5*40
print('크롤링 news') 
print(crawling_news)








import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

base_url = "https://news.daum.net/newsbox?regDate="



# 클로러 함수(페이지수, 검색날짜) 
def crawler_func(pages, date):
    base_url = "https://news.daum.net/newsbox?regDate="
    crawling_news = [] # 5 page 저장 
    
    url = base_url +date
    # url=https://news.daum.net/newsbox?regDate=20200505
    
    for page in range(1, pages+1): # 1~5 page
        p ='&page' +str(page)    
        url += p # url=url+p
    
    # url=https://news.daum.net/newsbox?regDate=20200505&page=1
    
        #1.url 요청
        res = req.urlopen(url)
        src = res.read() # source 
        data = src.decode('utf-8') # 디코딩 적용
    
        # 2.html 파싱
        html = BeautifulSoup(data, 'html.parser')
        
        # 3. tag 요소 추출
        #1) tag element 수집
        a_tag = html.select('a[class="link_txt"]')
        
        # 2) 자료수집
        crawling_news = []
        for a in a_tag:
            cont = str(a.string)# tag의 내용 가져오기-> 문자열 로변환
            crawling_news.append(cont.strip())
    
    return crawling_news



# 클로러 함수 호출 
crawling_news = crawler_func(5, '20210505') # (페이지수, 검색날짜)

print('크롤링 news 개수 =', len(crawling_news)) # 200=5*40
print('크롤링 news') 
print(crawling_news)


################################ 정답



def crawler_func(pages, date):
    base_url = "https://news.daum.net/newsbox?regDate="
    crawling_news = [] # 5 page news 저장

    url = base_url + date  
    
    # page 단위 news 수집 
    for page in range(1, pages+1) :  # 1~5 page
        p = '&page=' + str(page)
        url += p # final url 
        
        # 1. url 요청 
        res = req.urlopen(url)    
        src = res.read() # source 
        data = src.decode('utf-8') # 디코딩 적용 
        
        # 2.html 파싱  
        html = BeautifulSoup(data, 'html.parser')
        
        # 3. tag 요소 추출     
        # 1) tag element 수집 
        a_tag = html.select('a[class="link_txt"]')
        
        # 2) 자료 수집 
        page_news = [] # 1 page news 저장     
        for a in a_tag :
            cont = str(a.string) # 내용 가져오기 -> 문자열         
            page_news.append(cont.strip())
        
        crawling_news.extend(page_news[:40]) # 5 page news 저장
            
    return crawling_news


# 클로러 함수 호출 
crawling_news = crawler_func(5, '20210505') # (페이지수, 검색날짜)

print('크롤링 news 개수 =', len(crawling_news)) # 200=5*40
print('크롤링 news') 
print(crawling_news)
    
    