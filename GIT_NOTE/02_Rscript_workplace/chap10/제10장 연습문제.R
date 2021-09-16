#################################
## <제10장 연습문제>
################################# 

# 01. 우리나라 전체 중학교 2학년 여학생 평균 키가 148.5cm로 알려져 있는 상태에서  
# A중학교 2학년 전체 500명을 대상으로 10%인 50명을 표본으로 선정하여 표본평균신장을 
# 계산하고 모집단의 평균과 차이가 있는지를 검정하시오.(단일표본 T검정)

setwd('C:/ITWILL/2_Rwork/data')

# 단계1 : 데이터셋 가져오기
stheight<- read.csv("student_height.csv")
stheight
height <- stheight$height
head(height)

# 단계2 : 기술통계량/결측치 확인



# 단계3 : 정규성 검정


# 단계4 : 가설검정 - 양측검정




# 02. 교육방법에 따라 시험성적에 차이가 있는지 검정하시오.(독립표본 T검정)
#조건1) 파일 : twomethod.csv
#조건2) 변수 : method : 교육방법, score : 시험성적
#조건3) 모델 : 교육방법(명목)  ->  시험성적(비율)
#조건4) 전처리 : 결측치 제거 : 평균으로 대체 

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


#단계5: 가설검정



# 03.datas를 대상으로 연령별(age) 만족도(satis)에 차이가 있는지 검정하시오.
# (일원배치 분산분석 : 모수 검정)    

# 단계1 : dataset 생성 
#20대 만족도(10점 만족)


#30대 만족도

#40대 만족도


# DataFrame 생성 


# 독립변수 요인형 변환 : 집단변수 생성(숫자변수 : 사후검정 시 오류) 



# 단계2 : 등분산성 검정 : 연령에 따른 만족도의 분산 차이  


# 단계3 : 분산분석 


# 단계4. 분석분석 결과 해석 
    

# 단계5. 사후검정 : 각 집단간 차이검정 


# 04.airquality를 대상으로 월별(Month)로 오존량(Ozone)에 차이가 있는지 검정하시오.
# (일원배치 분산분석 : 비모수 검정)  
airquality
str(airquality)
# $ Ozone -> y : 연속형 변수 
# $ Month -> x : 집단변수 


# 단계 1: 전처리(결측치 제거)


# 단계 2: 동질성 검정 


# 단계 3: 분산분석(모수 vs 비모수) & 해석 


# 단계 4: 사후검정 : 집단별 평균(dplyr 패키지 이용) 
library(dplyr)

