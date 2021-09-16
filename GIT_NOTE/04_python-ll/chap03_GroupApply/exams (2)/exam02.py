'''
문2) movie_rating.csv 파일을 대상으로 다음 출력 결과와 같이 테이블을 작성하시오.
   <단계1> 피벗 테이블 작성    
   <단계2> 각 영화별 평점의 평균 구하기          
   
 <<출력 결과>>
title    Just My  Lady  Snakes  Superman  The Night  You Me
critic                                                     
Claudia      3.0   NaN     3.5       4.0        4.5     2.5
Gene         1.5   3.0     3.5       5.0        3.0     3.5
Jack         NaN   3.0     4.0       5.0        3.0     3.5
Lisa         3.0   2.5     3.5       3.5        3.0     2.5
Mick         2.0   3.0     4.0       3.0        3.0     2.0
Toby         NaN   NaN     4.5       4.0        NaN     1.0 

영화별 평점의 평균 :
 title
Just My      2.375000
Lady         2.875000
Snakes       3.833333
Superman     4.083333
The Night    3.300000
You Me       2.500000
'''
import pandas as pd

import os
os.chdir('C:/ITWILL/4_python-ll/data')

rating = pd.read_csv('movie_rating.csv')
print(rating.info())

#<단계1> 피벗 테이블 작성 







#<단계2> 각 영화별 평점의 평균 구하기
























#<단계1> 피벗 테이블 작성 


ptable = pd.pivot_table(data=rating,
               values='rating',
               index=['critic'],
               columns='title')

ptable
'''
title    Just My  Lady  Snakes  Superman  The Night  You Me
critic                                                     
Claudia      3.0   NaN     3.5       4.0        4.5     2.5
Gene         1.5   3.0     3.5       5.0        3.0     3.5
Jack         NaN   3.0     4.0       5.0        3.0     3.5
Lisa         3.0   2.5     3.5       3.5        3.0     2.5
Mick         2.0   3.0     4.0       3.0        3.0     2.0
Toby         NaN   NaN     4.5       4.0        NaN     1.0
'''



#<단계2> 각 영화별 평점의 평균 구하기
ptable_mean=ptable.mean(axis=0)

#or
ptable1 = pd.pivot_table(data=rating,
               values='rating',
               index=['title'],
               aggfunc='mean')

print(ptable1)






