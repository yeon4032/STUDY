# -*- coding: utf-8 -*-
"""
step03_func_app.py

함수 응용
1. 텍스트 전처리 함수 정의
2. 표본의 분산/표준편차 계산 함수
"""

#1. 텍스트 전처리 함수 정의
def clean_text(texts):
    from re import sub # re 모듈 가져오기
    
    #단계1: 소문자 변경
    text_re=[st.lower() for st in texts]
    
    #단계2: 숫자 제거:sub('pattern',rep,string)
    texts_re2=[sub('[0-9]', '',st) for st in text_re]
    
    # 단계3: 문장부호 제거
    punc_str='[,.?!:;]'
    texts_re3=[sub(punc_str, '',st) for st in texts_re2]
    
    # 단계4: 특수문자 제거
    spec_str='[@#$%^&*()]'
    texts_re4=[sub(spec_str, '',st) for st in texts_re3]
    
    # 단걔5: 2칸 이상 공백(white space) -> 1간 공백 
    texts_re5 = [ ' '.join(st.split()) for st in texts_re4]
    return texts_re5
    
    
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

texts_re5=clean_text(texts)
print('전처리 전')
print(texts) 
print('전처리 후')
print(texts_re5)    
 
   
#2. 표본의 분산/표준편차 계산 함수
dataset=[2,4,5,6,1,8]

#표본 분산과 표준 편차
from statistics import mean, variance, sqrt

print('표본 부산=', variance(dataset))
print('표본 표준편차=',sqrt(variance(dataset)))
    
'''
표본 분산=sum( (x변량- 산술평균)**2)/n-2 
표본 표준편차=sqrt(표본분산)
'''

#산술평균
def avg(data):
    return mean(data)    
    
avg(dataset) # 4.333333333333333

# 분산/표준편차
def var_sd(data):
    a=avg(data) # 함수 호출

    #list 내포
    diff = [(x - a)**2 for x in data]
    #print('diff=', diff)
    
    var= sum(diff)/(len(data)-1)
    sd = sqrt(var)

    return var, sd    

#함수 호출
var,sd = var_sd(dataset)
print('표본 분산=',var)
print('표본 표준편차=',sd)










































