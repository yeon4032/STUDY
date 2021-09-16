'''
문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 


문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문장 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''
import os
os.chdir('C:/ITWILL/3_python/workplace/step07_FileIO/data')

file = open("ftest.txt", mode = 'r')
texts = file.readlines() # 전체 줄단위 읽기 
print(texts) # list 반환 
'''
['programming is fun\n', 'very fun!\n', 'have a good time\n', 'mouse is input device\n', 'keyboard is input device\n', 'computer is input output system']
'''

sents = [] # 문장 저장 
words = [] # 단어 저장 

for line in texts : # list -> 문장 
    sents.append(line.strip()) # 문장 저장 
    type(line)
    for word in line.split(sep=' ') : # 문장 - 단어 
        words.append(word.strip()) # 단어 저장 
        
print(sents)    
print('문장 수 : ', len(sents))

print(words)    
print('단어 수 : ', len(words))

#풀이법 2
import os
os.chdir('C:/ITWILL/3_python/workplace/step07_FileIO/data')

file = open("ftest.txt", mode = 'r')

lines=file.readlines()
print(lines)

sentence=[]
words=[]
cnt3=0


for line in lines:
    cnt3+=1
    sentence.append(line.strip())
    words.extend(line.split())

print(sentence,cnt3)
print(words,len(words))





