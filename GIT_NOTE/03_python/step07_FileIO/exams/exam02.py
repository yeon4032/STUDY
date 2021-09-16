# -*- coding: utf-8 -*-
"""
문제2) obama.txt(오바바 연설문) 파일을 읽어와서 텍스트를 전처리한 후 다음과 같이 출력하시오.
  
  <출력 예시>  
전체 단어수 = 4,907개
최고 출현 단어 :  the
top10 word = ['the', 'and', 'of', 'to', 'our', 'that', 'a', 'you', 'we', 'applause']

단어 빈도수
the : 205
and : 195
of : 152
to : 140
our : 109
that : 91
a : 83
you : 82
we : 81
applause : 75
"""
import os 


# 텍스트 전처리 함수
def clean_text(texts) :
    from re import sub
    
    # 1. 소문자 변경     
    texts_re = texts.lower() 
    
    # 2. 숫자 제거 : list 내포
    texts_re2 = sub('[0-9]', '', texts_re) 
    
    # 3. 문장부호 제거 : sub('p', 'r', string)
    punc_str = '[,.?!:;]'    
    texts_re3 = sub(punc_str, '', texts_re2) 
    
    # 4. 특수문자 제거 : sub('p', 'r', string)
    spec_str = '[!@#$%^&*()]'    
    texts_re4 = sub(spec_str, '', texts_re3) 
        
    # 5. 공백(white space) 제거 
    texts_re5 = ' '.join(texts_re4.split()) 
    
    return texts_re5


try :
    # 1.파일 읽기(절대경로)
    os.chdir('C:/ITWILL/3_python/workplace/step07_FileIO/data')
    rfile = open('obama.txt', mode = 'r') # / or \\
    #print(rfile.read()) # 파일 전체 읽기
    
    texts = rfile.readlines()
    print(texts)    
       
    # 2.줄 단위 텍스트 전처리 

    
    # 3. 전체 단어수 & 최고 단어 

    
    # 4. Top10 단어 & 단어 빈도수 
    

except Exception as e:
    print('Error 발생 : ', e)
finally:
    rfile.close()
    
    
    
    