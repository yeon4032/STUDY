
####################################################################################################
## 네이버 금융에서 코스피 200의 주요제무정보를 여러 엑셀에 sheet 를 만들어 저장 
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