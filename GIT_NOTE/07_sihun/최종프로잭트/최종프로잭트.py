# -*- coding: utf-8 -*-
"""
최종 프로젝트
1. 코스피주식 업종에 따라 군집분석 및 업종 선택
2. 업종 주식가격 데이터 크롤링
3. RNN
4. 시각화
5. 업종별 주식 선택
6. 포트폴리오 최적화

"""
import pandas as pd
import urllib.request as req # 원격 서버 url 자료 요청
import numpy as np

# 1. 코스피주식 업종에 따라 군집분석 및 업종 선택

path='C:\\ITWILL\\sihun'
Dataset= pd.read_excel(path+'\\Sectors.xlsx')
Dataset = Dataset.iloc[:,0:4]
Dataset2 = Dataset.loc[:,['종목코드','업종명']]

# sector 이름 출력
Sector_name =Dataset.iloc[:,-1]
Sector=Sector_name.drop_duplicates()

'''
0             서비스업
1             기타금융
3              유통업
5             섬유의복
10           운수창고업
11            음식료품
18              증권
19              보험
20            전기전자
25             건설업
29              화학
30            철강금속
47              기계
50             의약품
57           비금속광물
69            운수장비
71             통신업
72           기타제조업
115          전기가스업
152           종이목재
201             은행
216             광업
284           의료정밀
309    농업, 임업 및 어업
Name: 업종명, dtype: object
'''
Secotor=list(Sector)

data=[]
for a in Sector:
    a=Dataset2[Dataset.iloc[:,-1] == a]
    data.append(a)

#DataFrame 생성 <- 첨삭 요구
service_industry=data[0]
Other_finance=data[1]
Distribution=data[2]
Textile_garments=data[3]
Transportation_warehousing_business=data[4]
F_B=data[5]
securities=data[6]
insurance=data[7]
electrical =data[8]
construction=data[9]
chemistry=data[10]
steel_metal=data[11]
machine=data[12]
medicines=data[13]
Non_metallic_minerals=data[14]
transport_equipment=data[15]
telecommunications=data[16]
Other_manufacturing=data[17]
Electricity_Gas=data[18]
paper_wood=data[19]
bank=data[20]
Mining=data[21]
Medical_Precision=data[22]
Agriculture_Forestry_Fisheries=data[23]
  

# 저평가된 주식을 찾는다는 가정하에 주식의 P/E와  ROE를 기준으로 찾는다. 
# P/E는 12~15 이하인 주식 .
# ROE가 20% 이상인 주식 ...
#주당순이익이 꾸준히 증가 ...
#http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC020

df=pd.read_excel('C:\\ITWILL\\sihun\\df_P_E.xlsx')
df=df.iloc[:,0:7]
type(df)


#종목코드기준으로 P/E, 종가추출
service=service_industry.iloc[:,] # 서비스 업 주식 코드
type(service)

company=[]
for a in list(df.code):
    company.append(a)
len(company) #874

P_E=[]
cnt=0
cnt2=-1
for company1 in company:
    cnt2=+1
    try:
        if service[cnt] == company1: 
            P_E.extend(df.iloc[cnt2])
            cnt=+1
        else:
            print('error')
            print(cnt)
    except Exception as e:
        print('error')
            
P_E=pd.DataFrame(P_E)
P_E.to_excel(excel_writer='C:\\ITWILL\\sihun\\service')


# Sector 별로 저평가된 주식을 찾고 주식을 선택한다.

#####################################################################
## 선택한 주식의 가격정보를 가지고 온다.
##################################################################
# 20페이지 일별 주식 가격 가지고 오기'
import pandas as pd
import urllib.request as req
import requests
#1. 한국 거래소 종목 가져오기
stock_code=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download',header=0)[0]

#한글 컬럼명을 영어로 변경
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

#종목코드가 6자리이기 때문에 6자리르 맞춰주기 위해 설절해줌
stock_code.code=stock_code.code.map('{:06d}'.format)

#크롤링
company='LG화학' # [수정 필요] list형으로 변경해서 모든 선택된 주식의 정보를 가지고 온다.
code=stock_code[stock_code.company==company].code.values[0] # 한국 증권 거래소에서 가지고온 데이터

Date=[]
price=[]
for page in range(1,21):
    url=f'https://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'
    table= pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)
    temp=table[0]
    temp=temp.dropna() # temp 형식 DataFrame 
    date=temp.iloc[:,0]
    price_d=temp.iloc[:,1]
    price.extend(price_d) # append or extend
    Date.extend(date)




##################################################################################################
### RNN 으로 각주식의 수익 예측 후 수익성 좋은 주식을 로만 다시 주식 선택 <- tensorflow 사용
##################################################################################################

# data 가지고 오기
data = price 
len(data) # 100
print(data)

# 2. RNN 구제에 맞게 reshape 
#x_data
x = np.array([data[i+j] for i in range(len(data)-10) for j in range(10)])
# 90 * 10 =900
'''
0~9
1~10
2~11
3~12
  :
89~98      
'''
len(x) #900

# train/val split for x
x_train = x[:700].reshape(70,10,1)
x_test = x[700:].reshape(-1,10,1)

x_train.shape #(70,10,1) - (batch_size, time steps, features)
x_test.shape # (20, 10, 1) - (batch_size, time steps, features)

#y_data
y = np.array([data[i+10] for i in range(len(data)-10)]) # 0 ~ 89
'''
10
11
 :
99
'''
len(y) # 90

# train/val split for y (70 vs 20)  
y_train = y[:70].reshape(70,1)
y_test = y[70:].reshape(20,1)
y_train.shape # (70, 1)
y_test.shape #  (20, 1)

# 3. model 생성
input_shape = (10, 1)

model = Sequential()

#RNN layer 추가
model.add(SimpleRNN(units=8, input_shape=input_shape, activation='tanh'))

#hidden layer 추가가능 (복잡한 계산의 경우)

# DNN layer 추가
model.add(Dense(units=1)) # 출력 : 회귀모델 - MSE, MAE
#최종 출력은 예측된 숫자나 class 분류 결과이기 때문에 DNN을 이용합니다.

# model 학습환경
model.compile(optimizer='sgd', loss='mse', metrics=['mae']) # sgd, adam 비교해서 선택

# model training
model.fit(x_train,y_train, epochs=400, verbose=1)

# model prediction
y_pred = model.predict(x_test)
print(y_pred)

# real value vs predict value
plt.plot(y_test, 'y--', label='real value')
plt.plot(y_pred, 'r--',label='predict value')
plt.legend(loc='best')
plt.show()


#########################################################################################
### 포트폴리오 최적화(최소한의 리스크로 최대의 수익을 창출할수있는 포트폴리오 생성) <- use R
#########################################################################################




























