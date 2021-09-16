#################################
## <제6장 연습문제>
################################# 

# 01. mtcars 데이터셋의 qsec(1/4마일 소요시간) 변수를 대상으로 극단치(상위 0.3%)를 
# 발견하고, 정제하여 mtcars_df 이름으로 서브셋을 생성하시오.

library(ggplot2)
str(mtcars) # 'data.frame':	32 obs. of  11 variables:


# (1) 이상치 통계
boxplot(mtcars$qsec)$stats # 1/4마일 소요시간 
# 일반적으로 상하위 0.3% 극단치로 본다.

# (2) 서브셋 생성 
mtcars_sub <- subset(mtcars, qsec >= 14.5 & qsec <= 20.22)

# (3) 정제 결과 확인 
boxplot(mtcars_sub$qsec)


# 02. 본문에서 생성된 dataset2의 resident 칼럼을 대상으로 NA 값을 제거한 후 dataset3 변수에 저장하시오.
# 방법1) subset 이용 : 특정 칼럼 결측치가 아닌 경우
dim(dataset2)
dataset3 <- subset(dataset2, !(is.na(dataset2$resident)) )  
dim(dataset3)

# 방법2) na.omit 이용 
dataset3 <- dataset2
resident <- na.omit(dataset2$resident) # 특정 칼럼만 결측치 제거 
dataset3$resident <- resident


# 03. 본문에서 생성된 dataset2의 직급(position) 칼럼을 대상으로 1급 -> 5급, 5급 -> 1급 형식으로
# 역코딩하여 position2 칼럼에 추가하시오.
position <- dataset2$position
cprosition <- 6 - position # 역코딩
dataset2$position2 <- cprosition # 칼럼 추가 


# 04. dataset2의 gender 칼럼을 대상으로 1->"남자", 2->"여자" 형태로 코딩 변경하여 
# gender2 칼럼에 추가하고, 파이 차트로 결과를 확인하시오.
dataset2$gender2[dataset2$gender == 1] <- "남자"
dataset2$gender2[dataset2$gender == 2] <- "여자"
table(dataset2$gender2)
# 남자 여자 
# 119   87
pie(table(dataset2$gender2))

# 05. 나이를 30세 이하 -> 1, 31~55 -> 2, 56이상 -> 3 으로 리코딩하여 age3 칼럼에 추가한 후 
# age, age2, age3 칼럼만 확인하시오.
dataset2$age3[dataset2$age <= 30] <- 1
dataset2$age3[dataset2$age > 30 & dataset2$age <= 55] <- 2
dataset2$age3[dataset2$age > 55] <- 3
dataset2[c("age","age2","age3")] # 결과확인 

# 06. 정제된 dataset2를 대상으로 작업 디렉터리(c:/itwill/2_Rwork/output)에 cleanData.csv 파일명으로 
# 따옴표와 행 이름을 제거하여 저장하고, new_data변수로 읽어오시오.

# (1) 정제된 데이터 저장
write.csv(dataset2, 'cleanData.csv', row.names = F, quote = F)

# (2) 저장된 파일 불러오기/확인
new_data <- read.csv('cleanData.csv')


# 07. user_data.csv와 return_data.csv 파일을 이용하여 각 고객별 
# 반품사유코드(return_code)를 대상으로 다음과 같이 파생변수를 추가하시오.

# <조건1> 반품사유코드에 대한 파생변수 칼럼명 설명 
# 제품이상(1) : return_code1, 변심(2) : return_code2, 
# 원인불명(3) :> return_code3, 기타(4) : return_code4 
return_data <- read.csv('return_data.csv')
head(return_data)
#   user_id return_code
# 1    1008           1
# 2    1009           2

library(reshape2)
return_df <- dcast(return_data, user_id ~ return_code, length)
head(return_df)
#  user_id 1 2 3 4
#1    1008 1 0 0 0
#2    1009 0 1 0 0

table(return_data$return_code)

names(return_df) <- c('user_id','return_code1','return_code2','return_code3','return_code4')
head(return_df)

# <조건2> 고객별 반품사유코드를 고객정보(user_data) 테이블에 추가(join)
user_return_data <- join(user_data, return_df, by='user_id')
head(user_return_data, 10)










