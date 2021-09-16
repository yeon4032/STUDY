# chap01_Basic

# 수업내용 
# 1. 패키지와 세션 보기 
# 2. 패키지 사용법 
# 3. 변수와 자료형 
# 4. 기본함수 사용 & 작업공간 


# 1. 패키지와 세션 보기
dim(available.packages()) # 패키지 개수 
# 17439    17

# 세션(session) : R시작 ~ 종료 
sessionInfo()
# R버전, OS, 다국어(locale), base packages(7)
# a <- 10
# b <- 20
# c <- a + b

# 주요 단축키 
# 실행 : Ctrl + Enter
# 자동완성 : Ctrl + Space bar
# 저장 : Ctrl + S
# 여러줄 주석 처리 : Ctrl + Shift + C(토글)

# R실행방법 2가지 

# 1) 줄 단위 
r <- rnorm(1000)
print(r) # 콘솔 출력 
hist(r) # Plots
mean(r) # 평균=0 
sd(r) # 표준편차=1

# 2) 블럭 단위 
pdf("c:/itwill/2_Rwork/output/hist.pdf") # open
hist(r)
dev.off() # close


# 2. 패키지 사용법
# package = 함수 + 데이터셋

# 1) 패키지 설치 : 기본 패키지 30개 이미 설치 
install.packages('stringr') # '패키지명' or "패키지명"
# old version 패키지 다운로드 
install.packages('https://cran.rstudio.com/bin/windows/contrib/3.4/KoNLP_0.80.1.zip',repos=NULL)
installed.packages()

# 2) 패키지 설치 경로 
.libPaths()
# [1] "C:/Users/itwill/Documents/R/win-library/4.0" -> 사용자 패키지 설치 
# [2] "C:/Program Files/R/R-4.0.5/library" -> 최초 30개 패키지 설치 

# 3) 패키지 사용 : in memory 
library(stringr)
library(help='stringr') # 패키지 정보 제공 

str <-"홍길동35이순신45"

# 한글 컴퓨터 이름 : 패키지 설치 오류 해결법 
# 1. 환경변수 : TEMP, TMP -> C:\TEMP 변경 
# 2. 패키지 설치 
# 3. 설치 안되면 R, Rstudio 삭제 후 다시 설치 

str_extract_all(str, '[0-9]{2}') # [1] "35" "45"
str_extract_all(str, '[가-힣]{3}') # "홍길동" "이순신"


# 4) 패키지 삭제 
remove.packages('stringr') # 물리적 폴더 삭제 

install.packages('stringr')

################################
## 패키지 설치 error 해결법 
################################

# 1. 최초 패키지 설치 
# - Rstudio 관리자 권한 실행 -> 패키지 설치 

# 2. 기존 패키지 설치 
# 1) remove.packages('패키지')
# 2) rebooting
# 3) install.packages('패키지')


# 3. 변수와 자료형

# 1) 변수(참조변수) : 객체가 저장된 주소를 저장 

# 2) 변수 작성 규칙 
# - 시작 영문, 숫자 혼용, 특수문자(_, .) 
# ex) kor100, member.id, member_id
# - 예약어, 함수명 사용 불가 
# - 대문소자 구분 
# - 가장 최근 값으로 수정 

kor <- 90
mat <- 80
tot = kor + mat # sum
tot # print(tot)

TOT = (kor + mat) * 0.1
TOT = (kor + mat) * 100
TOT

# scala vs vector
name <- "홍길동" # '홍길동'
age <- 35

#vector 
names <- c("홍길동", "이순신", "유관순") 
ages <- c(35, 45, 25)

names
names[2] # "이순신"
mean(ages) # 35

# 3) 자료형(data type)
int <- 1000
string <- '우리나라 대한민국'
boolean <- TRUE # FALSE
int; string; boolean

# mode(변수)
mode(int) # numeric
mode(string) # character
mode(boolean) # logical

# is.xxx(변수) -> T/F
is.numeric(int) # TRUE
is.character(int) # FALSE
is.logical(boolean) # TRUE
is.na() # NA -> NULL(결측치)

score <- c(50, 60, 70, NA, 80)
score # 50 60 70 NA 80

# NA->TRUE, not NA -> FALSE
is.na(score) # FALSE FALSE FALSE TRUE FALSE

# 4) 자료형 변환(Casting)
# 형식) as.xxxx(x)

# (1) 문자형 -> 숫자형 
x <- c(10, 20, 30, '40')
x
mode(x) # "character"
sum(x) # error
plot(x)
barplot(x) # error 

#as.xxxx(값)
num <- as.numeric(x) 
num
sum(num)
barplot(num)

# (2) 요인형(Factor) 변환 
# - 특정 변수 -> 집단변수 
# - 독립변수(설명변수) 범주형 경우 -> 더미변수(0,1)

# 문자형 -> 요인형 
gender <- c("M","F","F","M","M")
gender # "M" "F" "F" "M" "M"
plot(gender) # error

mode(gender) # "character"

fgender <- as.factor(gender)
fgender
#[1] M F F M M
#Levels: F(0) M(1)

str(fgender)
#Factor w/ 2 levels "F","M": 2 1 1 2 2

mode(fgender) # "numeric"
plot(fgender)


# mode vs class
# mode : 변수 자료형 반환 
# class : 객체(변수) 출처 반환 
mode(fgender) # "numeric"
class(fgender) # "factor" <- class 


# 요인형 변환시 주의사항 
num <- c(4,2,4,2)
mode(num) # "numeric"

# 숫자형 -> 요인형 
fnum <- as.factor(num)
fnum
# [1] 4 2 4 2
# Levels: 2 4

# 요인형 -> 숫자형 : 잘못된 결과 
num2 <- as.numeric(fnum)
num2 # 2 1 2 1

# (a) 요인형 -> 문자형 
snum <- as.character(fnum)

# (b) 문자형 -> 숫자형 
num2 <- as.numeric(snum)
num2


# (3) 날짜형 변환 
Sys.Date() # "2021-04-23"
Sys.time() # "2021-04-23 17:07:15 KST"

today <- "2021-04-23 17:07:15"
mode(today) # "character"

ctoday <- as.Date(today)
ctoday
mode(ctoday) # "numeric"
class(ctoday) # "Date"

# 4. 기본함수 사용 & 작업공간

# 1) 기본함수 : 7개 base 패키지에서 제공하는 함수 
help(as.Date) # 함수 도움말 

dates <- c("02/27/92", "02/27/92", "01/14/92", "02/28/92", "02/01/92")
length(dates) # 5
class(dates) # "character"

cdates <- as.Date(dates, "%m/%d/%y")
cdates
class(cdates) # "Date"

# 영어식 월 약자 -> 한국식 날짜 
edate <- '26-Apr-21' # 2021-04-26
kdate <- as.Date(edate, "%d-%b-%y")
kdate

# 다국어 정보 확인 
Sys.getlocale()

# 다국어 정보 수정 : 영어권 
Sys.setlocale(locale = 'English_USA')
kdate <- as.Date(edate, "%d-%b-%y")
kdate # "2021-04-26"

# 다국어 정보 수정 : 한국권 
Sys.setlocale(locale = 'Korean_Korea')


# 2) 기본 데이터셋 
data()
data(Nile) # 메모리 로딩 
Nile
mode(Nile) # "numeric"
plot(Nile)
mean(Nile) # 919.35


# 3) 작업공간 
getwd() # C:/ITWILL/2_Rwork
setwd("C:/ITWILL/2_Rwork/data")

emp <- read.csv("emp.csv")
emp


