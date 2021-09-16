# -*- coding: utf-8 -*-
"""
step05_csv_table.py


csv.file-> DB 테이블 저장
1.student 생성:HidiSQL 이용
    -> delete from student;
2.student.csv file colum read -> student 테이블 저장하기

"""

#exams > exam 03 완성.py 참고

import pandas as pd # csv file read
import pymysql # driver = python + DB(Mysql)
import os # file 경로 변경 or 확인
#file 경로 변경
os.chdir("C:/ITWILL/3_python/workplace/chap08_MariaDB/data")
st=pd.read_csv('student.csv')
print(st.info())

# 변수 생성
sno=st.sno
name=st.name
tel=st.tel
deptno=st.deptno
propno=st.propno

size=len(st)
print('전체학생수:',size) #전체학생수: 10 

#################################################

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
##################################################################
            #래코드 추가: student.csv file 이용해서 -> 레코드 추가
            for i in range(size): #0~9
                sql=f""" insert into student values(
                {sno[i]},'{name[i]}','{tel[i]}',{deptno[i]},{propno[i]})"""
                cursor.execute(sql)
                
            conn.commit() #db 추가
            print('stduent 테이블에 레코드가 추가되었습니다')

    else : # table 없는 경우         
        print('student 테이블이 없습니다.') 
        
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()

