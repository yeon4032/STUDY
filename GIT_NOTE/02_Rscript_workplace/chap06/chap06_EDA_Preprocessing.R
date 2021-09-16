# chap06_EDA_Preprocessing

# 1. 탐색적 데이터 조회

# 실습 데이터 읽어오기
setwd("C:/ITWILL/2_Rwork/data")
dataset <- read.csv("dataset.csv", header=TRUE) # 헤더가 있는 경우
# dataset.csv - 칼럼과 척도 관계 


# 1) 데이터 조회
# - 탐색적 데이터 분석을 위한 데이터 조회 

# (1) 데이터 셋 구조
names(dataset) # 변수명(컬럼)
attributes(dataset) # names(), class, row.names
str(dataset) # 데이터 구조보기
dim(dataset) # 차원보기 : 300 7
nrow(dataset) # 관측치 수 : 300
length(dataset) # 칼럼수 : 7 
length(dataset$resident) # 300

# (2) 데이터 셋 조회
# 전체 데이터 보기
dataset # print(dataset) 
View(dataset) # 뷰어창 출력

# 칼럼명 포함 간단 보기 
head(dataset)
head(dataset, 10) 
tail(dataset) 

# (3) 칼럼 조회 
# 형식) dataframe$칼럼명   
re <- dataset$resident # vector - 1차원  
re[1:10]
length(dataset$age) # data 수-300개 

# 형식) dataframe["칼럼명"] 
re2 <- dataset["gender"] # data.frame -> 2차원 
re2[1:10,]
dataset["price"]

# 형식) dataframe[색인] : 색인(index)으로 원소 위치 지정 
dataset[,2] # 두번째 컬럼 -> 1차원 
dataset[2] # 2차원 
dataset[6] # 여섯번째 컬럼
dataset[3,] # 3번째 관찰치(행) 전체
dataset[,3] # 3번째 변수(열) 전체

# dataset에서 2개 이상 칼럼 조회
dataset[c("job", "price")]
dataset[c("job":"price")] # error 
dataset[c(3:5)] # 숫자 색인 이용 
dataset[c(2,6)] 

dataset[c(1,2,3)] 
dataset[c(1:3)] 
dataset[c(2,4:6,3,1)] 
dataset[-c(2)] # dataset[c(1,3:7)] 


# 2. 결측치(NA) 발견과 처리

# 1) 결측치 확인 
summary(dataset$price) # NA's 30

table(is.na(dataset$price)) # 특정 변수 
#FALSE  TRUE 
# 270    30

table(is.na(dataset)) # 전체 변수 
#FALSE  TRUE 
#1982   118

# 그래프 이용 결측치 확인 
install.packages("VIM")
library(VIM)

aggr(dataset, prop = FALSE, numbers = TRUE)
# 왼쪽 그래프 : 각 변수 NA수
# 오른쪽 그래프 : 변수 조합에 의한 NA수 

# 2) 결측치 제거 
length(dataset$resident)#300
resident<-na.omit(dataset$resident)#특정 컬럼 결측치 제거  #컬럼의로 받았음으로 컬럼 으로 명명 한다 
length(resident)#269

dataset2 <- na.omit(dataset) # 전체 칼럼 결측치 제거 
dim(dataset) # 300   7
dim(dataset2) # 209   7


# 3) 결측치 상수 대체 
x <- dataset$price
dataset$price2 <- ifelse(is.na(x), 0, x) # new 변수 추가 

head(dataset[,c('price','price2')], 30)

# 3) 결측치 통계(중위수) 대체
dataset$price3 <- ifelse(is.na(x), median(x, na.rm = T), x)

head(dataset[,c('price','price2', 'price3')], 30)

# 3) 결측치 기계학습 대체 : 다중대체법(학습 -> 예측치 -> 채우기) 
# 적용 대상 : 완벽할 데이터셋(iris) 
# 결측치가 없는 행 학습 -> 결측치 예측 
install.packages('mice')
library(mice)


iris_df <- head(iris, 30)
dim(iris_df) # 30  5

iris_df

# 결측치 생성 
iris_df[1,1] <- NA # 5.1 
iris_df[3,3] <- NA # 1.3 

help(mice)

miceModel <- mice(iris_df) # m = 5
iris_df2 <- complete(miceModel) # 예측 dataset 생성 

iris_df2 # 5.2, 1.9


# 3. 이상치 발견과 정제
# - 정상 범주에서 크게 벗어난 값 
# - 분석 결과 왜곡 

# 1) 범주형(명목/서열) 변수 극단치 처리
gender <- dataset$gender
gender

table(gender)
# 0   1   2   5 
# 2 173 124   1

pie(table(gender))

# 성별 정제 
dataset <- subset(dataset, gender==1 | gender == 2)
pie(table(dataset$gender))

#subset :입출력 Dataframe
#ifelse :입출력이 vector

# 2) 연속형(등간/비율) 변수 극단치 처리 
dataset$price



# 극단치 발견 
plot(dataset$price) # 정제 전 
summary(dataset$price)
boxplot(dataset$price) # 이상치 : 상하위 0.3%

boxplot(dataset$price)$stats
#      [,1]
# [1,]  2.1
# [2,]  4.4
# [3,]  5.4
# [4,]  6.3
# [5,]  7.9

# 구매금액 정제 : 극단치 제거 
dataset <- subset(dataset, price >= 2.1 & price <= 7.9)
plot(dataset$price) # 정제 후 
dim(dataset) #  248   9

# 구매금액 정제 : NA 대체 
install.packages('ggplot2')
library(ggplot2)

str(mpg) 

hwy <- mpg$hwy

boxplot(hwy)$stats

# 1) 극단치 제거 
mpg_sub <- subset(mpg, hwy >= 12 & hwy <= 37) 
dim(mpg_sub) # 231  11

# 2) 극단치 -> NA 대체 
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy )
dim(mpg) # 234  11

table(mpg$hwy, useNA = "ifany") # <NA> 3


# 4. 코딩 변경 : 변수변환: 리코딩하기
#데이터의 가독성,척도 변경 최초 코딩 내용 변경을 목적으로 수행


#특정 칼럼 값 조회: 조건식
dataset$gender[dataset$gender==1] #명목척도 일시 = 사용
dataset$price[dataset$price>=3] #비율 척도 시 대소 관계 보여 주는 식

# 1) 데이터의 가독성
#형식) dtat.fram$새컬럼명[조건식]<- 값

dataset2$resident2[dataset2$resident == 1] <-"1.서울특별시"
dataset2$resident2[dataset2$resident == 2] <-"2.인천광역시"
dataset2$resident2[dataset2$resident == 3] <-"3.대전광역시"
dataset2$resident2[dataset2$resident == 4] <-"4.대구광역시"
dataset2$resident2[dataset2$resident == 5] <-"5.시구군"

#dataset과 dataset2의 행이 길이가 다름으로 위의 방식 사용 불가능. 
head(dataset2)



#2) 척도 변경: 비유척도(상관,회귀)-> 명목척도(교차, 카이제곱)
dataset2$age2[dataset2$age<= 30] <-"청년층"
dataset2$age2[dataset2$age> 30 & dataset2$age< 55 ] <-"중년층"
dataset2$age2[dataset2$age>= 55] <-"장년층"

table(dataset2$age2)
# 장년층 중년층 청년층 
#   54     98     57 


#3) 역코딩: 긍정순서(5->1)
survey<-dataset2$survey

#브로드케스트 연산
csurvey <- 6 - survey #배터 = 상수(scala) - 백터(vector)
csurvey[1:5]

#벡터 값 수정
dataset2$survey <- csurvey
head(dataset2)


#5.정제된 데이터 저장
#(1) 정제된 데이터 저장
getwd()
write.csv(dataset2,"cleanData.csv", quote=F, row.names=F)
# (2) 정제된 데이터 불러오기

new_data<-read.csv("cleanData.csv", header=TRUE)
head(new_data)


# 6. 탐색적 분석을 위한 시각화 

# 데이터셋 불러오기
setwd("C:/ITWILL/2_Rwork/data")
new_data <- read.csv("new_data.csv", header=TRUE)
new_data 
dim(new_data) #  231  15
str(new_data)

# 1) 명목척도(범주/서열) vs 명목척도(범주/서열) 
# - 거주지역과 성별 칼럼 시각화 
#table(행,열) : 교차분할표 <-범주형 자료 이용

resident_gender <- table(new_data$resident2, new_data$gender2)
resident_gender
gender_resident <- table(new_data$gender2, new_data$resident2)
gender_resident

# - 성별에 따른 거주지역 분포 현황 
barplot(resident_gender, beside=T, horiz=T,
        col = rainbow(5),
        legend = row.names(resident_gender),
        main = '성별에 따른 거주지역 분포 현황') 
# row.names(resident_gender) # 행 이름 

# - 거주지역에 따른 성별 분포 현황 
barplot(gender_resident, beside=T, 
        col=rep(c(2, 4),5), horiz=T,
        legend=c("남자","여자"),
        main = '거주지역별 성별 분포 현황')  

# 2) 비율척도(연속) vs 명목척도(범주/서열)
# - 나이와 직업유형에 따른 시각화 
install.packages("lattice")  # chap08
library(lattice)

#densityplot(y ~ x, data=dataset, groups=집단변수,)
#연속변수와 집단 변수 이용행 그래프만들수 있다
# 직업유형에 따른 나이 분포 현황   
densityplot( ~ age, data=new_data, groups = job2, #job2 -> 개인 사업,공무원,화사원
             plot.points=T, auto.key = T)
#age: 연속 변수(x) , job2 :집단변수 (y)
# plot.points=T : 밀도, auto.key = T : 범례 


# 3) 비율(연속) vs 명목(범주/서열) vs 명목(범주/서열) *변수가 3개 이상
# - 구매비용(연속):x칼럼 , 성별(명목):조건, 직급(서열):그룹   

# (1) 성별에 따른 직급별 구매비용 분석  
densityplot(~ price | factor(gender2), data=new_data, 
            groups = position2, plot.points=T, auto.key = T) 
# 조건(격자) : 성별, 그룹 : 직급 

# (2) 직급에 따른 성별 구매비용 분석  
densityplot(~ price | factor(position2), data=new_data, 
            groups = gender2, plot.points=T, auto.key = T) 
# 조건 : 직급(격자), 그룹 : 성별 


# 7.파생변수 생성 
# - 기존 변수로 새로운 변수 생성
#유형
#1.사칙연산
#2. 1:1->기존변수(1개)-> 새로운 변수 (1)
#3. 1:N -> 기존변수(1개) -> 새로운 변수(N)

setwd('C:/ITWILL/2_Rwork/data')
user_data <- read.csv('user_data.csv', header = T)
head(user_data) # user_id age house_type resident job 

# 1) 1:1 파생변수 생성 : 기존 칼럼 1개 -> 새로운 칼럼 1개
# - 주택 유형 :  0, 아파트 유형 : 1(더미변수 생성) : 주택 유형 파악 가능  
summary(user_data$house_type) # NA확인 - 없음 
table(user_data$house_type)
# 1   2   3   4 
# 32  47  21 300 

# dummy 생성 
house_type2 <- ifelse(user_data$house_type == 1 | user_data$house_type == 2, 0, 1)

# 결과 확인
house_type2[1:10] 

# 파생변수 추가 
user_data$주거환경 <- house_type2
head(user_data)


# 2) 1:N 파생변수 생성 : 각 id(고객)에 대한 구매상품, 지불방법 나열 
pay_data <- read.csv('pay_data.csv', header = T)
head(pay_data,10) # user_id product_type pay_method  price
table(pay_data$product_type)

install.packages('reshape2')
library(reshape2) # dcast() 함수 제공 

# (1) 고객별 상품 유형에 따른 구매금액 합계 파생변수 생성   
product_price <- dcast(pay_data, user_id ~ product_type, sum, na.rm=T) 
                     #데이터명, 앞변수(행)~ 뒷변수(열), 함수(sum, etc), na.rm=T (<-결측치 제거))
head(product_price, 3) # 행(고객 id) 열(상품 타입), sum(price)

names(product_price) <- c('user_id','식료품(1)','생필품(2)','의류(3)','잡화(4)','기타(5)')
head(product_price, 3) # 칼럼명 수정 확인 

# (2) 파생변수 추가(data.frame 합치기) 
install.packages('plyr') #테이블과 테이르 join 함수
library(plyr) # 패키지 로딩 

user_pay_data <- join(user_data, product_price, by='user_id')
                    #(테이블1, 테이블2, by='어떤 칼럼명 기준으로') 
head(user_pay_data,10)

# (3) 총 구매금액 파생변수 생성(사칙연산 : 지급방법 이용) 
user_pay_data$총구매금액 <- user_pay_data$`식료품(1)` +user_pay_data$`생필품(2)`+user_pay_data$`의류(3)` +
  user_pay_data$`잡화(4)` + user_pay_data$`기타(5)`
head(user_pay_data)

#eg)
#vector 생성
a<-c(1,2,1,2)
b<-c(1:4)
c<-c(10,20,30,40)
d<-c(100,200,300,400)

#DF 생성
df<-data.frame(a,b,c,d)
df

#dcast(dataset,기준변수~ 대상 변수,통계 or function)
dcast(df,a~b,sum) #d칼럼 대상: 마지막 숫자변수
#Using d as value column: use value.var to override.

dcast(df[1:3],a~b,sum) #c 칼럼 대상 : 대상 변수 선택
#Using c as value column: use value.var to override.





















