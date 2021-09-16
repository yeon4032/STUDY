'''
문2) winequality-both.csv 데이터셋을 이용하여 다음과 같이 처리하시오.
   <조건1> quality, type 칼럼으로 교차분할표 작성 
   <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬       
   <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균차이 검정
           -> 각 집단 평균 통계량 출력
   <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
'''


import pandas as pd
import os 
from scipy import stats


os.chdir('c:/itwill/4_python-ii/data')
wine = pd.read_csv('winequality-both.csv')
print(wine.info())

# <조건1> quality, type 칼럼으로 교차분할표 작성 
wine_tab = pd.crosstab(index=wine['quality'], 
                       columns=wine['type'])

print(wine_tab)
'''
type     red  white
quality            
3         10     20
4         53    163
5        681   1457
6        638   2198
7        199    880
8         18    175
9          0      5
'''

# <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬
wine_tab_sort = wine_tab.sort_values('white', ascending=False)
print(wine_tab_sort)
'''
type     red  white
quality            
6        638   2198
5        681   1457
7        199    880
8         18    175
4         53    163
3         10     20
9          0      5
'''


# <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정


# <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력





































import pandas as pd
import os 
from scipy import stats


os.chdir('C:/ITWILL/4_python-ll/data')
wine = pd.read_csv('winequality-both.csv')
print(wine.info())

# <조건1> quality, type 칼럼으로 교차분할표 작성 
wine_tab = pd.crosstab(index=wine['quality'], 
                       columns=wine['type'])

print(wine_tab)
'''
type     red  white
quality            
3         10     20
4         53    163
5        681   1457
6        638   2198
7        199    880
8         18    175
9          0      5
'''

# <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬
wine_tab_sort = wine_tab.sort_values('white', ascending=False)
print(wine_tab_sort)
'''
type     red  white
quality            
6        638   2198
5        681   1457
7        199    880
8         18    175
4         53    163
3         10     20
9          0      5
'''


# <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
red=wine.loc[wine['type']=='red','quality']
white=wine.loc[wine['type']=='white','quality'] 

two_sample2 = stats.ttest_ind(red, white)
print(two_sample2)
print('t검정 통계량 = %.16f, pvalue = %.16f'%(two_sample2))
#t검정 통계량 = -9.6856495541876964, pvalue = 0.0000000000000000
#[해설]red와인과 white 와인의 quality 차이가 있다.

# <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력
corr = wine.corr(method='pearson')
corr['alcohol']
'''
fixed acidity          -0.095452
volatile acidity       -0.037640
citric acid            -0.010493
residual sugar         -0.359415
chlorides              -0.256916
free sulfur dioxide    -0.179838
total sulfur dioxide   -0.265740
density                -0.686745
pH                      0.121248
sulphates              -0.003029
alcohol                 1.000000
quality                 0.444319
'''













