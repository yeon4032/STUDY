
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