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

lword <- unique(lword) # 중복 단어 벡터 제거
length(lword) # [1] 353(119개 제거)

lword <- sapply(lword, unique) # 중복 문장 제거 
length(lword) 


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

#----------------------------------------------------
# 5.단어 간 연관규칙 산출
#----------------------------------------------------
# 트랜잭션 데이터를 대상으로 지지도와 신뢰도를 적용하여 연관규칙 생성
# 형식) apriori(data, parameter = NULL, appearance = NULL, control = NULL)
tranrules <- apriori(wordtran, parameter=list(supp=0.25, conf=0.05)) 
inspect(tranrules) 

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