# -*- coding: utf-8 -*-
"""
step01_2_sqlite.py

SQLite3
  -내장 DBMS: 기기(휴대폰) 내부에서 사용
  -외부 접근 허용 안됨
"""

import sqlite3 #패키지 가져오기

print(sqlite3.sqlite_version_info) #(3, 35, 4)

 # DB 생성경로
path ='C:/ITWILL/3_python/workplace/chap08_MariaDB/data/'  

try:
    #1. db 연동 객체 생성
    conn = sqlite3.connect(path+'sqlite_db') # 파일형식으로 db 생성된다.
    #2.sql문 실행 객체 생성
    cursor=conn.cursor()
    
    #3. table 생성 : auto commit
    # test_tab 라는 테이블이 없으면 만들어라
    sql="""create table if not exists test_tab(
           name text(10), age numeric(3),addr text(50)) """ 
    cursor.execute(sql) # table 생성
    print('table 생성 완료')
    
    #4. 레코드 추가
    cursor.execute("insert into test_tab values('홍길동',35,'한양')")
    cursor.execute("insert into test_tab values('이순신',45,'해남')")
    cursor.execute("insert into test_tab values('강김친',55,'평양')")
    conn.commit() #db 반영
    
    #5. 레코드 조회
    cursor.execute("select *from test_tab")
    rows=cursor.fetchall()
    
    for row in rows:
        print(row)
    
    #6.table 제거: auto commit
    cursor.execute("drop table test_tab") # table 삭제
    print('***table 삭제***')
    
except Exception as e:
    print('db error:',e)
    conn.rollback()

finally:
    cursor.close();conn.close()





































