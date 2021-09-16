#chap16_AssociationAnalysis

###################################################
# 연관분석(Association Analysis)
###################################################

# 특징
# - 데이터베이스에서 사건의 연관규칙을 찾는 무방향성 데이터마이닝 기법                                            
# - 무방향성(x -> y변수 없음) -> 비지도 학습에 의한 패턴 분석 방법
# - 사건과 사건 간 연관성(관계)를 찾는 방법(예:기저귀와 맥주)
# - A와 B 제품 동시 구매 패턴(지지도)
# - A 제품 구매 시 B 제품 구매 패턴(신뢰도)


# 예) 장바구니 분석 : 장바구니 정보를 트랜잭션(상품 거래 정보)이라고 하며,
# 트랜잭션 내의 연관성을 살펴보는 분석기법
# 분석절차 : 거래내역 -> 품목 관찰 -> 상품 연관성에 대한 규칙(Rule) 발견

# 활용분야
# - 대형 마트, 백화점, 쇼핑몰 등에서 고객의 장바구니에 들어있는 품목 간의 
#   관계를 탐구하는 용도
# ex) 고객들은 어떤 상품들을 동시에 구매하는가?
#   - 맥주를 구매한 고객은 주로 어떤 상품을 함께 구매하는가?


#########################################
# 1. 연관규칙 평가 척도
#########################################

# 연관규칙의 평가 척도
# 1. 지지도(support) : 전체자료에서 A를 구매하고 B를 구매하는 거래 비율 
#  A->B 지지도 식 
#  -> A와 B를 포함한 거래수 / 전체 거래수
#  -> n(A, B) : 두 항목(A,B)이 동시에 포함되는 거래수
#  -> n : 전체 거래 수

# 2. 신뢰도(confidence) : A가 포함된 거래 중에서 B를 포함한 거래의 비율(조건부 확률)
# A->B 신뢰도 식
#  -> A와 B를 포함한 거래수 / A를 포함한 거래수

# 3. 향상도(Lift) : 하위 항목들이 독립에서 얼마나 벗어나는지의 정도를 측정한 값
# 향상도 식
#  -> 신뢰도 / B가 포함될 거래율


# <지지도와 신뢰도 예시>
# t1 : 라면,맥주,우유
# t2 : 라면,고기,우유
# t3 : 라면,과일,고기
# t4 : 고기,맥주,우유
# t5 : 라면,고기,우유
# t6 : 과일,우유


# A(lhs) -> B(rhs)       지지도         신뢰도          향상도
#  맥주 -> 고기         1/6=0.166       1/2=0.5      0.5/0.66(4/6)=0.75
#라면,우유-> 맥주       1/6=0.166       1/3=0.33     0.33/0.33(2/6)=1

## 연관성 규칙 분석을 위한 패키지
install.packages("arules") # association Rule
# read.transactions(),  apriori(), Adult 데이터셋 제공
library(arules) #read.transactions()함수 제공


# 1. transaction 객체 생성(파일 이용)
setwd("C:/ITWILL/2_Rwork/data")

#평서문-> 트랜잭션 객체 생성
tran<- read.transactions("tran.txt", format="basket", sep=",")
tran

# 6 transactions (rows) and
# 5 items (columns)

# 2. transaction 데이터 보기
inspect(tran)

# 3. rule 발견(생성) - 지지도,신뢰도 = 0.1
# apriori(트랜잭션 data, parameter=list(supp, conf))

# 연관성 규칙 평가 척도 - 지지도와 신뢰도
rule1 <- apriori(tran, parameter = list(supp=0.3, conf=0.1)) # 16 rule
rule2 <- apriori(tran, parameter = list(supp=0.1, conf=0.1)) # 35 rule 
inspect(rule) # 규칙 보기
inspect(rule2) # 규칙 보기

# 지지도, 신뢰도, maxlen 인수  
help("apriori") # support 0.1, confidence 0.8, and maxlen 10  
rule <- apriori(tran) 
rule<- apriori(tran, parameter = list(supp=0.1, conf=0.8, maxlen=10)) 
# maxlen 는 선행사건(lhs) + 후행사건(rhs)수
inspect(rule) 

#support confidence coverage left count
#coverage: lhs포함률 or 거래율
#Count: lhs 출연빈도, {} 경우: rhs 출현빈도


#연관규칙의 시각화
install.packages('arulesViz')
library(arulesViz)

plot(rule2,method='graph')

#후행사건:라면
na<- subset(rule2,rhs %in% '라면')
na#set of 8 rules

plot(na,method='graph')


#########################################
# 2. 트랜잭션 객체 생성 
#########################################

#형식)
#read.transactions(file, format=c("basket", "single"),
#      sep = NULL, cols=NULL, rm.duplicates=FALSE,encoding="unknown")
#------------------------------------------------------
#file : file name
#format : data set의 형식 지정(basket 또는 single)
# -> single : 데이터 구성(2개 칼럼) -> transaction ID에 의해서 상품(item)이 대응된 경우
# -> basket : 데이터 셋이 여러개의 상품으로 구성 -> transaction ID 없이 여러 상품(item) 구성
#sep : 상품 구분자
#cols : single인 경우 읽을 컬럼 수 지정, basket은 생략(transaction ID가 없는 경우)
#rm.duplicates : 중복 트랜잭션 항목 제거
#encoding : 인코딩 지정
#------------------------------------------------------

# (1) single 트랜잭션 객체 생성
## read demo data - sep 생략 : 공백으로 처리, single인 경우 cols 지정 
# format = "single" : 1개의 transaction id에 의해서 item이 연결된 경우 
setwd("C:/ITWILL/2_Rwork/data")
stran <- read.transactions("demo_single",format="single",cols=c(1,2)) 
inspect(stran)

# <실습> 중복 트랜잭션 객체 생성
stran2<- read.transactions("single_format.csv", format="single", sep=",", 
                           cols=c(1,2), rm.duplicates=T)
stran2
# transactions in sparse format with
# 248 transactions (rows) and
# 68 items (columns)

summary(stran2) # 248개 트랜잭션에 대한 기술통계 제공


# 트랜잭션 보기
inspect(stran2) # 248 트랜잭션 확인 

# 규칙 발견
astran2 <- apriori(stran2) # supp=0.1, conf=0.8와 동일함 
#astran2 <- apriori(stran2, parameter = list(supp=0.1, conf=0.8))
astran2 # set of 102 rules
attributes(astran2)
inspect(astran2)

# 향상도가 높은 순서로 정렬 (내림차순) 
inspect(sort(astran2, by="lift"))

# (2) basket 트랜잭션 데이터 가져오기
btran <- read.transactions("demo_basket",format="basket",sep=",") 
inspect(btran) # 트랜잭션 데이터 보기


##############################################
# 3. 연관규칙 시각화(Adult 데이터 셋 이용)
##############################################
#1)데이터셋 로드
library(arules)
data(Adult) # arules에서 제공되는 내장 데이터 로딩
str(Adult) # Formal class 'transactions' , 48842(행)
#Formal class 'transactions' [package "arules"] with 3 slots #Adult 자료는 이미 트렌잭션 형태이다
#class-> object 생성 역할
#3 slots -> object의 멤버(member) :객체 정보
#@data
#@itemInfor
#@itemsetInfo

#멤버 호출: object@member
Adult@data#희소행렬(sparse matrix)
# 115(item) x 48842(rows) sparse Matrix of class "ngCMatrix"
Adult@itemInfo

attributes(Adult)# 트랜잭션의 변수와 범주 보기
################ Adult 데이터 셋 #################
# 32,000개의 관찰치와 15개의 변수로 구성되어 있음
# 종속변수에 의해서 년간 개인 수입이 5만달러 이상 인지를
# 예측하는 데이터 셋으로 transactions 데이터로 읽어온
# 경우 48,842행과 115 항목으로 구성된다.
##################################################
# 15개 변수 목록 :
# y변수 : > 50K, <= 50K.
# 나이 : 연속.
# 직업유형(workclass) : 개인, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, 무급, 무근로.
# fnlwgt : 교육수준(연속)
# 교육 : 학사, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# 교육수 : 연속.
# 결혼상태 : 기혼 -civ- 배우자, 이혼, 미혼, 별거, 사별, 기혼-배우자 부재, 기혼 -AF- 배우자.
# 직업 : 기술 지원, 공예 수리, 기타 서비스, 판매, 경영진, 전문직, 핸들러 청소부, 기계 작업 검사, 임시 사무원, 농업 낚시, 운송 이동, 개인 주택- serv, 보호 -serv, Armed-Forces.
# 관계 : 아내, 자녀, 남편, 비 가족, 기타 친척, 미혼.
# 인종(race) : 백인, 아시아-태평양-섬, 아메리카-인도-에스키모, 기타, 흑인.
# 성별 : 여성, 남성.
# 자본이득(capital-gain) : 연속.
# 자본손실(capital-loss) : 연속.
# 주당시간(hours-per-week) : 연속.
# 출신국가(native-country) : 미국, 캄보디아, 영국, 푸에르토 리코, 캐나다, 독일 등 

# 2) 요약 통계량
summary(Adult)
#most frequent items: top5빈도

# sizes
# 9    10    11    12    13 ->itemset
# 19   971  2067 15623 30162 ->transaction

# 3) 연관 규칙 
#---------------------------------------------------------------
# 신뢰도 80%, 지지도 10%이 적용된 연관규칙 6137 발견   
#----------------------------------------------------------------
ar1 <- apriori(Adult, parameter = list(supp=0.1, conf=0.8))
ar2 <- apriori(Adult, parameter = list(supp=0.2)) # 지도도 높임
ar3 <- apriori(Adult, parameter = list(supp=0.2, conf=0.95)) # 신뢰도 높임
ar4 <- apriori(Adult, parameter = list(supp=0.3, conf=0.95)) # 신뢰도 높임
ar5 <- apriori(Adult, parameter = list(supp=0.35, conf=0.95)) # 신뢰도 높임
ar6 <- apriori(Adult, parameter = list(supp=0.4, conf=0.95)) # 신뢰도 높임
ar6#set of 36 rules
# 결과보기
inspect(head(ar6)) # 상위 6개 규칙 제공 -> inspect() 적용

# confidence(신뢰도) 기준 내림차순 정렬 상위 6개 출력
inspect(head(sort(ar6, decreasing=T, by="confidence")))

# lift(향상도) 기준 내림차순 정렬 상위 6개 출력
inspect(head(sort(ar6, by="lift"))) 


## 연관성 규칙에 대한 데이터 시각화를 위한 패키지
#install.packages("arulesViz") 
library(arulesViz) # rules값 대상 그래프를 그리는 패키지

plot(ar4) # 지지도(support), 신뢰도(conf) , 향상도(lift)에 대한 산포도
plot(ar5, method="graph") #  연관규칙 네트워크 그래프
# 각 연관규칙 별로 연관성 있는 항목(item) 끼리 묶여서 네트워크 형태로 시각화
#연관규칙 네트워크 그래프
#타원 크기: 지지도 (조합),타원 크면 지지 도 그타
#색상:향상도(관련성) 색상이 찐하면 관련성 높다.
#화살표: 아이템 간의 관계 의미 

# 중심 단어 위주 분석
# 안쪽으로 모이는 중심단어 : 후행사건(captical-loss=None)
# 바깥쪽으로 나가는 중심단어: 선행사건 (income= small)

#중심단어 기준 subset
#rhs: 자본손실없음(cpaital-loss=None)연관어
sub1<- subset(ar5, rhs %in% 'capital-loss=None')
sub1
inspect(sub1)
plot(sub1,method="graph")
#지지도: 타원 크기 

#lhs :수입적음(income=small) 연관어
sub2<- subset(ar5, lhs %in% 'income=small')
plot(sub2,method='graph')


######################################
# 4. 식료품점 데이터셋  
######################################

library(arules)

# transactions 데이터 가져오기
data("Groceries")  # 식료품점 데이터 로딩
str(Groceries) # Formal class 'transactions' [package "arules"] with 4 slots
Groceries
# 9835 transactions (rows) and
# 169 items (columns)
Groceries@itemInfo #아이템 이름 정보 확인
Groceries@data

rules <- apriori(Groceries, parameter=list(supp=0.001, conf=0.8))
inspect(rules) #410개 규칙

# 규칙을 구성하는 왼쪽(LHS) -> 오른쪽(RHS)의 item 빈도수 보기  
plot(rules, method="grouped")

# 최대 길이 3이내로 규칙 생성
rules <- apriori(Groceries, parameter=list(supp=0.001, conf=0.80, maxlen=3))
inspect(rules) # 29개 규칙

# confidence(신뢰도) 기준 내림차순으로 규칙 정렬
rules <- sort(rules, decreasing=T, by="confidence")
inspect(rules) 

library(arulesViz) # rules값 대상 그래프를 그리는 패키지
plot(rules, method="graph", control=list(type="items"))

#####################################################################3
# 최대 길이 3이내로 규칙 생성 바탕으로  

# 1. rhs=whole milk 
wmilk<-subset(rules,rhs %in% 'whole milk')
wmilk#set of 18 rules
plot(wmike,method="graph")
#1)지지도 높은 상품: 동시에 구매 가능성 높은 상품 (타원이 큰거)
#->herbs+rolls/buns,curd+hamburger meat, etc..

#향상도가 높은 상품 : 해당 상품과 관련성이 높다.(색이 찐한거)
#->sugar+rice,canned-fish + hygiene articles etc..


#2.rhs='other vegetable

ov<-subset(rules,rhs %in% 'other vegetables')
ov#set of 18 rules
plot(ov,method="graph")

#1) 지지도 높은 상품: 동시에  구매 가능성 높은 상품
#-> pork+butter milk, yogurt+rice, shopping-bags+herbs,etc...

#2) 향상도가 높은 상품: 해당 상품과 관련성이 높다.
#->oil+hard cheese, grapes + onions, etc...


#3. 두개 이상 item 조합 에대한 subset
yr<-subset(rules,lhs %in% c('yogurt','rice'))
yr#set of 6 rules 
plot(yr,method="graph")






































































