#################################
## <제9장 연습문제>
################################# 

# 01. 교육수준(education)과 흡연율(smoking) 간의 관련성을 분석하기 위한 가설을 수립하고, 
# 이를 토대로 가설을 검정하시오.[독립성 검정]

#귀무가설 : 
#연구가설 : 

#<단계 1> 파일 가져오기
setwd("c:/ITWILL/2_Rwork/data")
smoke <- read.csv("smoke.csv", header=TRUE)
# 변수 보기
head(smoke) # education, smoking 변수

#<단계 2> 코딩 변경 - 변수 리코딩 <- 가독성 제공    
# education(독립변수) : 1:대졸, 2:고졸, 3:중졸 


# smoking(종속변수): 1:과다흡연, 2:보통흡연, 3:비흡연
# education 변수 리코딩 : education2
# smoking 변수 리코딩 : smoking2


#<단계 3> 교차분할표 작성(table 함수 이용)  

#<단계 4> 독립성 검정(CrossTable 함수 이용)

#<단계 5> 검정결과 해석


# 02. 나이(age3)와 직위(position) 간의 관련성을 단계별로 분석하시오. [독립성 검정]
# 귀무가설 : 나이와 직위은 관련성이 없다.
# 대립가설 : 나이와 직위은 관련성이 있다.

#[단계 1] 파일 가져오기
data <- read.csv("cleanData.csv")
head(data)

#[단계 2] 변수 선택   
x <- data$position # 행 - 직위 변수 이용
y <- data$age2 # 열 - 나이 리코딩 변수 이용

df<-data.frame(x,y)
#[단계 3] 산점도를 이용한 변수간의 관련성 보기 - plot(x,y) 함수 이용
plot(x,y) #두 변인 간 상관성 확인


#[단계 4] 독립성 검정
chisq.test(x=x,y=y)
# X-squared = 287.9, df = 8, p-value < 2.2e-16

#[단계 5] 검정결과 해석 


# 03. 직업유형에 따른 응답정도에 차이가 있는가를 단계별로 검정하시오.[동질성 검정]

#[단계 1] 파일 가져오기
response <- read.csv("response.csv")
head(response) # 변수 보기
#   job response

# [단계 2] 코딩 변경 
# job 칼럼 코딩 변경 : 1:학생, 2:직장인, 3:주부 
# response 칼럼 코딩 변경 : 1:무응답, 2:낮음, 3:높음

# job 변수 리코딩 : job2


# response 변수 리코딩 : response2


# [단계 3] 교차분할표 작성


# [단계 4] 동질성 검정  


#[단계 5] 검정결과 해석
