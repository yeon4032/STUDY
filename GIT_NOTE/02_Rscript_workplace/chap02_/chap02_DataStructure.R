# chap02_DataStructure


#############################
## 제2장 자료구조의 유형 
#############################

# 1. Vector 자료구조 
# - 동일한 자료형을 갖는 1차원 배열구조
# - 생성 함수 : c(), seq(), rep()

# 1) c(값1, 값2, ...)함수
var1 <- c(23, -12, 10:20)
var1 #print(var1)
length(var1) # vector 길이 : 13 
mode(var1) # "numeric"
sum(var1) # 176

# 벡터 이름 지정 
ages <- c(30, 35, 40)
names(ages) = c("홍길동", "이순신", "강감찬")  
ages

# 객체 구조 확인 
str(ages)
# Named num [1:3] 30 35 40
# - attr(*, "names")= chr [1:3] "홍길동" "이순신" "강감찬"

# 2) seq(from, to, by)
seq(from=1, to=100, by=2)
seq(from=100, to=1, by=-2)

# 3) rep()
rep(1:3, 3)
rep(1:3, each=3)

# 4) 색인(index) : 값의 위치 
# 형식) 변수[n] : n=1 ~ n
a <- 1:50 # c(1:50)
a
a[10] # 10
a[11:20] # 11 12 13 14 15 16 17 18 19 20
a[c(10,20,30:40)]
a[-c(10,20)] # -기호 : 제외 

# 함수 이용 
length(a) # 50
a[10:length(a)]
# 짝수 수열 참조 
a[seq(2, length(a), 2)]


# 조건식 이용 
a[a>=10]
a[a>=10 & a<=30] # & : and 
a[a>=10 | a<=30] # | : or
a[!(a>=10)] # ! : not


# 2.Matrix 자료구조
# - 동일 자료형을 갖는 2차원 배열
# - 생성함수 : matrix, rbind, cbind
# - 처리함수 : apply

# 1) matrix
m1 <- matrix(data = 1:5, nrow = 1, ncol = 5)
m1
dim(m1) # shape : 1 5

m2 <- matrix(data=1:9, nrow=3, ncol = 3, byrow = TRUE)
dim(m2) # 3 3
m2

colnames(m2) <- c("one","two","three")
m2

# 2) rbind
x1 <- 1:5
x2 <- 6:10

m3 <- rbind(x1, x2)
m3
dim(m3) # 2 5

# 3) cbind
m4 <- cbind(x1, x2)
m4
dim(m4) # 5 2


# 4) matrix 색인 
# 형식) 변수[row, col]

m4[1,] # 1행 전체 
m4[,1] # 1열 전체 
m4[c(2,3),] # box형 참조
m4[-3,] # 2행 제외 

# ADsP
xy <- rbind(x1, x2)
xy
xy[1,]
xy[,1]
# 1) [1,]는 x1과 같다.(o)
# 2) [,1]는 x2와 같다.(x)
# 3) 2x5 행렬구조(o) 
# 4. matrix(o)


# 5) apply(data, 행/열, Func)
apply(m4, 1, mean) # 행 평균 
apply(m4, 2, mean) # 열 평균 
apply(m4, 2, sd) # 열 표준편차 


# 3. Array 자료구조 
# - 동일 자료형을 갖는 3차원 배열
# - 생성함수 : array(data, dim)

data <- 1:12
arr <- array(data = data, dim = c(3,2,2)) # (행,열,면)
arr
arr[,,2]

data("iris3")
iris3

# Array 색인 : 변수[행,열,면]
iris3[,,1] # 꽃의 종1 
iris3[,,2] # 꽃의 종2
iris3[,,3] # 꽃의 종3


# 4.DataFrame 자료구조 
# - 서로 다른 자료형을 갖는 컬럼
# - 생성함수 : data.frame
# - 처리함수 : apply

# 1) vector 생성 
eno <- 1:3
ename <- c("hong", "lee", "yoo")
age <- c(35, 45, 25)
pay <- c(250, 350, 250)

# 2) DataFrame 생성 
emp <- data.frame(eno, ename, age, pay)
emp

str(emp)
# 'data.frame':	3 obs. of  4 variables:
# $ eno  : int  1 2 3    : 이산형 
# $ ename: chr  "hong" "lee" "yoo" : 문자형(연산 x)
# $ age  : num  35 45 25 : 연속형 
# $ pay  : num  250 350 250 : 연속형 


# 3) 자료 참조 : object$column
pay <- emp$pay
mean(pay)

# 4) 변수[row, col]
emp[1, ] # hong 사원 정보 
emp[, 4] # pay 칼럼 정보 

x1 <- 1:5
x2 <- 6:10
df <- data.frame(X1=x1, X2=x2)
df

# 5) apply
apply(df, 2, mean)


# 5. List 
# - 1개 객체에 서로 다른 자료형과 서로 다른 데이터구조 저장 
# - 형식) list(key=value, key=value, ...)
# - key 이용 -> value 참조 


# 1) list(key=value) 형식 
member <- list(name="홍길동",
               age = 35,address="한양",
               gender="남자", htype="아파트")

member
# $name -> $key
# [1] "홍길동" -> value
# 
# $age
# [1] 35
# 
# $address
# [1] "한양"
# 
# $gender
# [1] "남자"
# 
# $htype
# [1] "아파트"


member$name # object$key -> value

# 2) list(value) 형식 : key 생략 -> 기본 key 제공 
member2 <- list("홍길동",35, "한양")
member2

# [[1]] -> 기본 key : [[n]]
# [1] "홍길동" -> value
# 
# [[2]]
# [1] 35
# 
# [[3]]
# [1] "한양"

member2[[1]] # "홍길동"


# 6. 문자열 처리 & 정규표현식(메타문자)
#install.packages('stringr')
library(stringr)

# 형식) str_extract('문자열', '패턴')
# ex) str_extract('###232&^%^', '[0-9]{3}')
str_extract('###232&^%^', '[0-9]{3}') # [1] "232"

re <- str_extract_all('###232&^%^234**$$', '[0-9]{3}')
re
#[[1]]
#[1] "232" "234"

re[[1]] # key(1) -> value(n)
re[[1]][2] # "234"

# 1) 반복관련 메타문자 : [x]: x1개 일치, {n} : n개 연속 
string <- "hong35lee45kang55유관순25이사도시55"
string

# (1) 숫자 추출 
re <- str_extract_all(string, '[0-9]{2}')
# [[1]]
# [1] "35" "45" "55" "25" "55"

# list -> vector(value)
age <- re[[1]]
num <- as.numeric(age)
mean(num) # 43

# (2) 영문 추출 
str_extract_all(string, '[a-z]{3,}')

# 3) 한글 이름 추출 
str_extract_all(string, '[가-힣]{3,}')
str_extract_all(string, '[가-힣]{3,4}')


# 2) 접두어/접미어 메타문자 : ^, $
email <- "kpjiju@naver.com" # "id@호스트이름.최상도메인 
str_extract_all(email, '^[a-z]\\w{3,}@\\w{3,}.com$')
# \\w : 숫자,영문,한글 혼용 단어 

# 패턴 불일치 예 
email2 <- "1kpjiju@naver.com" # "id@호스트이름.최상도메인 
str_extract_all(email2, '^[a-z]\\w{3,}@\\w{3,}.com$')

# 3) 부정 메타문자 : [^x]
str_extract_all(string, '[^0-9]{3,}') # 숫자 불용어 처리 

# 4) 문자열 길이
length(string) # 1
str_length(string) # 28


# 5) 문자열 교체 
str_replace_all(string, '[0-9]{2}', '-')

# 6) 문자열 분리(split) -> 토큰(문장 -> 단어, 문단 -> 문장)
string2 <- "홍길동,이순신,유관순"
names <- str_split(string2, ",")
names 

# list -> vector 
vnames <- unlist(names)
vnames

# 7) 단어 -> 문장 
sent <- str_c(vnames, collapse = ' ')
sent # "홍길동 이순신 유관순"


# 7. 서브셋(subset) 만들기 
x <- 1:5
y <- 6:10
z <- letters[1:5]

df <- data.frame(x, y, z)
df
#   x  y z
# 1 1  6 a
# 2 2  7 b
# 3 3  8 c
# 4 4  9 d
# 5 5 10 e

help(subset)
# subset(x, subset=조건식, select=칼럼명, drop = FALSE, ...)

# 1) subset=조건식 : 행 선택 
df2 <- subset(df, subset = y >= 8)
df2

# 2) select=c('칼럼명') : 열 선택 
df3 <- subset(df, select = c(x, y))
df3

# 3) %in% (목록)
df4 <- subset(df, z %in% c("a","c","e"))
df4

# 문제 
iris
str(iris)
# 'data.frame':	150 obs. of  5 variables:
# $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ... -> 연속형 
# $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ... -> 연속형
# $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ... -> 연속형
# $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ... -> 연속형
# $ Species     : Factor w/ 3 levels "setosa","versicolor", -> 요인형(더미변수)

# 문1) subset 생성 : 1,3,5번 칼럼 선택 -> iris_df
iris_df <- subset(iris, select = c(Sepal.Length, Petal.Length, Species))
str(iris_df)
# 'data.frame':	150 obs. of  3 variables:


# 문2) subset 생성 : 문1) 결과에서 3번 칼럼의 평균값 이상 선택 -> iris_df2 
mean(iris$Petal.Length) # 3번 칼럼 평균 : 3.758
iris_df2 <- subset(iris_df, subset = Petal.Length >= mean(iris$Petal.Length))
str(iris_df2)
# 'data.frame':	93 obs. of  3 variables:
# $ Sepal.Length: num  7 6.4 6.9 5.5 6.5 5.7 6.3 6.6 5.2 5.9 ...
# $ Petal.Length: num  4.7 4.5 4.9 4 4.6 4.5 4.7 4.6 3.9 4.2 ...
# $ Species     : Factor w/ 3 levels "setosa","versicolor",..: 2 2 2 2 2 2 2 2 2 2 ...











