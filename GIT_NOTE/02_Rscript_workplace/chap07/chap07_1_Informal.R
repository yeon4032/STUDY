######################################
## 1. 패키지 설치와 준비 
######################################

# 1) KoNLP 설치 
install.packages("KoNLP") # 오류 발생 : 최신 버전에서 패키지 사용 불가 
#Warning in install.packages :
#  package ‘KoNLP’ is not available (for R version 4.0.0)

# [오류 해결방법]
# - 현재 R 버전에서 제공하지 않는 패키지(KoNLP) 설치 방법

# [단계1] Rstudio 종료 


# [단계2] R 3.6.3 버전 다운로드 & 설치 : KoNLP 사용 버전  
# https://cran.r-project.org/bin/windows/base/old/
# 위 사이트 접속 후 'R 3.6.3 (February, 2020)' 클릭

sessionInfo()
#R version 3.6.3 (2020-02-29)


# [단계3] Rstudio 실행 & R 버전 확인 
# 메뉴 [Tools] -> [Global Options] -> [General] 탭에서
#      R version : 64-bit R-3.6.3  변경 -> RStudion 재시작 


# [단계4] 이전 R 버전에서 kONLP 설치 
install.packages("https://cran.rstudio.com/bin/windows/contrib/3.4/KoNLP_0.80.1.zip",
                 repos = NULL) #repos= NULL: 현재 사용중인 버전에 설치
# package ‘KoNLP’ successfully unpacked and MD5 sums checked
.libPaths()
# [1] "C:/Users/82104/Documents/R/win-library/3.6"
# [2] "C:/Program Files/R/R-3.6.3/library"     


# 2) Sejong 설치 : KoNLP와 의존성 있는 Sejong 설치 
install.packages("Sejong") #새종사전 제공

# 3) wordcloud 설치    
install.packages("wordcloud")   #단어구름 시각화

# 4) tm 설치 
install.packages("tm") #텍스트 마이닝: 전처리 함수수

# 5) 설치 위치 확인 
.libPaths()

# 6) KoNLP 의존성 패키지 모두 설치 & 로드 
install.packages(c('hash','rJava','tau','RSQLite','devtools')) # 30건 경고
library(hash)
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_151') # jdk 경로
library(rJava)
library(tau)
library(RSQLite)
library(devtools)

# 7) KoNLP 패키지 로딩
library(KoNLP) # 로딩 성공  

library(tm) # 전처리 용도 

library(wordcloud) # 단어 구름 시각화 


##################################################
# 1. 토픽분석(텍스트 마이닝) 
# - 시각화 : 단어 빈도수에 따른 워드 클라우드
###################################################


# 단계1 :  facebook_bigdata.txt 가져오기
facebook <- file(file.choose(), encoding="UTF-8")
facebook_data <- readLines(facebook) # 줄 단위 읽기 (문장 단위 읽기)
str(facebook_data) # chr [1:76] _-> 백터 자료
facebook_data[1:6] # 앞부분 6문장 확인 


# 단계2 : 세종 사전에 신규 단어 추가
# term='추가단어', tag=ncn(명사지시코드)
user_dic <- data.frame(term=c("R 프로그래밍","페이스북","김진성","소셜네트워크"), tag='ncn') #tag<- 품사
user_dic
# Sejong 사전에 신규 단어 추가 : KoNLP 제공 
buildDictionary(ext_dic='sejong', user_dic = user_dic)
#                추가한 사전,추가할 단어 
#일시적임
#370961 words dictionary was built.

# 단계3 : 단어추출 사용자 함수 정의
# (1) Sejong 사전에 등록된 신규 단어 테스트    
paste(extractNoun('김진성은 소셜네트워크에 가입했습니다.'), collapse ='') #문장을 넣어 세종 사전에 있는 명사를 추출
paste(extractNoun('홍길동은 많은 사람과 소통을 위해서 소셜네트워크에 가입하였습니다.'), collapse=" ")
#명사(단어 토큰) 추출 -> 단어 묶음

# (2) 사용자 정의 함수 실행 순서 : 문자변환 -> 명사 단어추출 -> 공백으로 합침
exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}

# (3) exNouns 함수 이용 단어 추출 
# 형식) sapply(vector, 함수) -> 76개 vector 문장(원소)에서 단어 추출 
facebook_nouns <- sapply(facebook_data, exNouns) #앞에있는 데이터를 함수어 apply.

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
facebook_nouns[4]


# 단계4 : 자료 전처리   
# (1) 말뭉치(코퍼스:Corpus) 생성 : 문장을 처리할 수 있는 자료의 집합 
myCorpus <- Corpus(VectorSource(facebook_nouns)) 
myCorpus
# <<SimpleCorpus>>
# Metadata:  corpus specific: 1, document level (indexed): 0
# Content:  documents: 76

# corpus 내용 보기
tm::inspect(myCorpus[1])  
inspect(myCorpus[2])

#arules vs tm 패키지에서 동일한 함수 사용 
#(tm 과 arules 패키지 둘다 inspect 함수 가 있음 이때 원하는 함수 하용 법.\)
arules::inspect() #arules 패키지 함수 사용 
tm::inspect(myCorpus[2]) #tm 패키지 함수 사용

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
topWord <- head(sort(wordResult, decreasing=T), 10) # 상위 10개 토픽추출 
# (2) 파일 차트 생성 
pie(topWord, col=rainbow(10), radius=1) 
# radius=1 : 반지름 지정 - 확대 기능  

# (3) 빈도수 백분율 적용 
pct <- round(topWord/sum(topWord)*100, 1) # 백분율

# (4) 단어와 백분율 하나로 합친다.
label <- paste(names(topWord), "\n", pct, "%")

# (5) 파이차트에 단어와 백분율을 레이블로 적용 
pie(topWord, main="SNS 빅데이터 관련 토픽분석", 
    col=rainbow(10), cex=0.8, labels=label)



###########################################
# 단계2 - 연관어 분석(단어와 단어 사이 연관성 분석) 
#   - 시각화 : 연관어 네트워크 시각화,
###########################################

# 한글 처리를 위한 패키지 설치
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jdk1.8.0_151')
library(rJava) # 아래와 같은 Error 발생 시 Sys.setenv()함수로 java 경로 지정
library(KoNLP) # rJava 라이브러리가 필요함

#----------------------------------------------------
# 1.텍스트 파일 가져오기
#----------------------------------------------------
marketing <- file("c:/ITWILL/2_Rwork/data/marketing.txt", encoding="UTF-8")
marketing2 <- readLines(marketing) # 줄 단위 데이터 생성
close(marketing) # 객체 닫기 
head(marketing2) # 앞부분 6줄 보기 - 줄 단위 문장 확인 
str(marketing2) # chr [1:472]
marketing2[1:5]

#----------------------------------------------------
# 2. 줄 단위 단어 추출
#----------------------------------------------------
# Map()함수 이용 줄 단위 단어 추출 
lword <- Map(extractNoun, marketing2) 
length(lword) # [1] 472
class(lword) # list
lword[1] #$key(원문)= value(단어벡터)
lword[472]

help(Map)
#생략 가능
#중복단어 제거 (unique)  
lword <- unique(lword) # 중복 단어 벡터 제거
length(lword) # [1] 353(119개 제거)

lword <- sapply(lword, unique) # 중복 문장 제거 
length(lword) #353

#####################################################
# list 처리함수: unique, sapply example
#####################################################
lst<-list(a=c(1,2,1),b=c(2,3,2),a = c(2,3,2))
lst
# $a
# [1] 1 2 1
# 
# $b
# [1] 2 3 2
# 
# $a
# [1] 2 3 2



unique(lst)  #값 중복 제거 (1행의 a 와 3행의 a 는 같은 이름이다 그로 3행 a는 제거된다)
# [[1]]
# [1] 1 2 1

# [[2]]
# [1] 2 3 2

sapply(lst,unique) #value 중복 제거
#      a b a
# [1,] 1 2 2
# [2,] 2 3 3




#----------------------------------------------------
# 3. 전처리
#----------------------------------------------------
# 1) 단어 길이 2음절~4음절 단어 필터링 함수 정의
filter1 <- function(x){
  nchar(x) <= 4 && nchar(x) >= 2 && is.hangul(x)
}

# 2) Filter(f,x) -> filter1() 함수를 적용하여 x 벡터 단위 필터링 
filter2 <- function(x){
  Filter(filter1, x)
}
# is.hangul() : KoNLP 패키지 제공
# Filter(f, x) : base
# nchar() : base -> 문자 수 반환

# 3) 줄 단어 대상 필터링
lword_final <- sapply(lword, filter2)
lword_final # 전처리 단어확인(2~4음절) 

#list 객체 처리 
#형식) sapply(list, Func)
#apply(matrix/DF,1/2,Func)

#----------------------------------------------
# 4. 트랜잭션 생성 : 연관분석을 위해서 단어를 트랜잭션으로 변환
#----------------------------------------------------
# arules 패키지 설치
install.packages("arules")
library(arules) 
#--------------------
# arules 패키지 제공 기능
# - Adult,Groceries 데이터 셋
# - as(),apriori(),inspect(),labels(),crossTable()=table()
#-------------------

# as(dataset, 'class') # 형변환 
wordtran <- as(lword_final, "transactions") # lword에 중복데이터가 있으면 error발생
wordtran 

# 트랜잭션 내용 보기 -> 각 트랜잭션의 단어 보기
inspect(wordtran)  

help(labels)
#----------------------------------------------------
# 5.단어 간 연관규칙 산출
#----------------------------------------------------
# 트랜잭션 데이터를 대상으로 지지도와 신뢰도를 적용하여 연관규칙 생성
# 형식) apriori(data, parameter = NULL, appearance = NULL, control = NULL)
tranrules <- apriori(wordtran, parameter=list(supp=0.25, conf=0.05)) 
tm::arinspect(tranrules) 

# transactions in sparse format with
# 353 transactions (rows) and   -> 문장의 개수
# 2423 items (columns) -> 단어 개수
help("data.frame")
#----------------------------------------------------
# 6.연관어 시각화 
#----------------------------------------------------
# (1) 데이터 구조 변경 : 연관규칙 -> label 추출  
rules <- labels(tranrules, ruleSep=" ")  
rules 

# 문자열로 묶인 연관단어 -> 공백 기준 list 변경 
rules <- sapply(rules, strsplit, " ",  USE.NAMES=F) # list 변환  
rules

# list -> matrix 반환
rulemat <- do.call("rbind", rules)
rulemat
class(rulemat)

# (2) 연관어 시각화를 위한 igraph 패키지 설치
install.packages("igraph") # graph.edgelist(), plot.igraph(), closeness() 함수 제공
library(igraph)   

# (3) edgelist보기 - 연관단어를 정점 형태의 목록 제공 
ruleg <- graph.edgelist(rulemat[c(12:59),], directed=F) # [1,]~[11,] "{}" 제외
ruleg

# (4) edgelist 시각화
X11() # 별도 창 제공 
plot.igraph(ruleg, vertex.label=V(ruleg)$name,
            vertex.label.cex=1.2, vertex.label.color='black', 
            vertex.size=20, vertex.color='green', vertex.frame.color='blue')


#############################################
# 단계3 - 감성 분석(단어의 긍정/부정 분석) 
#  - 시각화 : 파랑/빨강 -> 불만고객 시각화
#############################################

# 1. 데이터 가져오기() 
setwd("C:/ITWILL/2_Rwork/data")

data<-read.csv("reviews.csv") 
head(data,2)
str(data)

# 2. 단어 사전에 단어추가

# 긍정어/부정어 영어 사전 가져오기
posDic <- readLines("posDic.txt")
negDic <- readLines("negDic.txt")
length(posDic) # 2006
length(negDic) # 4783


# 긍정어/부정어 단어 추가 
posDic.final <-c(posDic, 'victor')
negDic.final <-c(negDic, 'vanquished')


# 3. 감성 분석 함수 정의-sentimental

# (1) 문자열 처리를 위한 패키지 로딩 
install.packages('plyr')
library(plyr) # laply()함수 제공
library(stringr) # str_split()함수 제공

# (2) 감성분석을 위한 함수 정의
sentimental = function(sentences, posDic, negDic){
  #리뷰     긍정    부정
  scores = laply(sentences, function(sentence, posDic, negDic) {
    
    #문장전처리
    sentence = gsub('[[:punct:]]', '', sentence) #문장부호 제거
    sentence = gsub('[[:cntrl:]]', '', sentence) #특수문자 제거
    sentence = gsub('\\d+', '', sentence) # 숫자 제거
    sentence = tolower(sentence) # 모두 소문자로 변경(단어가 모두 소문자 임)
    
    #문장-> 단어
    word.list = str_split(sentence, '\\s+') # 공백 기준으로 단어 생성 -> \\s+ : 공백 정규식, +(1개 이상) 
    words = unlist(word.list) # unlist() : list를 vector 객체로 구조변경
    
    #단어 vs 사전 비교
    pos.matches = match(words, posDic) # words의 단어를 posDic에서 matching
    neg.matches = match(words, negDic)
    
    #사전과 매칭된 단어 추출
    pos.matches = !is.na(pos.matches) # NA 제거, 위치(숫자)만 추출
    neg.matches = !is.na(neg.matches)
    
    # 점수 = 긍정-부정
    score = sum(pos.matches) - sum(neg.matches) # 긍정 - 부정    
    return(score)
  }, posDic, negDic)
  
  #df=점수 +텍스트
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
}

# 4. 감성 분석 : 두번째 변수(review) 전체 레코드 대상 감성분석
result<-sentimental(data[,2], posDic.final, negDic.final)
result
names(result) # "score" "text" 
dim(result) # 100   2
result$text
result$score # 100 줄 단위로 긍정어/부정어 사전을 적용한 점수 합계

# score값을 대상으로 color 칼럼 추가
result$color[result$score >=1] <- "blue"
result$color[result$score ==0] <- "green"
result$color[result$score < 0] <- "red"

# 감성분석 결과 차트보기
plot(result$score, col=result$color) # 산포도 색생 적용
barplot(result$score, col=result$color, main ="감성분석 결과화면") # 막대차트


# 5. 단어의 긍정/부정 분석 

# (1) 감성분석 빈도수 
table(result$color)

# (2) score 칼럼 리코딩 
result$remark[result$score >=1] <- "긍정"
result$remark[result$score ==0] <- "중립"
result$remark[result$score < 0] <- "부정"

sentiment_result<- table(result$remark)
sentiment_result

# (3) 제목, 색상, 원크기
pie(sentiment_result, main="감성분석 결과", 
    col=c("blue","red","green"), radius=0.8) # ->  1.2
