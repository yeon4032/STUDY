# -*- coding: utf-8 -*-
"""
step04_emp_table.py

-HidiSQL 이용: SQL 파일 불러오기 실습
 ->[파일] > [SQL 파일 불러오기] > emp.sql 파일 선택

1. table 생성(HidiSQL 이용)
    -> 기본키 자동번호 생성기:auto_increment
2.table 유무 판단: show tables;
    -> table 있는 경우 :  래코드 조회
    -> table 없는 경우 : 'table없음' 경고 메시지    
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
    
    #1.table 유무 판단:emp
    sql="show tables"
    cursor.execute(sql)
    tables = cursor.fetchall() # 검색 결과
    '''
    스위칭: 두 가지 상태 파악
    '''
    
    sw = False # off
    for table in tables:
        print('table:',table) # 반환시 tuple 타입 
        if 'emp'in table:     # or table[0]=='emp': 가능  if table=='emp; 불가능  ->  이유#('emp') != 'emp' **주의**
            sw = True #on
            
    if sw: #sw==True
        #2.레코드 조회
        sql="select *from emp"
        cursor.execute(sql)
        dataset=cursor.fetchall()
        
        for row in dataset:
            print(row)
            
        print('전체 레코드 수:', len(dataset))
    
    else:
        print('table 없음 ')
        sql="""create or replace table emp(
        eno int auto_increment primary key,
        ename varchar(20) not null,
        hiredate date not null,
        sal int not null,
        bonus int default 0,
        job varchar(20) not null,
        dno int)"""
        cursor.execute(sql) #실제 table생성
        #auto commit:conn.commit() 생략
        print('emp 테이블 생성')
        
        
        
except Exception as e:
    print('db connection err:', e)
    conn.rollback()
finally:
    cursor.close(); conn.close() # 객체 닫기 (역순)




















































