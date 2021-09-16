# -*- coding: utf-8 -*-
"""
Foresting data 만들기
"""
import pandas as pd # CSV file read

# dataset (분기별 데이터 사용)
code_A = ['006040', '004970', '009460']


excel2=[]
for code in code_A:
    try :
        url1=f'https://search.itooza.com/search.htm?seName={code}'
        table1=pd.read_html(url1,encoding="cp949")
        excel2.append(table1[2])   
        
    
    except Exception as e:
        print('error company :', code)



# 12 년치 재무정보
D=pd.DataFrame(excel2[0])
S=pd.DataFrame(excel2[1])
H=pd.DataFrame(excel2[2])

#D
D_EBIT= D.iloc[9,:]
D_Div = D.iloc[5,:]
D_P_B = D.iloc[4,:]
D_price = D.iloc[10,:]

#S
S_EBIT= S.iloc[9,:]
S_Div = S.iloc[5,:]
S_P_B = S.iloc[4,:]
S_price = S.iloc[10,:]

#H
H_EBIT= H.iloc[9,:]
H_Div = H.iloc[5,:]
H_P_B = H.iloc[4,:]
H_price = H.iloc[10,:]

#Dataset for Forcasting
Dataset_Forcasting =pd.concat([D_EBIT, D_Div, D_P_B, D_price,
                               S_EBIT, S_Div, S_P_B, S_price,
                               H_EBIT, H_Div, H_P_B, H_price],axis=1)

Dataset_Forcasting.columns = ["D_EBIT", "D_Div", "D_P_B","D_price",
                              "S_EBIT", "S_Div", "S_P_B","S_price",
                              "H_EBIT", "H_Div", "H_P_B","H_price"]

Dataset_Forcasting = Dataset_Forcasting.iloc[1:,:]
Dataset_Forcasting

Dataset_Forcasting.to_excel("C:\\ITWILL\\2_Rwork\\_Sihun project\\Forcasting_stock_price.xlsx")

