'''
문제1) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.  
 <조건1> 전자레인지 수량, 단가 수정 
 <조건2> HDTV 수량 수정 

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 5  400000 <- 수량, 단가 수정
4 HDTV 2 1500000  <- 수량 수정
전체 레코드 수 : 4


    [ 상품별 총금액 ]
냉장고 상품의 총금액은 1,700,000
세탁기 상품의 총금액은 1,650,000
전자레인지 상품의 총금액은 2,000,000
HDTV 상품의 총금액은 3,000,000
'''

import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    # db 연동 객체 생성
    conn = pymysql.connect(**config)
    # sql 문 실행 객체 생성
    cursor = conn.cursor()
    
    #3. Updat문:Update: code를 찾아 -> name,dan 수정한다 
    
    code = int(input('update code input:')) 
    su = int(input('su code input:')) 
    dan=int(input('update dan input:')) 
    
    sql=f"""update goods set su = '{su}', dan={dan} where 
            code = {code}"""
    cursor.execute(sql) # 레코드 수정
    conn.commit() #db반영
    
    
    #1. select문 :전체 레코드 조회
    sql="select *from goods"
    cursor.execute(sql) # 실제 sql문 실행
    # 레코드 조회 결과
    print('\n\t[ 상품별 총급액]')
    dataset=cursor.fetchall() # 레코드 가져오기    
    
    for row in dataset:
        #print(row) # tuple (1, '냉장고', 2, 850000)
        print(row[0],row[1],row[2],row[3]) # 1 냉장고 2 850000
        # 인덱스 없이는 tuple 로 나온고 인데스 있으면 tuple 이 벗겨짐.
    sql="select *from goods"
    cursor.execute(sql)
    dataset1=cursor.fetchall()  
    for row1 in dataset1:
        print('{0} 상품의 총금액은 {1:3,d}'.format(row1[1],row1[2]*row1[3]))

except Exception as e :
    print('db connection err:', e)
    conn.rollback() # 이전 상태 리턴
finally:
    cursor.close(); conn.close() # 객체 닫기 (역순)
