#################################
## <제1장 연습문제>
#################################

#01. 다음 조건에 맞게 name, age, address 변수를 생성하고 출력하시오.

#조건1) name, age, address 변수에 자신의 이름, 나이, 주소를 만들고 출력한다. 
name='홍길동'
age=35
address='서울'
#조건2) mode() 함수를 이용하여 각 변수의 자료형(data type)을 확인한다.
mode(name)
mode(age)
mode(address)

#02. 다음 rain 변수는 비 유무를 나타내는 변수이다. 이 변수를 요인형(Factor)으로 변경하시오.  
rain <- c('YES', 'No', 'YES', 'YES', 'NO')
as.factor(rain)

#03. R에서 제공하는 c()함수를 이용하여 다음과 같이 벡터를 생성하고, 데이터를 처리하시오.

#조건1) 2,4,6,8,10의 자료를 벡터형 변수 num을 생성한다.
num<- c(2,4,6,8,10)
#조건2) 생성된 벡터를 대상으로 평균을 구한다.
mean(num)

#04. R에서 제공하는 women 데이터 셋을 이용하여 다음 조건에 맞게 처리하시오.

#조건1) women은 어떤 데이터 셋 인지를 쓰시오?
data() #Average Heights and Weights for American Women

#조건2) women 데이터 셋의 자료형은 무엇인가?
mode(women) # "list"

#조건3) plot() 함수를 이용하여 기본 차트 그리기
plot(women)

#05. 현재 작업 공간을 확인하고 "C:/ITWILL/2_Rwork/output"로 변경하시오.

getwd()

setwd('C:/ITWILL/2_Rwork/output')

#06. R 프로그래밍 언어의 특징에서 in memory computing에 대해서 설명하시오.
# 사용할 모든 패키지와 데이터셋은 메모리에 로딩되어야 실행할 수 있다.












