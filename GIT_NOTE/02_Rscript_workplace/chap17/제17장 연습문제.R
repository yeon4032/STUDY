####################################
## 제17장 RandomForest 연습문제 
####################################

# 01. 날씨 데이터셋을 이용하여 단계별로 RandomForest 모델을 생성하시오.
#  <단계1> 1,2,22,23 칼럼 제외
#  <단계2> y변수 : RainTomorrow -> 이항변수 변경
#  <단계3> 모델 생성 : Tree 400개, 분류변수 4개 이용
#  <단계4> Confusion matrix 이용 분류정확도 구하기 
#  <단계5> 분류정확도 개선에 기여하는 TOP3 변수 확인하기  

weatherAUS = read.csv(file.choose()) # weatherAUS.csv 

#  <단계1> 1,2,22,23 칼럼 제외
df = weatherAUS[ ,c(-1,-2, -22, -23)]
str(df)

#  <단계2> y변수 : RainTomorrow -> 이항변수 변경


#  <단계3> 모델 생성 : Tree 400개, 분류변수 4개 이용 


#  <단계4> Confusion matrix 이용 분류정확도 구하기


#  <단계5> 분류정확도 개선에 기여하는 TOP3 변수 확인하기  


# 02. 대출여부 데이터셋의 변수 목록을 보고 단계별로 RandomForest 모델을 생성하시오. 
#  <단계1> 1,5 칼럼 제외
#  <단계2> y변수 : Personal.Loan -> 이항변수 변경
#  <단계3> 모델 생성 : Tree 500개, 분류변수 3개 이용
#  <단계4> Confusion matrix 이용 분류정확도 구하기 
#  <단계5> 분류정확도 개선에 기여하는 TOP3 변수 확인하기


#  <대출여부 데이터셋 변수 목록>  
bank = read.csv('UniversalBank.csv',  stringsAsFactors = F)
str(bank) 
# <대출여부 변수 목록> 
#'data.frame':	5000 obs. of  14 variables:
#$ ID                :고객구분(제외)  int  1 2 3 4 5 6 7 8 9 10 ...
#$ Age               :나이  int  25 45 39 35 35 37 53 50 35 34 ...
#$ Experience        :경력  int  1 19 15 9 8 13 27 24 10 9 ...
#$ Income            :소득  int  49 34 11 100 45 29 72 22 81 180 ...
#$ ZIP.Code          :우편번호(제외)  int  91107 90089 94720 94112 91330 92121 91711 93943 90089 93023 ...
#$ Family            :가족수  int  4 3 1 1 4 4 2 1 3 1 ...
#$ CCAvg             :월 신용카드 사용액  num  1.6 1.5 1 2.7 1 0.4 1.5 0.3 0.6 8.9 ...
#$ Education         :교육수준  int  1 1 1 2 2 2 2 3 2 3 ...
#$ Mortgage          :담보채권  int  0 0 0 0 0 155 0 0 104 0 ...
#$ Personal.Loan     :개인대출(Y변수:수락 or 거절)  int  0 0 0 0 0 0 0 0 0 1 ...
#$ Securities.Account:유가증권계정  int  1 1 0 0 0 0 0 0 0 0 ...
#$ CD.Account        :CD계좌  int  0 0 0 0 0 0 0 0 0 0 ...
#$ Online            :온라인뱅킹  int  0 0 0 0 0 1 1 0 1 0 ...
#$ CreditCard        :신용카드  int  0 0 0 0 1 0 0 1 0 0 ...


# <단계1> 1,5 칼럼 제외


# <단계2> y변수 : Personal.Loan -> 이항변수 변경


# <단계3> 모델 생성 : Tree 500개, 분류변수 3개 이용 


# <단계4> Confusion matrix 이용 분류정확도 구하기


# <단계5> 분류정확도 개선에 기여하는 TOP3 변수 확인하기  

