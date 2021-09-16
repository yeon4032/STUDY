# chap04_2_Function

# 1. 사용자정의함수 

# 함수명 <- function([인수]){
#   실행문1
#   실행문2
#   [return(값)]
# }

# 함수 정의 
fx <- function(x){
  calc = x^2 + x*2 + 5
  cat('calc=', calc)
  return(calc) # 반환 
}

# 함수 호출 
result = fx(2) # x=2
cat('result=', result)


# 인수(매개변수)가 없는 함수 
f1 <- function(){
  cat('인수가 없는 함수')
}

f1() # 함수 호출 

# 인수가 있는 경우 
f2 <- function(x){ # x : 가인수
  cat('x의 값 =', x, '\n')
  print(x^2)
}

f2(25) # 함수 호출(실인수)

# 반환(리턴)값이 있는 함수 
f3 <- function(x, y){
  add <- x + y
  return(add)
}

add = f3(10, 20) # 함수 호출 & 반환값 
cat('add =', add)


avg <- function(x, y){
  tot = f3(x, y) # 다른 함수 호출 
  a = tot / 2
  #df = data.frame(tot, a)
  return(a)
}

cat('avg =', avg(10, 20)) # avg = 15


# 문1) 표본분산, 표본표준편차를 구하는 함수를 정의하기 
# 함수명 : var_sd
x <- c(7, 5, 12, 9, 15, 6)
x
mean(x) # 9
var(x) # 14.8
sd(x) # 3.847077
sqrt(var(x)) # 3.847077

# 표본분산 : var = sum((x - 산술평균)^2) / (n-1)
# 표본표준편차 : sd = sqrt(var)


# 산술평균 함수 
avg <- function(x){
  return(sum(x) / length(x))
}

# 분산과 표준편차 함수 
var_sd <- function(x){
  # 1. 산술평균 
  a <- avg(x)
  # 2. 분산
  var <- sum((x - a)^2) / (length(x)-1)
  # 3. 표준편차 
  sd <- sqrt(var)
  cat('분산 =', var, '\n')
  cat('표준편차 =', sd)
}

var_sd(x) # 함수 호출 
# 분산 = 14.8 
# 표준편차 = 3.847077 

# 구구단(2*1=2 ~ 2*9=18)을 출력하는 함수 정의 
gugu <- function(dan){
  cat('***', dan,'단 **\n')
  for(i in 1:9){
    cat(dan,'*',i,'=', dan*i, '\n')
  }
}

gugu(2)
gugu(5)
gugu(9)


# 2. R 주요 내장함수 

# 1) 기술통계함수 

vec <- 1:10          
min(vec)                   # 최소값
max(vec)                   # 최대값
range(vec)                  # 범위
mean(vec)                   # 평균
median(vec)                # 중위수
sum(vec)                   # 합계
prod(vec)                  # 데이터의 곱
1*2*3*4*5*6*7*8*9*10
summary(vec)               # 요약통계량 

sd(rnorm(10))      # 정규분포 자료 10개(무작위 추출)를 대상으로 표준편차 구하기
factorial(5) # 팩토리얼=120(1*2*3*4*5)
sqrt(49) # 루트


# 2) 반올림 관련 함수 
x <- c(1.5, 2.5, -1.3, 2.5)
round(mean(x)) # 1.3 -> 1
ceiling(mean(x)) # x보다 큰 정수 
floor(mean(x)) # x보다 작은 정수 


# 3) 난수 생성 & 확률분포 
# 연속확률분포 : 주어진 구간에서 나올 수 있는 셀 수 없는 값 
# 이산확률분포 : 주어진 구간에서 나올 수 있는 셀 수 있는 값 
# 분석기사 : 보기에서 다른 유형의 확률분포 고르기 
# - 정규분포, 지수분포, Z/F/T분포, 이항분포 

# (1) 정규분포를 따르는 난수 : 연속확률분포(연속형/실수형)
# 형식) rnorm(n, mean=0, sd=1)
n <- 1000
r <- rnorm(n, mean=0, sd=1) # N(0, 1^2)
r
hist(r) # 대칭성 

# (2) 균등분포를 따르는 난수 : 연속확률분포(연속형/실수형)
# 형식) runif(n, min=0, max=1)
r2 <- runif(n, min = 0, max = 1) # 0~1 사이 확률 
r2
hist(r2) # 균등성 

# (3) 이항분포를 따르는 난수 : 이산확률분포(이산형/정수형)
# 형식) rbinom(n, size, prob) -> n : 반복, size : 시행횟수, prob : 성공확률 

# size=1 : 베르누이분포  
r3 <- rbinom(n=10, size = 1, prob = 0.5) # B(1, 0.5)
r3 # 0 0 0 1 1 0 1 0 0 0 
# 1 1 1 0 0 1 1 0 1 0

set.seed(123) # 동일한 난수 제공 
r3 <- rbinom(n=10, size = 1, prob = 0.5)
r3 # 1 1 1 0 0 1 1 0 1 0

r3 <- rbinom(n=10, size = 1, prob = 0.5)
r3 # 0 1 0 1 1 0 1 1 1 0

# size = n : 이항분포  
r3_2 <- rbinom(n=10, size = 10, prob = 0.5) # B(10, 0.5)
r3_2 # 5 5 7 5 8 3 5 4 4 7


# (4) sample(x, size, replace, prob)

# 비복원 추출 : x >= size, replace=FALSE
dim(iris) #  150   5
nrow(iris) # 150

idx <- sample(x=nrow(iris), size=nrow(iris)*0.7, replace=FALSE)
idx; length(idx) # 105

train <- iris[idx,]
train # 훈련셋 
dim(train) # 105   5

test <- iris[-idx,]
test # 검정셋 
dim(test) # 45  5

# 홀드아웃 방식 : 70% vs 30%

# 복원추출 : x < size, replace = TRUE
sp <- sample(x=2, size = nrow(iris), replace = TRUE, prob=c(0.7, 0.3))
table(sp) # 1:103  2:47

train <- iris[sp == 1, ]
dim(train)
test <- iris[sp == 2, ]
dim(test)


# 문) 비복원 추출 방식 : 
# bmi.csv 파일을 대상으로 80:20 비율로 훈련셋/검정셋 샘플링하기 
getwd() # "C:/ITWILL/2_Rwork/data"

bmi <- read.csv('bmi.csv')
dim(bmi) # 20000     3

# 80% vs 20% -> 홀드아웃 방식 
idx <- sample(x=nrow(bmi), size=nrow(bmi)*0.8) # replace 생략 

train <- bmi[idx, ]
test <- bmi[-idx, ]
dim(train) # 16000     3
dim(test) # 4000    3
















