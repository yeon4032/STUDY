# chap07_3_newsCrawling

# 1. 패키지 설치 
install.packages('httr') #서버로 부터 url요청 
install.packages('XML')  #html 파싱(문서 변환)

library(httr) # GET() 제공  
library(XML) # html 파싱 


# 2. url 요청
url <- "http://media.daum.net/"
web = GET(url) #웹문서 소스 제공
web
# Response [https://news.daum.net/]
# Date: 2021-05-04 05:38
# Status: 200 <-정상적 응답의 숫자임
# Content-Type: text/html;charset=UTF-8
# Size: 63 kB

# 3. html 파싱(source -> html) 
html <- htmlTreeParse(web, useInternalNodes = T, trim = T, encoding="utf-8") # 소문자 주의  
# useInternalNodes = T : root node 
# trim = T : 앞뒷 공백 제거 
# encoding = 'utf-8' : 문자셋 인코딩 

html
#<a href="www.naver.com"> 네이버</a >


# html root node 찾기 
rootNode <- xmlRoot(html)

# 4. tag 자료 수집 : ["//tag[@속성='속성값']"]
news <- xpathSApply(rootNode, "//a[@class='link_txt']", xmlValue)
# xmlValue : 해당 tag 내용 
news
length(news)#62

#기사 내용 선정: 코스피,검색어 순위 등등 제외
idx <-which(news == '코스피') #47

news<- news[1:(idx - 1)]
news

## 5. Crawling 결과 전처리 
# 형식) gsub(pattern, replacement, x) -  전처리 용도  (x=대상)

news_pre <- gsub("[\r\n\t]", ' ', news) # 이스케이프 제거 
news_pre <- gsub('[[:punct:]]',' ',news_pre) # 문장부호 제거(\) 
news_pre <- gsub('[[:cntrl:]]',' ',news_pre) # 특수문자 제거
#news_pre <- gsub('\\d+',' ',news_pre) # 숫자 제거(코로나19 숫자 유지) 
news_pre <- gsub('[a-z]+',' ',news_pre) # 영문자 제거 
news_pre <- gsub('[A-Z]+',' ',news_pre) # 영문자 제거 
news_pre <- gsub('\\s+',' ',news_pre) # 2개 이상 공백 교체

news_pre # 전처리 확인(이스케이프, 특수문자, 영문, 공백) 
#[46] "한강 실종 의대생 父 석고대죄할 사람이 이제야 조문 거절 "       


#6. file save/read
getwd()
setwd('C:/ITWILL/2_Rwork/output')

write.csv(news_pre,'news_data.csv',quote=F,) #행번호 저장 

#저장한 뉴스 정보 가지고 오기 
news_data<-read.csv('news_data.csv',stringsAsFactors = F)
str(news_data)

# 칼럼명 붙여주기
names(news_data)<-c('NO','News_test')
head(news_data)
# NO                                                            News_test
# 1  1 이낙연 공개행보 재개 이낙연 경제단체 찾아 청년 일자리 통큰 확대 요청
# 2  2                           추격 고삐 이낙연 공개행보 정세균 5 가시권 
# 3  3       다시 움직이는 이낙연 경제계 찾아 규제 풀 테니 청년채용 확대를 
# 4  4                      6살 아이 사망 낮술 운전 상고 포기 징역 8년 확정
# 5  5               6세 아이 숨지게 한 낮술 운전자 상고 포기 징역 8년 확정
# 6  6             대낮 음주운전 6세 아동 사망 50대 상고 포기 징역 8년 확정

#news 가져오기
news_test<-news_data$News_test



#practice question

#7.토픽분석
# 1단계 ~8단계



# 단계1 : 이미 뉴스 가져옴


# 단계2 : 세종 사전에 신규 단어 추가
# term='추가단어', tag=ncn(명사지시코드)
library(KoNLP)
library(tm)
library(wordcloud)


user_dic <- data.frame(term=c(" 펜테믹","코로나19","타다"), tag='ncn') #tag<- 품사
user_dic
# Sejong 사전에 신규 단어 추가 : KoNLP 제공 
buildDictionary(ext_dic='sejong', user_dic = user_dic)
#                추가한 사전,추가할 단어 
#일시적임
#370961 words dictionary was built.

# 단계3 : 단어추출 사용자 함수 정의
# (1) Sejong 사전에 등록된 신규 단어 테스트    
paste(extractNoun('우리나라는 현재 코로나19 때문에 공황상태이다.'), collapse ='') #문장을 넣어 세종 사전에 있는 명사를 추출
# [1] "우리나라코로나19때문공황상태"

#첫번째 뉴스 기사
news_text[1]

paste(extractNoun(news_text[1]),collapse=' ')


# (2) 사용자 정의 함수 실행 순서 : 문자변환 -> 명사 단어추출 -> 공백으로 합침
exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}

# (3) exNouns 함수 이용 단어 추출 
# 형식) sapply(vector, 함수) -> 76개 vector 문장(원소)에서 단어 추출 
facebook_nouns <- sapply(news_test, exNouns) #앞에있는 데이터를 함수어 apply.

facebook_nouns[1:3]
#str(facebook_nouns) -> 백터 내용 
#attr(*, "names")= chr [1:76] -> 백터 원소 이름

vec_names<-names(facebook_nouns)
names(facebook_nouns) <-1:76
#vec_names [1]# 백터 이름
#facebook_nouns[1]# 실제값 (첫문장은 실제 데이터 ,두번째 문장은 백터 이름)


# (4) 단어 추출 결과
str(facebook_nouns) # [1:76] attr(*, 'names')=ch [1:76] 
facebook_nouns[1] # vector names:원래문장(윗문장), vector:단어 추출(아랫문장)
facebook_nouns[2]


# 단계4 : 자료 전처리   
# (1) 말뭉치(코퍼스:Corpus) 생성 : 문장을 처리할 수 있는 자료의 집합 
myCorpus <- Corpus(VectorSource(facebook_nouns)) 
myCorpus
# <<SimpleCorpus>>
# Metadata:  corpus specific: 1, document level (indexed): 0
# Content:  documents: 76

# corpus 내용 보기
inspect(myCorpus[1])  
inspect(myCorpus[2])


# (2) 자료 전처리 : 말뭉치 대상 전처리  :tm_map(Corpus,Func)
# 뒷 함수(removePunctuation) 를 앞에 말뭉치에(myCorpus) 대입하라 (for first sentence)
myCorpusPrepro <- tm_map(myCorpus, removePunctuation) # 문장부호 제거  
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) # 수치 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) # 소문자 변경
# 영문 대상 불용어 제외 : stopwords()
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english')) # 불용어제거 #(말뭉치, 함수, 어떠한단어)

# (3) 전처리 결과 확인 
myCorpusPrepro # Content:  documents: 76
inspect(myCorpusPrepro[1:3]) # 데이터 전처리 결과 확인(숫자, 문장부호, 영문 상태 확인)

help(tolower)


# 단계5 : 단어 선별(단어 길이 2개 이상)
# (1) 한글 단어길이 2음절 ~ 8음절(한글 1개 2byte) 
myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(4,16))) 

# 696*76 #52896
# 단어 출현 빈도: 1256
# 희소 빈도 : 총 샐에서(52896) - 단어 출현 (1256)
#1256/51640 #0.02432223 ->2.4%
myCorpusPrepro_term #단어문서 행렬 (희소 행렬)
# <<TermDocumentMatrix (terms: 696, documents: 76)>> -> 단어:696, 문자:76 
#   Non-/sparse entries: 1256/51640 -> 단어 출현 빈도/희소 빈도
# Sparsity           : 98% ->히소비율
# Maximal term length: 12 (6음절 최대)
# Weighting          : term frequency (tf) -> 가중치


# (2) Corpus -> 평서문 변환 : matrix -> data.frame 변경
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 
dim(myTerm_df)  #[1] 696  76

myTerm_df[100:105,30:40]

# 단계6 : 단어 빈도수 구하기
# (1) 단어 빈도수 내림차순 정렬
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) #각 단어 합계 -> 내림차순 정렬
wordResult[1:10] # top10 단어  


# (2) 불용어 제거 
myStopwords = c(stopwords('english'), "사용"); # 제거할 문자 추가
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, myStopwords) # 불용어제거


# (3) 단어 선별과 평서문 변환
myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(4,16))) # 2음절 ~ 8음절

# (4) 말뭉치 객체를 평서문으로 변환
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 

#(5) 단어 출현 빈도수 구하기
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]


# 단계7 : 단어구름에 디자인 적용(빈도수, 색상, 랜덤, 회전 등)
# (1) 단어 이름 생성 -> 빈도수의 이름
myName <- names(wordResult)  

# (2) 단어이름과 빈도수로 data.frame 생성
word.df <- data.frame(word=myName, freq=wordResult) 
str(word.df) # word, freq 변수
head(word.df)

# (3) 단어 색상과 글꼴 지정
pal <- brewer.pal(12,"Paired") # 12가지 색상 pal <- brewer.pal(9,"Set1") # Set1~ Set3
# 폰트 설정세팅 : "맑은 고딕", "서울남산체 B"
windowsFonts(malgun=windowsFont("맑은 고딕"))  #windows

# (4) 단어 구름 시각화: 크기,최소빈도수,순서,회전,색상,글꼴 지정  
wordcloud(word.df$word, word.df$freq, 
          scale=c(3,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")


# 단계8 : 차트 시각화  
#(1) 상위 10개 토픽추출
topWord <- head(sort(wordResult, decreasing=T), 5) # 상위 10개 토픽추출 
# (2) 파일 차트 생성 
pie(topWord, col=rainbow(5), radius=1) 
# radius=1 : 반지름 지정 - 확대 기능  

# (3) 빈도수 백분율 적용 
pct <- round(topWord/sum(topWord)*100, 1) # 백분율

# (4) 단어와 백분율 하나로 합친다.
label <- paste(names(topWord), "\n", pct, "%")

# (5) 파이차트에 단어와 백분율을 레이블로 적용 
pie(topWord, main="SNS 빅데이터 관련 토픽분석", 
    col=rainbow(10), cex=0.8, labels=label)











