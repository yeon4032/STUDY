# -*- coding: utf-8 -*-
"""
step06_join_sub.py

1.table 생성과 레코드 추가 :HidSQL이용 (dept.sql 파일)
2.emp vs dept -> join & subquery
  ->ANSI 표준 JOIN
"""

import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config) #db연동
    cursor=conn.cursor() #sql 문 실행 객체
    
    # 1. ANSI inner join
    sal=250
    sql=f"""select e.eno,e.ename,e.sal,d.dno 
            from emp e INNER JOIN dept d
            ON e.dno = d.dno and e.sal >= {sal}"""
    cursor.execute(sql) #join 실행
    rows=cursor.fetchall()
    
    for row in rows:
        print(row[0], row[1], row[2], row[3])
        
    print('검색된 레코드 수:', len(rows))
    
    #2. subqeury: dept(dno) -> emp 정보 출력
    dno= int(input('부서번호:')) #10
    sql= f"""select eno, ename, hiredate, job, dno
             from emp 
             where dno = (select dno from dept where dno={dno})"""
    
    cursor.execute(sql)
    rows=cursor.fetchall()
    
    if rows:
        for row in rows:
            print(row) # tuple
    else:
        print('해당 부서는 없음')
    '''
    문)subquery: 사원이름(emp) input -> 부서(dept)정보 출력하기
    
    '''
    #3. subqeury
    ename= input('이름:') 
    sql= f"""select *
             from dept
             where dno = (select dno from emp where ename='{ename}')"""
    
    cursor.execute(sql)
    row=cursor.fetchone()
    
    if row:
        print(row[0],row[1],row[2])

    else:
        print('해당 부서는 없음')  
    
        
except Exception as e:
    print('db error:',e)
    conn.rollback()
finally:
    cursor.close(); conn.close()


































