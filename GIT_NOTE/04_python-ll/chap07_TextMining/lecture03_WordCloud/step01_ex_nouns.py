# -*- coding: utf-8 -*-
"""
step01_ex_nouns.py

1. text file 읽기
2. 명사 추출: kkma
3. 전처리: 단어 길이 제한, 숫자 제외
4. 단어 구름 시각화: install 필요
"""

from konlpy.tag import Kkma     # 형태소
from wordcloud import WordCloud # Class

# 1. text file 읽기
path="C:/ITWILL/4_python-ll/workspace/chap07_TextMining/data"
file=open(path +'/text_data.txt',mode='r',encoding='utf-8')
doc=file.read()
print(doc)

kkma=Kkma()

# 문단 -> 문장
ex_sent = kkma.sentences(doc)
print(ex_sent)
# ['형태소 분석을 시작합니다.', '나는 데이터 분석을 좋아합니다.', '직업은 데이터 분석 전문가 입니다.', 'Text mining 기법은 2000대 초반에 개발된 기술이다.']
len(ex_sent) # 4

#문단 -> 명사 
ex_nouns=kkma.nouns(doc)
print(ex_nouns)
# ['형태소', '분석', '나', '데이터', '직업', '전문가', '기법', '2000', '2000대', '대', '초반', '개발', '기술']
len(ex_nouns)# 13


# 2. 명사 추출: 문장 -> 명사  (명사 중복 추출 가능)
nouns=[] # 중복 명사 저장

for sent in ex_sent: # 형태소 분석을 시작합니다. 
    for noun in kkma.nouns(sent): # 문장-> 명사 추출
        nouns.append(noun)

print(nouns)
#['형태소', '분석', '나', '데이터', '직업', '전문가', '기법', '2000', '2000', '2000대', '대', '대', '초반', '개발', '기술']
len(nouns) # 15


# 3. 전처리: 단어 길이 제한, 숫자 제외
from re import match # 숫자 제외
nouns_count={} # 단어 카운터

for noun in nouns:
    if len(noun) > 1 and not(match('^[0-9]',noun)):
        nouns_count[noun] = nouns_count.get(noun,0) + 1

print(nouns_count)
'''
{'형태소': 1, '분석': 3, '데이터': 2, '직업': 1, '전문가': 1, '기법': 1, '초반': 1, '개발': 1, '기술': 1}
'''

#4. 단어 구름 시각화
#1) Top5 word
from collections import Counter #class

word_count=Counter(nouns_count)
top5_word=word_count.most_common(5) #top5
print(top5_word)
#[('분석', 3), ('데이터', 2), ('형태소', 1), ('직업', 1), ('전문가', 1)]

# 2) word cloud 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')

wc_result = wc.generate_from_frequencies(dict(top5_word))

import matplotlib.pyplot as plt

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기
plt.show()
