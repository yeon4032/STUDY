# -*- coding: utf-8 -*-
"""
step07_groupby.py

select 집계함수(avg,sum) from emp (테이블명)
groupby 집단변수(컬럼명: dno,job) ->(부서번호, 직책)
having 조건식;
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
    conn=pymysql.connect(**config)
    cursor=conn.cursor()
    
    #emp테이블: 부서번호 or 직책
    gcol=int(input('1.부서,2.직책:'))
    
    if gcol > 2 or gcol < 1:
        print('그룹 불가')
    else:
        if gcol == 1:
            sql="""select dno, sum(sal), round(avg(sal),2)
                from emp
                group by dno
                order by dno"""
        
        else: # elif gocl=2
            sql="""select job, sum(sal), avg(sal)
                from emp
                group by job
                order by job"""
        
        cursor.execute(sql)
        rows=cursor.fetchall()
        
        for row in rows:
            print(row[0],row[1],row[2])
            
        print('전체 레코드 수:', len(rows))
        
        '''
        문제) 부서별 급여 평균을 계산하여 평균이 300 이상인 부서만 출력하시요
        having 절 이용
        '''
      
        if gcol == 1:
            print('\n**평균 급여 300 이상 부서**')
            sql="""select dno, sum(sal), round(avg(sal),2)
                from emp
                group by dno
                having round(avg(sal),2)>=300
                order by dno"""
        cursor.execute(sql)
        rows=cursor.fetchall()        
        
        for row in rows:
            print(row[0],row[1],row[2])
            
        print('전체 레코드 수:', len(rows))
    
except Exception as e:
    print('db err:',e)
    conn.rollback()
    
finally:
    cursor.close();conn.close()
