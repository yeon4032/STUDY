#################################
## <제7장-2 연습문제>
################################# 


# 01. 트럼프 연설문(trump.txt)과 오바마 연설문(obama.txt)을 대상으로 빈도수가 2회 이상 단어를 대상으로 단어구름 시각화하시오.
# [단계1], [단계4] ~ [단계8]

# 필요한 패키지 로딩 
library(tm) # 전처리 용도 
library(wordcloud) # 단어 구름 시각화 


# [단계1] 파일 가져오기 
obama <-file(file.choose())  # obama.txt
obama_data<-readLines(obama)
head(obama_data)
str(obama_data) # chr [1:496] -> 496개 문장 


# [단계4] : 자료 전처리   
# (1) 말뭉치(코퍼스:Corpus) 생성 : 문장을 처리할 수 있는 자료의 집합 
myCorpus <- Corpus(VectorSource(obama_data)) 
myCorpus # Content:  documents: 496
inspect(myCorpus[1:3])


# (2) 자료 전처리 : 말뭉치 대상 전처리 : tm_map(Corpus, Func)
# 경고메시지 무시 
myCorpusPrepro <- tm_map(myCorpus, removePunctuation) # 문장부호 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) # 수치 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) # 소문자 변경
# 영문 대상 불용어 제외 : stopwords()
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english')) # 불용어제거


# (3) 전처리 결과 확인 
myCorpusPrepro # documents: 496
inspect(myCorpusPrepro[1:3]) # 데이터 전처리 결과 확인(숫자, 문장부호, 영문 상태 확인)
# [2] [*] OBAMA: Hello Skybrook! -> before
# [2]  obama hello skybrook -> after


# [단계5] : 단어-문서 행렬(단어 길이 2개 이상)
myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                        control=list(wordLengths=c(2,16))) 

myCorpusPrepro_term
#<<TermDocumentMatrix (terms: 1309, documents: 496)>> -> 단어vs문서 
#Non-/sparse entries: 2350/646914
#Sparsity           : 100%
#Maximal term length: 16 -> 최대 단어길이 
#Weighting          : term frequency (tf)

# (2) Corpus -> 평서문 변환 : matrix -> data.frame 변경
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 
dim(myTerm_df) # 1309  496

# [단계6] : 단어 빈도수 구하기
# (1) 단어 빈도수 내림차순 정렬
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) # 각 단어 합계 -> 내림 정렬 
wordResult[1:10] # top10 단어  


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

# (4) 단어 구름 시각화: 크기,최소빈도수=2회 이상 ,순서,회전,색상,글꼴 지정  
wordcloud(word.df$word, word.df$freq, 
          scale=c(3,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")


# [단계8] : 차트 시각화  
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
pie(topWord, main="Obama 대통령 후보 연설문", 
    col=rainbow(10), cex=0.8, labels=label)


# 02. 공공데이터 사이트에서 관심분야 데이터 셋을 다운로드 받아서 빈도수가 5회 이상 단어를 이용하여 
#      단어 구름으로 시각화 하시오.
# 공공데이터 사이트 : www.data.go.kr 또는 기타 사이트 










