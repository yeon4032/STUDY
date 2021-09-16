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





























