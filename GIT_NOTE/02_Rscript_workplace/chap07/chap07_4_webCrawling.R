#chap07_4_webCrawling

#url <- "http://news.daum.net/newsbox
#수집기간 : 2021.2월 (28일) -> 5page
28*5 #140


library(httr) #URL 요청 패키지
library(XML)  #html 패싱
library(stringr) #URL 만들기
library(stringr)
#1. url 생성: 수집기간  
#https://news.daum.net/newsbox?regDate=20210201&tab_cate=NE&page=2

urlbase<-'https://news.daum.net/newsbox?tab_cate=NE&regDate='

# 1)date 결합
date<-seq(20210201,20210228,1)
date

urlist<-str_c(urlbase, date)
urlist

# 2) page 결합
pages<-str_c('&page=',c(1:5))
pages

urlist2<-outer(urlist,pages,str_c) #1:n 문자열 결합
urlist2
length(urlist2) #140
class((urlist2)) #matrix

urlist3<-as.vector(urlist2) #사용의 편의를 위해
urlist3

urlfinal<-sort(urlist3) #날짜순 정렬
urlfinal


#2.crawler :자료수집 함수
newscralwer<-function(url){
  # 2. url 요청
  url <- "http://media.daum.net/"
  web = GET(url) #웹문서 소스 제공
  web
  
  # 3. html 파싱(source -> html) 
  html <- htmlTreeParse(web, useInternalNodes = T, trim = T, encoding="utf-8") # 소문자 주의  
  help("htmlTreeParse")
  # html root node 찾기 
  rootNode <- xmlRoot(html)
  
  # 4. tag 자료 수집 : ["//tag[@속성='속성값']"]
  news <- xpathSApply(rootNode, "//a[@class='link_txt']", xmlValue)
  news<- news[1:46]
  return(news)
}

length(urlfinal) #140

#함수 호출
re_news <- newscralwer(urlfinal[1])
re_news

cnt<-1
for(url in urlfinal){ #140번 반복
  cat(cnt,'page \n')
  re_news<-newscralwer(url)
  print(re_news)
  cnt<- cnt+1
}

help(newscralwer)
help(cat)












