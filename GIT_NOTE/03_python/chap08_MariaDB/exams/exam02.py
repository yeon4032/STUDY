'''
문제2) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
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

try:
    # db 연결 객체 생성 
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        # 1. 레코드 조회
        if menu == 1 : 
            sel=int(input('1. 전체,2 상품명:'))
            if sel==1 :#전체 레코드 조회
                sql="select *from goods"
                cursor.execute(sql) # 실제 sql문 실행
            
                # 레코드 조회 결과
                dataset=cursor.fetchall() # 레코드 가져오기    
                for row in dataset:
                    print(row[0],row[1],row[2],row[3]) # 1 냉장고 2 850000
                
                print('전체 레코드 수:', len(dataset)) #전체 레코드 수: 4
        
            elif sel==2: # 상품명 조회
                name = input('상품명 입력:')
                sql=f"select *from goods where name like'%{name}%'"
                cursor.execute(sql)
                dataset = cursor.fetchall()
                
                if dataset:
                    for row in dataset:
                        print(row[0],row[1],row[2],row[3])
                
                else:
                    print('검색된 레코드 없음')
                    
        # 2. 레코드 추가
        elif menu == 2: 
            
            #키보드 입력 
            code = int(input('code input:'))
            name = input('name input:')
            su= int(input('su input:'))
            dan=int(input('dan input:'))
    
            sql= f"insert into goods values({code},'{name}',{su},{dan})"
            cursor.execute(sql) # 레코드 추가
            conn.commit() #db 반영  
       
        # 3. 레코드 수정    
        elif menu == 3: 
            #3. Updat문:Update: code를 찾아 -> name,dan 수정한다 
            code = int(input('update code input:')) # 5
            name = input('update name input:') # 가스레인지
            dan=int(input('update dan input:')) # 450000
    
            sql=f"""update goods set name = '{name}', dan={dan} where 
                code = {code}"""
            cursor.execute(sql) # 레코드 수정
            conn.commit() #db반영
        
        # 4. 레코드 삭제
        elif menu == 4: 
            #4.Delete문 : Delete : code -> 존재 -> 레코드 삭제
            code = int(input('delete code input:'))
            
            sql=f"select *from goods where code= {code}"
            cursor.execute(sql)
            row=cursor.fetchone() # 하나의 레코드 가지고 오기 & cursor.fecthall은 전체 레코드 가져오기
    
            if row : #레코드 있는 경우
                sql=f"delete from goods where code= {code}"
                cursor.execute(sql) # 실제 레코드 삭제
                conn.commit() # db 반영
            
            else: # 검색된 레코드 없다
                print('해당 code 없음')
        
        #5. 프로그램 종료 # 반복 exit    
        elif menu == 5 : 
            print('프로그램 종료')
            break 
        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
