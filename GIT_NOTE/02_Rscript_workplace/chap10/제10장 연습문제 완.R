#################################
## <제10장 연습문제>
################################# 

# 01. 우리나라 전체 중학교 2학년 여학생 평균 키가 148.5cm로 알려져 있는 상태에서  
# A중학교 2학년 전체 500명을 대상으로 10%인 50명을 표본으로 선정하여 표본평균신장을 
# 계산하고 모집단의 평균과 차이가 있는지를 검정하시오.(단일표본 T검정)

H0:우리나라 여학생 평균 키는 148.cm 이다.

setwd('C:/ITWILL/2_Rwork/data')

# 단계1 : 데이터셋 가져오기
stheight<- read.csv("student_height.csv")
stheight
height <- stheight$height
head(height)

# 단계2 : 기술통계량/결측치 확인
length(height) #50
summary(height) # 149.4 

x1 <- na.omit(height)
x1 # 정제 데이터 
mean(x1) # 149.4 -> 평균신장

# 단계3 : 정규성 검정
shapiro.test(x1)
#W = 0.88711, p-value = 0.0001853 <0.05 ->정규분포 아님.
hist(x1)
#왼쪽으로 왜곡

# 단계4 : 가설검정 - 양측검정
wilcox.test(x1,mu=148.5)
#V = 826, p-value = 0.067
#p>알파 so cannot reject H0





# 02. 교육방법에 따라 시험성적에 차이가 있는지 검정하시오.(독립표본 T검정)
#조건1) 파일 : twomethod.csv
#조건2) 변수 : method : 교육방법, score : 시험성적
#조건3) 모델 : 교육방법(명목)  ->  시험성적(비율)
#조건4) 전처리 : 결측치 제거 : 평균으로 대체 

H0:교육방법에따라 성적의 차이가 없다. 

#단계1. 실습파일 가져오기
Data<- read.csv("twomethod.csv", header=TRUE)
head(Data) #3개 변수 확인 -> id method score

#단계2. 두 집단 subset 작성
unique(Data$method) #1,2
#변수 선택-> 서브셋 생성
data_df <- Data[c('method', 'score')]

#단계3. 데이터 분리
# 1) 집단(교육방법)으로 분리
method1 <- subset(data_df, method==1) #방법1
method2 <- subset(data_df, method==2) #방법2
dim(method1)
dim(method2)
# 2) 교육방법에서 시험성적 추출
score1<-method1$score
score2<-method2$score

#단계4 : 분포모양 검정
var.test(score1, score2) 
#F = 1.0648, num df = 21, denom df = 34, p-value = 0.8494

#단계5: 가설검정
t.test(score1, score2)
t.test(method1_score, method2_score, alter="two.sided", conf.int=TRUE, conf.level=0.95)
# t = -5.6056, df = 43.705, p-value = 1.303e-06
# p<0.05 so we reject H0
#z/t/f =-1.96 ~+1.96





# 03.datas를 대상으로 연령별(age) 만족도(satis)에 차이가 있는지 검정하시오.
# (일원배치 분산분석 : 모수 검정)    

H0:연령별 만족도 는 차이가 없다.

# 단계1 : dataset 생성 
#20대 만족도(10점 만족)
age20 <- rep(20, 10)
satis20 <- c(5,7,10,6,8,3,9,5,6,5)
df1 <- data.frame(age=age20, satis=satis20)

#30대 만족도
age30 <- rep(30, 10)
satis30 <- c(8,7,10,6,8,5,9,7,6,6)
df2 <- data.frame(age=age30, satis=satis30)

#40대 만족도
age40 <- rep(40, 10)
satis40 <- c(8,9,10,6,8,7,9,7,9,8)
df3 <- data.frame(age=age40, satis=satis40)

# DataFrame 생성 
datas <- rbind(df1, df2, df3)
datas # age satis
str(datas)

# 독립변수 요인형 변환 : 집단변수 생성(숫자변수 : 사후검정 시 오류) 
datas$age <- as.factor(datas$age)
str(datas) # $ age  : Factor w/ 3 levels
 

# 단계2 : 등분산성 검정 : 연령에 따른 만족도의 분산 차이  
# bartlett.test(종속변수 ~ 독립변수) # 독립변수(세 집단)
bartlett.test(satis ~ age,data=datas)
# Bartlett's K-squared = 2.7777, df = 2, p-value = 0.2494
#동질함

# 단계3 : 분산분석 
# 동질한 경우 : aov() - Analysis of Variance(분산분석) # aov(종속변수 ~ 독립변수, data=data set)
# 동질하지 않은 경우 - kruskal.test()
outcome<-aov(satis ~ age,data=datas)

# 단계4. 분석분석 결과 해석 
summary(outcome) 
            Df Sum Sq  Mean Sq  Fvalue  Pr(>F)  
age          2  14.47   7.233   2.607   0.0922 .
Residuals   27  74.90   2.774   

#p-value>0.05 so H0 is not rejected. 

# 단계5. 사후검정 : 각 집단간 차이검정 
TukeyHSD(outcome)
#       diff        lwr      upr     p adj
# 30-20  0.8 -1.0468164 2.646816 0.5379671 <-차이가 없다
# 40-20  1.7 -0.1468164 3.546816 0.0756158 <- 차이가 없다
# 40-30  0.9 -0.9468164 2.746816 0.4586358<- 차이가 없다






# 04.airquality를 대상으로 월별(Month)로 오존량(Ozone)에 차이가 있는지 검정하시오.
# (일원배치 분산분석 : 비모수 검정)  

airquality
str(airquality)
# $ Ozone -> y : 연속형 변수 
# $ Month -> x : 집단변수 
table(airquality$Month) # 5  6  7  8  9
table(airquality$Ozone)
# 단계 1: 전처리(결측치 제거)
summary(airquality) # 결측치 발견 
dataset <- na.omit(airquality) # 결측치 제거 


# 단계 2: 동질성 검정 
bartlett.test(Ozone ~ Month,data=dataset)
#Bartlett's K-squared = 13.969, df = 4, p-value = 0.007395

# 단계 3: 분산분석(모수 vs 비모수) & 해석 
outcome2<-kruskal.test(Ozone ~ Month,data=dataset)
#Kruskal-Wallis chi-squared = 26.309, df = 4, p-value = 2.742e-05 -> 집단 차이가 있다. 

# 단계 4: 사후검정 : 집단별 평균(dplyr 패키지 이용) 
library(dplyr)
dataset %>% group_by(Month) %>% summarize(avg = mean(Ozone))

#    Month    avg
#    <int>    <dbl>
# 1     5     24.1
# 2     6     29.4
# 3     7     59.1
# 4     8     60  
# 5     9     31.4
