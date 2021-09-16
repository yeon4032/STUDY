# -*- coding: utf-8 -*-
"""
문제3) HidiSQL을 이용하여 다음과 같은 student 테이블을 만들고, 
      DB 연동 프로그램으로 레코드를 추가하고, 조회하시오.
  
조건1> HidiSQL 이용 : student 테이블 만들기       
       테이블 칼럼 구성 : 학번,이름,전화번호,학과,지도교수 
create or replace table student( 
  studno int primary key,              
  sname varchar(10) not null,                        
  tel varchar(15),     
  deptno int,                
  profno  int                
);  


조건2> DB 연동 프로그램 : 테이블에 레코드가 없으면 레코드 추가(insert)  
insert into student values (9411,'서진수','055)381-2158',201,1001);
insert into student values (9413,'이미경','02)266-8947',103,3002);
insert into student values (9415,'박동호','031)740-6388',202,4003);

조건3> DB 연동 프로그램 : 테이블에 레코드가 있으면 레코드 조회(select)   
"""

import pymysql # driver = python + DB(Mysql)


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
    # sql문 실행 객체 
    cursor = conn.cursor()    
    
    # 1. table 유무 판단 : student 
    cursor.execute("show tables") # table 목록 조회 
    tables = cursor.fetchall() # table 목록 가져오기 
    
    sw = False # off
    for table in tables :
        if 'student' in table :
            sw = True # on
        
    
    # 2. 레코드 추가 or 레코드 조회 
    if sw : # table 있는 경우 
        #래코드 유무 판단 -> 없으면 레코드 추가-> 있으면 레코드 조회
        cursor.execute("select *from student")
        rows=cursor.fetchall()
        if rows:
            #레코드 조회
            for row in rows:
                print(row) 
            print('전체 레코드 수:', len(rows)) #전체 레코드 수: 4
        
        else:
            
            cursor.execute("insert into student values (9411,'서진수','055)381-2158',201,1001);") # 레코드 추가
            cursor.execute("insert into student values (9413,'이미경','02)266-8947',103,3002);") # 레코드 추가
            cursor.execute("insert into student values (9415,'박동호','031)740-6388',202,4003);") # 레코드 추가
            conn.commit() #db 반영
            print('레코드가 추가되었습니다')

    else : # table 없는 경우         
        print('student 테이블이 없습니다.') 
        
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
    
    


    
    