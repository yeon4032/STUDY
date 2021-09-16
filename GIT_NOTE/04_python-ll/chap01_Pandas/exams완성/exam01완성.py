''' 
step02 관련문제 
문1) score.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> tv 칼럼이 0인 관측치 2개 삭제 (조건식 이용)
   조건2> score, academy 칼럼만 추출하여 DataFrame 생성
   조건3> score, academy 칼럼의 평균 계산 
   - <<출력 결과 >> 참고    
   
<<출력 결과 >>
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
score      76.500
academy     1.625   
'''

import pandas as pd
import os
os.chdir("c:/ITWILL/4_Python-II/data") # file 경로 변경 

score = pd.read_csv('score.csv')
print(score.info())
'''
RangeIndex: 10 entries, 0 to 9
Data columns (total 6 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   name     10 non-null     object
 1   score    10 non-null     int64 
 2   iq       10 non-null     int64 
 3   academy  10 non-null     int64 
 4   game     10 non-null     int64 
 5   tv       10 non-null     int64 
'''
print(score)


# 조건1> tv 칼럼이 0인 관측치 2개 삭제 (조건식 이용)
df = score[score.tv != 0]

print(df)

# 조건2> score, academy 칼럼만 추출하여 DataFrame 생성
df2 = df[['score', 'academy']]
df2 

# 조건3> score, academy 칼럼의 평균 계산
col_mean = df2.mean(axis = 0) # 열 단위 평균 
print(col_mean)
# score      76.500
# academy     1.625

