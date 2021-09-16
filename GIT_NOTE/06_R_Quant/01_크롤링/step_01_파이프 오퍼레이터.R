# step_01:파이프 오퍼레이터 (%>%)
#sqrt(max(3,5))와 같은 표현법을 간단히표현하는 방법

#EG)
#표 2.3: 파이프 오퍼레이터의 표현과 내용 비교
#내용	표현.방법
#F(x) =	x %>% F
#G(F(x)) =	x %>% F %>% G

#문제1: log(), diff(), exp(), round()에 대한 값을 순차적으로 구하고자 합니다
x = c(0.3078, 0.2577, 0.5523, 0.0564, 0.4685,
      0.4838, 0.8124, 0.3703, 0.5466, 0.1703)

# 방법 1 
x1 = log(x)
x2 = diff(x1)
x3 = exp(x2)
round(x3, 2)

# 방법2
round(exp(diff(log(x))), 2)

#방법 3 :파이프 오퍼레이터 (%>%)
library(magrittr)
x %>% log() %>% diff() %>% exp() %>% round(., 2)

# 오류에 대한 예외처리
#for loop 구문을 통해 수천 종목에 해당하는 웹페이지에 접속해 해당 데이터를 읽어옵니다.
#tryCatch() 함수를 이용하면 예외처리, 즉 오류가 발생할 경우 이를 무시하고 넘어갈 수 있습니다.

# 함수 tryCath
result = tryCatch({
  expr
}, warning = function(w) {
  warning-handler-code
}, error = function(e) {
  error-handler-code
}, finally = {
  cleanup-code
})

#문제1
number = data.frame(1,2,3,"4",5, stringsAsFactors = FALSE)

for (i in number) {
  print(i^2)
}

#[1] 1
#[1] 4
#[1] 9
#Error in h(simpleError(msg, call)) : -> 4 번째 데이터가 str 임으로 안됨

for (i in number) {
  tryCatch({
    print(i^2)
  }, error = function(e) {
    print(paste('Error:', i))
  })
}

#[1] 1
#[1] 4
#[1] 9
#[1] "Error: 4"
#[1] 25





