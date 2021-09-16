#################################
## <제4장 연습문제>
#################################   
# 01. 다음 3개의 vector 데이터를 이용하여 client 데이터프레임을 
# 생성하고, 조건에 맞게 처리하시오.

# vector 준비 
name <-c("유관순","홍길동","이순신","신사임당")
gender <- c("F","M","M","F")
price <-c(50,65,45,75)

# 데이터프레임 생성 

# <조건1> price가 65만원 이상인 고객은 "Best" 미만이면 
#     "Normal" 문자열을 result 변수에 넣고, client의 객체에 컬럼으로 추가하기
# 힌트 : ifelse() 함수 이용 
client$result<-ifelse(client$price>=65,'Best','Normal')

# <조건2> result의 빈도수를 구하시오. 힌트) table()함수 이용
table(client$result)

# <조건3> gender가 'M'이면 "Male", 'F'이면 "Female" 형식으로 client의 객체에
#  gender2 컬럼을 추가하고 빈도수 구하기 # 힌트 : ifelse() 함수 이용 
client$gender2<-ifelse(client$gender=='M',"MAle","Female")
table(client$gender2)
# Female   MAle 
#   2      2 

# 02. 다음 벡터(EMP)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
# 이 벡터 데이터를 이용하여 다음과 같은 출력결과가 나타나도록 함수를 정의하시오. 

# <Vector 준비>
EMP <- c("2014홍길동220", "2020이순신300", "2010유관순260")

for(e in EMP){
  print(e)
}

# <출력 결과>
# 전체 급여 평균 : 260


#힌트) 사용 함수
#stringr 패키지 : str_extract()
#숫자변환 함수 : as.numeric()함수






# 함수 호출 
emp_pay(EMP)




