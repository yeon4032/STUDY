# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:06:19 2021

@author: sihun
"""

#주식 데이터 가져 와서 차트 그리기

'''
step

1. 한국 거래소 종목 가져오기
2. 주식 데이터 가져오기
3. 차트 그리기
'''
# 금융 데이터 일별 시세를 크롤링 해보기

import pandas as pd
import urllib.request as req # 원격 서버 url 자료 요청
import numpy as np
#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

type(stock_code)
#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
stock_code.code=stock_code.code.map('{:06d}'.format)


# 2. 주식 데이터 가지고 오기
# 근 4년간 제무 정보 &저장 as lg_df2
company='LG화학'
code=stock_code[stock_code.company==company].code.values[0] # 한국 증권 거래소에서 가지고온 데이터
#"051910"
code=stock_code[stock_code.company==company].iloc[0,1]

url1=f'https://finance.naver.com/item/main.nhn?code={code}'
table1=pd.read_html(url1,encoding="cp949")

table1[3]
type(table1)#list
table3=pd.DataFrame(table1[3])
table3.to_excel(excel_writer='C:\\ITWILL\\sihun\\lg_df2.xlsx')


####################################################################################################
## 200 개 excel file 저장 -> data load
#####################################################################################################
#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
stock_code.code=stock_code.code.map('{:06d}'.format)

#자동으로 excel 저장.
path='C:\\ITWILL\\sihun'
kospi=pd.read_excel(path+'\\code.xlsx')
company1=list(kospi.iloc[1:,1])

cnt=-1
error=[]
excel=[]
for company in company1:
    print(company)
    try :
        cnt+=1
        code=stock_code[stock_code.company==company].code.values[0]
        url1=f'https://finance.naver.com/item/main.nhn?code={code}'
        table1=pd.read_html(url1,encoding="cp949")
        excel.append(table1[3])   
        
    
    except Exception as e:
        print('error company :', company,cnt)
        error.append(cnt)
        
print(error) # error 나오는 색인 from cmpany1 list.
#[6, 8, 11, 25, 26, 32, 33, 39, 49, 54, 64, 71, 88, 97, 118, 123, 146, 156, 170]
'''
# 200개의 회사를 200개의 excel 파일에 저장
for a in range(0,200):
    excel[a].to_excel(excel_writer=f'C:\\ITWILL\\sihun\\kopsi excel\\lg_df{a}.xlsx') 
'''  
# 200 개의 excel 파일이 만들어 진다. 이것은 나머지 작업을 함에 있어 효율적이지 못하다.

################################################################################
## 하나의 액셀에 여러 sheet 만들어서 각각의 sheet에  주식 정보 저장 -> Data load continue
##################################################################################
'''
# 오류 발생 왜냐하면 하나의 기업이 지워지면 색인이 당겨져서 다음 색인 삭제시 다른 기업 이사라짐.
company1=list(kospi.iloc[1:,1])
number=[6, 8, 11, 25, 26, 32, 33, 39, 49, 54, 64, 71, 88, 97, 118, 123, 146, 156, 170]
 
for num in number:
    company1.remove(company1[num])
'''

company1=list(kospi.iloc[1:,1])
number=[6, 8, 11, 25, 26, 32, 33, 39, 49, 54, 64, 71, 88, 97, 118, 123, 146, 156, 170]
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
add_list = [number[i] - a[i] for i in range(len(a))]

for num in add_list:
    company1.remove(company1[num])
company1=list(company1) #200-19


# import xlsxwriter
'''
# 10개의 회사 정보를 하나의 액셀 파일일에 저장
with pd.ExcelWriter('C:\\ITWILL\\sihun\\sheet\\Kospi_df.xlsx') as writer:
    for a in list(range(0,10)):
        company2=company1[a]
        print(company2)
        excel[a].to_excel(writer,sheet_name=f'{company2}')
'''

# 자동으로 181 개의 데이터를 10개의 액첼 파일에 저장
list(range(20))
c=0
d=10
for b in range(10):
    with pd.ExcelWriter(f'C:\\ITWILL\\sihun\\sheet\\Kospi_df{b}.xlsx') as writer:
        c+=10
        d+=10
        for a in list(range(c,d)):
            company2=company1[a]
            print(company2)
            excel[a].to_excel(writer,sheet_name=f'{company2}')
            
            
            
            
#############################################################################################3
##### y 변수 가지고 오기 
#################################################################################################            
lg_stockprice = [63200, 91700, 135000, 150000]            
            
            
            
            
            

 
############################################################################################3
### 2.필요 데이터 전처리 및 x 변수 생성 only for LG 전자
##################################################################################################33
from sklearn.model_selection import train_test_split # dataset split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import accuracy_score,classification_report

# 1. 매출액 증가율 찾기
df0 = pd.read_excel('C:\\ITWILL\\sihun\\sheet2\\Kospi_df0.xlsx')
sales = df0.iloc[3,6:-1] # 분기별
sales[0]

sales_growth_rate = [] 
for a in list(range(5)):
    try :
        diff=sales[a+1]-sales[a]
        growth=diff/sales[a]
        sales_growth_rate.append(growth)
    except Exception as e:
        print('error')


# 2.  ROE,P/E,P/B
ROE=  df0.iloc[8,7:11]
P_E = df0.iloc[13,7:11]
P_B = df0.iloc[15,7:11]

ROE=pd.to_numeric(ROE)
#P_E=pd.to_numeric(P_E)
P_B=pd.to_numeric(P_B)
sales_growth_rate= pd.DataFrame(sales_growth_rate)

# 데이터 프레임 생성
X=pd.DataFrame([1,2,3,4])
X['sales_growth_rate']=sales_growth_rate
X['ROE'] = ROE.reset_index(drop=True)
#X['P_E'] = P_E.reset_index(drop=True)
X['P_B'] = P_B.reset_index(drop=True)
X=X.iloc[:,1:]
y=lg_stockprice

# 정규화
X_nor = minmax_scale(X)
#y_nor = minmax_scale(y)

# train_test_split 
X_train,X_test,y_train,y_test= train_test_split(X_nor,y,test_size=0.75)

nb=GaussianNB()
#y_train = y_train.astype('int')
model=nb.fit(X_train,y_train)

y_pred=model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print(report)



























##################################################################################################33
## 다른 website에서 위의 워킹 다시하기
####################################################################################################
import pandas as pd
import urllib.request as req # 원격 서버 url 자료 요청
import numpy as np


#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
stock_code.code=stock_code.code.map('{:06d}'.format)

#자동으로 excel 저장.

path='C:\\ITWILL\\sihun'
kospi=pd.read_excel(path+'\\code.xlsx')
company1=list(kospi.iloc[1:,1])

cnt=-1
error=[]
excel2=[]
for company in company1:
    print(company)
    try :
        cnt+=1
        code=stock_code[stock_code.company==company].code.values[0]
        url1=f'https://search.itooza.com/search.htm?seName={code}'
        table1=pd.read_html(url1,encoding="cp949")
        excel2.append(table1[3])   
        
    
    except Exception as e:
        print('error company :', company,cnt)
        error.append(cnt)
#error#[6, 8, 11, 25, 26, 32, 33, 39, 49, 54, 64, 71, 88, 97, 118, 123, 146, 156, 170]
#error company : 현대차 6
#error company : 기아차 8
#error company : POSCO 11
#error company : KT&G 25
#error company : 한국전력 26
#error company : KT 32
#error company : 금호석유 39


################################################################################
## 하나의 액셀에 여러 sheet 만들어서 각각의 sheet에  주식 정보 저장 -> Data load continue
##################################################################################
company3=list(kospi.iloc[1:,1])
number2=[6, 8, 11, 25, 26, 32, 33, 39, 49, 54, 64, 71, 88, 97, 118, 123, 146, 156, 170]
a2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
add_list2 = [number2[i] - a2[i] for i in range(len(a2))]

for num in add_list2:
    company3.remove(company3[num])

company3=list(company3) #200-19

# import xlsxwriter
'''
# 10개의 회사 정보를 하나의 액셀 파일일에 저장
with pd.ExcelWriter('C:\\ITWILL\\sihun\\sheet\\Kospi_df.xlsx') as writer:
    for a in list(range(0,10)):
        company2=company1[a]
        print(company2)
        excel[a].to_excel(writer,sheet_name=f'{company2}')
'''

# 자동으로 181 개의 데이터를 10개의 액첼 파일에 저장
list(range(20))
c=0
d=10
for b in range(10):
    with pd.ExcelWriter(f'C:\\ITWILL\\sihun\\sheet2\\Kospi_df{b}.xlsx') as writer:
        c+=10
        d+=10
        for a in list(range(c,d)):
            company4=company3[a]
            print(company4)
            excel2[a].to_excel(writer,sheet_name=f'{company4}')

       
#######################################################################################33
## 변수인 분기별 std 찾기
#######################################################################################
import pandas as pd
import requests
import urllib.request as req # 원격 서버 url 자료 요청
import pandas as pd
import urllib.request as req # 원격 서버 url 자료 요청

#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
stock_code.code=stock_code.code.map('{:06d}'.format)

# sk이노베이션 std of price, 거래량 평균 찾기
company='SK이노베이션'
code=stock_code[stock_code.company==company].code.values[0] # 한국 증권 거래소에서 가지고온 데이터

price=[]
data=[]
vol=[]
for page in range(1,80):
    url=f'https://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'
    table= pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text) #headers에서 지정된 내용은 사용자가 접속한 브라우저(에이전트)를 감지하는 속성 입니다.
    temp=table[0]
    temp=temp.dropna() # temp 형식 DataFrame 
    price_d=temp.iloc[:,1]
    price.extend(price_d) # append or extend
    data_R=temp.iloc[:,0]
    data.extend(data_R)
    volumn=temp.iloc[:,-1]
    vol.extend(volumn)

print(price)
print(data)
print(vol)
data=pd.DataFrame(data)
price=pd.DataFrame(price)
vol=pd.DataFrame(vol)
'''
data['data']=data
data['day']=price
data['vol']=volumn
'''
#최종 DataFrame for vol and price 

# 분기별 가격 변동
Q1 = price.iloc[75:135]
Q2 = price.iloc[135:196]
Q3 = price.iloc[196:260]
Q4 = price.iloc[261:321]
Q5 = price.iloc[321:383]
Q6 = price.iloc[383:445]
Q7 = price.iloc[445:508]
Q8 = price.iloc[508:570]
Q9 = price.iloc[570:629]
Q10 = price.iloc[629:691]


# 표준편차
std1=np.array(Q1.std())
std2=np.array(Q2.std())
std3=np.array(Q3.std())
std4=np.array(Q4.std())
std5=np.array(Q5.std())
std6=np.array(Q6.std())
std7=np.array(Q7.std())
std8=np.array(Q8.std())
std9=np.array(Q9.std())
std10=np.array(Q10.std())

std=[std10,std9,std8,std7,std6,std5,std4,std3,std2,std1]
std=pd.DataFrame(std)


# 거래량
V_Q1 = vol.iloc[75:135]
V_Q2 = vol.iloc[135:196]
V_Q3 = vol.iloc[196:260]
V_Q4 = vol.iloc[261:321]
V_Q5 = vol.iloc[321:383]
V_Q6 = vol.iloc[383:445]
V_Q7 = vol.iloc[445:508]
V_Q8 = vol.iloc[508:570]
V_Q9 = vol.iloc[570:629]
V_Q10 = vol.iloc[629:691]

# 평균
V_Q1=np.array(V_Q1.mean())
V_Q2=np.array(V_Q2.mean())
V_Q3=np.array(V_Q3.mean())
V_Q4=np.array(V_Q4.mean())
V_Q5=np.array(V_Q5.mean())
V_Q6=np.array(V_Q6.mean())
V_Q7=np.array(V_Q7.mean())
V_Q8=np.array(V_Q8.mean())
V_Q9=np.array(V_Q9.mean())
V_Q10=np.array(V_Q10.mean())

V=[V_Q10,V_Q9,V_Q8,V_Q7,V_Q6,V_Q5,V_Q4,V_Q3,V_Q2,V_Q1]
V=pd.DataFrame(std)


############################################################################################3
### 2.필요 데이터 전처리 및 x & y  변수 생성 only for sk 이노베이션
##################################################################################################33
from sklearn.model_selection import train_test_split # dataset split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import matplotlib.pyplot as plt

# 1. 매출액 증가율 찾기
df0 = pd.read_excel('C:\\ITWILL\\sihun\\sheet2\\Kospi_df0.xlsx')
sales = df0.iloc[9,2:] # 분기별
sales

sales_growth_rate = []
year=[11,10,9,8,7,6,5,4,3,2,1,0]
for a in year:
    try :
        diff=sales[a]-sales[a+1]
        growth=diff/sales[a+1]
        print(growth)
        sales_growth_rate.append(growth)
    except Exception as e:
        print('error')
        
#log_data <- log(data)

# 2.  ROE,P/B,pp순이익률
ROE =  df0.iloc[7,2:]
P_B = df0.iloc[4,2:]
B_p=1/P_B
PP=df0.iloc[8,:]

# 좌우 전환
ROE = np.array(ROE) 
B_p = np.array(B_p)
PP=np.array(PP)
ROE = np.flip(ROE) # 좌우 반전
B_p = np.flip(B_p)
PP = np.flip(PP)

# DataFrame 으로 변환
ROE=pd.DataFrame(ROE)
ROE=ROE.iloc[1:11,:]
B_p = pd.DataFrame(B_p)
B_p =B_p.iloc[1:11,:] 
PP=pd.DataFrame(PP)
PP=PP.iloc[1:11,:]
sales_growth_rate= pd.DataFrame(sales_growth_rate)


# 데이터 프레임 생성
X=pd.DataFrame([0,1,2,3,4,5,6,7,8,9,10])
X['sales_growth_rate']=sales_growth_rate
X['ROE'] = ROE.reset_index(drop=True)
X['B_p'] =B_p.reset_index(drop=True)
X['std']=std
X['vol']=V
X['pp']=PP.reset_index(drop=True)
X=X.iloc[:9,1:]

# y (주가)
y=df0.iloc[10,2:]
y = np.flip(y)
y = y.iloc[1:11]

# dataframe + y
X['y']=y.reset_index(drop=True)
X
#설명력 확인
from statsmodels.formula.api import ols

obj = ols(formula='y~ sales_growth_rate + B_p + ROE + vol + std + pp',data=X.fillna(0.00001))
model= obj.fit()
model.summary()
'''
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.955
Model:                            OLS   Adj. R-squared:                  0.880

=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
Intercept          2.998e+05   2.92e+04     10.255      0.002    2.07e+05    3.93e+05
sales_growth_rate  2282.6798   1537.344      1.485      0.234   -2609.834    7175.193
B_p               -1.167e+05   1.94e+04     -5.999      0.009   -1.79e+05   -5.48e+04
ROE               -3988.5179   1549.323     -2.574      0.082   -8919.154     942.119
vol                  -0.3464      1.605     -0.216      0.843      -5.454       4.761
std                  -0.3464      1.605     -0.216      0.843      -5.454       4.761
pp                 9752.7155   4978.947      1.959      0.145   -6092.517    2.56e+04
==============================================================================
# vol 과 std 는 y 값에 영량을 유의미하게 미치지 않는다. 그럼으로 제외하고 다시 model 을 생성 한다.
'''

obj = ols(formula='y~ sales_growth_rate + B_p + ROE  + pp',data=X.fillna(0.00001))
model= obj.fit() # model 생성
model.summary()
'''
                           OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.954
Model:                            OLS   Adj. R-squared:                  0.909
Me
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
Intercept          2.984e+05   2.49e+04     11.970      0.000    2.29e+05    3.68e+05
sales_growth_rate  2319.3013   1333.482      1.739      0.157   -1383.039    6021.641
B_p               -1.171e+05   1.69e+04     -6.946      0.002   -1.64e+05   -7.03e+04
ROE               -4117.1896   1248.043     -3.299      0.030   -7582.312    -652.067
pp                 9994.4667   4233.888      2.361      0.078   -1760.690    2.17e+04
==============================================================================
# vol 과 std를 제외해 보니 model 의 정확도가 상승했다.
'''

# 이상치 확인
plt.boxplot(X['B_p'])
plt.boxplot(X['ROE'])
plt.boxplot(X['pp'])
plt.boxplot(X['sales_growth_rate'])


#이상치 제거
B_p=np.log((X['B_p']+1).astype('float'))
ROE=np.log((X['ROE']+1).astype('float'))
sales_growth_rate=np.log((X['sales_growth_rate']+1).astype('float'))
V=np.log((X['vol']+1).astype('float'))
PP=np.log((X['pp']+1).astype('float'))

X1=pd.DataFrame([1,2,3,4,5,6,7,8,9])
X1['sales_growth_rate']=sales_growth_rate
X1['ROE'] = ROE.reset_index(drop=True)
X1['B_p'] =B_p.reset_index(drop=True)
X1['pp']=PP.reset_index(drop=True)
X1=X1.iloc[:,1:]
#X1.fillna(0.0000001)

# 정규화
#X_nor = minmax_scale(X)
#y_nor = minmax_scale(y)

#Y
y=[0,1,0,0,1,1,1,0,0,1]
y=pd.DataFrame(y)


# train_test_split 
X_train,X_test,y_train,y_test= train_test_split(X1,y,test_size=0.3)

#model
nb=GaussianNB()
y_train = y_train.astype('int')

X_train=pd.DataFrame(X_train)
X_train.fillna(0.0000000000001)
X_train=np.array(X_train)
X_train= X_train.astype('int')


model=nb.fit(X_train,y_train)

#평가
X_test=pd.DataFrame(X_test)
X_test.fillna(0.0000000000001)
X_test=np.array(X_test)
X_test= X_test.astype('int')


y_pred=model.predict(X_test)
acc=accuracy_score(y_test,y_pred)

report=classification_report(y_test,y_pred)
print(report)
'''
Output from spyder call 'get_namespace_view':
              precision    recall  f1-score   support

           0       0.00      0.00      0.00         1
           1       0.67      1.00      0.80         2

    accuracy                           0.67         3
   macro avg       0.33      0.50      0.40         3
weighted avg       0.44      0.67      0.53         3
# 결과는 조금 싫망적이다. 너무 낮은 정확도를 보이고 있다. 
# 이러한 문제를 해결하기 위해 randomforest 모델을 이용해서 다시 측정해 보자.
'''


##############################################################################################
### Random Foresst
#################################################################################################
from sklearn.ensemble import RandomForestClassifier # model 
# model 생성
obj = RandomForestClassifier()
y=y[0]
model= obj.fit(X=X1.fillna(0.0000001),y=y[:-1])

#test set 생성
idx = np.random.choice(a=len(X1), size=100, replace=True)

X_test,y_test= X1[idx], y[idx]

# model 평가
y_pred= model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
#100%

# new data를 바탕으로 정확도 측정!!! 집에서


        
        
        