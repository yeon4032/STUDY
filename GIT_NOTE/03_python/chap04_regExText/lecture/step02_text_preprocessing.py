# -*- coding: utf-8 -*-
"""
step02_text_preprocessing.py

텍스트 전처리: 특수문자, 불용어 처리
"""
# 텍스트 전처리 
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,  A124&***$?']
len(texts) # 3
type(texts) #list
type(texts[0]) #str


#단계1: 소문자 변경
text_re=[] #결과 저장

for st in texts:
    re=st.lower() # str.lower() : 소문자로 변경
    text_re.append(re)
    
print(text_re)

# another way

#list 내포: 변수 =[실행문 for]
text_re=[st.lower() for st in texts]
print(text_re)
# ['afab54747,asabag?', 'abtta $$;a12:2424.', 'uysfsfa,  a124&***$?']

#단계2: 숫자 제거:sub('pattern',rep,string)
import re # re 모듈추가
texts_re2=[re.sub('[0-9]', '',st) for st in text_re]
print(texts_re2)
#['afab,asabag?', 'abtta $$;a:.', 'uysfsfa,  a&***$?']

# 단계3: 문장부호 제거
punc_str='[,.?!:;]'
texts_re3=[re.sub(punc_str, '',st) for st in texts_re2]
print(texts_re3)
#['afabasabag', 'abtta $$a', 'uysfsfa  a&***$']


# 단계4: 특수문자 제거
spec_str='[@#$%^&*()]'
texts_re4=[re.sub(spec_str, '',st) for st in texts_re3]
print(texts_re4)
#['afabasabag', 'abtta a', 'uysfsfa  a']

# 단걔5: 2칸 이상 공백(white space) -> 1간 공백 
texts_re5 = [ ' '.join(st.split()) for st in texts_re4]
#'abtta a' -> 'abtta' 'a' -> 'abtta a'
print(texts_re5)
#['afabasabag', 'abtta a', 'uysfsfa a']

