# -*- coding: utf-8 -*-
"""
step03_text_preprocessing.py

text file 전처리 + 단어 빈도수 
"""

# 1. 텍스트 전처리 함수 정의 
# chap05_Function > lecture > step03 참조 

def clean_text(texts) :
    from re import sub # re 모듈 가져오기 
    
    # 단계1 : 소문자 변경   
    texts_re = [ st.lower() for st in texts]
        
    # 단계2 : 숫자 제거 
    texts_re2 = [sub('[0-9]', '', st) for st in texts_re]
    
    
    # 단계3 : 문장부호 제거 
    punc_str = '[,.?!:;]'
    texts_re3 = [sub(punc_str, '', st) for st in texts_re2]
    
    
    # 단계4 : 특수문자 제거 
    spec_str = '[@#$%^&*()]'
    texts_re4 = [sub(spec_str, '', st) for st in texts_re3]
    
    
    # 단계5 : 2칸 이상 공백(white space) 제거 -> 1칸 공백 
    texts_re5 = [' '.join(st.split()) for st in texts_re4 ]
    
    return texts_re5


# 2. file read 
import os 
# 파일 경로 변경 
os.chdir('C:\\ITWILL/3_Python-I/workspace/chap07_FileIO/data')
# file 객체 생성 
rfile = open('texts.txt', mode ='r', encoding='utf-8')
#print(rfile.read())

texts = rfile.readlines()
print(texts)
'''
['우리나라    대한민국, 우리나라%$ 만세\n', '비아그&라 500GRAM 정력 최고!\n', '나는 대한민국 사람\n', '보험료 15000원에 평생 보장 마감 임박\n', '나는 홍길동']
'''
print(len(texts)) # 5
rfile.close()

# 3. texts 전처리 
texts_re5 = clean_text(texts)
print('texts 전처리 후 ')
print(texts_re5)

# 4. file save
''' 
wfile = open('texts_write.txt', mode='w', encoding='utf-8')

for line in texts_re5 :
    wfile.write(line + '\n')

wfile.close() 
'''

# 5. word count 
words = [] # 단어 저장 
wc = {} # 단어 빈도수 저장 

rfile = open('texts_write.txt', mode='r', encoding='utf-8')
texts = rfile.readlines() 
print(texts)
'''
['우리나라 대한민국 우리나라 만세\n', '비아그라 gram 정력 최고\n', '나는 대한민국 사람\n', '보험료 원에 평생 보장 마감 임박\n', '나는 홍길동\n']
'''

# list -> 단어 추출 
print(texts)
for line in texts :
    print(line)
    for word in line.split() :
        print(word)
        words.append(word.strip())

print(words) # 단어 벡터 

# 단어 -> 단어 출현빈도수 
for word in words :
    wc[word] = wc.get(word, 0) + 1
print(wc)
print(wc, len(wc)) # 16
'''
{'우리나라': 2, '대한민국': 2, '만세': 1, '비아그라': 1, 'gram': 1, '정력': 1, '최고': 1, '나는': 2, '사람': 1, '보험료': 1, '원에': 1, '평생': 1, '보장': 1, '마감': 1, '임박': 1, '홍길동': 1}
'''

# 6. Top N 단어 출력 
# 1) 최고 출현 단어 
re = max(wc, key=wc.get) # value 기준 
print('최고 출현 단어 : ', re) # 최고 출현 단어 :  우리나라

# 2) Top5 word 출력 
wc_sorted = sorted(wc, key=wc.get, reverse=True) # value 기준 내림차순 정렬 
print(wc_sorted) # list 
'''
['우리나라', '대한민국', '나는', '만세', '비아그라', 'gram', '정력', '최고', '사람', '보험료', '원에', '평생', '보장', '마감', '임박', '홍길동']
'''
print('Top5 word :', wc_sorted[:5])
# Top5 word : ['우리나라', '대한민국', '나는', '만세', '비아그라']

print('단어 -> 빈도수')
for word in wc_sorted[:5] :
    print(word, wc[word], sep=' -> ')
    
wc[word]    
'''
단어 -> 빈도수
우리나라 -> 2
대한민국 -> 2
나는 -> 2
만세 -> 1
비아그라 -> 1
''' 














