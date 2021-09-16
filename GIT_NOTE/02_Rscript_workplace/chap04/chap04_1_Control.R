# chap04_1_Control 

# <실습> 산술연산자 
num1 <- 100 # 피연산자1
num2 <- 20  # 피연산자2
result <- num1 + num2 # 덧셈
result # 120
result <- num1 - num2 # 뺄셈
result # 80
result <- num1 * num2 # 곱셈
result # 2000
result <- num1 / num2 # 나눗셈
result # 5

result <- num1 %% num2 # 나머지 계산
result # 0

result <- num1^2 # 제곱 계산(num1 ** 2)
result # 10000
result <- num1^num2 # 100의 20승
result # 1e+40 -> 1 * 10의 40승과 동일한 결과

x <- 10
x = 10

# <실습> 관계연산자 : T/F
# (1) 동등비교 
boolean <- num1 == num2 # 두 변수의 값이 같은지 비교
boolean # FALSE
boolean <- num1 != num2 # 두 변수의 값이 다른지 비교
boolean # TRUE

# (2) 크기비교 
boolean <- num1 > num2 # num1값이 큰지 비교
boolean # TRUE
boolean <- num1 >= num2 # num1값이 크거나 같은지 비교 
boolean # TRUE
boolean <- num1 < num2 # num2 이 큰지 비교
boolean # FALSE
boolean <- num1 <= num2 # num2 이 크거나 같은지 비교
boolean # FALSE

# <실습> 논리연산자(and, or, not, xor)
logical <- num1 >= 50 & num2 <=10 # 두 관계식이 같은지 판단 
logical # FALSE
logical <- num1 >= 50 | num2 <=10 # 두 관계식 중 하나라도 같은지 판단
logical # TRUE

logical <- num1 >= 50 # 관계식 판단
logical # TRUE
logical <- !(num1 >= 50) # 괄호 안의 관계식 판단 결과에 대한 부정
logical # FALSE

x <- TRUE; y <- FALSE
xor(x,y) # [1] TRUE
x <- TRUE; y <- TRUE
xor(x,y) # FALSE


# 1. 조건문 : if(조건식), ifelse(조건식), which(조건식)

# 1) if형식1
# if(조건식){
#    실행문 
# }else{
#   실행문
# }

x <- 10
y <- 50

if(x > y){  # 조건식 : 산술,관계,논리연산자  
  cat('x > y') # TRUE
}else{
  cat('x < y') # FALSE
}

# 학점 구하기 
score <- scan()
score

if(score >= 60){
  cat('합격 :', score)
}else{
  cat('불합격 :', score)
}

# 2) if형식2 
# if(조건식1){
#    실행문1 
# }else if(조건식2){
#   실행문2
# }else{
#  실행문3
# }

if(score>=90 & score <= 100){
  cat('A학점 : ', score)
}else if(score >= 80){
  cat('B학점 : ', score)
}else if(score >= 70){
  cat('C학점 : ', score) 
}else{
  cat('F학점 : ', score) 
}

# 문1) 키보드로 입력한 숫자를 짝수 or 홀수 구분하기 
num <- scan()

if(num %% 2 == 0){
  cat(num, '은 짝수')
}else{
  cat(num, '은 홀수')
}


# 2) ifelse(조건식, 참, 거짓)
# if + 반복
# vector 입력 -> ifelse() -> vector 출력 

score <- c(75,85,65,NA,72,55)
ifelse(score >= 70, '합격', '불합격')
# [1] "합격"   "합격"   "불합격" NA "합격"   "불합격"

# 결측치 처리 
ifelse(is.na(score), 0, score)
# 75 85 65  0 72 55

getwd() # "C:/ITWILL/2_Rwork/data"
excel <- read.csv('excel.csv', header = TRUE)
str(excel)

q3 <- excel$q3
length(q3) # 402

table(q3) # 5점 척도 -> 범주형 
result <- ifelse(q3 >= 3, '큰 값', '작은 값')
table(result)


# 3) which()
x <- c(2,5,10:20, 50)
x

idx <- which(x == 19) # 12 -> index
x[idx] # 19


no <- c(1:5)
name <-c("홍길동","이순신","강감찬","유관순","김유신")
score <- c(85,78,89,90,74)

exam <- data.frame(학번=no,이름=name,성적=score)
exam

idx <- which(exam$'이름' == '이순신')
exam[idx,]


# 2. 반복문 : for(), while()

# 1) for(변수 in 값){ 실행문 }
num <- 1:10
num # 1  2  3  4  5  6  7  8  9 10

d <- numeric() # 빈 vector

for(x in num){
  cat('x=', x, '\n')
  d[x] <- x^2 # d[10] <- 10^2
}

cat('d=', d)

for(x in num){
  if(x %% 2 == 0){ # 짝수 
    print(x)
  }else{ # 홀수 
    next # skip
  } 
}  

even <- 0 # 짝수 합 
odd <- 0 # 홀수 합 

for(x in num){
  if(x %% 2 == 0){ # 짝수 
    even <- even + x # 누적변수 
  }else{ # 홀수 
    odd <- odd + x
  } 
}  

cat('even=', even, ', odd=', odd)


# 학성관리 
kor <- c(65, 89, 56)
eng <- c(89,78,56)
mat <- c(90, 78, 55)
name <- c('홍길동', '이순신', '유관순')

student <- data.frame(name, kor, eng, mat)
student

# 총점과 평균 칼럼 추가 
tot <- student$kor + student$eng + student$mat
tot
student$tot <- tot
student$avg <- round(tot/3, 2)

student

# grade 칼럼 : for문 + index
size <- length(student$name)
grade <- character() # 빈 벡터 

for(i in 1:size){
  if(student$avg[i] >= 90){
    grade[i] <- 'A'
  }else if(student$avg[i] >= 80){
    grade[i] <- 'B'
  }else if(student$avg[i] >= 70){
    grade[i] <- 'C'
  }else{
    grade[i] <- 'F'
  }
}

student$grade <- grade
student

# grade2 칼럼 : ifelse(조건식, 참, 거짓) = for + if
student$grade2 <- ifelse(student$avg >= 90, 'A', 
                         ifelse(student$avg >= 80, 'B',
                                ifelse(student$avg >= 70, 'C','F')))
student


# 2) while(조건식){반복문}
i = 0 # 초기화 

while (i < 10) {
  i <- i + 1 # 카운터 변수 
  cat(i, ' ') # 같은 라인 중복 출력 
}

# 문2) while문으로 x의 각 변량의 제곱 계산하여 y에 저장하기 
x <- c(2, 5, 7, 4, 8)
y <- numeric() # 빈 벡터 

i <- 0 # 색인 역할   

while(i < length(x)){
  i <- i + 1 # 카운터  
  y[i] <- x[i]^2
}

cat('y =', y)


y2 <- ifelse(x>1, x^2, x^2)
y2
