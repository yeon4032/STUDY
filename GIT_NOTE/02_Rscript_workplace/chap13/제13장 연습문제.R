#################################
## <제13장 연습문제>
################################# 

# 01.  admit 객체를 대상으로 다음과 같이 로지스틱 회귀분석을 수행하시오.
# <조건1> 변수 모델링 : y변수 : admit, x변수 : gre, gpa, rank 
# <조건2> 7:3비율로 데이터셋을 구성하여 모델과 예측치 생성 
# <조건3> 분류 정확도 구하기 

# 파일 불러오기
setwd("c:/itwill/2_Rwork/data")
admit <- read.csv("admit.csv")
str(admit) 

# 1. train/test data 구성 

# 2. model 생성 


# 3. predict 생성 


# 4. 모델 평가(분류정확도) : 혼돈 matrix 이용/ROC Curve 이용
# 1) 혼돈 matrix 이용


# 2) ROCR 패키지 제공 함수 : prediction() -> performance

library(ROCR)
# ROCR 패키지 제공 함수 : prediction() -> performance































