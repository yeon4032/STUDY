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

Secotor=list(Sector)

data=[]
for a in Sector:
    a=Dataset2[Dataset.iloc[:,-1] == a]
    data.append(a)

#Sector 별로 DataFrame 생성
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
telecommunications=data[16]  ####
Other_manufacturing=data[17]
Electricity_Gas=data[18]     ####
paper_wood=data[19]          #####
bank=data[20]
Mining=data[21]
Medical_Precision=data[22]              ####
Agriculture_Forestry_Fisheries=data[23] ####


# 저평가된 주식을 찾는다는 가정하에 주식의 P/E기준으로 찾는다.  
# P/E는 12~15 이하인 주식 .

df=pd.read_excel('C:\\ITWILL\\sihun\\df_P_E.xlsx')
df=df.iloc[:,0:7]
type(df)
df.info()

#종목코드기준으로 P/E, 종가추출 

#telecommunications
telecommunications = telecommunications.iloc[:,] # 서비스 업 주식 코드
type(telecommunications)
len(telecommunications)
company=[]
for a in list(df.iloc[:,0]):
    company.append(a)
len(company) #874


tel_P_E=[]
cnt=0
for company1 in company:    
    try:
        for i in range(len(telecommunications)) :
            if telecommunications.iloc[i, 0] == company1:
                print('company1-2 :', company1)                
                
                tel_P_E.append(df.loc[cnt, ['종목코드','종목명','PER']]) # 이부분이 
        cnt+=1
            #else:
                #print('error')
    except Exception as e:
        print('error :', e)
    
tel_P_E=pd.DataFrame(tel_P_E)
# tel_P_E.to_excel(excel_writer='C:\\ITWILL\\sihun\\service.xlsx')


# Electricity_Gas
Electricity_Gas = Electricity_Gas.iloc[:,] # 서비스 업 주식 코드
type(Electricity_Gas)
len(Electricity_Gas)
company=[]
for a in list(df.iloc[:,0]):
    company.append(a)
len(company) #874

Electricity_Gas.iloc[0,0]

Ele_P_E=[]
cnt=0
for company1 in company:    
    try:
        for i in range(len(Electricity_Gas)) :
            if Electricity_Gas.iloc[i, 0] == company1:
                print('company1-2 :', company1)                
                
                Ele_P_E.append(df.loc[cnt, ['종목코드','종목명','PER']]) # 이부분이 
        cnt+=1
#            else:
#               print('error')
    except Exception as e:
        print('error :', e)
    
Ele_P_E=pd.DataFrame(Ele_P_E)
#Ele_P_E.to_excel(excel_writer='C:\\ITWILL\\sihun\\service')


# paper_wood
paper_wood = paper_wood.iloc[:,] # 서비스 업 주식 코드
type(paper_wood)
len(paper_wood)
company=[]
for a in list(df.iloc[:,0]):
    company.append(a)
len(company) #874

paper_wood.iloc[0,0]

pap_P_E=[]
cnt=0
for company1 in company:    
    try:
        for i in range(len(paper_wood)) :
            if paper_wood.iloc[i, 0] == company1:
                print('company1-2 :', company1)                
                
                pap_P_E.append(df.loc[cnt, ['종목코드','종목명','PER']]) # 이부분이 
        cnt+=1
            #else:
                #print('error')
    except Exception as e:
        print('error :', e)
    
pap_P_E=pd.DataFrame(pap_P_E)
#pap_P_E.to_excel(excel_writer='C:\\ITWILL\\sihun\\service')


# Medical_Precision
Medical_Precision = Medical_Precision.iloc[:,] # 서비스 업 주식 코드
type(Medical_Precision)
len(Medical_Precision)

company=[]
for a in list(df.iloc[:,0]):
    company.append(a)
len(company) #874

Medical_Precision.iloc[0,0]

Med_P_E=[]
cnt=0
for company1 in company:    
    try:
        for i in range(len(Medical_Precision)) :
            if Medical_Precision.iloc[i, 0] == company1:
                print('company1-2 :', company1)                
                
                Med_P_E.append(df.loc[cnt, ['종목코드','종목명','PER']]) # 이부분이 
        cnt+=1
            #else:
                #print('error')
    except Exception as e:
        print('error :', e)
    
Med_P_E=pd.DataFrame(Med_P_E)
#Med_P_E.to_excel(excel_writer='C:\\ITWILL\\sihun\\service')


# Agriculture_Forestry_Fisheries
Agriculture_Forestry_Fisheries = Agriculture_Forestry_Fisheries.iloc[:,] # 서비스 업 주식 코드
type(Agriculture_Forestry_Fisheries)
len(Agriculture_Forestry_Fisheries)
company=[]
for a in list(df.iloc[:,0]):
    company.append(a)
len(company) #874

Agriculture_Forestry_Fisheries.iloc[0,0]

Agr_P_E=[]
cnt=0
for company1 in company:    
    try:
        for i in range(len(Agriculture_Forestry_Fisheries)) :
            if Agriculture_Forestry_Fisheries.iloc[i, 0] == company1:
                print('company1-2 :', company1)                
                
                Agr_P_E.append(df.loc[cnt, ['종목코드','종목명','PER']]) # 이부분이 
        cnt+=1
            #else:
                #print('error')
    except Exception as e:
        print('error :', e)
    
Agr_P_E=pd.DataFrame(Agr_P_E)
#Agr_P_E.to_excel(excel_writer='C:\\ITWILL\\sihun\\service')


# DataFrame for 5sector
DataFrame_for_5sector=pd.concat([Agr_P_E,Med_P_E,pap_P_E,Ele_P_E,tel_P_E])
DataFrame_for_5sector=DataFrame_for_5sector.replace(['-'],16)
print(DataFrame_for_5sector)

DataFrame_for_5sector['PER_int']=pd.to_numeric(DataFrame_for_5sector['PER'])
DataFrame_P_E_H = DataFrame_for_5sector[DataFrame_for_5sector.iloc[:,3]>=12.5].index # 12.5 이상인 PER 제거 하기위해 index 값 찾기
DataFrame_for_5sector =DataFrame_for_5sector.drop(DataFrame_P_E_H) # PER 12.5 이상 삭제.
DataFrame_for_5sector
type(DataFrame_for_5sector)

##########################################################################################################################
#### PHL,PL,P 로 저평가 주식 한번더 거르기
#########################################################################################################################
import requests
from bs4 import BeautifulSoup

#회사코트 
company_code =DataFrame_for_5sector.iloc[0:,0]
comapny_code=company_code.reset_index()
len(company_code) #19

# 현제 주가 찾는 크롤러
def get_bs_obj(company_code):
    url='https://finance.naver.com/item/sise.nhn?code='+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today =bs_obj.find("p",{"class" : "no_today"}) # find 함수를 이용해서 class가 no_today 찾기
    blind_now = no_today.find("span", {"class" : "blind"}) # class rk no_today 에서 span 의 blind 에 있는 정보 가지고 오기
    return blind_now.text


# 52주 동아 Highest & lowest price찾는 크롤러
def get_bs_obj(company_code):
    url='https://finance.naver.com/item/sise.nhn?code='+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_hightest_lowest(company_code):
    bs_obj = get_bs_obj(company_code)
    
    # 52주최고 & 최저
    table=bs_obj.find("table",{"class":"rwidth"})
    trs = table.findAll("tr")    
    second_tr=trs[1]
    second_tr_ems = second_tr.findAll("em") # 52주최고
    print(second_tr_ems) #[<em>193,000</em>, <em>70,600</em>]
    Highest_52weeks = second_tr_ems[0].text
    lowest_52weeks = second_tr_ems[1].text
    return {"Hightest" : Highest_52weeks, "lowest": lowest_52weeks}


# Dataset 만들기
H_L_dataset=[]
for code in company_code:
    H_L_data = get_hightest_lowest(code)
    H_L_dataset.append(H_L_data)

H_L_dataset=pd.DataFrame(H_L_dataset).reset_index()
len(H_L_dataset) # 19

C_Price=[]
for code in company_code:
    price = get_price(code)
    C_Price.append(price)

C_Price = pd.DataFrame(C_Price).reset_index()
len(C_Price) # 19


# 최종 H_L dataset 생성
H_L_C_dataset = pd.concat([comapny_code,H_L_dataset,C_Price],axis=1)
H_L_C_dataset = H_L_C_dataset.drop(['index'],axis='columns')
H_L_C_dataset.rename(columns={0:'current_price'}, inplace=True)

# 시간 있으면 re.sub 사용해서 다시 전처리 도전해 -> re.sub('[,]', '', 칼럼명
H_L_C_dataset.to_csv("C:\\ITWILL\\sihun\\High_low")
H_L_C_dataset=pd.read_csv("C:\\ITWILL\\sihun\\High_low", thousands=',')
len(H_L_C_dataset)#19

####################
## 코딩 변경 필요
####################
# P < 1.5
P_C=[]
check=[]
for p in range(len(H_L_C_dataset)):
    P_C.append(H_L_C_dataset.iloc[p,-1]/H_L_C_dataset.iloc[p,-2])
    if (H_L_C_dataset.iloc[p,-1] / H_L_C_dataset.iloc[p,-2]) <= 1.5:
        print(H_L_C_dataset.iloc[p])
        check.append(H_L_C_dataset.iloc[p])
        
check=pd.DataFrame(check).reset_index()
len(check)#15

'''
PHL_006040 = float(H_L_C_dataset['current_price'][0])/float(H_L_C_dataset['lowest'][0]) 
PHL_030720 = float(H_L_C_dataset['current_price'][1])/float(H_L_C_dataset['lowest'][1]) 
PHL_004970 = float(H_L_C_dataset['current_price'][3])/float(H_L_C_dataset['lowest'][3]) 
PHL_029460 = float(H_L_C_dataset['current_price'][5])/float(H_L_C_dataset['lowest'][5]) 
PHL_213500 = float(H_L_C_dataset['current_price'][9])/float(H_L_C_dataset['lowest'][9]) 
PHL_009460 = float(H_L_C_dataset['current_price'][10])/float(H_L_C_dataset['lowest'][10]) 
PHL_267290 = float(H_L_C_dataset['current_price'][11])/float(H_L_C_dataset['lowest'][11])
PHL_117580 = float(H_L_C_dataset['current_price'][12])/float(H_L_C_dataset['lowest'][12])
PHL_034590 = float(H_L_C_dataset['current_price'][15])/float(H_L_C_dataset['lowest'][15])
PHL_071320 = float(H_L_C_dataset['current_price'][16])/float(H_L_C_dataset['lowest'][16])
PHL_032640 = float(H_L_C_dataset['current_price'][17])/float(H_L_C_dataset['lowest'][17])
PHL_017670 = float(H_L_C_dataset['current_price'][18])/float(H_L_C_dataset['lowest'][18])
'''
#PHL > 1.65
PHL=[]
PHL_Final=[]
for a in range(len(check)):
    PHL.append(check.iloc[a,-3]/check.iloc[a,-2])
    if (check.iloc[a,-3]/check.iloc[a,-2]) > 1.65:
        print(check.iloc[a])
        PHL_Final.append(check.iloc[a])
    
PHL_Final=pd.DataFrame(PHL_Final).reset_index()
len(PHL_Final)#3

'''
PHL_006040 = float(H_L_C_dataset['Hightest'][0])/float(H_L_C_dataset['lowest'][0]) 
PHL_004970 = float(H_L_C_dataset['Hightest'][3])/float(H_L_C_dataset['lowest'][3]) 
PHL_009460 = float(H_L_C_dataset['Hightest'][10])/float(H_L_C_dataset['lowest'][10]) 
'''

#최종 선택 주식 
#006040 ,004970 ,009460 

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
company=["동원산업","신라교역","한창제지"] 
code=[]
for a in company:
    code.append(stock_code[stock_code.company==a].code.values[0])

code #  ['006040', '004970', '009460']



Dong_Date=[]
Dong_price=[]
Sin_Date=[]
Sin_price=[]
Han_Date=[]
Han_price=[]
for code1 in code:    
    if code1 == '006040':
        for page in range(1,21):
            url=f'https://finance.naver.com/item/sise_day.nhn?code={code1}&page={page}'
            table= pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)
            temp=table[0]
            temp=temp.dropna() # temp 형식 DataFrame 
            date1=temp.iloc[:,0]
            price_d1=temp.iloc[:,1]
            Dong_price.extend(price_d1) # append or extend
            Dong_Date.extend(date1)
            
    elif code1=='004970':
        for page in range(1,21):
            url=f'https://finance.naver.com/item/sise_day.nhn?code={code1}&page={page}'
            table= pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)
            temp=table[0]
            temp=temp.dropna() # temp 형식 DataFrame 
            date2=temp.iloc[:,0]
            price_d2=temp.iloc[:,1]
            Sin_price.extend(price_d2) # append or extend
            Sin_Date.extend(date2)
    
    else:
        for page in range(1,21):
            url=f'https://finance.naver.com/item/sise_day.nhn?code={code1}&page={page}'
            table= pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)
            temp=table[0]
            temp=temp.dropna() # temp 형식 DataFrame 
            date3=temp.iloc[:,0]
            price_d3=temp.iloc[:,1]
            Han_price.extend(price_d3) # append or extend
            Han_Date.extend(date3)

#Create Price Dataset 

# Dong_Date & Dong_price
Dong_Date=pd.DataFrame(Dong_Date)
Dong_Date.rename(columns={0:'Date'}, inplace=True)

Dong_price=pd.DataFrame(Dong_price)
Dong_price.rename(columns={0:'Dong_price'}, inplace=True)

# Sin_Date & Sin_price
Sin_price=pd.DataFrame(Sin_price)
Sin_price.rename(columns={0:'Sin_price'}, inplace=True)
# Sin_Date=pd.DataFrame(Sin_Date)

# Han_Date & Han_price
Han_price=pd.DataFrame(Han_price)
Han_price.rename(columns={0:'Han_price'}, inplace=True)
#Han_Date=pd.DataFrame(Han_Date)

# create Dataset
price_Date_Dataset = pd.concat([Dong_Date,Dong_price,Sin_price,Han_price],axis=1)
price_Date_Dataset.to_excel("C:\\ITWILL\\sihun\\최종프로잭트\\price_Date_Dataset3.xlsx")
