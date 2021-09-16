'''  
문4) tips.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 파일 정보 보기 
   조건2> header를 포함한 앞부분 5개 관측치 보기 
   조건3> header를 포함한 뒷부분 5개 관측치 보기 
   조건4> 숫자 칼럼 대상 요약통계량 보기 
   조건5> 흡연자(smoker) 유무 빈도수 계산  
   조건6> 요일(day) 칼럼의 유일한 값 출력 
'''

import pandas as pd
import os
os.chdir("C:/ITWILL/4_python-ll/data") # file 경로 변경 

tips = pd.read_csv('tips.csv')



#조건1> 파일 정보 보기 


#조건2> header를 포함한 앞부분 5개 관측치 보기 


#조건3> header를 포함한 뒷부분 5개 관측치 보기 


#조건4> 숫자 칼럼 대상 요약통계량 보기 

#조건5> 흡연자(smoker) 유무 빈도수 계산  


#조건6> 요일(day) 칼럼의 유일한 값 출력 






























#조건1> 파일 정보 보기 
tips.info()

#조건2> header를 포함한 앞부분 5개 관측치 보기 
tips.head()

#조건3> header를 포함한 뒷부분 5개 관측치 보기 
tips.tail()

#조건4> 숫자 칼럼 대상 요약통계량 보기 
tips.describe()

#조건5> 흡연자(smoker) 유무 빈도수 계산  
tips.value_counts()

#조건6> 요일(day) 칼럼의 유일한 값 출력 
tips['day'].unique()



























