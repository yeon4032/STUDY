'''
step03 관련 문제

문) word count
   - 여러 줄의 문자열에서 공백을 기준으로 단어를 분류하고, 단어 수 출력하기
'''

multiline="""안녕 Python 세계로 오신걸
환영 합니다.
파이션은 비단뱀 처럼 매력적인 언어 입니다."""


print('줄 단위 출력')
lines = multiline.split("\n") # 엔터키 기준
print(lines) # 줄 단위 원소 벡터 

# 줄 단위 출력 
for line in lines :
    print(line)

print('단어 단위 출력')
words = str(lines).split(" ") # 공백 기준
# 단어 단위 출력 
for word in words :
    print(word)

# 공백 문자를 기준으로 단어수 카운터 
cnt = 0
doc = [] # 빈 list : 줄 단위 저장
word  = [] # 빈 list : 단어 저장   
    
for line in multiline.split("\n"):   
    doc.append(line) # 줄 단위 문장을 빈 list에 추가    
    for w in line.split(" "): # 공백으로 분리
        word.append(w) 
        print(w)
        cnt += 1  
print('단어수 :',cnt) # 단어수 출력 
print(doc) # 줄 단위 문장 출력
print(word) # 줄 단위 단어 출력

'''
안녕하세요.
Python
세계로
오신걸
환영합니다.
파이션은
비단뱀
처럼
매력적인
언어입니다.
단어수 : 10
'''