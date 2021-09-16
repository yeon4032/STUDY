# -*- coding: utf-8 -*-
##################################################################################################33
## 다른 아이투자에서 크롤링해서 재무정보 여러 액셀에 여러sheet로 저장.
####################################################################################################
import pandas as pd
import urllib.request as req # 원격 서버 url 자료 요청
import numpy as np
#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
#url_new=https://search.itooza.com/search.htm?seName={company}

stock_code.code=stock_code.code.map('{:06d}'.format)

company='LG화학'
code=stock_code[stock_code.company==company].code.values[0] # 한국 증권 거래소에서 가지고온 데이터
#"051910"
code=stock_code[stock_code.company==company].iloc[0,1]

url1=f'https://search.itooza.com/search.htm?seName={code}'
table1=pd.read_html(url1,encoding="cp949")

table1[4] # 연간
table1[4] # 분기
###############################################################################

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
volumn=pd.DataFrame(vol)
data['data']=data
data['day']=price
data['vol']=volumn

#최종 DataFrame for vol and price 
data

# 분기별 가격 변동
Q1 = data.iloc[75:135,1:]
Q2 = data.iloc[135:196,1:]
Q3 = data.iloc[196:260,1:]
Q4 = data.iloc[261:321,1:]
Q5 = data.iloc[321:383,1:]
Q6 = data.iloc[383:445,1:]
Q7 = data.iloc[445:508,1:]
Q8 = data.iloc[508:570,1:]
Q9 = data.iloc[570:629,1:]
Q10 = data.iloc[629:691,1:]


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
vol1=data.iloc[:,2]
V_Q1 = vol1.iloc[75:135]
V_Q2 = vol1.iloc[135:196]
V_Q3 = vol1.iloc[196:260]
V_Q4 = vol1.iloc[261:321]
V_Q5 = vol1.iloc[321:383]
V_Q6 = vol1.iloc[383:445]
V_Q7 = vol1.iloc[445:508]
V_Q8 = vol1.iloc[508:570]
V_Q9 = vol1.iloc[570:629]
V_Q10 = vol1.iloc[629:691]

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
### 2.필요 데이터 전처리 및 x & y  변수 생성 only for LG 전자
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
# 2.  ROE,P/B,순이익률
ROE =  df0.iloc[7,2:]
#P_E = df0.iloc[2,2:]
P_B = df0.iloc[4,2:]
B_p=1/P_B
PP=df0.iloc[8,:]



ROE = np.array(ROE) 
B_p = np.array(B_p)
PP=np.array(PP)

ROE = np.flip(ROE) # 좌우 반전
B_p = np.flip(B_p)
PP = np.flip(PP)

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
X=X.iloc[:10,1:]

# 이상치 확인
plt.boxplot(X['B_p'])
plt.boxplot(X['ROE'])
plt.boxplot(X['vol'])
plt.boxplot(X['pp'])
plt.boxplot(X['sales_growth_rate'])

plt.boxplot(X['std']) # no need

#이상치 제거
B_p=np.log((X['B_p']+1).astype('float'))
ROE=np.log((X['ROE']+1).astype('float'))
sales_growth_rate=np.log((X['sales_growth_rate']+1).astype('float'))
V=np.log((X['vol']+1).astype('float'))
PP=np.log((X['pp']+1).astype('float'))

X['sales_growth_rate']=sales_growth_rate
X['ROE'] = ROE.reset_index(drop=True)
X['B_p'] =B_p.reset_index(drop=True)
X['std']=std
X['vol']=V
X['pp']=PP.reset_index(drop=True)
X.fillna(0)

#Y
y=[0,1,0,0,1,1,1,0,0,1]
y=pd.DataFrame(y)

# 정규화
X_nor = minmax_scale(X)
#y_nor = minmax_scale(y)

# train_test_split 
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3)

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


