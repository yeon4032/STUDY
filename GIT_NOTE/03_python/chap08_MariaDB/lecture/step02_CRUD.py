# -*- coding: utf-8 -*-
"""
step02_CRUD.py

크루드(CRUD)
- Create(insert),Read(select),Update, Delete

"""

import pymysql # driver = python 과 db  연결해주는 중간자 역학

print(pymysql.version_info) #(1, 4, 0, 'final', 0) 1.4버전 사용중


#db 연동 환경변수
config = {
    'host' : '127.0.0.1', #나의 시스템 서버 사용
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}


try:
    # db 연동 객체 생성
    conn = pymysql.connect(**config)
    # sql 문 실행 객체 생성
    cursor = conn.cursor()
    
    #2. insert문: Create
    #키보드 입력 
    '''
    code = int(input('code input:'))
    name = input('name input:')
    su= int(input('su input:'))
    dan=int(input('dan input:'))
    
    sql= f"insert into goods values({code},'{name}',{su},{dan})"
    cursor.execute(sql) # 레코드 추가
    conn.commit() #db 반영 

    #키보드 입력 아님
    sql="insert into goods values(5,'가스레인지',3,400000)"
    cursor.execute(sql) # 레코드 추가
    conn.commit() #db 반영
    '''
    
    #3. Updat문:Update: code를 찾아 -> name,dan 수정한다 
    
    '''
    code = int(input('update code input:')) # 5
    name = input('update name input:') # 가스레인지
    dan=int(input('update dan input:')) # 450000
    
    sql=f"""update goods set name = '{name}', dan={dan} where 
            code = {code}"""
    cursor.execute(sql) # 레코드 수정
    conn.commit() #db반영
    '''
    #4.Delete문 : Delete : code -> 존재 -> 레코드 삭제
    '''
    code = int(input('delete code input:'))
    
    #code : primary key so 중복불가
    sql=f"select *from goods where code= {code}"
    cursor.execute(sql)
    row=cursor.fetchone() # 하나의 레코드 가지고 오기 & cursor.fecthall은 전체 레코드 가져오기
    
    if row : #레코드 있는 경우
        sql=f"delete from goods where code= {code}"
        cursor.execute(sql) # 실제 레코드 삭제
        conn.commit() # db 반영
    else: # 검색된 레코드 없다
        print('해당 code 없음')
    '''
    #1. select문 :전체 레코드 조회
    sql="select *from goods"
    cursor.execute(sql) # 실제 sql문 실행
    # 레코드 조회 결과
    dataset=cursor.fetchall() # 레코드 가져오기    
    for row in dataset:
        #print(row) # tuple (1, '냉장고', 2, 850000)
        print(row[0],row[1],row[2],row[3]) # 1 냉장고 2 850000
        # 인덱스 없이는 tuple 로 나온고 인데스 있으면 tuple 이 벗겨짐.
        
    print('전체 레코드 수:', len(dataset)) #전체 레코드 수: 4
        
except Exception as e:
    print('db connection err:', e)
finally:
    cursor.close(); conn.close() # 객체 닫기 (역순)



