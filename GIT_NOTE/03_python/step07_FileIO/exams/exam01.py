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

texts=file.readlines()
print(texts)

sentence=[]
words=[]
for st in texts:
    sentence.append(st.strip())
    for word in st.split(sep=' '):
        words.append(word.strip())




print(sentence)    
print(words)


