# -*- coding: utf-8 -*-
"""
step01_statistics.py

statistics 모듈의 주요 함수
    - 기술통계: 대푯값,산포도, 왜도/첨도 
"""
import statistics as st # 기술통계
import pandas as pd # csv file
import os # file path

os.chdir('C:/ITWILL/4_python-ll/data')

dataset=pd.read_csv('descriptive.csv')
dataset.info()


x=dataset['cost'] # 구매비율
print(x)

#1.대푯값
#x.mean() -> 5.351000000000002
st.mean(x) # 평균:5.351
st.median(x) #중위수:5.4
st.median_low(x)  #낮은 중위수:5.4
st.median_high(x) #높은 중위수:5.4
st.mode(x) #  최빈수:6.0 

# x변량의 빈도수
x.value_counts()

# 2. 산포도: 분산,표준편차,사분위수
st.variance(x) # 표본의 분산

st.stdev(x) #표본의 표준편차

'''
표준편차 = 분산의 제곱근
분산 = 표준편차의 제곱
'''
st.sqrt(st.variance(x)) # 표준편차
st.math.pow(st.stdev(x),2) # 분산

# 사분위수
st.quantiles(x) #[25%: 1사분의수,50%: 2사분위수,75%: 3사분위수]
# [4.425000000000001, 5.4, 6.2]
st.median(x) # 중위수 = 제2사분위수

#3. 왜도/첨도
import scipy.stats as sts

#1) 왜도 (기울어 짐의 정도) : 0기준
'''
왜도=0 : 정규분포
왜도>0 : 왼쪽 치우침
왜도<0 : 오른쪽 치우침
'''

sts.skew(x)
#-0.1531779106237012  <- 오른쪽 치우침

# 2) 첨도: 0기준 or 3기준
sts.kurtosis(x,fisher=True) #첨도를 영을 기준으로 비교
#-0.1830774864331568
sts.kurtosis(x,fisher=False) #첨도를 삼을 기준으로 비교
#2.816922513566843
'''
첨도=0(3) : 정규분표
첨도>0(3) : 정규분포에 비해 위로 뾰족함
첨도<0(3) : 정규분포에 비해 완만함 아래임
'''

#히스토그램(hist) + 밀도분포곡선(kde)
import seaborn as sn 
#sn.distplot(x,hist=True,kde=True)
#warnings<-사용가능하나 곧 없어질거임

sn.displot(x,kind='hist', kde=True)




































