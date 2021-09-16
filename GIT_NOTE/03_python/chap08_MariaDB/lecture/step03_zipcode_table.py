# -*- coding: utf-8 -*-
"""
step03_zipcode_table.py

-text file-> DB table 저장
<작업 순서>
1.table 생성: HidSQL 이용 하여 생성
2.zipcode.txt -> [서울]선택 -> 래코드 추가
3.table-> 레코드 조회(동으로 검색) 

"""

import pymysql # driver = python 과 db  연결해주는 중간자 역학
import os # 경로 변경/확인
os.chdir('C:/ITWILL/3_python/workplace/chap08_MariaDB/data/')

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
    print('~~db연동 성공~~') #~~ db 연동 성공 ~~
    
    #1. 레코드 추가 & 조회
    cursor.execute("select *from zipcode_tab")
    dataset=cursor.fetchall()
    
    if not(dataset): #래코드 없는 경우 - > 레코드 추가
        file=open('zipcode.txt',mode='r',encoding='utf-8')
        line=file.readline()

        while line:
            tokens=line.split(sep='\t') # 4~5 개
            if tokens[1] == '서울':
                zipcode = str(tokens[0]) # 135-806
                city=tokens[1]
                gu=tokens[2]
                dong=tokens[3]
                detail=tokens[4]
                
            if detail: #상세주소 있음
                sql=f"""insert into zipcode_tab values(
                '{zipcode}','{city}','{gu}','{dong}','{detail}')"""
    
            else: #상세주소 없음
                sql=f"""insert into zipcode_tab(zipcode,city,gu,dong) values(
                '{zipcode}','{city}','{gu}','{dong}')"""
                
            cursor.execute(sql) # 레코드 삽입    
            conn.commit()
    
            line=file.readline() # 2줄 ~ end줄
        #exit
        file.close()
        print('~~레코드 추가 성공~~')
        
    else: #래코드 있는 경우 -> 조회(동 or 구)
        choice = int(input('1.동 검색, 2.구 검색:'))
        if choice==1:
            dong=input('검색할 동 입력:')
            sql=f"select *from zipcode_tab where dong like '%{dong}%'"
            cursor.execute(sql) # 조회
            rows=cursor.fetchall() # 레코드 가져오기
            for r in rows:
                print(r[0],r[1],r[2],r[3],r[4])
                
            print('검색된 레코드는 수',len(rows))
            
        elif choice==2:
            gu=input('검색할 구 입력:')
            sql=f"select *from zipcode_tab where gu like '%{gu}%'"
            cursor.execute(sql) # 조회
            gu_rows=cursor.fetchall() # 레코드 가져오기
            for g_r in gu_rows:
                print(g_r[0],g_r[1],g_r[2],g_r[3],g_r[4])
                
            print('검색된 레코드는 수',len(gu_rows))
        
        else:
            print('해당 번호는 없습니다.')
  
except Exception as e:
    print('db connection err:', e)
finally:
    cursor.close(); conn.close() # 객체 닫기 (역순)
