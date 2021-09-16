# -*- coding: utf-8 -*-
"""
step02_text_file.py

텍스트 파일 입출력

형식) open('파일경로\\파일명',mode='r'or 'w' or 'a') r-> 읽기용(기본), w->쓰기용 a-> 쓰기용 

"""

import os # 파일경로 확인/변경
try:
    #1.파일 읽기
    print('현재 경로:',os.getcwd()) #현재 경로: C:\ITWILL\3_python\workplace\step07_FileIO\lecture
    #파일 경로 변경
    os.chdir('C:\\ITWILL/3_python/workplace/step07_FileIO/data')
    
    #파일 불러오기
    file=open('ftest.txt', mode='r') # 1)객체 생성
    print(file.read()) # 전체 파일 읽기 - 2)객체 사용
    # file.close() #객체 닫기 <- it usually wirten at finally part
    
    #2. 파일 쓰기
    file2=open('ftest2.txt', mode='w') #1)객체 생성
    file2.write('my first text ~~') #2) 객체 사용
    file2.close() # becuase of file3 we have to put file2.close to complete the working of file2.
    
    #3. 파일 추가
    file3=open('ftest2.txt',mode='a') # 1)객체 생성 mode=a 는 기존 문장에 새로운 문장 추가시 사용
    file3.write('\nmy second text ~~') #2) 객체 사용
    file3.close()
    #4. 파일 읽기
    '''
    file.read(): 전체 문서 읽기
    file.readline(): 한 줄 단위 읽기
    file.readlines(): 줄 단위 전체 읽기
    '''
    
    file4=open('ftest2.txt', mode ='r')
    
    line=file4.readline() #한 줄 읽기 -string
    print('readline') # string  반환 -string
    print(line)     #my first text ~~\n - list

    lines= file4.readlines() # 줄 단위 전체 읽기
    print('readlines')
    print(lines) # list 반환
    #['my first text ~~\n', 'my second text ~~']
    
    #줄단위 출력
    for line in lines:
        print(line.strip()) # 문장 끝 불용제거(이스케이프문자, 공백)제거
    '''
    print(line)
    my first text ~~

    my second text ~~
    '''
    '''
    print(line.strip())
    my first text ~~
    my second text ~~
    '''
    
    #strip() 예
    x='agagaget\n\t\r'
    print(x.strip()) #agagaget: 불용제거됨
    
    #with문 이용: 파일 입출력
    with open('ftest3.txt', mode='w',encoding='utf-8') as file:
        file.write('파이썬 파일 작성 연습')
        file.write('\n파이썬 파일 작성 연습2')
        #file.close() 생략
    
    with open('ftest3.txt', mode='r',encoding='utf-8') as file:
        print(file.readline().strip()) # \n제거 하기 위해 strip() 사용
        print(file.readline())
        #file.close() 생략
        
except Exception as e:
    print('예외발생:',e)
finally:
    file4.close; file.close() #3) 객체 닫기 for 1 & 2







