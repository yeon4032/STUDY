#################################
## <제3장 연습문제>
#################################   
#01. 본문에서 작성한 titanic 변수를 다음과 같은 단계를 통해서 “titanic.csv” 파일로 저장한 후 파일을 불러오시오.

#[단계 2] 'titanic.csv' 파일을 titanicData 변수로 가져와서 결과를 확인하고, titanicData의 관측치와 칼럼수를 확인한다.
#힌트: str() 함수 사용
setwd('C:/ITWILL/2_Rwork/output')
write.csv(titanic, 'titanic.csv')

#[단계 2] “titanic.csv” 파일을 titanicData 변수로 가져와서 결과를 확인하고, titanicData의 관측치와 칼럼수를 확인한다.
#힌트: str() 함수 사용
titanicData <- read.csv('titanic.csv')
str(titanicData)

#[단계 3] 1번, 3번 칼럼을 제외한 나머지 칼럼을 대상으로 상위 6개의 관측치를 확인한다. 
titanicData[1:6, -c(1,3)]


# 02. R에서 제공하는 quakes 데이터셋을 대상으로 다음과 같이 처리하시오

data("quakes")
quakes # 지진 진앙지 데이터 셋 
str(quakes)
# 'data.frame':	1000 obs. of  5 variables:

# 단계1) 현재 경로에 row.names, quote 없이 "quakes_df.csv" 파일명으로 저장 
write.csv(quakes, "quakes_df.csv", row.names = FALSE, quote = FALSE)

# 단계2) quakes_data로 파일 읽기 
quakes_data <- read.csv("quakes_df.csv")

# 단계3) mag 변수를 대상으로 평균 계산하기 
mag <- quakes_data$mag
mean(mag)

# 03. R에서 제공하는 CO2 데이터셋을 대상으로 다음과 같이 파일로 저장하시오.
# 힌트 : subset() 함수 이용 

data("CO2")
CO2
# 단계1) Treatment 칼럼 값이 'nonchilled'인 경우 'CO2_df1.csv' 파일로 저장 
df1 <- subset(CO2, Treatment=='nonchilled')
write.csv(df1, "CO2_df1.csv", row.names = F)

# 단계2) Treatment 칼럼 값이 'chilled'인 경우 'CO2_df2.csv' 파일로 저장 
df2 <- subset(CO2, Treatment=='chilled')
write.csv(df2, "CO2_df2.csv", row.names = F)


