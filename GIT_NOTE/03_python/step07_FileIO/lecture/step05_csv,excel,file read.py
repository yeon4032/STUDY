# -*- coding: utf-8 -*-
"""
csv,excel,file read
 - 칼럼 단위로 작성된 excel 파일 유형 읽기/쓰기
 - pandas 패키지 필요

anacanda prompt 에서 패키지 설피
> pip install pandas

"""

import pandas as pd # 별칭
######################################
### 1. csv file read
######################################

#1. 파일 읽기
path = 'C:/ITWILL/3_python/workplace/step07_FileIO/data/'
bmi = pd.read_csv(path+'bmi.csv')

print(bmi.info()) # str() 

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64 
 1   weight  20000 non-null  int64 
 2   label   20000 non-null  object
dtypes: int64(2), object(1)
memory usage: 468.9+ KB
None
'''

#2. 내용 확인
bmi.head() # 앞부분 5개 행 
bmi.tail() # 뒷부분 5개 행
'''
앞
   height  weight   label
0     184      61    thin
1     189      56    thin
2     183      79  normal
3     143      40  normal
4     187      66  normal

뒤
     height  weight   label
19995     168      74     fat
19996     190      62    thin
19997     179      77  normal
19998     148      57     fat
19999     167      71     fat
'''

# 3. 변수 선택: DF['컬럼명'] or DF.칼럼명
height=bmi['height'] # DF['컬럼명']
weight=bmi.weight #DF.칼럼명
label = bmi.label #DF.칼럼명

len(height)
height
#Name: height, Length: 20000, dtype: int64

h_mean=height.mean() # 평균 :164.9379
print('키 평균=',h_mean) #키 평균= 164.9379

w_mean=weight.mean()
print('몸무게 평균=',w_mean) #몸무게 평균= 62.40995

# 범주형 : 범주별 빈도수 
lab_cnt=label.value_counts()
print(lab_cnt)
'''
normal    7677
fat       7425
thin      4898
Name: label, dtype: int64
'''


##################################################
### 2. excel file read
##################################################
'''
- pandas 패키지 필요
- xlrd 패키지 필요
> pip install xlrd 
'''

ex = pd.ExcelFile(path+'sam_kospi.xlsx') # object 생성

kospi=ex.parse('sam_kospi') # 시트명 파싱

print(kospi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   Date    247 non-null    datetime64[ns] # 날짜형
 1   Open    247 non-null    int64          # 숫자형 
 2   High    247 non-null    int64         
 3   Low     247 non-null    int64         
 4   Close   247 non-null    int64         
 5   Volume  247 non-null    int64         
dtypes: datetime64[ns](1), int64(5)
memory usage: 11.7 KB
None
'''

#변수 선태
high = kospi.High
low = kospi.Low

print('high mean=', high.mean())
print('low mean= ', low.mean())


# 칼럼 추가 :파생 변수
kospi['Diff']= high-low
print(kospi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   Date    247 non-null    datetime64[ns]
 1   Open    247 non-null    int64         
 2   High    247 non-null    int64         
 3   Low     247 non-null    int64         
 4   Close   247 non-null    int64         
 5   Volume  247 non-null    int64         
 6   Diff    247 non-null    int64         
dtypes: datetime64[ns](1), int64(6)
memory usage: 13.6 KB
None
'''

kospi

'''
          Date     Open     High      Low    Close  Volume   Diff
0   2015-10-30  1345000  1390000  1341000  1372000  498776  49000
1   2015-10-29  1330000  1392000  1324000  1325000  622336  68000
2   2015-10-28  1294000  1308000  1291000  1308000  257374  17000
3   2015-10-27  1282000  1299000  1281000  1298000  131144  18000
4   2015-10-26  1298000  1298000  1272000  1292000  151996  26000
..         ...      ...      ...      ...      ...     ...    ...
242 2014-11-07  1218000  1218000  1195000  1206000  107688  23000
243 2014-11-06  1198000  1210000  1193000  1204000  168497  17000
244 2014-11-05  1215000  1225000  1194000  1202000  187182  31000
245 2014-11-04  1219000  1242000  1205000  1217000  237045  37000
246 2014-11-03  1250000  1252000  1216000  1235000  263940  36000
'''

#csv파일 정장
kospi.to_csv(path+'kospi_df.csv', index=None, encoding='utf-8') # index =None will remove 위의 첫번째 열 
kospi_df=pd.read_csv(path + 'kospi.to_csv', encoding='utf-8')
print(kospi_df)
















































