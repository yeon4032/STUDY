# -*- coding: utf-8 -*-
"""
step01_db_test.py

>pip install pymysql

-phython + db  연동 테스트
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
    #1. db 연동 객체 생성
    conn = pymysql.connect(**config)
    #2. sql 문 실행 객체 생성
    cursor = conn.cursor()
    print('~~db연동 성공~~') #~~ db 연동 성공 ~~
    #3. sql문 작성
    sql="select *from goods"
    cursor.execute(sql) # 실제 sql문 실행
    #4. 레코드 조회 결과
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



























